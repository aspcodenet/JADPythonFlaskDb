from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:hejsan123@localhost/testdatabasen'
db = SQLAlchemy(app)

class Bil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=True, nullable=False)
    modell = db.Column(db.String(20), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=True, nullable=False)



class Mat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=True, nullable=False)
    pris = db.Column(db.Integer, unique=True, nullable=False)
    typ = db.Column(db.String(1), unique=True, nullable=False) #Vegetarisk, Kött,

db.create_all()


q = Mat.query.filter_by(typ='V').all()
for x in q:
    print(x)



while(True):
    print("Skapa en ny!!")
    namn = input("Namn")
    pris = int(input("pris"))
    typ = input("typ")
    v1 = Mat(namn=namn, pris=pris, typ=typ)
    db.session.add(v1)
    db.session.commit()

# db.create_all()

# v1 = Bil(namn="Volvo", modell="XC60", year=2016)
# v2 = Bil(namn="Saab", modell="V4", year=1973)

# db.session.add(v1)
# db.session.add(v2)
# db.session.commit()

