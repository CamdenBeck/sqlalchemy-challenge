# sqlalchemy-challenge

Project Overview

    This project queries Hawaii weather data stored in a SQLite database. It then uses that data for a flask API with which a user can query the database.

Installation Steps

    # sqlalchemy-challenge

    ## Installation
    
    ### Prerequisites

    Before you begin, ensure you have met the following requirements:
    - You have installed Python. You can download it from [python.org](https://python.org/downloads/).
    - You have installed [Anaconda](https://www.anaconda.com/products/distribution). You can download it from the Anaconda website.
    - You have a `git` client installed. You can download it from [git-scm.com](https://git-scm.com/).

    ### Clone the Repository
    ```bash
    git clone https://github.com/CamdenBeck/sqlalchemy-challenge.git
    cd sqlalchemy-challenge

Usage Instructions

    Run the app.py file. It will start a server and provide a link to put into a browser. When the page is loaded, it will display different queries to enter. Each query will return some data in the json format.

    Run `app.py` to run the flask API.

API Route Examples

    Static Routes:

        "/api/v1.0/precipitation"
        "/api/v1.0/stations"
        "/api/v1.0/tobs"

    Dynamic Routes:

        "/api/v1.0/<start>"

        - Replace <start> with any date you want (before the end date) to get data during and after the provided date.

        "/api/v1.0/<start>/<end>"

        - Replace <start> and <end> with any dates to get data between the specified dates.

Dependencies List
    
    Install each of these python dependencies using `pip install <python_library>`
    1. matplotlib
    2. numpy
    3. pandas
    4. datetime
    5. sqlalchemy
    6. flask

References

    climate.ipynb starter code:
    “Module 10 Challenge”, https://bootcampspot.instructure.com/courses/6252/assignments/88731?module_item_id=1328218. Accessed 11 Dec. 2024.

    hawaii.sqlite:
    “Module 10 Challenge”, https://bootcampspot.instructure.com/courses/6252/assignments/88731?module_item_id=1328218. Accessed 11 Dec. 2024.

    hawaii_measurements.csv:
    “Module 10 Challenge”, https://bootcampspot.instructure.com/courses/6252/assignments/88731?module_item_id=1328218. Accessed 11 Dec. 2024.

    hawaii_stations.csv:
    “Module 10 Challenge”, https://bootcampspot.instructure.com/courses/6252/assignments/88731?module_item_id=1328218. Accessed 11 Dec. 2024.

    Instructor Mark Flynn and TA Benjamin Chilcoat provided help.