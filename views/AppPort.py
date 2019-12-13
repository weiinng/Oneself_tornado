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


class gitVideolist(BaseHandler):
    def get(self, *args, **kwargs):
        microall = sess.query(Micro_video).all()[:10]
        video_list = []
        for micro in microall:
            item = {}
            item["id"] = micro.id
            item["title"] = micro.name
            item["length"] = micro.length
            item["playnum"] = micro.amount
            try:
                item["video_img"] = sess.query(Picture.picture_name).filter(Picture.micro_video_id == micro.id)[0][0]
            except:
                item["video_img"]=""
            item["video_url"] = sess.query(Movie.movie_name).filter(Movie.micro_video_id == micro.id)[0][0]
            video_column = sess.query(Columngroup.id, Columngroup.name, Columngroup.img).filter(
                Columngroup.id == micro.column_id)
            item["column_id"] = video_column[0][0]
            item["column_name"] = video_column[0][1]
            item["column_img"] = video_column[0][2]
            video_list.append(item)
        return self.write(json.dumps({"status": 200, "msg": "返回成功", 'video_list':video_list}, cls=AlchemyEncoder, ensure_ascii=False))


