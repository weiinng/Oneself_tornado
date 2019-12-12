import qiniu
from config import *

access_key = qiniu_page["access_key"]
secret_key = qiniu_page["secret_key"]
bucket_name = qiniu_page["bucket_name"]
url = qiniu_page['bucket_name']



def qiniu_upload(key, localfile):   # 图片名称   
    q = qiniu.Auth(access_key, secret_key)    
    token = q.upload_token(bucket_name, key, 3600)    
    ret, info = qiniu.put_file(token, key, localfile)    
    try:
        res = "{0}{1}".format(url, ret['key'])
        return "http://q2cbcbetl.bkt.clouddn.com/" + key
    except:
        return 404

# key = '微信图片_20180408124226.jpg'
# localfile = "../static/imgs/123321.png"
# img_url = "http://q2cbcbetl.bkt.clouddn.com/" + key
# res = qiniu_upload(key,localfile)
# print(qiniu_upload(key,localfile))
