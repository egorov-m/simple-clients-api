from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    handlers = {
        "ValidationError": _handle_validation_error,
        "NotFound": _handle_not_found_error,
        "Http404": _handle_not_found_error
    }

    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    response = response or Response()
    response.data = {
        "status": int(status.HTTP_500_INTERNAL_SERVER_ERROR),
        "code": "INTERNAL_SERVER_ERROR"
    }
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return response


def _handle_not_found_error(exc: NotFound, context, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    response.data = {
        "status": 404,
        "code": "ENTITY_NOT_FOUND"
    }

    return response


def _handle_validation_error(exc: ValidationError, context, response: Response):
    response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    response.data = {
        "status": 422,
        "code": "VALIDATION_EXCEPTION",
        "exceptions": [{
            "field": "",
            "rule": item.code,
            "message": item
        } for item in exc.detail]
    }

    return response


def _handle_generic_error(exc, context, response):
    return response
