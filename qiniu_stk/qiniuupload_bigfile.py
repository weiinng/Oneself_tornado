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
q = Auth(access_key, secret_key)

#上传大的视频
def uploadBigVideo(keyNmae,localfile):
    # try:
    # 定义文件的key
    key = "{}{}".format(int(time.time()),keyNmae)
    # 判断七牛key是否已经存在
    buc = BucketManager(q)
    res, info1 = buc.stat(bucket_name, key)
    if (res != None):
        exit(res.text)
    # 上传文件的地址
    if (os.path.exists(localfile) == False):
        exit('文件不存在')
        return "文件不存在"
    # 获取上传的token
    token = q.upload_token(bucket_name, key, 36000000)
    # 上传文件
    ret, info = put_file(token, key, localfile)
    if (ret == None):
        # 上传失败
        exit(res.text)
        return "上传失败！"
    exit('上传成功')
    return ret["key"]
    # except:
    #     return 404

print(uploadBigVideo("movie1.mp4","movie1.mp4"))



