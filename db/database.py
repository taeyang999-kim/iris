import pymysql
from config import DB_CONFIG

class Database:
    def __init__(self):
        self.conn = pymysql.connect(**DB_CONFIG)

        with self.conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS iris_records (
                id INT AUTO_INCREMENT PRIMARY KEY,
                sl FLOAT,
                sw FLOAT,
                pl FLOAT,
                pw FLOAT,
                result VARCHAR(50)
            )
            """)
        self.conn.commit()

    def save_iris(self, sl, sw, pl, pw, result):
        with self.conn.cursor() as cursor:
            sql = """
            INSERT INTO iris_records (sl, sw, pl, pw, result)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (sl, sw, pl, pw, result))
        self.conn.commit()

    def get_all_iris(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
            SELECT id, sl, sw, pl, pw, result
            FROM iris_records
            ORDER BY id DESC
            """)
            return cursor.fetchall()
    def get_result_stats(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
            SELECT result, COUNT(*)
            FROM iris_records
            GROUP BY result
            """)
            return cursor.fetchall()

    def close(self):
        self.conn.close()