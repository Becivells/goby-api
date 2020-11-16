'''
内部接口请不要直接调用
'''

import sys
from enum import Enum
from urllib.parse import urljoin

from . import data


class Client():
    '''
    goby 客户端模式，主要用于任务分发和一些其他操作
    '''

    def __init__(self, apiurl: str, core: dict(type=object, help="需要实现Core对象")):
        '''
        :param apiurl:
        :param core:
        '''

        self.apiurl = apiurl + '/' + '/api/v1/'
        self._request = core

    def version(self, **kwargs) -> dict:
        '''
        得到节点环境信息
        :param kwargs:
        :return: json
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        return self._request.get(url, kwargs)

    def check(self, **kwargs) -> dict:
        '''
       检查节点状态

        :param kwargs:
        :return: json
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        return self._request.get(url, kwargs)

    def getEnvi(self, **kwargs) -> dict:
        '''
        得到节点环境信息

        :param kwargs:
        :return: json
            statusCode 状态码
            messages   信息
            data       返回数据
        '''
        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        return self._request.get(url, kwargs)

    def listAdapters(self, **kwargs) -> dict:
        '''
        列出节点网卡信息

        :param kwargs:
        :return: json
            statusCode 状态码
            messages   信息
            data       返回数据
        '''
        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        return self._request.get(url, kwargs)

    def listSupport(self, **kwargs) -> dict:
        '''
        得到支持的端口信息

        :param kwargs:
        :return: json
            statusCode 状态码
            messages   信息
            data       返回数据
        '''
        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        return self._request.get(url, kwargs)

    def startScan(self, ips: list, ports: data.ports, opt_interface: str,
                  vul_type: data.vul_type = data.vul_type.General_PoC, pocs_hosts=None, opt_queue=0, opt_random=True,
                  opt_rate=100, opt_portscanmode: data.portscanmode = data.portscanmode.Assets_first,
                  opt_screenshot=False,opt_deepAnalysis=True, opt_extracthost=False, opt_fofaFetchSubdomainEnabled=False, opt_fofaEmail="",
                  opt_fofaKey="", opt_fofaFetchSize=100, opt_pingFirst=False, opt_pingCheckSize=10,
                  opt_pingConcurrent=2, opt_pingSendCount=2, opt_proxy=None,
                  **kwargs) -> dict:
        '''
        开始一个扫描任务

        :param ips:      要扫描的 IP 地址
        :param ports:    扫描任务指定要扫描的端口或者默认类型
        :param opt_interface:  用于扫描的网络接口
        :param vul_type:   漏洞类型  General_PoC Brute_Force  All Empty
        :param vul_poc:
        :param opt_queue:
        :param opt_random:  随机 IP 扫描
        :param opt_rate:
        :param opt_portscanmode: # 资产优先或者同时扫描
        :param opt_screenshot:   # 截图
        :param opt_extracthost:  # 自动爬取子域名
        :param opt_fofaFetchSubdomainEnabled:
        :param opt_fofaEmail:
        :param opt_fofaKey:
        :param opt_fofaFetchSize:   # fofa 获取的数据条数
        :param opt_pingFirst:       # ping 扫描优先
        :param opt_pingCheckSize:   # ping 检查次数
        :param opt_pingConcurrent:  # ping 并发数
        :param opt_pingSendCount:   # ping 重发次数
        :param opt_proxy: 代理模式
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        ports = ports.value if isinstance(ports, Enum) else ports
        vul_type = vul_type.value if isinstance(vul_type, Enum) else str(vul_type)
        opt_portscanmode = opt_portscanmode.value if isinstance(opt_portscanmode, Enum) else opt_portscanmode

        if pocs_hosts is None:
            pocs_hosts = []

        kwargs.update({
            "asset": {
                "ips": ips,
                "ports": ports
            },
            "vulnerability": {
                "type": vul_type,
                "pocs": pocs_hosts
            },
            "options": {
                "queue": opt_queue,
                "random": opt_random,
                "rate": opt_rate,
                "interface": opt_interface,
                "portscanmode": opt_portscanmode,  # 扫描方式
                "screenshot": opt_screenshot,  # 网站截图
                "deepAnalysis": opt_deepAnalysis,
                "extracthost": opt_extracthost,  # 自动爬取子域名
                "fofaFetchSubdomainEnabled": opt_fofaFetchSubdomainEnabled,  # 开启 fofa 查询
                "fofaEmail": opt_fofaEmail,  # fofa email
                "fofaKey": opt_fofaKey,  # fofa key
                "fofaFetchSize": opt_fofaFetchSize,  # fofa 获取的数据条数
                "pingFirst": opt_pingFirst,  # ping 扫描优先
                "pingCheckSize": opt_pingCheckSize,  # ping 检查次数
                "pingConcurrent": opt_pingConcurrent,  # ping 并发数
                "pingSendCount": opt_pingSendCount  # ping 重发次数
            }
        })

        if opt_proxy:
            kwargs['options'].update({"proxy": opt_proxy})

        return self._request.post(url, json=kwargs)

    def stopScan(self, taskId, **kwargs) -> dict:
        '''
        停止某个扫描任务

        :param taskId:
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        kwargs.update({
            "taskId": taskId
        })

        return self._request.post(url, json=kwargs)

    def resumeScan(self, taskId, opt_interface, opt_queue=0, opt_rate=100,
                   opt_portscanmode: data.portscanmode = data.portscanmode.Assets_first,
                   opt_screenshot=False, opt_extracthost=False, opt_proxy=None, **kwargs) -> dict:
        '''
        重启一个未完成的扫描任务

        :param taskId:
        :param opt_interface:
        :param opt_queue:
        :param opt_rate:
        :param opt_portscanmode:
        :param opt_screenshot:
        :param opt_extracthost:
        :param opt_proxy:
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        opt_portscanmode = opt_portscanmode.value if isinstance(opt_portscanmode, Enum) else opt_portscanmode

        kwargs.update({
            "taskId": taskId,
            "options": {
                "queue": opt_queue,
                "random": True,
                "rate": opt_rate,
                "interface": opt_interface,
                "portscanmode": opt_portscanmode,
                "proxy": None,
                "screenshot": opt_screenshot,
                "extracthost": opt_extracthost,
                "deepAnalysis": True
            }
        })

        if opt_proxy:
            kwargs['options'].update({"proxy": opt_proxy})

        return self._request.post(url, json=kwargs)

    def deleteTask(self, taskId, **kwargs) -> dict:
        '''
        删除某个扫描任务

        :param taskId:
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        kwargs.update({
            "taskId": taskId
        })

        return self._request.post(url, json=kwargs)

    def tasks(self, **kwargs):
        '''
        得到所有任务信息

        :param kwargs:
        :return: json
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        return self._request.get(url, kwargs)

    def getStatisticsData(self, taskId, **kwargs) -> dict:
        '''
        得到某次扫描任务统计数据

        :param taskId:
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        kwargs.update({
            "taskId": taskId
        })

        return self._request.post(url, json=kwargs)

    def getProgress(self, taskId, **kwargs) -> dict:
        '''
        某次扫描任务进度查询

        :param taskId:
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        kwargs.update({
            "taskId": taskId
        })

        return self._request.post(url, json=kwargs)
