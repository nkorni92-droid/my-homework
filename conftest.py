import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from api.yougile_api import YougileAPI


@pytest.fixture
def api():
    return YougileAPI()


@pytest.fixture
def created_project(api):
    """
    Фикстура для создания временного проекта и его удаления после теста
    """
    response = api.create_project("Test Project for Testing")
    print(f"\nFIXTURE CREATE: Status={response.status_code}")
    print(f"FIXTURE CREATE: Body={response.text}")
    
    if response.status_code == 201:
        data = response.json()
        project_id = data.get("id")
        print(f"FIXTURE: Created project with id={project_id}")
        
        # Получаем проект, чтобы увидеть его структуру
        get_response = api.get_project(project_id)
        print(f"FIXTURE GET: Status={get_response.status_code}")
        print(f"FIXTURE GET: Body={get_response.text}")
        
        yield project_id
        
        # Удаляем проект после теста
        delete_response = api.delete_project(project_id)
        print(f"FIXTURE DELETE: Status={delete_response.status_code}")
    else:
        print(f"FIXTURE: Failed to create project")
        yield None