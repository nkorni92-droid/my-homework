# test_crud.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Subject, User
from config import DATABASE_URL

@pytest.fixture
def db_session():
    """Создает новую сессию для каждого теста"""
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
    
    # Откат изменений после теста
    session.rollback()
    session.close()

class TestStudentCRUD:
    """Тесты для CRUD операций со студентами"""
    
    def test_create_student(self, db_session):
        """Тест на добавление студента"""
        # Узнаем максимальный user_id
        max_id = db_session.query(Student.user_id).order_by(Student.user_id.desc()).first()
        new_id = (max_id[0] + 1) if max_id and max_id[0] else 1
        
        # Создаем тестового студента
        new_student = Student(
            user_id=new_id,
            level="Beginner",
            education_form="Full-time",
            subject_id=1
        )
        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)
        
        # Проверяем, что студент создан
        assert new_student.user_id == new_id
        assert new_student.level == "Beginner"
        assert new_student.education_form == "Full-time"
        
        # Удаляем тестовые данные
        db_session.delete(new_student)
        db_session.commit()
    
    def test_update_student(self, db_session):
        """Тест на изменение студента"""
        # Создаем студента
        max_id = db_session.query(Student.user_id).order_by(Student.user_id.desc()).first()
        new_id = (max_id[0] + 1) if max_id and max_id[0] else 1
        
        student = Student(
            user_id=new_id,
            level="Beginner",
            education_form="Full-time",
            subject_id=1
        )
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
        
        # Изменяем уровень
        student.level = "Advanced"
        student.education_form = "Part-time"
        db_session.commit()
        db_session.refresh(student)
        
        # Проверяем изменения
        updated_student = db_session.query(Student).filter(
            Student.user_id == new_id
        ).first()
        assert updated_student.level == "Advanced"
        assert updated_student.education_form == "Part-time"
        
        # Удаляем тестовые данные
        db_session.delete(student)
        db_session.commit()
    
    def test_delete_student(self, db_session):
        """Тест на удаление студента"""
        # Создаем студента
        max_id = db_session.query(Student.user_id).order_by(Student.user_id.desc()).first()
        new_id = (max_id[0] + 1) if max_id and max_id[0] else 1
        
        student = Student(
            user_id=new_id,
            level="Beginner",
            education_form="Full-time",
            subject_id=1
        )
        db_session.add(student)
        db_session.commit()
        student_id = student.user_id
        
        # Физическое удаление
        db_session.delete(student)
        db_session.commit()
        
        # Проверяем что запись удалена
        deleted_student = db_session.query(Student).filter(
            Student.user_id == student_id
        ).first()
        assert deleted_student is None

class TestSubjectCRUD:
    """Тесты для CRUD операций с предметами"""
    
    def test_create_subject(self, db_session):
        """Тест на добавление предмета"""
        # Узнаем максимальный subject_id
        max_id = db_session.query(Subject.subject_id).order_by(Subject.subject_id.desc()).first()
        new_id = (max_id[0] + 1) if max_id and max_id[0] else 1
        
        # Создаем предмет
        subject = Subject(
            subject_id=new_id,
            subject_title="Test Subject Python"
        )
        db_session.add(subject)
        db_session.commit()
        db_session.refresh(subject)
        
        assert subject.subject_id == new_id
        assert subject.subject_title == "Test Subject Python"
        
        # Очистка
        db_session.delete(subject)
        db_session.commit()
    
    def test_update_subject(self, db_session):
        """Тест на изменение предмета"""
        max_id = db_session.query(Subject.subject_id).order_by(Subject.subject_id.desc()).first()
        new_id = (max_id[0] + 1) if max_id and max_id[0] else 1
        
        subject = Subject(
            subject_id=new_id,
            subject_title="Original Title"
        )
        db_session.add(subject)
        db_session.commit()
        db_session.refresh(subject)
        
        # Изменяем название
        subject.subject_title = "Updated Title"
        db_session.commit()
        db_session.refresh(subject)
        
        assert subject.subject_title == "Updated Title"
        
        db_session.delete(subject)
        db_session.commit()
    
    def test_delete_subject(self, db_session):
        """Тест на удаление предмета"""
        max_id = db_session.query(Subject.subject_id).order_by(Subject.subject_id.desc()).first()
        new_id = (max_id[0] + 1) if max_id and max_id[0] else 1
        
        subject = Subject(
            subject_id=new_id,
            subject_title="Subject to Delete"
        )
        db_session.add(subject)
        db_session.commit()
        subject_id = subject.subject_id
        
        # Удаление
        db_session.delete(subject)
        db_session.commit()
        
        # Проверка
        deleted = db_session.query(Subject).filter(
            Subject.subject_id == subject_id
        ).first()
        assert deleted is None

class TestUserCRUD:
    """Тесты для CRUD операций с пользователями (бонус)"""
    
    def test_create_user(self, db_session):
        """Тест на добавление пользователя"""
        max_id = db_session.query(User.user_id).order_by(User.user_id.desc()).first()
        new_id = (max_id[0] + 1) if max_id and max_id[0] else 1
        
        # Создаем уникальный email
        test_email = f"test.user.{new_id}@example.com"
        
        user = User(
            user_id=new_id,
            user_email=test_email,
            subject_id=1
        )
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)
        
        assert user.user_id == new_id
        assert user.user_email == test_email
        
        db_session.delete(user)
        db_session.commit()