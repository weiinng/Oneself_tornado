#多对多查询分类
from models import *

# claandvideo = sess.query(ClassAndvideo).all()
# for a in claandvideo:
    # print(a.id)


# clas = sess.query(Classify).all()

# clasandvideo = sess.query(ClassAndvideo).all()

# 分类下的所有电影
# 创建也给空列表
clasvideolist = []
clas = sess.query(Classify).all()
for cls in clas:
    # 创建一个字典
    item = {}
    item["clasId"]=cls.id
    item["clasName"] = cls.name
    #创建一个视频列表，存放当前分类一下的所有视频
    videos = []
    #找出关联表与 与上面分类id有关的所有字段
    clasandvideo = sess.query(ClassAndvideo).filter(ClassAndvideo.class_id==cls.id).all()
    #遍历关联表
    for clasvideo in clasandvideo:
        #创建一个存放视频的字典对象
        video_disc = {}
        #查询 video_id == 关联表.video_id
        video = sess.query(Video).filter(Video.id==clasvideo.video_id).one()
        video_disc["video_id"] = video.id
        video_disc["video_name"] = video.name
        #存入视频字符串
        videos.append(video_disc)
    #字典添加 video列表 =》列表内是字典
    item["videos"]=videos
    #将字典添加到列表
    clasvideolist.append(item)
# print(clasvideolist)
#遍历取出来
for a in clasvideolist:
    print(a)



    '''
给视频添加分类思路
后台增加视频的html，增加一个下拉菜单，查百度看看多选怎么用 
self.get_arguments()
这个函数是获取post返回的列表
一个列表进行两次commit,取出id，在将video_id 以及做关联的 class_id 存入classadnvideo

class_s = self.get_arguments([1,2,3,4,5],[])
video = Video(id=id,name=name)
sess.add(video)
sess.commit()
ps:好像有一个方法可以获取到返回的id
for a in class_s:
    class_id = ClassAndVideo(class_id = a,video_id = ？？？？)
    sess.add(class_id)
sess.commit()
    '''
