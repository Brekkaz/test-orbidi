import logging

import asyncpg


class Database:
    """
    Administrador de base de datos postgress
    """
    def __init__(
        self,
        user: str,
        password: str,
        host: str,
        port: str,
        database: str,
        min_pool_size: int = 10,
        max_pool_size: int = 10,
    ):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self._cursor = None
        self.min_pool_size = min_pool_size
        self.max_pool_size = max_pool_size

        self.connection_pool = None

    async def connect(self):
        """
        crea un pool de conexiones a la base de datos
        """
        if not self.connection_pool:
            try:
                self.connection_pool = await asyncpg.create_pool(
                    min_size=self.min_pool_size,
                    max_size=self.max_pool_size,
                    command_timeout=60,
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                )

            except Exception as e:
                print(e)

    async def fetch_one(self, query: str, *params):
        """
        Ejecuta consultas de unico resultado
        """
        async with self.connection_pool.acquire() as conn:
            stm = await conn.prepare(query)
            result = await stm.fetchrow(*params)
            logging.info(f"Results {result}")
            return result

    async def fetch_many(self, query: str, *params):
        """
        Ejecuta consultas de multiples resultados
        """
        async with self.connection_pool.acquire() as conn:
            stm = await conn.prepare(query)
            result = await stm.fetch(*params)
            logging.info(f"Results {result}")
            return result

    async def execute(self, query: str, *params):
        """
        Ejecuta comandos de unica sentencia
        """
        async with self.connection_pool.acquire() as conn:
            result = await conn.execute(query, *params)
            logging.info(f"Results {result}")
            return result

    async def execute_many(self, query: str, values):
        """
        Ejecuta comandos de multiples sentencias
        """
        async with self.connection_pool.acquire() as conn:
            result = await conn.executemany(query, values)
            logging.info(f"Results {result}")
            return result

    async def close(self):
        """
        Cierra la conexion 
        """
        if not self.connection_pool:
            try:
                await self.connection_pool.close()
                logging.info("Database pool connection closed")
            except Exception as e:
                logging.error(e)
