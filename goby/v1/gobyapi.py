import requests
from urllib.parse import urljoin
from .client import Client
from .asset import Asset
from .poc import Poc
from goby.version import version


class Api():
    '''
    goby api 接口
    '''

    def __init__(self, apiurl: dict(type=str, help="url eg http://127.0.0.1")="http://127.0.0.1:8361",user:str="",
                 password: dict(type=str, help="密码")="", **kwargs):
        '''

        :param apiurl: apiurl 接口 defalut 127.0.0.1:8631
        :param user: 用户
        :param password:  密码
        :param kwargs:  requests 的参数可以设置到这里如代理,header 等
        '''
        self._apiurl = apiurl
        self._core = _Core((user,password), **kwargs)
        self.client = Client(self._apiurl,self._core)
        self.asset = Asset(self._apiurl,self._core)
        self.poc = Poc(self._apiurl,self._core)

class _Core():
    def __init__(self, auth: tuple, **kwargs):
        self.kwargs = kwargs
        self._header()
        self.session = requests.session()
        self.session.auth = auth

    def _header(self):
        '''
        处理 header 和 ua 头
        :return:
        '''
        if 'headers' in self.kwargs:
            self.kwargs['headers'].update({
                "Content-Type": "application/json"
            })
            if "User-Agent" not in self.kwargs['headers']:
                self.kwargs['headers'].update({
                    "User-Agent": "goby-api %s" % version
                })
        else:
            self.kwargs['headers'] = {
                "Content-Type": "application/json",
                "User-Agent": "goby-api %s" % version
            }
        if 'verify' not in self.kwargs:
            self.kwargs['verify'] = False

    def get(self, url: dict(type="", help="这是一个url"), data: dict) -> dict:
        '''

        :param url:
        :param data:
        :return:
        '''
        errinfo = {"statusCode": 200, "messages": "", "data": None}
        if data:
            data = "?"+"&".join(["%s=%s"%(k,v)for k,v in data.items()])
        else:
            data = ""
        url = urljoin(url,data)

        try:
            content = self.session.get(url,  **self.kwargs)
            if content.status_code == 200:
                return content.json()
            else:
                raise ValueError("status_code %s is error " % (content.status_code))
        except Exception as e:
            errinfo["messages"] = "goby-api error info: " + str(e)
            return errinfo
    def get_content(self, url: dict(type="", help="这是一个url"), data: dict) -> str:
        '''

        :param url:
        :param data:
        :return:
        '''
        errinfo = {"statusCode": 200, "messages": "", "data": None}
        if data:
            data = "?"+"&".join(["%s=%s"%(k,v)for k,v in data.items()])
        else:
            data = ""
        url = urljoin(url,data)

        try:
            content = self.session.get(url,  **self.kwargs)
            if content.status_code == 200:
                return content.content
            else:
                raise ValueError("status_code %s is error " % (content.status_code))
        except Exception as e:
            errinfo["messages"] = "goby-api error info: " + str(e)
            return errinfo

    def post(self, url: dict(type="", help="这是一个url"), data: dict=None,json=None) -> dict:
        '''
        post 请求数据
        :param url: api
        :param data: json数据
        :param kwargs:
        :return:
        '''
        errinfo = {"statusCode":200,"messages":"","data":None}
        try:
            content = self.session.post(url,data=data, json=json, **self.kwargs)
            if content.status_code == 200:
                return content.json()
            else:
                raise ValueError("status_code %s is error " % (content.status_code))
        except Exception as e:
            errinfo["messages"] = "goby-api error info: " + str(e)
            return errinfo
