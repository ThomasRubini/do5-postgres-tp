from flask import Flask, request

from models import *
from flask import render_template

@app.route('/prof')
def get_prof():
    profs = Prof.query.all()
    return render_template('prof.html', profs=profs)

@app.route('/add_eleve', methods=['GET'])
def get_eleve():
    return render_template('add_eleve.html')

@app.route('/add_eleve', methods=['POST'])
def add_eleve():
    idel = request.form.get('idel')
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    college = request.form.get('college')
    niveau = request.form.get('niveau')
    date_naissance = request.form.get('date_naissance')
    sexe = request.form.get('sexe')
    try:
        eleve = Eleve(idel=idel, nom=nom, prenom=prenom, college=college, niveau=niveau, date_naissance=date_naissance, sexe=sexe)
        db.session.add(eleve)
        db.session.commit()
    except Exception as e:
        return "Erreur lors de l'ajout de l'élève: " + str(e)
    return 'Eleve ajouté'

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
