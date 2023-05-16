from django.utils.encoding import escape_uri_path
from rest_framework.views import APIView
from rest_framework.response import Response
from mdc_mock.models import MdcMockModel
from mdc_mock.serializers import MdcMockSerializers
from mdc_mock.result import success, error
from django.http import StreamingHttpResponse, HttpResponse
import logging
from django.views.decorators.csrf import csrf_exempt
from mdc_mock.comon.forwarding_requests import request_
import json
from django.shortcuts import render, redirect

logger = logging.getLogger('views')


# Create your views here.

class MdcMockView(APIView):
    @staticmethod
    def get(request):

        # l = MdcMockModel.objects.all()
        # bs = MdcMockSerializers(l, many=True)
        # return success(data=bs.data)
        return render(request, template_name='mock/mock_list_tables.html')

    @staticmethod
    def post(request):
        bs = MdcMockSerializers(data=request.data)
        if bs.is_valid():
            # 名称判重
            if MdcMockModel.objects.filter(mockName=request.data.get('mockName')):
                return error(message='名称不能重复', data=bs.errors)
            else:
                bs.save()
                return success(data=bs.data)
        else:
            return error(message='参数错误', data=bs.errors)

    @staticmethod
    def put(request):
        bs = MdcMockSerializers(data=request.data)
        if bs.is_valid():
            # 名称判重
            if MdcMockModel.objects.filter(mockName=request.data.get('mockName')):
                return error(message='名称不能重复', data=bs.errors)
            else:
                bs.update(instance=MdcMockModel.objects.filter(id=request.data.get('id')).first(),
                          validated_data=bs.validated_data)
                return success(data=bs.data)
        else:
            return error(message='参数错误', data=bs.errors)

    @staticmethod
    def delete(request):
        del_list = request.GET.get('ids')

        logger.info(del_list)
        del_data = MdcMockModel.objects.filter(id__in=del_list).delete()
        return success(data=del_data)


class MdcMockResponseView(APIView):
    @staticmethod
    def get(request):
        url = request.path_info
        params = request.full_path()
        instance = MdcMockModel.objects.filter(requestUrl=url, method=1).first()
        if not instance:
            response = request_(method='get', url=url, params=params)
            return error(message='服务命中失败，请求转移', data=json.loads(response.text))
        return Response(data=instance.requestBody, headers=instance.requestHeaders)

    @staticmethod
    def post(request):
        url = request.path_info
        params = request.full_path()
        instance = MdcMockModel.objects.filter(requestUrl=url, method=2).first()
        if not instance:
            response = request_(method='get', url=url, params=params)
            return error(message='服务命中失败，请求转移', data=json.loads(response.text))
        return Response(data=instance.requestBody, headers=instance.requestHeaders)

    @staticmethod
    def put(request):
        url = request.path_info
        params = request.full_path()
        instance = MdcMockModel.objects.filter(requestUrl=url, method=3).first()
        if not instance:
            response = request_(method='get', url=url, params=params)
            return error(message='服务命中失败，请求转移', data=json.loads(response.text))

        return Response(data=instance.requestBody, headers=instance.requestHeaders)


@csrf_exempt
def file_download(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        file_path = r'D:\files' + '\\' + name
        if name:
            from mdc_mock.comon.tools import FileHandle
            f = FileHandle()
            response = StreamingHttpResponse(f.file_iterator(file_path))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment; filename*=utf-8''{}'.format(escape_uri_path(name))
            return response
        else:
            return HttpResponse()


@csrf_exempt
def file_upload(request):
    if request.method == 'POST':
        file = request.FILES.get('file', None)
        file_name = request.POST.get('name', None)
        file_path = r'D:\files'
        if file:
            with open(file_path + '\\' + file_name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        return HttpResponse()
