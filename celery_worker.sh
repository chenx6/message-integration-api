#!/usr/bin/bash
celery -A 'celery_app.worker' worker # --beat