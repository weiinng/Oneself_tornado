# 导入依赖
from sqlalchemy import create_engine         # 创建引擎对象的模块
from sqlalchemy.orm import sessionmaker      # 创建和数据库连接会话
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey,Text,DECIMAL # 内置的创建类的方法属性
from sqlalchemy.ext.declarative import declarative_base # 基础类模块
from sqlalchemy.ext.declarative import DeclarativeMeta  # 解码模块
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
    username = Column(String(60))                #用户名
    account = Column(String(60))                 #账号
    password = Column(String(255))               #密码
    is_super = Column(Integer,default=0)         #是否是超级管理员 0位否1为是



#用户表
class User(Base,IdBase):
    __tablename__ = "user"
    name = Column(String(60),default="")                    #用户名
    password = Column(String(255))                          #密码
    phone = Column(String(11))                              #手机号登录
    email = Column(String(60),default="")                   #邮箱
    age = Column(Integer,default=0)                         #年龄  0为保密  大于则显示
    gender  = Column(Integer,default=0)                     #性别  0为保密 1为男  2为女
    head_img = Column(String(255),default="")               #用户头像
    birthplace = Column(String(100),default="")             #地址
    is_member = Column(Integer,default=0)                   #是否会员(会员等级1~9)
    is_activate = Column(Integer,default=0)                 #是否激活
    create_time = Column(DateTime(),default=datetime.now)   #注册时间（精确到秒）



# 视频表
class Video(Base,IdBase):
    __tablename__ = "video"
    name = Column(String(100))                   #电影名（必填）
    english_name = Column(String(100))           #英文名
    director = Column(String(100),default="")    #导演
    cinemanufacturer = Column(String(100))       #制片人
    protagonist = Column(String(100))            #主演
    cost = Column(String(100))                   #制片成本
    scriptwriter = Column(String(100))           #编剧
    release_date = Column(String(100))           #上映时间 
    box_office = Column(String(100))             #票房
    intro = Column(Text)                         #电影简介 （必填）
    year = Column(String(100))                   #制片年份 （必填）
    region = Column(String(100))                 #影片地区 （必填）
    length = Column(String(100))                 #片长  
    types = Column(Integer)                      #类型 
    tag = Column(String(100))                    #影片标签
    resolution = Column(String(100))             #分辨率
    path = Column(String(100))                   #播放路径  （必填）
    amount = Column(Integer,default=0)           #播放次数
    hot = Column(Integer)                        #热度值
    img1 = Column(String(255))                   #视频的一张缩略图        （必填）
    img2 = Column(String(255))                   #视频的轮播图 可以没有
    thiscat_id = Column(Integer)                 #视频所属的栏目   （必填）
    video_weight = Column(Integer,default=40)    #视频权重（0~99）越小越靠前默认为40
    video_source = Column(Integer)               #这个会获取到管理员的id，超级管理员可以直接指定
    is_vip = Column(Integer,default=0)           #是否是会员视频 0为否  1为是
    is_selection = Column(Integer,default=0)     #是否为精选 默认为否
    is_audit = Column(Integer,default=0)         #视频来源 》主管理员可以不需要审核，其他需要主管理员审核
    is_show = Column(Integer,default=0)          #0为显示  1为不显示



# 分类表
class Classify(Base,IdBase):
    __tablename__ = "classify"
    name = Column(String(60))               # 分类名
    video_id = Column(Integer)              # 视频id
    micro_video_id = Column(Integer)        # 微视频id




#分类and视频
class ClassAndvideo(Base,IdBase):
    __tablename__ = "classandvideo"
    class_id = Column(Integer)
    video_id = Column(Integer,nullable=False)



# 栏目表
class Columns(Base,IdBase):
    __tablename__ = "columns"
    name = Column(String(100))                                  #栏目名称
    creation_time = Column(DateTime(),default=datetime.now)     #创建时间（精确到秒）


# 标签表
class Label(Base,IdBase):
    __tablename__ = "label"
    name = Column(String(100))                                  #标签名称
    creation_time = Column(DateTime(),default=datetime.now)     #发布时间（精确到秒）



