

## 版本

```
v1.17.160+beta
```



## 认证方式

1. Basic 认证




## /api/v1/vulnerabilityStatisticsData [poc]

```
POST /api/v1/vulnerabilityStatisticsData HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 27
Authorization: Basic Og==
Host: 127.0.0.1:8361
Connection: close

{"taskId":"20191106163230"}
```





## /api/v1/vulnerabilitySearch [poc]

```
POST /api/v1/vulnerabilitySearch HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 165
Authorization: Basic Og==
Host: 127.0.0.1:8361
Connection: close

{"taskId":"20191106163230","type":"vulnerability","query":"taskId=\"20191106163230\"","options":{"order":{"level":"desc","nums":"desc"},"page":{"page":1,"size":20}}}
```



## /api/v1/version  [client]

### 获取版本 Version

```
GET /api/v1/version HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close
```



## /api/v1/verifyPoc





## /api/v1/tasks [client]

### 获取任务列表

```
GET /api/v1/tasks HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close

```



## /api/v1/stopScan [client]

### 停止扫描

```
POST /api/v1/stopScan HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 27
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close

{"taskId":"20191107120743"}HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 07 Nov 2019 04:16:13 GMT
Content-Length: 66
Connection: close

{"statusCode":500,"messages":"no active task running","data":null}


POST /api/v1/stopScan HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 27
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close

{"taskId":"20191107141215"}
```

## 

## /api/v1/resumeScan [client]

### 重新扫描



```
POST /api/v1/resumeScan HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 180
Authorization: Basic Og==
Host: 127.0.0.1:8361
Connection: close

{"taskId":"20191109233425","options":{"queue":0,"random":true,"rate":1,"interface":"en0","portscanmode":1,"proxy":"socket5://127.0.0.1:1080","screenshot":true,"extracthost":false}}
```





## /api/v1/rescanVulnerability [poc]
```
POST /api/v1/rescanVulnerability HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 66
Authorization: Basic Og==
Host: 127.0.0.1:8361
Connection: close

{"taskId":"20191106163230","options":{"type":"0","pocs_hosts":{}}}HTTP/1.1 200 OK
Content-Type: application/json
Date: Sun, 10 Nov 2019 04:31:29 GMT
Content-Length: 44
Connection: close

{"statusCode":200,"messages":"","data":null}
```



## /api/v1/listSupport  [client]

### 扫描设置

````
GET /api/v1/listSupport HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close

````





## /api/v1/listAdapters [client]

### 列出网卡信息

```
GET /api/v1/listAdapters HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close

HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 07 Nov 2019 06:07:23 GMT
Content-Length: 131
Connection: close

{"statusCode":200,"messages":"","data":[{"Name":"eth0","IP":"10.10.100.96"},{"Name":"lo","IP":"127.0.0.1"},{"Name":"any","IP":""}]}
```



## /api/v1/ipSegment [asset]

```
POST /api/v1/ipSegment HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 56
Authorization: Basic Og==
Host: 127.0.0.1:8361
Connection: close

{"taskId":"20191106163230","type":"1","ipb":"10.10.0.0"}HTTP/1.1 200 OK
Content-Type: application/json
Date: Sun, 10 Nov 2019 03:15:03 GMT
Content-Length: 170
Connection: close

{"statusCode":200,"messages":"","data":{"lists":[{"name":"10.10.100.0","value":42},{"name":"10.10.200.0","value":31},{"name":"10.10.50.0","value":17}],"total":{"ips":3}}}
```



## /api/v1/importAssets
## /api/v1/hostSearch 


## /api/v1/getWebList [f]  [asset]

```
POST /api/v1/getWebList HTTP/1.1
Host: 127.0.0.1:8361
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 27

{"taskId":"20191106163230"}
```



## /api/v1/getValueCategory [asset]

资产搜索

```
POST /api/v1/getValueCategory HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 27
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close

{"taskId":"20191107141215"}
```





## /api/v1/getStatisticsData [client]

getStatisticsData

```
POST /api/v1/getStatisticsData HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 27
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close

{"taskId":"20191107141215"}
```



## /api/v1/getProgress [client]

### 得到进度

```
POST /api/v1/getProgress HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 27
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close

{"taskId":"20191107141215"}
```





## /api/v1/getPocs [poc]

```
POST /api/v1/getPocs HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 194
Authorization: Basic Og==
Host: 127.0.0.1:8361
Connection: close

{"taskId":"20191109233425","query":"vultype=0 && vulcategory=\"all\"","options":{"reloadPocs":false,"order":{"vul_nums":"desc","level":"desc","host_nums":"desc"},"page":{"page":0,"size":10000}}}
```



