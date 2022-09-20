# Import dependencies

import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# setup the database
engine = create_engine('sqlite:///hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# setup Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    o = '''
        <dl>
        <dt>Welcome to the Hawaii Climate Analysis API</dt>
        <dt>Available Routes:</dt>
        <dt>/api/v1.0/precipitation</dt>
        <dt>/api/v1.0/stations</dt>
        <dt>/api/v1.0/tobs</dt>
        <dt>/api/v1.0/temp/start/end</dt>
        </dl>''' 
    return(o)




''' def welcome():
    return(
  
    Welcome to the Climate Analysis API!\n
    Available Routes:\n
    /api/v1.0/precipitation\n
    /api/v1.0/stations\n
    /api/v1.0/tobs\n
    /api/v1.0/temp/start/end
)
   '''  

        
    
''' def welcome():
    o = (f'Welcome to the Hawaii Climate Analysis API\n'
         f'Available Routes:\n'
         f'/api/v1.0/precipitation\n'
         f'/api/v1.0/stations\n'
         f'/api/v1.0/tobs\n'
         f'/api/v1.0/temp/start/end')

    print(o)
    return(o) '''


