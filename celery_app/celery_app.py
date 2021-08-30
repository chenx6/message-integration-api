from celery import Celery

# TODO 用 Redis 或者 RabbitMQ 代替 SQLite
celery_app = Celery(
    broker="sqla+sqlite:///instance/celery_broker.db",
    backend="db+sqlite:///instance/celery_backend.db",
)

celery_app.config_from_object("celery_app.celeryconfig")
