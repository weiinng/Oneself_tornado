from .base import BaseHandler
from models import *
import json


# 后台首页
# 首页
class Ceshi(BaseHandler):
    def get(self, *args, **kwargs):
        print("有人对我发起了请求！")
        goods_list = "请求到了页面！"
        return self.write(json.dumps({"status": 200, "msg": "返回成功", 'goods': goods_list}, cls=AlchemyEncoder, ensure_ascii=False))

#qiniu
class QiniuUpToken(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/01demo.html')
    def post(self, *args, **kwargs):
        pass
