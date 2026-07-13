import requests
from config import BASE_URL, API_TOKEN


class YougileAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }

    def create_project(self, title, users=None):
        """
        Создание нового проекта
        """
        url = f"{self.base_url}/projects"
        data = {
            "title": title
        }
        
        if users:
            data["users"] = users
            
        response = requests.post(url, json=data, headers=self.headers)
        return response

    def update_project(self, project_id, title=None, users=None, deleted=None):
        """
        Обновление существующего проекта
        """
        url = f"{self.base_url}/projects/{project_id}"
        data = {}
        
        if title is not None:
            data["title"] = title
        if users is not None:
            data["users"] = users
        if deleted is not None:
            data["deleted"] = deleted
            
        response = requests.put(url, json=data, headers=self.headers)
        return response

    def get_project(self, project_id):
        """
        Получение проекта по ID
        """
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def delete_project(self, project_id):
        """
        Удаление проекта
        """
        return self.update_project(project_id, deleted=True)