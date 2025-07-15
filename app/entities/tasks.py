from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, text, DateTime

from ..database import Base


class Tasks(Base):
    __tablename__="tasks"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, server_default=text("false"), default=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), default=datetime.now)
    