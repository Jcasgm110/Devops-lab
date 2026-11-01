import os
import psycopg2
from flask import Flask

app = Flask(__name__)


def get_conn():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )


@app.route("/")
def home():
    conn = get_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS visitas "
                "(id SERIAL PRIMARY KEY, quando TIMESTAMP DEFAULT now())"
            )
            cur.execute("INSERT INTO visitas DEFAULT VALUES")
            cur.execute("SELECT count(*) FROM visitas")
            total = cur.fetchone()[0]
    conn.close()
    return f"Olá do contentor! Visitas: {total}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)