from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.backend.app.db import SessionLocal
from services.backend.app.db.models import WebPage
router = APIRouter(prefix="/api/v1/history", tags=["history"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_all_pages(db: Session = Depends(get_db)):
    pages = db.query(WebPage).order_by(WebPage.created_at.desc()).all()
    return pages

@router.get("/{page_id}")
def get_page(page_id: int, db: Session = Depends(get_db)):
    page = db.query(WebPage).filter(WebPage.id == page_id).first()
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    return page