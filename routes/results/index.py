from routes.blueprints import results
import fastf1
import datetime


@results.route("/results/<round>")
def round(round):
    try:
        year = datetime.datetime.now().year
        session = fastf1.get_session(int(year), int(round), "R")
        session.load()

        return session.results.to_json()
    except:
        year = datetime.datetime.now().year
        event = fastf1.get_event(int(year), int(round)).to_json()

        return event
