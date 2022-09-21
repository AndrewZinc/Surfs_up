# Import dependencies

import datetime as dt
import json
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlite3
from flask import Flask, jsonify, request, url_for

# setup the database
engine = create_engine('sqlite:///hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
#session = Session(engine)

# setup Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    o = """
        <dl>
        <dt>Welcome to the Hawaii Climate Analysis API</dt>
        <dt>Available Routes:</dt>
        <dt>/api/v1.0/precipitation</dt>
        <dt>/api/v1.0/stations</dt>
        <dt>/api/v1.0/tobs</dt>
        <dt>/api/v1.0/temp/start/end</dt>
        </dl>"""
    return(o)
    
@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
        
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
    
@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route('/api/v1.0/tobs')
def temp_monthly():
    session = Session(engine)
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
def stats1(start=None):
    session = Session(engine)
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

@app.route("/api/v1.0/temp/<start>/<end>")
def stats2(start=None, end=None):
    session = Session(engine)
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

