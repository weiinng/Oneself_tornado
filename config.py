import os

BASE_DIRS = os.path.dirname(__file__)


#参数
options = {
    'port':8000,
}

#配置
setting = {
    'static_path':os.path.join(BASE_DIRS,'static'),
    'template_path':os.path.join(BASE_DIRS,'templates'),
    'debug':True,
    # 'autoreload':True
}

#mysql配置
HOSTNAME = '106.13.137.97'
PORT = '3306'
DATABASE = 'red_db'
USERNAME = 'root'
PASSWORD = '123456'


#redis配置
REDIS_HOST = '127.0.0.1'
REDIS_POST = 6379