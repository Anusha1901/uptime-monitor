from apscheduler.schedulers.background import BackgroundScheduler

from app.database.database import SessionLocal
from app.database.models import HealthCheck
from app.database.models import URL
from app.services.ping_service import ping_url

scheduler = BackgroundScheduler()


def monitor_urls():

    db = SessionLocal()

    try:

        urls = db.query(URL).all()

        for monitored_url in urls:

            result = ping_url(monitored_url.url)

            health_check = HealthCheck(
                url_id=monitored_url.id,
                status_code=result["status_code"],
                response_time=result["response_time"],
                is_up=result["is_up"],
                error_message=result["error_message"],
            )

            db.add(health_check)

        db.commit()

    finally:
        db.close()


def start_scheduler(interval: int):

    scheduler.add_job(
        monitor_urls,
        "interval",
        seconds=interval,
        id="url_monitor",
        replace_existing=True,
    )

    scheduler.start()