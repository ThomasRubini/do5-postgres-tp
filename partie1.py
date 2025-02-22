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

def use_vetud_view(conn, idel):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM vetud WHERE idel = %s", (idel,))

    vetud_view = cursor.fetchall()
    print("'Vetud' view content:")
    print(vetud_view)

def insert_into_eleve(conn, idel, nom, prenom, college, niveau, date_naissance, sexe):
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Eleve(idel, nom, prenom, college, niveau, date_naissance, sexe) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (idel, nom, prenom, college, niveau, date_naissance, sexe)
    )
    conn.commit()

    print(f"Inserted into 'Eleve' successfully")

def main():
    conn = get_conn()
    # Q1
    get_postgres_version(conn)
    # Q2
    get_prof_table_content(conn)
    # Q3
    use_vetud_view(conn, "1")
    # Q4
    insert_into_eleve(conn, 11, "Doe", "John", "0341278E", "6eme", "2000-01-01", "GARCON")




if __name__ == "__main__":
    main()
