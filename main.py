import psycopg2

def get_conn():
    connection = psycopg2.connect(
        dbname="postgres",
        user="root",
        password="root",
        host="localhost",
        port="5432"
    )

    return connection

def get_postgres_version(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT version()")

    version = cursor.fetchone()
    print(f"PostgreSQL version: {version}")

def get_prof_table_content(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Prof")

    prof_table = cursor.fetchall()
    print("'Prof' table content:")
    print(prof_table)

def main():
    conn = get_conn()
    # Q1
    get_postgres_version(conn)
    # Q2
    get_prof_table_content(conn)


if __name__ == "__main__":
    main()
