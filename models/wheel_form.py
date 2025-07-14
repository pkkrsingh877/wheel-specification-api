from sqlalchemy import Column, String, JSON
from database.session import Base

class WheelForm(Base):
    __tablename__ = "wheel_forms"

    formNumber = Column(String, primary_key=True, index=True)
    submittedBy = Column(String, nullable=False)
    submittedDate = Column(String, nullable=False)
    fields = Column(JSON, nullable=False)