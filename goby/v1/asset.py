'''
内部接口请不要直接调用
'''

import sys
from urllib.parse import urljoin


class Asset():
    '''
    goby 资产查询，主要用于任务分发和一些其他操作
    '''

    def __init__(self, apiurl: str, core: dict(type=object, help="需要实现Core对象")):
        '''
        :param apiurl:
        :param core:
        '''
        self.apiurl = apiurl + '/' + '/api/v1/'
        self._request = core

    def getHostLists(self, taskId, **kwargs) -> dict:
        '''
        得到某次扫描任务的存活的ip

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

    def getWebList(self, taskId, **kwargs) -> dict:
        '''
        得到某次扫描任务所有的 Web 列表

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

    def getIPInfo(self, taskId, ip, **kwargs) -> dict:
        '''
        查看某个 IP 资产信息

        :param taskId:
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        kwargs.update({
            "ip": ip,
            "taskId": taskId
        })

        return self._request.post(url, json=kwargs)

    def assetTags(self, taskId, **kwargs) -> dict:
        '''
        网络结构图

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

    def getValueCategory(self, taskId, **kwargs) -> dict:
        '''
        得到某次任务资产的分类信息

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

    def assetSearch(self, query, opt_order: dict = None, opt_page=1, opt_page_size=20, **kwargs) -> dict:
        '''
        资产搜索
        :param query: "taskId=\"20191107141215\""  port  vulname  product 组件 protocol parent_category 资产类型
        :param opt_order:  {
              "vulnerabilities": "desc",
              "assets": "desc"
            }
        :param opt_page:
        :param opt_size:
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        if opt_order is None:
            opt_order = {
                "vulnerabilities": "desc",
                "assets": "desc"
            }

        kwargs.update({
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

    def getChildrenCategory(self, query=None, **kwargs) -> dict:
        '''
        得到某次任务某类资产信息
        todo 友好查询方式

        :param query:  "taskId=\"20191106163230\" && parent_category=\"Support System\""
            'Support System'
            'Software System'
             Enterprise Application
             Network Device
        Network Security
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)
        kwargs.update({
            "query": query
        })

        return self._request.post(url, json=kwargs)

    def exportAssets(self, taskId, **kwargs) -> dict:
        '''
        导出资产
        :param kwargs:
        :return: json
            statusCode 状态码
            messages   信息
            data       返回数据
        '''
        kwargs.update({
            "taskId": taskId
        })
        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        return self._request.get_content(url, data=kwargs)

    def ipSegment(self, taskId, ipb, type=1, **kwargs) -> dict:
        '''
        IP矩阵图
        :param taskId:
        :param ipb:
        :param type:
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)
        kwargs.update({
            "taskId": taskId,
            "type": type,
            "ipb": ipb
        })

        return self._request.post(url, json=kwargs)
# /api/getCrawlerURLs

    def getCrawlerURLs (self, taskId,hostInfo, **kwargs) -> dict:
        '''
        某次扫描任务进度查询

        :param taskId: 任务编号
        :param hostInfo: 扫描的 url http://xxx.com
        :param kwargs:
        :return:
            statusCode 状态码
            messages   信息
            data       返回数据
        '''

        url = urljoin(self.apiurl, sys._getframe().f_code.co_name)

        kwargs.update({
            "taskId": taskId,
            "hostInfo":hostInfo
        })

        return self._request.post(url, json=kwargs)