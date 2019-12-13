import os

BASE_DIRS = os.path.dirname(__file__)


#参数
options = {
    'port':8000,
}

options_img={
    'port':8001
}



#配置
setting = {
    'static_path':os.path.join(BASE_DIRS,'static'),         # 静态资源
    'template_path':os.path.join(BASE_DIRS,'templates'),    # html页面
    'debug':True,
    # 'autoreload':True
}

#mysql配置
HOSTNAME = '106.13.67.197'   #ip地址
PORT = '3306'                #端口
DATABASE = 'zzzzz'          #数据库名
USERNAME = 'root'            #账号
PASSWORD = '123456'          #密码


#redis配置
REDIS_HOST = '127.0.0.1'    #本地展示地址
REDIS_POST = 6379           


#七牛云配置
qiniu_page = {
    "access_key":"I4CrykkGIkn6t5ebigiaWZdVURypDGgyAHBSVsvI",     # 您的七牛密匙access_key
    "secret_key":"dmAHKa5kXI4Z6XyqiIPQJAuu3zrDHkmXJMrKgden",     # 您的七牛密匙secret_key
    "bucket_name":"redinnovation",                               # 您的七牛空间名
    "url":'redinnovation.s3-cn-north-1.qiniucs.com',             # 临时域名
}
