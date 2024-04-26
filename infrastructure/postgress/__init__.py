import os

from infrastructure.postgress.connection import Database
from infrastructure.utils.io import read_file


async def init_db(database: Database):
    """
    Ejecuta de manera ordenada los comandos DDL para la 
    creacion de la base de datos.
    """
    await create_extensions(database=database)
    await create_functions(database=database)
    await create_tables(database=database)
    await create_triggers(database=database)


async def create_extensions(database: Database):
    base = os.path.dirname(__file__)
    tables = [
        read_file(os.path.join(base, "scripts/extensions/001_uuid.sql")),
    ]
    for table in tables:
        await database.execute(table)


async def create_functions(database: Database):
    base = os.path.dirname(__file__)
    tables = [
        read_file(os.path.join(base, "scripts/functions/001_updated_at.sql")),
    ]
    for table in tables:
        await database.execute(table)


async def create_tables(database: Database):
    base = os.path.dirname(__file__)
    tables = [
        read_file(os.path.join(base, "scripts/tables/001_category.sql")),
        read_file(os.path.join(base, "scripts/tables/002_location.sql")),
        read_file(os.path.join(base, "scripts/tables/003_category_location.sql")),
    ]
    for table in tables:
        await database.execute(table)


async def create_triggers(database: Database):
    base = os.path.dirname(__file__)
    tables = [
        read_file(os.path.join(base, "scripts/triggers/001_category.sql")),
        read_file(os.path.join(base, "scripts/triggers/002_location.sql")),
        read_file(os.path.join(base, "scripts/triggers/003_category_location.sql")),
    ]
    for table in tables:
        await database.execute(table)
