from flask import Flask

from models import *
from flask import render_template

@app.route('/prof')
def get_prof():
    profs = Prof.query.all()
    return render_template('prof.html', profs=profs)

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
