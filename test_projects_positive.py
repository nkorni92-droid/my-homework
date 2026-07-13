import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest


class TestCreateProjectPositive:
    """Позитивные тесты на создание проекта"""
    
    def test_create_project_with_required_fields(self, api):
        """Создание проекта только с обязательными полями"""
        response = api.create_project("Новый проект")
        
        print(f"\nTEST CREATE: Status={response.status_code}")
        print(f"TEST CREATE: Response={response.text}")
        
        assert response.status_code == 201, f"Expected 201, got {response.status_code}: {response.text}"
        data = response.json()
        
        # Проверяем, что ответ содержит id
        assert "id" in data, f"Response doesn't contain 'id': {data}"
        
        # Получаем созданный проект для проверки
        get_response = api.get_project(data["id"])
        print(f"TEST GET: Status={get_response.status_code}")
        print(f"TEST GET: Response={get_response.text}")
        
        assert get_response.status_code == 200
        project_data = get_response.json()
        
        # Проверяем название
        title = project_data.get("title") or project_data.get("name")
        assert title is not None, f"Response doesn't contain title/name: {project_data}"
        assert title == "Новый проект"
        
        # Удаляем проект после теста
        api.delete_project(data["id"])
    
    def test_create_project_with_users(self, api):
        """Создание проекта с пользователями (проверяем, принимает ли API)"""
        response = api.create_project(
            title="Проект с пользователями",
            users={"admin": "admin"}
        )
        
        print(f"\nTEST CREATE USERS: Status={response.status_code}")
        print(f"TEST CREATE USERS: Response={response.text}")
        
        # API может принимать или не принимать users при создании
        # Проверяем, что вернулся успех или понятная ошибка
        if response.status_code == 201:
            data = response.json()
            assert "id" in data
            api.delete_project(data["id"])
        else:
            # Если users не поддерживается при создании, это тоже ок
            print("Users field might not be supported on creation")
            assert response.status_code in [400, 422]


class TestUpdateProjectPositive:
    """Позитивные тесты на обновление проекта"""
    
    def test_update_project_title(self, api, created_project):
        """Обновление названия проекта"""
        if not created_project:
            pytest.skip("Failed to create test project")
        
        response = api.update_project(created_project, title="Обновленное название")
        
        print(f"\nTEST UPDATE TITLE: Status={response.status_code}")
        print(f"TEST UPDATE TITLE: Response={response.text}")
        
        # API может возвращать 200 или 201
        assert response.status_code in [200, 201], f"Update failed: {response.text}"
        
        # Проверяем через GET что обновление применилось
        get_updated = api.get_project(created_project)
        print(f"TEST GET AFTER UPDATE: {get_updated.text}")
        
        assert get_updated.status_code == 200
        updated_data = get_updated.json()
        title = updated_data.get("title") or updated_data.get("name")
        assert title == "Обновленное название"
    
    def test_get_project_success(self, api, created_project):
        """Успешное получение проекта"""
        if not created_project:
            pytest.skip("Failed to create test project")
        
        response = api.get_project(created_project)
        
        print(f"\nTEST GET: Status={response.status_code}")
        print(f"TEST GET: Response={response.text}")
        
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert data["id"] == created_project
        # Проверяем что есть хотя бы title
        assert ("title" in data) or ("name" in data), f"No title field: {data}"


class TestDeleteProjectPositive:
    """Позитивные тесты на удаление проекта"""
    
    def test_delete_project_success(self, api):
        """Успешное удаление проекта"""
        # Создаем проект для удаления
        create_response = api.create_project("Проект для удаления")
        assert create_response.status_code == 201
        project_id = create_response.json()["id"]
        
        # Удаляем проект
        delete_response = api.delete_project(project_id)
        print(f"\nTEST DELETE: Status={delete_response.status_code}")
        print(f"TEST DELETE: Response={delete_response.text}")
        
        assert delete_response.status_code in [200, 201, 204]
        
        # Проверяем что проект все еще доступен, но помечен как удаленный
        get_response = api.get_project(project_id)
        print(f"TEST GET DELETED: Status={get_response.status_code}")
        print(f"TEST GET DELETED: Body={get_response.text}")
        
        # API может возвращать 200 с флагом deleted или 404
        if get_response.status_code == 200:
            data = get_response.json()
            # Проверяем что есть флаг deleted
            assert data.get("deleted") == True, f"Project should be marked as deleted: {data}"
            print("Project is marked as deleted (soft delete)")
        else:
            assert get_response.status_code in [404, 403]