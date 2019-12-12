#多对多查询分类
from models import *


# claandvideo = sess.query(ClassAndvideo).all()
# for a in claandvideo:
    # print(a.id)


# clas = sess.query(Classify).all()

# clasandvideo = sess.query(ClassAndvideo).all()

# 分类下的所有电影
# 创建也给空列表

# clasvideolist = []
# clas = sess.query(Classify).all()
# for cls in clas:
#     # 创建一个字典
#     item = {}
#     item["clasId"]=cls.id
#     item["clasName"] = cls.name
#     #创建一个视频列表，存放当前分类一下的所有视频
#     videos = []
#     #找出关联表与 与上面分类id有关的所有字段
#     clasandvideo = sess.query(ClassAndvideo).filter(ClassAndvideo.class_id==cls.id).all()
#     #遍历关联表
#     for clasvideo in clasandvideo:
#         #创建一个存放视频的字典对象
#         video_disc = {}
#         #查询 video_id == 关联表.video_id
#         video = sess.query(Video).filter(Video.id==clasvideo.video_id).one()
#         video_disc["video_id"] = video.id
#         video_disc["video_name"] = video.name
#         #存入视频字符串
#         videos.append(video_disc)
#     #字典添加 video列表 =》列表内是字典
#     item["videos"]=videos
#     #将字典添加到列表
#     clasvideolist.append(item)
# # print(clasvideolist)
# #遍历取出来
# for a in clasvideolist:
#     print(a)



#     '''
# 给视频添加分类思路
# 后台增加视频的html，增加一个下拉菜单，查百度看看多选怎么用 
# self.get_arguments()
# 这个函数是获取post返回的列表
# 一个列表进行两次commit,取出id，在将video_id 以及做关联的 class_id 存入classadnvideo

# class_s = self.get_arguments([1,2,3,4,5],[])
# video = Video(id=id,name=name)
# sess.add(video)
# sess.commit()
# ps:好像有一个方法可以获取到返回的id
# for a in class_s:
#     class_id = ClassAndVideo(class_id = a,video_id = ？？？？)
#     sess.add(class_id)
# sess.commit()
#     '''
# coding: utf-8

# import qiniu
# access_key = "I4CrykkGIkn6t5ebigiaWZdVURypDGgyAHBSVsvI"
# secret_key = "dmAHKa5kXI4Z6XyqiIPQJAuu3zrDHkmXJMrKgden"
# bucket_name = "redinnovation"
# url = 'redinnovation.s3-cn-north-1.qiniucs.com'
# q = qiniu.Auth(access_key, secret_key)
# # 上传图片demo

# def qiniu_upload(key, localfile):
#     token = q.upload_token(bucket_name, key, 3600)
#     ret, info = qiniu.put_file(token, key, localfile)
#     if ret:
#         return '{0}{1}'.format(url, ret['key'])
#     else:
#         raise print('上传失败请重试！')
# key = '微信图片_20180408124226.jpg'
# localfile = "static/imgs/123321.png"
# res = qiniu_upload(key,localfile)
# img_url = "http://q2cbcbetl.bkt.clouddn.com/"+key





# import os

# import configparser

# from UploadFile2OSS import UploadFle2OSS

# def uploadVideo2OSS(uplaoddate):
#     '''
#     上传视频
#     :return:
#     '''
#     basedir_drv = readConfigContent('video', 'basedir_drv')+uplaoddate

#     ossDir_drv = readConfigContent('video', 'ossDir_drv')+uplaoddate

#     fun1 = UploadFle2OSS(basedir_drv, ossDir_drv)

#     fun1.dir_list_file(basedir_drv)

# #其中readConfigContent是读取配置文件的函数，如下：
# def readConfigContent(content, keyValue):
#     '''
#     读取配置文件信息
#     :param content:
#     :param keyValue:
#     :return:
#     '''
#     configFile = os.getcwd() + '/config'  # 开发环境

#     cf = configparser.ConfigParser()

#     cf.read(configFile)

#     value = cf.get(content, keyValue)

#     return value

#  
# # 最后写主函数调用：
# if __name__=='__main__':

#     uploadFile = 'test' #上传视频的本地目录

#     uploadVideo2OSS(uploadFile)









# access_key = '替换成你的'
# # 个人中心->密匙管理->SK
# secret_key = '替换成你的'
# # 七牛空间名
# bucket_name = '替换成你的'
# #临时域名
# url = '替换成你的'
# q = qiniu.Auth(access_key, secret_key)


# def qiniu_upload(key, localfile):
 
#     token = q.upload_token(bucket_name, key, 3600)
#     ret, info = qiniu.put_file(token, key, localfile)
#     if ret:
#         return 'http://{0}/{1}'.format(url, ret['key'])
#     else:
#         raise Exception('上传失败，请重试')

# @csrf_exempt
# def upload_qiniu(request):
#     """
#               @api {POST} /upload_qiniu/ [上传图片至七牛]
#                * @apiVersion 0.0.1
#                * @apiGroup upload
#               @apiParamExample {params} 请求参数
#                   "image":""       "图片文件"
#               @apiSuccessExample {json} 成功返回
#                       {
#                 "message": "",
#                 "next": "",
#                 "data": "",
#                 "response": "ok",
#                 "error": ""
#             }
#               @apiSuccessExample {json} 失败返回
#               {
#                   "message": "",
#                   "next": "",
#                   "data": null,
#                   "response": "fail",
#                   "error": "上传失败"，"缺少参数"
#               }
#               """
#     image = request.FILES.get("image")
#     if not image:
#         return ajax.jsonp_fail(request, u"缺少参数")
#     service_name = save_block_file(image)
#     data=qiniu_upload(service_name,get_absolute_file_path(service_name))
#     if data:
#         return ajax.jsonp_ok(request, data)
#     else:
#         return ajax.jsonp_fail(request, u"上传失败")

# def save_upload_file(new_file_path, raw_file,name):
#     """
#     功能说明：保存上传文件
#     raw_file:原始文件对象
#     new_file_path:新文件绝对路径
#     """
#     try:
#         # 如果新文件存在则删除
#         if os.path.exists(new_file_path):
#             try:
#                 os.remove(new_file_path)
#             except:
#                 pass

#         content = raw_file.read()
#         fp = open(new_file_path, 'wb')
#         fp.write(content)
#         fp.close()
#         return name
#     except Exception as e:
#         print (e)
#         return False


# def save_block_file(block_file):
#     """
#     :param block_file: 文件对象
#     :return:
#     """
#     # 唯一标识 + 文件名   201801171.png
#     now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#     name = '%s%s' % (now_time, block_file.name)
#     block_file_path = get_absolute_file_path(name).replace("\\", "/")
#     # 文件上传保存
#     return save_upload_file(block_file_path, block_file, name)


# def get_absolute_file_path(file_name):
#     """
#     功能说明：返回绝对路径字符串
#     file_name:文件名字
#     """
#     media_root = settings.UPLOAD
#     print ("media_root",media_root)
#     absolute_file_path = os.path.join(media_root, file_name)
#     print("absolute_file_path", absolute_file_path)
#     # 返回文件绝对路径中目录路径
#     file_dir = os.path.dirname(absolute_file_path)
#     print ("file_dir", file_dir)
#     if not os.path.exists(file_dir):
#         # 创建路径
#         os.makedirs(file_dir)
#     return absolute_file_path
