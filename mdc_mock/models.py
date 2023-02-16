from django.db import models


# Create your models here.

class MdcMockModel(models.Model):
    STATUS_CODE_CHOICES = (
        (1, 200),
        (2, 403),
        (3, 500),
        (4, 503)
    )
    METHOD = (
        (1, 'GET'),
        (2, 'POST'),
        (3, 'PUT')
    )
    mockName = models.CharField(max_length=100, verbose_name='mock接口名称', default='')
    # 请求触发条件
    requestUrl = models.CharField(max_length=100,verbose_name='请求路径', default=None)
    requestHeaders = models.JSONField(verbose_name='请求头', default=None)
    method = models.IntegerField(choices=METHOD, verbose_name='请求方法', default=2)
    requestParamsKey = models.CharField(max_length=100, verbose_name='请求参数', default=None)
    requestParamsValue = models.CharField(max_length=100, verbose_name='请求参数', default=None)
    requestBody = models.JSONField(verbose_name='请求体', default=None)
    # 响应内容
    responseHeaders = models.JSONField(verbose_name='响应头', default=None)
    responseBody = models.JSONField(verbose_name='响应体', default=None)
    responseStatus_code = models.IntegerField(choices=STATUS_CODE_CHOICES, verbose_name='状态码', default=1)
    responseTime = models.IntegerField(default=4, verbose_name='响应时间')
    remark = models.TextField(max_length=100)
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'mdc_mock_tb'
