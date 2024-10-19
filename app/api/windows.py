from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas import windows_schema
import app.services.window as window_service 
import app.services.services as services_service
from uuid import UUID

router = APIRouter()

@router.post("/")
def create_window(window: windows_schema.WindowBase, db_session: Session = Depends(get_db)):
    """
    Создание нового окна
    """
    return window_service.create_window(db_session, window)

@router.delete("/{id}")
def delete_window(id: UUID, db_session: Session = Depends(get_db)):
    """"Удаление окна"""
    
    found = window_service.delete_window(db_session, id)
    if not found:
        raise HTTPException(status_code=404, detail="Окно не найдено")
    return found

@router.get("/{id}")
def get_window(id: UUID, db_session: Session = Depends(get_db)):
    """Получение окна по id"""
    
    window_found =  window_service.get_window(db_session, id)
    if not window_found:
        raise HTTPException(status_code=404, detail="Окно не найдено")
    
    services = []
    for wc in window_found.services:
        services.append(services_service.get_service_by_id(wc.service_id))
        
    wc = window_found.as_dict()
    wc['services'] = services
    return wc

@router.put("/{id}")
def update_window(id: UUID, window: windows_schema.WindowBase, db_session: Session = Depends(get_db)):
    window_found = window_service.get_window(db_session, id)
    if not window_found:
        raise HTTPException(status_code=404, detail="Окно не найдено")
    return window_service.update_window(db_session, id, window)

@router.post("/{id}/link/{service_id}")
def link_service_to_window(id: UUID, service_id: UUID, db_session: Session = Depends(get_db)):
    """Связывание окна и сервиса"""
    
    window_found = window_service.get_window(db_session, id)
    if not window_found:
        raise HTTPException(status_code=404, detail="Окно не найдено")
    
    return window_service.link_service_to_window(db_session, id, service_id)

@router.post("/{id}/unlink/{service_id}")
def unlink_service_from_window(id: UUID, service_id: UUID, db_session: Session = Depends(get_db)):
    """Отвязывание окна и сервиса"""
    
    window_found = window_service.get_window(db_session, id)
    if not window_found:
        raise HTTPException(status_code=404, detail="Окно не найдено")
    
    return window_service.unlink_service_from_window(db_session, id, service_id)
