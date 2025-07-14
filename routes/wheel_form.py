from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.wheel_form import WheelForm
from schemas.wheel_form import WheelFormCreate, WheelFormResponse
from database.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.wheel_form import WheelForm
from schemas.wheel_form import WheelFormCreate, WheelFormResponse
from database.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/wheel-specifications", response_model=WheelFormResponse, status_code=201)
def create_form(form: WheelFormCreate, db: Session = Depends(get_db)):
    if db.query(WheelForm).filter_by(formNumber=form.formNumber).first():
        raise HTTPException(status_code=400, detail="Form already exists")

    db_form = WheelForm(**form.model_dump())
    db.add(db_form)
    db.commit()
    db.refresh(db_form)

    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": db_form.formNumber,
            "submittedBy": db_form.submittedBy,
            "submittedDate": db_form.submittedDate,
            "status": "Saved"
        }
    }
