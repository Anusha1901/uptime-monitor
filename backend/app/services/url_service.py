from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.models import HealthCheck, URL
from app.schemas.schemas import URLStatusResponse


def get_all_urls_with_latest_status(db: Session):
    """
    Returns every monitored URL along with its latest health check.
    """

    latest_checks = (
        db.query(
            HealthCheck.url_id,
            func.max(HealthCheck.checked_at).label("latest_checked"),
        )
        .group_by(HealthCheck.url_id)
        .subquery()
    )

    results = (
        db.query(URL, HealthCheck)
        .outerjoin(
            latest_checks,
            URL.id == latest_checks.c.url_id,
        )
        .outerjoin(
            HealthCheck,
            (HealthCheck.url_id == latest_checks.c.url_id)
            & (HealthCheck.checked_at == latest_checks.c.latest_checked),
        )
        .all()
    )

    response = []

    for url, latest in results:
        response.append(
            URLStatusResponse(
                id=url.id,
                url=url.url,
                status="UP" if latest and latest.is_up else "DOWN",
                status_code=latest.status_code if latest else None,
                response_time=latest.response_time if latest else None,
                last_checked=latest.checked_at if latest else None,
                error_message=latest.error_message if latest else None,
            )
        )

    return response