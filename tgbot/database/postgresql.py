import asyncio

from asyncpg import Pool, create_pool


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool = None
        self.loop = loop

    async def connect(self, user, password, host, port, database) -> None:
        self.pool: Pool = await create_pool(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += ' AND '.join([
            f'{item} = ${num}' for num, item in enumerate(parameters, start=1)
        ])
        return sql, tuple(parameters.values())


db = Database(loop=asyncio.get_event_loop())
