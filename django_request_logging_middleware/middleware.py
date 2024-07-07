import traceback
from pymongo import MongoClient
from .conf import config


class ExceptionLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Initialize MongoDB client
        self.mongo_client = MongoClient(config.MONGO_URI)
        self.db = self.mongo_client[config.MONGO_DB_NAME]
        self.collection = self.db[config.MONGO_COLLECTION_NAME]

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code >= config.MIN_STATUS_CODE:
            self.log_request_data(request, response)
        return response

    def process_exception(self, request, exception):
        # Log exception details
        exception_details = {
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "request_data": self.get_request_data(request),
        }
        self.collection.insert_one(exception_details)

    def log_request_data(self, request, response):
        request_data = self.get_request_data(request)
        log_entry = {"status_code": response.status_code, "request_data": request_data}
        self.collection.insert_one(log_entry)

    def get_request_data(self, request):
        return {
            "url": request.build_absolute_uri(),
            "method": request.method,
            "headers": dict(request.headers),
            "body": request.body.decode("utf-8") if request.body else None,
        }
