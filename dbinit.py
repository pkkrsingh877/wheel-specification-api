from database.session import Base, engine
from models.wheel_form import WheelForm  # Import all models you want to create

Base.metadata.create_all(bind=engine)
