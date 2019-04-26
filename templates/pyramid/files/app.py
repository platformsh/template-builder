import sys
import uuid
import traceback

import redis
import pymysql
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import platformshconfig


pshconfig = platformshconfig.Config()


def hello_world(request):

    tests = {
        "database": wrap_test(test_mysql, pshconfig.credentials("database")),
        "redis": wrap_test(test_redis, pshconfig.credentials("redis"))
    }

    return Response(str(tests))


def wrap_test(callback, *args, **kwargs):
    try:
        result = callback(*args, **kwargs)
        return {
            "status": "OK",
            "return": result,
        }
    except Exception:
        return {
            "status": "ERROR",
            "error": traceback.format_exception(*sys.exc_info())
        }


def test_mysql(instance):
    connection = pymysql.connect(
        host=instance["host"],
        port=instance["port"],
        user=instance["username"],
        password=instance["password"],
        db=instance["path"],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

    finally:
        connection.close()


def test_redis(instance):
    r = redis.StrictRedis(
        host=instance["host"],
        port=instance["port"],
        db=0,
    )
    key_name = "foo-%s" + str(uuid.uuid4())
    value = b"bar"

    r.set(key_name, "bar")
    assert value == r.get(key_name)


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()

    server = make_server('127.0.0.1', int(pshconfig.port), app)
    server.serve_forever()
