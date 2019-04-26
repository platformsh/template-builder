import traceback
import uuid
import sys

from http.server import BaseHTTPRequestHandler, HTTPServer
import pymysql
import redis

from platformshconfig import Config


config = Config()


class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        tests = {
            "mysql": self.wrap_test(self.test_mysql, config.credentials("database")),
            "redis": self.wrap_test(self.test_redis, config.credentials("redis"))
        }

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(bytes(str(tests), "utf8"))
        return

    @staticmethod
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

    @staticmethod
    def test_mysql(instance):
      connection = pymysql.connect(
          host=instance["host"],
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

    @staticmethod
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


if __name__ == "__main__":
    server_address = ('127.0.0.1', int(config.port))
    httpd = HTTPServer(server_address, myHandler)
    httpd.serve_forever()
