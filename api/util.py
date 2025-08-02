import json
import logging

import redis
from sqlalchemy.orm import Session

import config
from models import Todo

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
)
logger = logging.getLogger(__name__)


def check_postgres():
    try:
        db = next(config.get_db())
        db.execute("SELECT 1")
        return {"status": "healthy"}
    except Exception as e:
        logger.error(f"Postgres health check failed: {e}")
        return {"status": "unhealthy"}


def check_redis():
    try:
        r = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)
        r.ping()
        return {"status": "healthy"}
    except Exception as e:
        logger.error(f"Redis health check failed: {e}")
        return {"status": "unhealthy"}


def check_elasticmq():
    # Implement check according to your setup
    try:
        # Example placeholder, replace with actual check
        return {"status": "healthy"}
    except Exception as e:
        logger.error(f"ElasticMQ health check failed: {e}")
        return {"status": "unhealthy"}


def get_all_todos(db: Session):
    return db.query(Todo).all()


def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def get_cached_todos():
    r = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)
    todos_json = r.get("todos")
    if todos_json:
        return json.loads(todos_json)
    return None


def get_cached_todo(todo_id: int):
    r = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)
    todo_json = r.get(f"todo:{todo_id}")
    if todo_json:
        return json.loads(todo_json)
    return None


def create_todo(db: Session, todo_data: dict):
    todo = Todo(**todo_data)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def update_todo(db: Session, todo_id: int, update_data: dict):
    todo = get_todo_by_id(db, todo_id)
    if not todo:
        return None
    for key, value in update_data.items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo_id: int):
    todo = get_todo_by_id(db, todo_id)
    if todo:
        db.delete(todo)
        db.commit()
        return True
    return False


def send_notification(todo_id: int, event_type: str, data: dict = None):
    # Your SQS or notification logic here
    logger.info(f"Notification sent for todo_id={todo_id} event={event_type}")


# Add two blank lines before next function according to flake8
