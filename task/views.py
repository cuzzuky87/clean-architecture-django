from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.exceptions import NotFound, ValidationError, APIException
from .entities import DomainException
from .use_case import TaskUseCase


def postpone_task(request, id):
    # validate
    # call use case
    # handleException
    # return serialized data
    pass