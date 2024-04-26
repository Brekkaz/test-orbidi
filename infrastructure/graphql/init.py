from typing import Optional

import strawberry
from strawberry.tools import merge_types
from fastapi import FastAPI, Depends
from graphql import GraphQLError
from starlette.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from strawberry.types import ExecutionContext
from infrastructure.graphql.state import AppState
from settings import settings
from infrastructure.postgress.connection import Database
from infrastructure.postgress import init_db
from infrastructure.graphql.category.query import CategoryQuery
from infrastructure.graphql.category.mutation import CategoryMutation
from application.category import Category as CategoryUseCase
from application.location import Location as LocationUseCase
from infrastructure.postgress.category.repository import PostgressCategoryRepository
from infrastructure.postgress.location.repository import PostgressLocationRepository


class Schema(strawberry.Schema):
    def process_errors(
            self,
            errors: list[GraphQLError],
            execution_context: Optional[ExecutionContext] = None,
    ) -> None:
        pass


async def init_database(database: Database):
    await init_db(database=database)


database_instance = Database(
    user=settings.db_user,
    password=settings.db_password,
    host=settings.db_host,
    port=settings.db_port,
    database=settings.db_name
)


def create_app():
    Query = merge_types("QueryRoot", (CategoryQuery,))
    Mutation = merge_types("MutationRoot", (CategoryMutation,))

    schema = Schema(query=Query, mutation=Mutation)

    def app_state() -> AppState:
        return AppState(
            category=CategoryUseCase(repository=PostgressCategoryRepository(database=database_instance)),
            location=LocationUseCase(repository=PostgressLocationRepository(database=database_instance)),
        )

    async def get_context(state=Depends(app_state)):
        return state

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
        await database_instance.connect()
        #await init_database(database=database_instance)

    @app.on_event("shutdown")
    async def shutdown():
        await database_instance.close()

    app.include_router(graphql_app, prefix="/graphql")

    return app
