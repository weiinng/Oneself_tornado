# 导入依赖
from sqlalchemy import create_engine # 创建引擎对象的模块
from sqlalchemy.orm import sessionmaker # 创建和数据库连接会话
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey,Text,DECIMAL # 内置的创建类的方法属性
from sqlalchemy.ext.declarative import declarative_base # 基础类模块
from sqlalchemy.ext.declarative import DeclarativeMeta #解码模块
import json
from datetime import datetime
import pymysql
from config import *

db_url = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, DATABASE)
engine = create_engine(db_url)
pymysql.install_as_MySQLdb()
Session=sessionmaker(bind=engine)
sess=Session()
Base = declarative_base(bind=engine)



class IdBase(object):
    id = Column(Integer, primary_key=True, autoincrement=True)

#管理员用户
class AdminUser(Base,IdBase):
    __tablename__ = "adminuser"
    username = Column(String(60))  #用户名
    account = Column(String(60))  #账号
    password = Column(String(255)) #密码
    is_super = Column(Integer,default=0) #是否是超级管理员 0位否1为是






#用户表
class User(Base,IdBase):
    __tablename__ = "user"
    name = Column(String(60),default="")         #用户名
    password = Column(String(255))        #密码
    phone = Column(String(11))            #手机号登录
    email = Column(String(60),default="")             #邮箱
    age = Column(Integer,default=0)          #年龄  0为保密  大于则显示
    gender  = Column(Integer,default=0)       #性别  0为保密 1为男  2为女
    head_img = Column(String(255),default="")            #用户头像
    birthplace = Column(String(100),default="")          #地址
    is_member = Column(Integer,default=0)      #是否会员(会员等级1~9)
    is_activate = Column(Integer,default=0)    # 是否激活
    create_time = Column(DateTime(),default=datetime.now)       # 注册时间（精确到秒）


# 视频表
class Video(Base,IdBase):
    __tablename__ = "video"
    name = Column(String(60))           #电影名 （必填）
    intro = Column(Text)                # 电影简介 （必填）
    year = Column(String(100))              #制片年份 （必填）
    region = Column(String(100))           #影片地区 （必填）
    director = Column(String(100),default="")          #导演
    types = Column(Integer)           #影片类型  必需字段 0为短视频 1为电影
    tag = Column(String(100))      #影片标签
    resolution = Column(String(100))   #分辨率
    length = Column(String(100))           #视频时长
    path = Column(String(100))           #播放路径  （必填）
    amount = Column(Integer,default=0)     #播放次数
    hot = Column(Integer)          #热度值
    img1 = Column(String(255))     #视频的一张缩略图        （必填）
    img2 = Column(String(255))     #视频的轮播图 可以没有
    thiscat_id = Column(Integer)   #视频所属的栏目   （必填）
    video_weight = Column(Integer,default=40)   #视频权重（0~99）越小越靠前默认为40
    video_source = Column(Integer)       #这个会获取到管理员的id，超级管理员可以直接指定
    is_vip = Column(Integer,default=0)    #是否是会员视频 0为否  1为是
    is_selection = Column(Integer,default=0)  #是否为精选 默认为否
    is_audit = Column(Integer,default=0) #视频来源 》主管理员可以不需要审核，其他需要主管理员审核
    is_show = Column(Integer,default=0)    #0为显示  1为不显示


# 分类表
class Classify(Base,IdBase):
    __tablename__ = "classify"
    name = Column(String(60))             # 分类名


#分类and视频
class ClassAndvideo(Base,IdBase):
    __tablename__ = "classandvideo"
    class_id = Column(Integer)
    video_id = Column(Integer,nullable=False)


# 大V
class Big_V(Base,IdBase):
    __tablename__ = "big_v"
    name = Column(String(60))      #名字
    year = Column(String(100))             #生日
    profession = Column(String(100))           #职业
    gender = Column(Integer)    #性别  0为女  1为男
    region = Column(Text)             #简介
    director = Column(String(255))           #家乡
    img = Column(String(500))      #照片

#大V 身份表
class Identity(Base,IdBase):
    __tablename__ = "identity"
    name = Column(String(60))  #身份名称

#大V and 身份
class V_and_identity(Base,IdBase):
    __tablename__ = "v_and_identity"
    v_id = Column(Integer)
    identity_id = Column(Integer)


#大V and 电影表
class V_andvideo(Base,IdBase):
    __tablename__ = "v_andvideo"
    v_id = Column(Integer)
    video_id = Column(Integer)



# 评论表
class Comment(Base,IdBase):
    __tablename__ = "comment"
    content = Column(Text)               # 内容
    comment_time = Column(DateTime(),default=datetime.now)       # 评论时间（精确到秒）
    inform = Column(Integer,default=0)          # 举报
    types = Column(Integer,default=0) #评论类型,如果为0则是对电影的评论，如果大于0 是追加评论。
    user_id = Column(Integer)   #用户id
    video_id = Column(Integer)   #电影id


#用户收藏表
class Collect(Base,IdBase):
    __tablename__ = "collect"
    user_id = Column(Integer)
    video_id = Column(Integer)

#用户关注表
class Attention(Base,IdBase):
    __tablename__ = "attention"
    user_id = Column(Integer)
    big_v_id = Column(Integer)
    types = Column(Integer) #关注的类型 1为栏目，2为明星 3为导演 4位主持人


# 点赞表
class Praise(Base,IdBase):
    __tablename__ = "praise"
    user_id = Column(Integer)   #回复id
    movie_id = Column(Integer)   #电影id
    pratype = Column(Integer) #点赞类型 1为视频点赞  2为大V点赞

#意见反馈表
class Opinion(Base,IdBase):
    __tablename__ = "opinion"
    title = Column(String(60))
    types = Column(String(60))  #做出下拉菜单
    body = Column(Text)  #内容



def sqlalchemy_json(self):
    obj_dict = self.__dict__
    return dict((key, obj_dict[key]) for key in obj_dict if not key.startswith("_"))
Base.__json__ = sqlalchemy_json



class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:  # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)

    





if __name__ == "__main__":
    #创建表
    Base.metadata.create_all()
    # Base.metadata.drop_all()