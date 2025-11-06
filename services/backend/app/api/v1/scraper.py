from fastapi import APIRouter, HTTPException,Depends
from pydantic import BaseModel
from services.scraper.extractor import extract_page
from services.backend.app.ai.summarizer import summarizer
from services.backend.app.db.models import WebPage
from services.backend.app.db import SessionLocal
router = APIRouter(
    prefix="/api/v1/scrape",
    tags=["Scraper"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

class ScrapeRequest(BaseModel):
    url: str
    summarize:bool = True ## for automatic summary of the given info

@router.post("/")
async def scrape_url(req: ScrapeRequest, db=Depends(get_db)):
    try:
        existing_page = db.query(WebPage).filter(WebPage.url == req.url).first()
        if existing_page:
            return {"status": "exists", "data": existing_page.id}
        result = extract_page(req.url)
        summary = summarizer(result["cleaned_text"]) if req.summarize else ""

        page = WebPage(
            url=req.url,
            title=result["title"],
            description=result["description"],
            cleaned_text=result["cleaned_text"],
            summary=summary,
            word_count=result["word_count"]
        )

        db.add(page)
        db.commit()
        db.refresh(page)
        return {"status": "success", "data": page.id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

