from routes.blueprints import standings
from fastf1.ergast import Ergast
import datetime
import json


@standings.route("/standings/constructors")
def constructors():
    ergast = Ergast()
    currentYear = datetime.datetime.now().year
    standings = None
    standings = ergast.get_constructor_standings(currentYear, result_type="raw")

    if not standings:
        standings = ergast.get_constructor_standings(currentYear - 1, result_type="raw")

    return json.dumps(standings)


@standings.route("/standings/drivers")
def drivers():
    ergast = Ergast()
    currentYear = datetime.datetime.now().year
    standings = None
    standings = ergast.get_driver_standings(currentYear, result_type="raw")

    if not standings:
        standings = ergast.get_driver_standings(currentYear - 1, result_type="raw")

    return json.dumps(standings)
