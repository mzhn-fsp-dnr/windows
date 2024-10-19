import requests
from app.schemas.service_schema import ServiceSchema
from app.core.config import conf_settings

# URL микросервиса
API_URL = conf_settings.SERVICES_URL

def get_service_by_id(service_id: str) -> ServiceSchema:
    try:
        response = requests.get(f'{API_URL}/{service_id}')

        data = response.json()
        result = ServiceSchema(**data)

        return result
    except requests.RequestException as e:
        print("ERROR: ", e)
        return None