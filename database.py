import psycopg2 # type: ignore
from psycopg2.extras import RealDictCursor # type: ignore
import config

def get_connection():
  conn = psycopg2.connect(
    dbname=config.DB_NAME,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT,
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