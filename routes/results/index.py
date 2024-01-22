from routes.blueprints import results
import fastf1
import datetime


@results.route("/results/<round>")
def next_event(round):
    try:
        year = datetime.datetime.now().year
        session = fastf1.get_session(int(year), int(round), "R")
        session.load()

        print(session.results)

        return session.results.to_json()
    except fastf1.core.DataNotLoadedError:
        year = datetime.datetime.now().year
        event = fastf1.get_event(year, round).to_json()

        return event

