from routes.blueprints import circuits
from fastf1.ergast import Ergast
import datetime
import json


@circuits.route("/circuits")
def circuit_list():
    ergast = Ergast()
    currentYear = datetime.datetime.now().year
    circuits = ergast.get_circuits(currentYear, result_type="raw")

    return json.dumps(circuits)
