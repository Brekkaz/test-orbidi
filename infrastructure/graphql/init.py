from typing import Optional

import strawberry
from strawberry.tools import merge_types
from fastapi import FastAPI, Depends
from graphql import GraphQLError
from starlette.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from strawberry.types import ExecutionContext
from infrastructure.graphql.category.dataloaders import create_category_data_loader
from infrastructure.graphql.location.dataloaders import create_location_data_loader
from infrastructure.graphql.state import AppState
from settings import settings
from infrastructure.postgress.connection import Database
from infrastructure.postgress import init_db
from infrastructure.graphql.category.query import CategoryQuery
from infrastructure.graphql.category.mutation import CategoryMutation
from infrastructure.graphql.location.query import LocationQuery
from infrastructure.graphql.location.mutation import LocationMutation
from application.category import Category as CategoryUseCase
from application.location import Location as LocationUseCase
from infrastructure.postgress.category.repository import PostgressCategoryRepository
from infrastructure.postgress.location.repository import PostgressLocationRepository


class Schema(strawberry.federation.Schema):
    def process_errors(
        self,
        errors: list[GraphQLError],
        execution_context: Optional[ExecutionContext] = None,
    ) -> None:
        pass    

database_instance = Database(
    user=settings.db_user,
    password=settings.db_password,
    host=settings.db_host,
    port=settings.db_port,
    database=settings.db_name,
)

def create_app():
    """
    configura e instancia el servidor graphql
    """
    #consolida las queries de todos los modulos en la query principal
    Query = merge_types("QueryRoot", (CategoryQuery, LocationQuery))
    #consolida las mutaciones de todos los modulos en la mutacion principal
    Mutation = merge_types("MutationRoot", (CategoryMutation, LocationMutation))

    #configura el esquema
    schema = Schema(query=Query, mutation=Mutation, enable_federation_2=True)

    #instancia el estado de la aplicacion con los casos de uso y dataloaders que necesitan los metodos
    def app_state() -> AppState:
        return AppState(
            category=CategoryUseCase(
                repository=PostgressCategoryRepository(database=database_instance)
            ),
            location=LocationUseCase(
                repository=PostgressLocationRepository(database=database_instance)
            ),
            categories_loader=create_category_data_loader(
                repository=PostgressCategoryRepository(database=database_instance)
            ),
            location_loader=create_location_data_loader(
                repository=PostgressLocationRepository(database=database_instance)
            ),
        )

    async def get_context(state=Depends(app_state)):
        return state

    #vincula el estado al esquema
    graphql_app = GraphQLRouter(schema, context_getter=get_context)

    app = FastAPI()

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    async def startup():
        app.state = app_state()
        #construye la base de datos; todas las sentencias implementan idempotencia
        await database_instance.connect()
        await init_db(database=database_instance)

    @app.on_event("shutdown")
    async def shutdown():
        #desconecta la base de datos al terminar la aplicacion
        await database_instance.close()

    #habilita el endpoint de graphql handleandolo con el esquema
    app.include_router(graphql_app, prefix="/graphql")

    return app
