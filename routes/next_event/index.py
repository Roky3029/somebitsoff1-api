from routes.blueprints import next_event
import datetime
import fastf1


@next_event.route("/next_event")
def next_event():
    next_event = fastf1.get_events_remaining()

    if not next_event.empty:
        return next_event.to_json()
    else:
        currentYear = datetime.datetime.now().year
        date_var = datetime.datetime(currentYear + 1, 1, 1)
        next_events = fastf1.get_events_remaining(dt=date_var)
        next_event = next_events.iloc[0].to_json()
        return next_event
