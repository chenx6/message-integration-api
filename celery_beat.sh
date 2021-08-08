#!/usr/bin/bash
celery -A 'celery_app.worker' beat \
    --max-interval 60 \
    -s instance/celerybeat-schedule