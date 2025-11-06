from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WebPage(Base):
    __tablename__ = "web_pages"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(500), unique=True, nullable=False)
    title = Column(String(300))
    description = Column(Text)
    summary = Column(Text)
    cleaned_text = Column(Text)
    word_count = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
