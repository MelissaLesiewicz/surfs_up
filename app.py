import datetime as dt
from flask.globals import session
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy import engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify

#create engine
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, relflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

# create app
app = Flask(__name__)

# create app route
@app.route('/')

def welcome():
    return (
        '''
        Welcome to teh Climate Analysis API!
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
        ''')
    
