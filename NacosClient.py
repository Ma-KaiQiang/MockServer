import uvicorn

from nacos import NacosClient


def register_server_to_nacos(service_ip, port, service_name, namespaceId, namespace, group):
    """
    注册服务到nacos
    :param service_ip:  django启动的服务所在的ip
    :param port:  django启动的服务所在的端口
    :param service_name:  服务名称
    :param namespaceId:  命名空间Id
    :param namespace: 命名空间
    :return: None
    """
    nacos_client = NacosClient('http://127.0.0.1', 8848)  # Nacos注册中心提供的ip和端口
    # 注册服务
    try:
        response = nacos_client.instance().register(ip=service_ip, port=port, serviceName=service_name, ephemeral=True )
        # ephemeral=True,namespaceId=namespaceId, namespace=namespace, groupName=group
        print('register', response)
    except Exception as e:
        print('register err:')
        print(e.__str__())

    # 查询服务详情
    try:
        response = nacos_client.instance().detail(ip=service_ip, port=port, serviceName=service_name,
                                                  namespaceId=namespaceId)
        print('detail', response)
    except Exception as e:
        print(e.__str__())

    # 自动心跳包
    try:
        response = nacos_client.instance().auto_beat(ip=service_ip, port=port, serviceName=service_name,
                                                     namespaceId=namespaceId)
        print('send_beat', response)
    except Exception as e:
        print('send beat err:')
        print(e.__str__())


if __name__ == '__main__':
    # django运行服务地址
    service_ip = '10.27.128.158'
    # django运行服务名称
    service_name = 'service.django'
    # django命名空间ID
    namespaceId = '628da9e7-d34d-4e0c-b87e-118807ecca70'
    # django命名空间
    namespace = 'hsc-nwpu-django-namespace'
    # django组
    group = 'hsc-nwpu-django-group'
    # django服务器运行端口
    port = 8888

    register_server_to_nacos(service_ip, port, service_name, namespaceId, namespace, group)
    # discover_service_on_nacos(service_name)

    # uvicorn运行django程序
    uvicorn.run("app_backen.asgi:application", host="0.0.0.0", port=port, log_level="info", reload=False)

