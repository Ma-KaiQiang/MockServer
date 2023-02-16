from colorama import Fore, Back, Style, init
import requests, json
import re
import logging

logger = logging.getLogger('django')


def json_beautify(data):
    if not isinstance(data, dict):
        data = json.loads(data)
    data_ = json.dumps(data, skipkeys=True, sort_keys=True, indent=2)
    data_ = data_.encode('utf-8').decode('unicode_escape')
    print(Fore.YELLOW + data_)


def request(func):
    def wrapper(*args, **kwargs):
        url = kwargs.get('url')
        params = kwargs.get('params')
        body = kwargs.get('json')
        headers = kwargs.get('headers')

        if body:
            if isinstance(body, str):
                body = eval(body)
            else:
                pass
        else:
            body = None

        if headers:
            headers = eval(headers)
        else:
            headers = None
        func_name = func.__name__

        try:

            print(Fore.LIGHTMAGENTA_EX + 'requests parameter：', end='\n\n')
            json_beautify(kwargs)
            res = func(*args, url=url, params=params, json=body, headers=headers)
            print(Fore.GREEN + '-' * 80 + ' Response ' + '-' * 80, end='\n\n')
            print(
                Fore.LIGHTMAGENTA_EX + f'response parameter：\t\tstatus code：{res.status_code}\t\tresponse time：{res.elapsed.total_seconds()} ',
                end='\n\n')
            json_beautify(res.text)
            return res
        except Exception as msg:
            print("warning: {}".format(msg))
            return False

    return wrapper


class RequestBusiness():

    @request
    def post(self, **kwargs):
        response = requests.post(url=kwargs.get('url'), params=kwargs.get('params'),
                                 json=kwargs.get('body'), headers=kwargs.get('headers'), timeout=10,
                                 )
        return response

    @request
    def get(self, **kwargs):
        response = requests.get(url=kwargs.get('url'), params=kwargs.get('params'), headers=kwargs.get('headers'),
                                timeout=10)
        return response

    @request
    def put(self, **kwargs):
        response = requests.put(url=kwargs.get('url'), params=kwargs.get('params'), json=kwargs.get('body'),
                                headers=kwargs.get('headers'), timeout=10)
        return response

    @request
    def delete(self, **kwargs):
        response = requests.delete(url=kwargs.get('url'), params=kwargs.get('params'), json=kwargs.get('body'),
                                   headers=kwargs.get('headers'), timeout=10)
        return response

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return


def request_(method, url, body=None, headers=None, params=None):
    structure = {
        "url": url,
        "body": body,
        "params": params,
        "headers": headers

    }
    with RequestBusiness() as r:
        if method == 'get':
            res = r.get(structure)
        elif method == 'post':
            res = r.post(structure)
        elif method == 'put':
            res = r.put(structure)
        elif method == 'delete':
            res = r.delete(structure)
        else:
            logger.warning('请输入正确的请求方式')
            return False
        return res

