from models import *


def get_postgres_version():
    db.engine.connect()
    print(f"PostgreSQL version: {db.engine.dialect.server_version_info}")


def get_prof_table_content():
    print("'Prof' table content:")
    print(Prof.query.all())

def use_vetud_view(idel):
    print(f"Eleve {idel} information:")
    print(VEtud.query.filter_by(idel=idel).all())

def insert_into_eleve(idel, nom, prenom, college, niveau, date_naissance, sexe):
    eleve = Eleve(idel=idel, nom=nom, prenom=prenom, college=college, niveau=niveau, date_naissance=date_naissance, sexe=sexe)
    db.session.add(eleve)
    db.session.commit()
    print(f"Eleve {idel} inserted")

def main():
    with app.app_context():
        # Q1
        get_postgres_version()
        # Q2
        get_prof_table_content()
        # Q3
        use_vetud_view(1)
        # Q4
        insert_into_eleve(11, "Doe", "John", "0341278E", "6eme", "2000-01-01", "GARCON")



if __name__ == "__main__":
    main()