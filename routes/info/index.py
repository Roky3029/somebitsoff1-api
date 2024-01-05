from routes.blueprints import info
from fastf1.ergast import Ergast
import datetime
import json


@info.route("/info/constructors")
def constructors():
    ergast = Ergast()
    currentYear = datetime.datetime.now().year
    constructors = ergast.get_constructor_info(currentYear, result_type="raw")

    return json.dumps(constructors)


@info.route("/info/drivers")
def drivers():
    ergast = Ergast()
    currentYear = datetime.datetime.now().year
    drivers = ergast.get_driver_info(currentYear).to_json()

    return drivers
