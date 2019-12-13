from qiniu import Auth, put_file, etag
from qiniu import BucketManager
import qiniu.config
import requests
import json
import jsonpath
import time
import os
from config import *

access_key = qiniu_page["access_key"]
secret_key = qiniu_page["secret_key"]
bucket_name = qiniu_page["bucket_name"]
url = qiniu_page['bucket_name']

# 七牛的配置信息

q = Auth(access_key, secret_key)
# 文件上传的七牛空间


# 定义文件的key
key = 'big/file/movic.apk'

# 判断七牛key是否已经存在
buc = BucketManager(q)
res, info1 = buc.stat(bucket_name, key)
if(res != None):
    exit(res.text)

# 上传文件的地址
localfile  = '../movie1.mp4'
if(os.path.exists(localfile) == False):
    exit('文件不存在')

# 获取上传的token
token = q.upload_token(bucket_name, key, 36000000)

# 上传文件
ret, info = put_file(token, key, localfile)
if(ret == None):
    # 上传失败
    exit(res.text)
exit('上传成功')