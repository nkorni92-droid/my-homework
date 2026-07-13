import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import requests
from config import BASE_URL, API_TOKEN


class TestCreateProjectNegative:
    """Негативные тесты на создание проекта"""
    
    def test_create_project_without_title(self, api):
        """Создание проекта без обязательного поля title"""
        url = f"{BASE_URL}/projects"
        headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json={}, headers=headers)
        
        print(f"\nTEST CREATE EMPTY: Status={response.status_code}")
        print(f"TEST CREATE EMPTY: Response={response.text}")
        
        assert response.status_code in [400, 422]
    
    def test_create_project_empty_title(self, api):
        """Создание проекта с пустым title"""
        response = api.create_project(title="")
        
        print(f"\nTEST CREATE EMPTY TITLE: Status={response.status_code}")
        print(f"TEST CREATE EMPTY TITLE: Response={response.text}")
        
        assert response.status_code in [400, 422]
    
    def test_create_project_with_invalid_field(self, api):
        """Создание проекта с недопустимым полем (description)"""
        url = f"{BASE_URL}/projects"
        headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }
        data = {
            "title": "Test",
            "description": "Should not be here"
        }
        response = requests.post(url, json=data, headers=headers)
        
        print(f"\nTEST CREATE INVALID FIELD: Status={response.status_code}")
        print(f"TEST CREATE INVALID FIELD: Response={response.text}")
        
        assert response.status_code in [400, 422]


class TestUpdateProjectNegative:
    """Негативные тесты на обновление проекта"""
    
    def test_update_nonexistent_project(self, api):
        """Обновление несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api.update_project(fake_id, title="New Title")
        
        print(f"\nTEST UPDATE FAKE: Status={response.status_code}")
        print(f"TEST UPDATE FAKE: Response={response.text}")
        
        assert response.status_code in [404, 403]
    
    def test_update_project_invalid_id(self, api):
        """Обновление проекта с некорректным ID"""
        response = api.update_project("invalid-id", title="New Title")
        
        print(f"\nTEST UPDATE INVALID ID: Status={response.status_code}")
        print(f"TEST UPDATE INVALID ID: Response={response.text}")
        
        assert response.status_code in [400, 404, 422]
    
    def test_update_project_empty_title(self, api, created_project):
        """Обновление проекта с пустым названием"""
        if not created_project:
            pytest.skip("Failed to create test project")
        
        response = api.update_project(created_project, title="")
        
        print(f"\nTEST UPDATE EMPTY TITLE: Status={response.status_code}")
        print(f"TEST UPDATE EMPTY TITLE: Response={response.text}")
        
        assert response.status_code in [400, 422]


class TestGetProjectNegative:
    """Негативные тесты на получение проекта"""
    
    def test_get_nonexistent_project(self, api):
        """Получение несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api.get_project(fake_id)
        
        print(f"\nTEST GET FAKE: Status={response.status_code}")
        print(f"TEST GET FAKE: Response={response.text}")
        
        assert response.status_code in [404, 403]
    
    def test_get_project_invalid_id(self, api):
        """Получение проекта с некорректным ID"""
        response = api.get_project("invalid-id")
        
        print(f"\nTEST GET INVALID ID: Status={response.status_code}")
        print(f"TEST GET INVALID ID: Response={response.text}")
        
        assert response.status_code in [400, 404, 422]