import psycopg2 # type: ignore
from psycopg2.extras import RealDictCursor # type: ignore

def get_connection():
  conn = psycopg2.connect(
    database="api_bjb",
    host="localhost",
    user="postgres",
    password="marcell",
    port="5432",
    cursor_factory=RealDictCursor
  )
  return conn

def fetch_api_info(api_keyword):
  conn = get_connection()
  cur = conn.cursor()
  cur.execute("SELECT * FROM api_specification WHERE keyword = %s", (api_keyword,))
  result = cur.fetchone()
  cur.close()
  conn.close()
  return result