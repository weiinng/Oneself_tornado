import qiniu
from config import *

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

# key = '微信图片_20180408124226.jpg'
# localfile = "../static/imgs/123321.png"
# img_url = "http://q2cbcbetl.bkt.clouddn.com/" + key
# res = qiniu_upload(key,localfile)
# print(qiniu_upload(key,localfile))


from qiniu import Auth
# 路径问题解决方案1 直接传网络地址
from qiniu import BucketManager
def setUrlUp(imgName,imgPage):
    bucket = BucketManager(q)
    url = imgPage
    key = imgName
    ret,info = bucket.fetch(url, bucket_name, key)
    print(info)
    assert ret['key'] == key
# print(setUrlUp("小心心","https://video.pearvideo.com/mp4/adshort/20191209/cont-1630783-14678805_adpkg-ad_hd.mp4"))


#获取视频的播放时长
# pip install moviepy /可以传网络资源

#长代码连接 https://blog.csdn.net/longjuanfengzc/article/details/103006691
from moviepy.editor import VideoFileClip

clip = VideoFileClip("https://video.pearvideo.com/mp4/adshort/20191209/cont-1630783-14678805_adpkg-ad_hd.mp4")
# print(clip.duration)


# https://blog.csdn.net/y472360651/article/details/79272927

