from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.database import get_db
from app.database.models import URL
from app.schemas.schemas import URLCreate
from app.schemas.schemas import URLResponse
from app.database.models import HealthCheck
from app.schemas.schemas import URLStatusResponse
from app.services.url_service import get_all_urls_with_latest_status

router = APIRouter()


@router.post("/urls", response_model=URLResponse)
def add_url(url: URLCreate, db: Session = Depends(get_db)):

    existing_url = db.query(URL).filter(URL.url == str(url.url)).first()

    if existing_url:
        raise HTTPException(
            status_code=400,
            detail="URL already exists."
        )

    new_url = URL(url=str(url.url))

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return new_url


@router.get("/urls", response_model=list[URLStatusResponse])
def get_urls(db: Session = Depends(get_db)):
    return get_all_urls_with_latest_status(db)