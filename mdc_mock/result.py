# -*- coding:utf-8 -*-

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status


class HttpCode(object):
    success = 0
    error = -1


def result(code=HttpCode.success, message='success', sta=status.HTTP_200_OK, data=None, **kwargs):
    json_dict = {'code': code, 'message': message, 'data': data}
    if kwargs:
        json_dict.update(**kwargs)
    return Response(json_dict, status=sta,**kwargs)


def success(data=None,**kwargs):
    return result(code=HttpCode.success, message='success', data=data,**kwargs)


def error(message='', data=None):
    return result(code=HttpCode.error, message=message, data=data, sta=status.HTTP_500_INTERNAL_SERVER_ERROR)
