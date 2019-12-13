import qiniu
from config import *
from moviepy.editor import VideoFileClip
from qiniu import BucketManager

access_key = qiniu_page["access_key"]
secret_key = qiniu_page["secret_key"]
bucket_name = qiniu_page["bucket_name"]
url = qiniu_page['bucket_name']
q = qiniu.Auth(access_key, secret_key)

def qiniu_upload(key, localfile):   # 图片名称
    token = q.upload_token(bucket_name, key, 3600)    
    ret, info = qiniu.put_file(token, key, localfile)    
    try:
        res = "{0}{1}".format(url, ret['key'])
        return "http://q2cbcbetl.bkt.clouddn.com/" + key
    except:
        return 404


# 长代码连接 https://blog.csdn.net/longjuanfengzc/article/details/103006691
#获取视频的播放时长 # pip install moviepy /可以传网络资源
def gitVideoTime(videoUrl):
    clip = VideoFileClip(videoUrl)
    time = clip.duration
    return time


# 路径问题解决方案1 直接传网络地址
def setUrlUp(imgName,imgPage):
    try:
        bucket = BucketManager(q)
        url = imgPage
        key = imgName
        ret, info = bucket.fetch(url, bucket_name, key)
        # print(info)
        return ret["key"]
    except:
        return 404


print(setUrlUp("消防员跳蒙古舞走红,网友:求当女婿","https://video.pearvideo.com/mp4/adshort/20191212/cont-1631908-14689699_adpkg-ad_hd.mp4"))







videoUrl = "https://video.pearvideo.com/mp4/adshort/20191212/cont-1631908-14689699_adpkg-ad_hd.mp4"






# https://blog.csdn.net/y472360651/article/details/79272927

