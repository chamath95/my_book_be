from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "status": 0,
            "data": response.data
        }

    return response
