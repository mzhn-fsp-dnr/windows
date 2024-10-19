from sqlalchemy.orm import Session
from app.schemas import windows_schema, common
from app.models import window_model
from typing import List

def get_window(db_session: Session, id: str):
        return db_session.query(window_model.Window).filter(window_model.Window.id == id).first()


def create_window(db_session: Session, window: windows_schema):
        db_window =  window_model.Window(**window.dict())
        db_session.add(db_window)
        db_session.commit()
        db_session.refresh(db_window)
        return db_window

def delete_window(db_session: Session, id: str):
        db_window = get_window(db_session, id)
        if db_window:
                db_session.delete(db_window)
                db_session.commit()
        return db_window 

def update_window(db_session: Session, id:str, window: windows_schema):
        db_window = get_window(db_session, id)
        if db_window:
                db_window.name = window.name
                db_session.add(db_window)
                db_session.commit()
        return db_window

def link_service_to_window(db_session: Session, window_id: str, service_id: str):
        db_window = get_window(db_session, window_id)
        if db_window:
                db_window_service =  window_model.WindowService(service_id=service_id, window_id=window_id)
                db_window.services.append(db_window_service)
                db_session.add(db_window)
                db_session.commit()
        return db_window

def unlink_service_from_window(db_session: Session, window_id: str, service_id: str):
        db_window = get_window(db_session, window_id)
        if db_window:
                db_window_service =  window_model.WindowService(service_id=service_id, window_id=window_id)
                db_window.services.remove(db_window_service)
                db_session.add(db_window)
                db_session.commit()
        return db_window