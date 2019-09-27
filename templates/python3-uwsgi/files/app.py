import traceback
import uuid
import sys

import pymysql
import redis

from platformshconfig import Config


config = Config()


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


# uwsgi requires the WSGI entry point to be named "application"
def application(env, start_response):

    tests = {
        "mysql": wrap_test(test_mysql, config.credentials("database")),
        "redis": wrap_test(test_redis, config.credentials("rediscache"))
    }

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes(str(tests), "utf8")]
