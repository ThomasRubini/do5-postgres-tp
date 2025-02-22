
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/postgres'
db = SQLAlchemy()
db.init_app(app)

class Etablissement(db.Model):
    __tablename__ = 'etablissement'
    rne = db.Column(db.String(8), primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    localite = db.Column(db.String(30))

class Prof(db.Model):
    idp = db.Column(db.Integer, primary_key=True, nullable=False)
    nom = db.Column(db.String(20), nullable=False)
    annee_naissance = db.Column(db.Integer)
    rne = db.Column(db.String(8), db.ForeignKey('etablissement.rne'))
    ville = db.Column(db.String(30))

    def __repr__(self):
        return f"<Prof {self.idp} {self.nom} {self.annee_naissance} {self.rne} {self.ville}>"

class Niveau(db.Model):
    __tablename__ = 'niveau'
    niveau = db.Column(db.String(4), primary_key=True, nullable=False)
    __table_args__ = (
        db.CheckConstraint("niveau in ('6eme', '5eme', '4eme','3eme')", name='chk_niveau'),
    )

class Eleve(db.Model):
    __tablename__ = 'eleve'
    idel = db.Column(db.Integer, primary_key=True, nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(30))
    college = db.Column(db.String(8), db.ForeignKey('etablissement.rne'))
    niveau = db.Column(db.String(4), db.ForeignKey('niveau.niveau'))

class Exercice(db.Model):
    __tablename__ = 'exercice'
    idex = db.Column(db.Integer, primary_key=True, nullable=False)
    contenu = db.Column(db.String(250))
    niveau = db.Column(db.String(4), db.ForeignKey('niveau.niveau'))
    proprietaire = db.Column(db.Integer, db.ForeignKey('prof.idp'))
    date_creation = db.Column(db.Date)

class Devoir(db.Model):
    __tablename__ = 'devoir'
    idd = db.Column(db.Integer, primary_key=True, nullable=False)
    date_creation = db.Column(db.Date)
    prof_createur = db.Column(db.Integer, db.ForeignKey('prof.idp'), nullable=False)
    niveau = db.Column(db.String(4), db.ForeignKey('niveau.niveau'))

class Notion(db.Model):
    __tablename__ = 'notion'
    idexo = db.Column(db.Integer, db.ForeignKey('exercice.idex'), primary_key=True)
    notion = db.Column(db.String(20))

class Contenu(db.Model):
    __tablename__ = 'contenu'
    idd = db.Column(db.Integer, db.ForeignKey('devoir.idd'), primary_key=True)
    idex = db.Column(db.Integer, db.ForeignKey('exercice.idex'), primary_key=True)
    bareme = db.Column(db.Float)

class Passage(db.Model):
    __tablename__ = 'passage'
    idd = db.Column(db.Integer, db.ForeignKey('devoir.idd'), primary_key=True)
    idel = db.Column(db.Integer, db.ForeignKey('eleve.idel'), primary_key=True)
    date_passage = db.Column(db.Date, primary_key=True)
    note = db.Column(db.Integer)

# view
class VEtud(db.Model):
    __tablename__ = 'vetud'
    idel = db.Column(db.Integer, primary_key=True, nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(30))
    date_naissance = db.Column(db.Date)
    nbdevoirs = db.Column(db.Integer)

    def __repr__(self):
        return f"<VEtud {self.idel} {self.nom} {self.prenom} {self.date_naissance} {self.nbdevoirs}>"
