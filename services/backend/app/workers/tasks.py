from celery import Celery
from services.scraper.extractor import extract_page

# ✅ Proper Celery initialization
celery_app = Celery(
    "webbrain_worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery_app.task(name="scrape_url_task")
def scrape_url_task(url: str) -> dict:
    """
    Background task to scrape and extract data from a given URL.
    """
    try:
        result = extract_page(url)
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