## /api/v1/getPOCInfo
```
POST /api/v1/getPOCInfo HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 55
Authorization: Basic Og==
Host: 127.0.0.1:8361
Connection: close

{"vulname":"Eternalblue/DOUBLEPULSAR MS17-010 SMB RCE"}
```



## /api/v1/getIPInfo  [fluz] [asset]

```
POST /api/v1/getIPInfo HTTP/1.1
Host: 127.0.0.1:8361
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 44

{"taskId":"20191109232223","ip":"10.10.200.124"}
```



## /api/v1/getHostLists [fluz] [asset]

```
POST /api/v1/getHostLists HTTP/1.1
Host: 127.0.0.1:8361
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/json;charset=UTF-8
Content-Length: 31

{"taskId":"20191109222426"}
```



## /api/v1/getEnvi [client]

### 得到节点环境

```
GET /api/v1/getEnvi HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close
```



```
HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 07 Nov 2019 03:56:08 GMT
Content-Length: 157
Connection: close

{"statusCode":200,"messages":"","data":{"dir":"/home/wenzhi/goby-linux-x64-1.4.76/golib","interface":"eth0","ip":"10.10.100.96","network":"10.10.100.96/16"}}GET /api/v1/getEnvi HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close

```



## /api/v1/getChildrenCategory【asset】

```
POST /api/v1/getChildrenCategory HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 75
Authorization: Basic Og==
Host: 127.0.0.1:8361
Connection: close

{"query":"taskId=\"20191106163230\" && parent_category=\"Support System\""}
```



## /api/v1/exportAssets  [asset]
```
GET /api/v1/exportAssets?taskId=20191106163230 HTTP/1.1
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Authorization: Basic Og==
Host: 127.0.0.1:8361
Connection: close
```



## /api/v1/deleteTask【client】

### 删除任务

```
POST /api/v1/deleteTask HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 27
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close

{"taskId":"20191107135314"}HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 07 Nov 2019 06:10:28 GMT
Content-Length: 44
Connection: close

{"statusCode":200,"messages":"","data":null}
```



## /apiv1/deleteAssets [f err]

```
POST /api/v1/deleteAssets HTTP/1.1
Host: 127.0.0.1:8361
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 49

{"taskId":"20191106163230","ips":["10.10.50.70"]}
```



## /api/v1/debugPoc
## /api/v1/check [client]

```
GET /api/v1/check HTTP/1.1
Host: 127.0.0.1:8361
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
```



## /api/v1/assetTags [asset]
```
POST /api/v1/assetTags HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 27
Authorization: Basic Og==
Host: 127.0.0.1:8361
Connection: close

{"taskId":"20191106163230"}
```





## /api/v1/startScan [client]

### 开始任务  [client]

````
POST /api/v1/startScan HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 766
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close
````

```json
{
  "asset": {
    "ips": [
      "10.10.10.0/24"
    ],
    "ports": "7"
  },
  "vulnerability": {
    "type": "2",
    "pocs_hosts": null   //pocs替换为pocs_hosts
  },
  "options": {
    "queue": 0,
    "random": true,
    "rate": 100,
    "portscanmode": 0,
    "screenshot": true,
    "deepAnalysis": true,
    "extracthost": true,
    "fofaFetchSubdomainEnabled": true,
    "fofaEmail": "",
    "fofaKey": "",
    "fofaFetchSize": 1000,
    "pingFirst": false,
    "pingCheckSize": 10,
    "pingConcurrent": 2,
    "pingSendCount": 2
  }
}
```

返回值
```angular2

{"statusCode":200,"messages":"","data":{"taskId":"20200624115501"}}
```


## /api/v1/assetSearch [asset]

### 得到全部资产

```
POST /api/v1/assetSearch HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 128
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close

{"query":"taskId=\"20191107141215\"","options":{"order":{"vulnerabilities":"desc","assets":"desc"},"page":{"page":1,"size":20}}}
```

### 根据IP查询

```
POST /api/v1/assetSearch HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 143
Authorization: Basic dXNlcjpwYXNz
Host: 10.10.100.96:8361
Connection: close

{"query":"taskId=\"20191107141215\" && ip=\"10.10.200.124\"","options":{"order":{"vulnerabilities":"desc","assets":"desc"},"page":{"size":20}}}
```

## /api/v1/getCrawlerURLs

```
POST /api/v1/getCrawlerURLs HTTP/1.1
Content-Type: application/json;charset=UTF-8
Content-Length: 72
Authorization: Basic Og==
Host: 127.0.0.1:8361
Connection: close

{
"taskId":"20201024231641",
"hostInfo":"http://xx.xx.xx.xx:8080"
}
```

## /api/v1/assetDetail



