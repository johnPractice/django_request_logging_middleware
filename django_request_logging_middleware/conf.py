from django.conf import settings

DEFAULTS = {
    "MONGO_URI": "mongodb://localhost:27017",
    "MONGO_DB_NAME": "django_logs",
    "MONGO_COLLECTION_NAME": "exceptions",
    "MIN_STATUS_CODE": 500,
}


class MiddlewareConfig:
    def __init__(self):
        config = getattr(settings, "DJANGO_CAPTURE_REQUEST_ERROR", {})
        for key, value in DEFAULTS.items():
            setattr(self, key, config.get(key, value))


config = MiddlewareConfig()
