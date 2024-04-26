import os

from infrastructure.postgress.connection import Database
from infrastructure.utils.io import read_file


async def init_db(database: Database):
    await create_tables(database=database)


async def create_tables(database: Database):
    base = os.path.dirname(__file__)
    tables = [
        read_file(os.path.join(base, "scripts/tables/category.sql")),
        #read_file(os.path.join(base, "scripts/tables/location.sql")),
    ]
    for table in tables:
        print(table)
        await database.execute(table)
