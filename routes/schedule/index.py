from routes.blueprints import schedule
import datetime
import fastf1


@schedule.route("/schedule")
def schedule():
    currentYear = datetime.datetime.now().year
    schedule = fastf1.get_event_schedule(currentYear).to_json()

    return schedule
