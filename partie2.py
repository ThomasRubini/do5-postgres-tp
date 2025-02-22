from models import *


def get_postgres_version(conn):
    pass


def get_prof_table_content():
    print("'Prof' table content:")
    print(Prof.query.all())

def use_vetud_view(conn, idel):
    pass

def insert_into_eleve(conn, idel, nom, prenom, college, niveau, date_naissance, sexe):
    pass

def main():
    with app.app_context():
        # Q2
        get_prof_table_content()


if __name__ == "__main__":
    main()