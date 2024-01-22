from routes.blueprints import event
import fastf1
import datetime


@event.route("/event/<round>")
def next_event(round):
    year = datetime.datetime.now().year
    event = fastf1.get_event(int(year), int(round))

    return event.to_json()
