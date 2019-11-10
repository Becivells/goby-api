'''
goby python api

https://gobies.org/

from goby.v1 import GobyApi
from goby.v1 import data

z = GobyApi()
print(z.client.version())
envi= z.client.getEnvi()
print(envi)
print(z.client.tasks())
scanresult = z.client.startScan(ips=["192.168.3.32"],ports=data.ports.ALL_Ports,opt_interface="en0")

接口一共有三个模块 client、poc、asset 所有与客户端相关的都放到 client 与资产相关的放到 asset 与 poc 相关的放到 poc
'''

from .version import version

__version__ = version