# 微视频表
class Micro_video(Base,IdBase):
    __tablename__ = "micro_video"
    name = Column(String(100))                               #微视频内容标题(必填)
    length = Column(String(100))                             #片长
    issue_time = Column(DateTime(),default=datetime.now)     #发布时间（精确到秒）
    is_show = Column(Integer,default=0)                      #发布状态
    user_id = Column(Integer)                                #用户id




# 大V   明星
class Big_V(Base,IdBase):
    __tablename__ = "big_v"
    name = Column(String(60))                   #名字
    english_name = Column(String(60))           #英文名
    year = Column(String(100))                  #生日 
    gender = Column(String(100))                #性别  
    nation = Column(String(100))                #民族              
    nationality = Column(String(255))           #国籍
    director = Column(String(255))              #出生地
    profession = Column(String(100))            #职业
    region = Column(Text)                       #简介
    graduate_academy = Column(String(255))      #毕业院校
    blood_type = Column(String(255))            #血型
    stature = Column(String(255))               #身高
    weight = Column(String(255))                #体重
    constellation = Column(String(255))         #星座
    main_achievements = Column(String(255))     #主要成就
    in_work = Column(String(500))               #代表作品
    img = Column(String(500))                   #照片




#大V 身份表
class Identity(Base,IdBase):
    __tablename__ = "identity"
    name = Column(String(60))         #身份名称



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
    content = Column(Text)                                   # 内容
    comment_time = Column(DateTime(),default=datetime.now)   # 评论时间（精确到秒）
    inform = Column(Integer,default=0)                       # 举报
    types = Column(Integer,default=0)                        #评论类型,如果为0则是对电影的评论，如果大于0 是追加评论。
    user_id = Column(Integer)                                #用户id
    video_id = Column(Integer)                               #电影id
    micro_video_id = Column(Integer)                         #微视频id


#用户收藏表
class Collect(Base,IdBase):
    __tablename__ = "collect"
    user_id = Column(Integer)            #用户id
    video_id = Column(Integer)           #视频id
    micro_video_id = Column(Integer)     #微视频id





#用户关注表
class Attention(Base,IdBase):
    __tablename__ = "attention"
    user_id = Column(Integer)               #用户id
    big_v_id = Column(Integer)              #视频id
    micro_video_id = Column(Integer)        #微视频id
    types = Column(Integer)                 #关注的类型 1为栏目，2为明星 3为导演 4位主持人



# 点赞表
class Praise(Base,IdBase):
    __tablename__ = "praise"
    user_id = Column(Integer)                #用户id
    movie_id = Column(Integer)               #电影id
    micro_video_id = Column(Integer)         #微视频id
    pratype = Column(Integer)                #点赞类型 1为视频点赞  2为大V点赞




#意见反馈表
class Opinion(Base,IdBase):
    __tablename__ = "opinion"
    title = Column(String(60))      
    user_id = Column(Integer)       #用户id
    types = Column(String(60))      #做出下拉菜单
    body = Column(Text)             #内容




# 图片表
class Picture(Base):
    __tablename__ = 'picture'
    id = Column(Integer, primary_key=True, autoincrement=True)
    picture_name = Column(String(500))      #图片名称
    big_v_id = Column(Integer)              #明星id
    video_id = Column(Integer)              #视频id
    user_id = Column(Integer)               #用户id
    micro_video_id = Column(Integer)        #微视频id



#系统表
class System(Base):
    __tablename__ = 'system'
    id = Column(Integer, primary_key = True,autoincrement=True)  
    site_name = Column(String(255))                 # 网站名称
    domain_name  = Column(String(255))              # 服务器域名
    describe = Column(Text)                         # 描述
    copyrights = Column(String(255))                # 底部版权信息
    number = Column(Integer,default=0)              # 后台登录失败最大次数
    SMTP_server = Column(String(255))               # SMTP服务器
    SMTP_port = Column(Integer,default=0)           # SMTP 端口
    mail_account = Column(String(255))              # 邮箱帐号
    email_password  = Column(Integer,default=0)     # 邮箱密码
    email_address = Column(String(255))             # 收件邮箱地址





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