import traceback
import uuid
import sys

import uvicorn
from fastapi import FastAPI

from asyncmy import connect
from asyncmy.cursors import DictCursor

import aioredis

from platformshconfig import Config

app = FastAPI()
config = Config()


@app.get("/")
async def root():
    tests = {
        "database": await wrap_test(test_mysql, config.credentials("database")),
        "redis": await wrap_test(test_redis, config.credentials("rediscache"))
    }
    return tests


async def wrap_test(callback, *args, **kwargs):
    try:
        result = await callback(*args, **kwargs)
        return {
            "status": "OK",
            "return": result,
        }
    except Exception:
        return {
            "status": "ERROR",
            "error": traceback.format_exception(*sys.exc_info())
        }


async def test_mysql(instance):
    connection = await connect(
        host=instance["host"],
        port=instance["port"],
        user=instance["username"],
        password=instance["password"],
        database=instance["path"],
        charset='utf8mb4',
    )

    async with connection.cursor(cursor=DictCursor) as cursor:
        await cursor.execute("SELECT 1")


async def test_redis(instance):
    r = aioredis.from_url("redis://{}:{}".format(
        instance["host"],
        instance["port"],
    ))

    key_name = "foo-%s" + str(uuid.uuid4())
    value = b"bar"

    await r.set(key_name, "bar")
    assert value == await r.get(key_name)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=int(config.port))
