'''
内部接口请不要直接调用
'''

import sys
from urllib.parse import urljoin


class Poc():
    '''
    goby Poc 管理
    '''

    def __init__(self, apiurl: str, core: dict(type=object, help="需要实现Core对象")):
        '''
        :param apiurl:
        :param core:
        '''
        self.apiurl = apiurl + '/' + '/api/v1/'
        self._request = core

    def getPocs(self, taskId, query, opt_reloadPocs=False, opt_order=None, opt_page=0, opt_page_size=10000,
                **kwargs) -> dict:
        '''
        得到 Pocs 列表

        :param taskId:
        :param query: "vultype=0 && vulcategory=\"all\""
        :param opt_reloadPocs:
        :param opt_order:
        :param opt_page:
        :param opt_size:
        :param kwargs:
        :return:
        '''
        '''
        得到PoC列表
        :param kwargs:
        :return: json
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        if opt_order is None:
            opt_order = {
                "vul_nums": "desc",
                "level": "desc",
                "host_nums": "desc"
            }
        kwargs.update({
            "taskId": taskId,
            "query": query,
            "options": {
                "reloadPocs": opt_reloadPocs,
                "order": opt_order,
                "page": {
                    "page": opt_page,
                    "size": opt_page_size
                }
            }
        })

        return self._request.post(url, json=kwargs)

    def vulnerabilityStatisticsData(self, taskId, **kwargs) -> dict:
        '''
        漏洞信息统计

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

    def vulnerabilitySearch(self, taskId, query, type="vulnerability", opt_order=None, opt_page=1, opt_page_size=20,
                            **kwargs) -> dict:
        '''
        漏洞信息搜索

        :param taskId:
        :param query:  "taskId=\"20191106163230\""
        :param type:
        :param opt_order:
        :param opt_page:
        :param opt_page_size:
        :param kwargs:

        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        if opt_order is None:
            opt_order = {
                "level": "desc",
                "nums": "desc"
            }

        kwargs.update({
            "taskId": taskId,
            "type": type,
            "query": query,
            "options": {
                "order": opt_order,
                "page": {
                    "page": opt_page,
                    "size": opt_page_size
                }
            }
        })

        return self._request.post(url, json=kwargs)

    def getPOCInfo(self, vulname, **kwargs) -> dict:
        '''
        得到 poc 详情

        :param vulname:
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        kwargs.update({
            "vulname": vulname
        })

        return self._request.post(url, json=kwargs)

    def rescanVulnerability(self, taskId, opt_type=0, opt_pocs_hosts: dict = None, **kwargs) -> dict:
        '''
        重新扫描漏洞

        :param vulname:
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        if opt_pocs_hosts is None:
            opt_pocs_hosts = {}

        kwargs.update({
            "taskId": taskId,
            "options": {
                "type": opt_type,
                "pocs_hosts": opt_pocs_hosts
            }
        })

        return self._request.post(url, json=kwargs)
