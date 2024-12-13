# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
# session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """Home page displays all possible queries"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= '2016-08-23').all()
    session.close()


    result_dict = [{'date': result.date,
                   'prcp': result.prcp} for result in results]
    return jsonify(result_dict)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(station.station).all()
    session.close()

    all_stations = list(np.ravel(results))
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results = session.query(measurement.tobs).filter(measurement.date >='2016-08-23', measurement.station == 'USC00519281').all()
    session.close()

    all_tobs = list(np.ravel(results))
    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>", methods=['GET'])
def start(start):
    session = Session(engine)
    temperatures = session.query(func.min(measurement.tobs).label('min_temp'),
                                 func.avg(measurement.tobs).label('avg_temp'),
                                 func.max(measurement.tobs).label('max_temp')).filter(measurement.date >= f"{start}").all()
    session.close()

    result = {'min_temp': temperatures[0].min_temp,
              'avg_temp': temperatures[0].avg_temp,
              'max_temp': temperatures[0].max_temp}
    return jsonify(result)


@app.route("/api/v1.0/<start>/<end>", methods=['GET'])
def start_to_end(start, end):
    session = Session(engine)
    temperatures = session.query(func.min(measurement.tobs).label('min_temp'),
                                 func.avg(measurement.tobs).label('avg_temp'),
                                 func.max(measurement.tobs).label('max_temp')).filter(measurement.date >= f"{start}",
                                                                                      measurement.date <= f"{end}").all()
    session.close()

    result = {'min_temp': temperatures[0].min_temp,
              'avg_temp': temperatures[0].avg_temp,
              'max_temp': temperatures[0].max_temp}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)