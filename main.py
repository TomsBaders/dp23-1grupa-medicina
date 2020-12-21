from flask import Flask, render_template, redirect, request
import json
import math
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

# Sataisīju pamata importus [Niks]
client  = MongoClient("") # Jāievieto MongoDB tokens [Niks]

db = client['guest']
med_db = db['medicina']
slimnicas_db = db['slimnicas']
arsti_db = db['arsti']
# Datubāžu setup, šitos nosaukumus vai nu likt iekšā Mongo, vai nomainīt uz izvēlētajiem [Niks]


app = Flask(__name__)

# Te vajag ievietot "get_pages" definējumu. Sākumā BIJA ievietots, taču kaut kas nebija noslēgts un nevarēju turpināt rakstīt kodu  [Niks]

# Šeit vajag būt "get_page_by_id" definēšanai, neizdevās to pāŗveidot slimnīcu vairantam [Niks]

@app.route('/')
def home():
    return render_template("home.html") # tātad jāveido home.html failu [Niks]

@app.route("/search")
def search():
    slimnicasNosaukums = set()
    amats = set()
    pieejamiba = set() # šie 3 ir tiešas prasības no uzdevuma formulējuma. [Niks]

    #Te jāievieto FOR loop lai dabūtu slimnīcas, darbības jomas un pieejamības [Niks]

    return render_template("search.html")

# Pagaidām nerakstīšu vairāk, jo nav neviena pamata lapa. [Niks]