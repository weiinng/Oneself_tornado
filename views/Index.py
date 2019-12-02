from .base import BaseHandler
from models import AdminUser,sess
import json


# 后台首页
# 首页
class Index(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/index.html')





# 我的桌面
class Welcome(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/welcome.html')


# 视频管理
class Article_list(BaseHandler):
    def get(self, *args, **kwargs):
        video = sess.query(Video).all()
        lens = len(video)
        self.render('../templates/article_list.html', lens=lens)


# 上传视频
class Article_add(BaseHandler):
    def get(self, *args, **kwargs):
        movie = sess.query(Movie).all()
        self.render('../templates/article_add.html', movie=movie)


# 图片管理
class Picture_list(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/picture_list.html')


# 添加图片
class Picture_add(BaseHandler):
    def get(self, *args, **kwargs):
        movie = sess.query(Movie).all()
        self.render('../templates/picture_add.html', movie=movie)


# 图片展示
class Picture_show(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/picture_show.html')


# 删除图片
class Picture_del(BaseHandler):
    def get(self, id):
        self.redirect('/picture_list')


# #修改图片
# class Picture_edit(BaseHandler):
#     def get(self,id):
#         user = sess.query(User).filter_by(id=id).first()
#         self.render('../templates/member-update.html',user=user)
#     def post(self, id):
#         p = sess.query(User).filter_by(id=id).first()
#         name = self.get_argument('name')
#         gender = self.get_argument('gender')
#         birthplace = self.get_argument('birthplace')
#         phone = self.get_argument('phone')
#         p.name = name
#         p.gender = gender
#         p.birthplace = birthplace
#         p.phone = phone
#         sess.commit()
#         self.redirect('/member_list')





# 明星管理
class Product_brand(BaseHandler):
    def get(self, *args, **kwargs):
        celebrity = sess.query(Celebrity).all()
        lens = len(celebrity)
        c_list = []
        for i in celebrity:
            c_dict = {}
            c_dict['id'] = i.id
            c_dict['celebrity_name'] = i.celebrity_name
            c_dict['year'] = i.year
            c_dict['types'] = i.types
            c_dict['gender'] = i.gender
            c_dict['region'] = i.region
            c_dict['actor'] = i.actor
            c_dict['director'] = i.director
            c_list.append(c_dict)
        # str_json = json.dumps(c_list,indent=2,ensure_ascii=False)
        self.render('../templates/product_brand.html', celebrity=c_list, lens=lens)

    def post(self, *args, **kwargs):
        title = self.get_argument('title', '')
        celebrity = sess.query(Celebrity).filter(Celebrity.celebrity_name.like('%' + title + '%')).all()
        lens = len(celebrity)
        lens = len(celebrity)
        c_list = []
        for i in celebrity:
            c_dict = {}
            c_dict['id'] = i.id
            c_dict['celebrity_name'] = i.celebrity_name
            c_dict['year'] = i.year
            c_dict['types'] = i.types
            c_dict['gender'] = i.gender
            c_dict['region'] = i.region
            c_dict['actor'] = i.actor
            c_dict['director'] = i.director
            c_list.append(c_dict)
        # str_json = json.dumps(c_list,indent=2,ensure_ascii=False)
        self.render('../templates/product_brand.html', celebrity=c_list, lens=lens)


# 添加明星
class Product_brand_add(BaseHandler):
    def get(self, *args, **kwargs):
        # movie = sess.query(Movie).all()
        self.render('../templates/product_brand_add.html')

    def post(self, *args, **kwargs):
        celebrity_name = self.get_argument('celebrity_name', '')
        year = self.get_argument('year', '')
        region = self.get_argument('region', '')
        gender = self.get_argument('gender', '')
        director = self.get_argument('director', '')
        actor = self.get_argument('actor', '')
        celebrity = Celebrity(celebrity_name=celebrity_name, year=year, region=region, director=director, actor=actor,
                              gender=gender)
        sess.add(celebrity)
        sess.commit()
        self.redirect('/product_brand')


# 删除明星
class Active_del(BaseHandler):
    def get(self, id):
        celebrity = sess.query(Celebrity).filter(Celebrity.id == id).one()
        sess.delete(celebrity)
        sess.commit()
        self.redirect('/product_brand')


# 修改明星
class Product_brand_edit(BaseHandler):
    def get(self, id):
        celebrity = sess.query(Celebrity).filter_by(id=id).first()
        self.render('../templates/product_brand_edit.html', celebrity=celebrity)

    def post(self, id):
        p = sess.query(Celebrity).filter_by(id=id).first()
        celebrity_name = self.get_argument('celebrity_name', '')
        year = self.get_argument('year', '')
        region = self.get_argument('region', '')
        gender = self.get_argument('gender', '')
        director = self.get_argument('director', '')
        actor = self.get_argument('actor', '')
        p.celebrity_name = celebrity_name
        p.year = year
        p.region = region
        p.gender = gender
        p.director = director
        p.actor = actor
        sess.commit()
        self.redirect('/product_brand')


import os


# 明星上传图片
class Upload_brand(BaseHandler):
    async def get(self):
        celebrity = sess.query(Celebrity).all()
        self.render('../templates/upload_brand.html', celebrity=celebrity)

    async def post(self):
        # 上传路径
        upload_path = os.path.dirname(os.path.dirname(__file__)) + "/static/upload/"
        # 接收文件，以对象的形式
        img = self.request.files.get('file', None)
        # 获取jquery传来的值
        goods = self.get_argument('goods')
        # 写入本地
        for meta in img:
            filename = meta['filename']
            file_path = upload_path + filename
            with open(file_path, 'wb') as up:
                up.write(meta['body'])
            g_img = Picture(picture_name=filename,
                            celebrity_id=goods
                            )
            sess.add(g_img)
            sess.commit()
            print(g_img)
        self.write(json.dumps({'status': 'ok'}, ensure_ascii=False))


# 分类管理
class Product_category(BaseHandler):
    def get(self, *args, **kwargs):
        classify = sess.query(Classify).all()
        lens = len(classify)
        self.render('../templates/product_category.html', lens=lens)

    def post(self, *args, **kwargs):
        title = self.get_argument('title', '')
        classify = sess.query(Classify).filter(Classify.name.like('%' + title + '%')).all()
        a = []
        for i in classify:
            b = {}
            b['id'] = i.id
            b['name'] = i.name
            a.append(b)
        str_json = json.dumps(a, indent=2, ensure_ascii=False)
        self.write(str_json)


# 添加分类
class Product_category_add(BaseHandler):
    def get(self, *args, **kwargs):
        classify = sess.query(Classify).all()
        self.render('../templates/product_category_add.html', classify=classify)

    def post(self, *args, **kwargs):
        name = self.get_argument('name', '')
        classify = Classify(name=name)
        sess.add(classify)
        sess.commit()
        self.redirect('/product_category_add')


# 删除分类
class Category_del(BaseHandler):
    def get(self, id):
        classify = sess.query(Classify).filter(Classify.id == id).one()
        sess.delete(classify)
        sess.commit()
        self.redirect('/product_category_add')


# 影片管理
class Product_list(BaseHandler):
    def get(self, *args, **kwargs):
        movie = sess.query(Movie).all()
        lens = len(movie)
        m_list = []
        for i in movie:
            m_dict = {}
            m_dict['id'] = i.id
            m_dict['movie_name'] = i.movie_name
            m_dict['year'] = i.year
            m_dict['region'] = i.region
            m_dict['director'] = i.director
            m_dict['movie_intro'] = i.movie_intro
            m_dict['types'] = i.types
            m_dict['propertys'] = i.propertys
            m_dict['resolution'] = i.resolution
            m_dict['length'] = i.length
            m_dict['path'] = i.path
            m_dict['amount'] = i.amount
            m_dict['propertys'] = i.propertys
            m_dict['is_soldout'] = i.is_soldout
            m_dict['is_audit'] = i.is_audit
            m_list.append(m_dict)
        self.render('../templates/product_list.html', movie=m_list, lens=lens)

    def post(self, *args, **kwargs):
        title = self.get_argument('title', '')
        movie = sess.query(Movie).filter(Movie.movie_name.like('%' + title + '%')).all()
        lens = len(movie)
        m_list = []
        for i in movie:
            m_dict = {}
            m_dict['id'] = i.id
            m_dict['movie_name'] = i.movie_name
            m_dict['year'] = i.year
            m_dict['region'] = i.region
            m_dict['director'] = i.director
            m_dict['movie_intro'] = i.movie_intro
            m_dict['types'] = i.types
            m_dict['propertys'] = i.propertys
            m_dict['resolution'] = i.resolution
            m_dict['length'] = i.length
            m_dict['path'] = i.path
            m_dict['amount'] = i.amount
            m_dict['propertys'] = i.propertys
            m_dict['is_soldout'] = i.is_soldout
            m_dict['is_audit'] = i.is_audit
            m_list.append(m_dict)
        self.render('../templates/product_list.html', movie=m_list, lens=lens)
        # str_json = json.dumps(a,indent=2,ensure_ascii=False)
        # self.write(str_json)


# 添加影片
class Product_add(BaseHandler):
    def get(self, *args, **kwargs):
        classify = sess.query(Classify).all()
        self.render('../templates/product_add.html', classify=classify)

    def post(self, *args, **kwargs):
        movie_name = self.get_argument('movie_name', '')
        region = self.get_argument('region', '')
        year = self.get_argument('year', '')
        director = self.get_argument('director', '')
        movie_intro = self.get_argument('movie_intro', '')
        classify_id = self.get_argument('classify_id')
        movie = Movie(movie_name=movie_name, region=region, year=year, director=director, movie_intro=movie_intro,
                      classify_id=classify_id)
        sess.add(movie)
        sess.commit()
        self.redirect('/product_list')


# 删除影片
class Product_del(BaseHandler):
    def get(self, id):
        movie = sess.query(Movie).filter(Movie.id == id).one()
        sess.delete(movie)
        sess.commit()
        self.redirect('/product_list')


# #修改影片
class Product_edit(BaseHandler):
    def get(self, id):
        classify = sess.query(Classify).all()
        movie = sess.query(Movie).filter_by(id=id).first()
        self.render('../templates/product_edit.html', classify=classify, movie=movie)

    def post(self, id):
        p = sess.query(Movie).filter_by(id=id).first()
        movie_name = self.get_argument('movie_name', '')
        region = self.get_argument('region', '')
        year = self.get_argument('year', '')
        director = self.get_argument('director', '')
        movie_intro = self.get_argument('movie_intro', '')
        classify_id = self.get_argument('classify_id')
        p.movie_name = movie_name
        p.region = region
        p.year = year
        p.director = director
        p.movie_intro = movie_intro
        p.classify_id = classify_id
        sess.commit()
        self.redirect('/product_list')


import os


# 电影上传图片
class Upload_product(BaseHandler):
    async def get(self):
        movie = sess.query(Movie).all()
        self.render('../templates/upload_product.html', movie=movie)

    async def post(self):
        # 上传路径
        upload_path = os.path.dirname(os.path.dirname(__file__)) + "/static/upload/"
        # 接收文件，以对象的形式
        img = self.request.files.get('file', None)
        # 获取jquery传来的值
        goods = self.get_argument('goods')
        # 写入本地
        for meta in img:
            filename = meta['filename']
            file_path = upload_path + filename
            with open(file_path, 'wb') as up:
                up.write(meta['body'])
            g_img = Picture(picture_name=filename,
                            movie_id=goods
                            )
            sess.add(g_img)
            sess.commit()
        self.write(json.dumps({'status': 'ok'}, ensure_ascii=False))


# 评论列表
class Feedment_list(BaseHandler):
    def get(self, *args, **kwargs):
        comment = sess.query(Comment).all()
        lens = len(comment)
        self.render('../templates/feedment_list.html', comment=comment, lens=lens)


# 删除评论
class Feedment_del(BaseHandler):
    def get(self, id):
        comment = sess.query(Comment).filter(Comment.id == id).one()
        sess.delete(comment)
        sess.commit()
        self.redirect('/product_list')


# 意见反馈
class Feedback_list(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/feedback_list.html')





# 等级管理
class Member_level(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/member_level.html')


# 积分管理
class Member_scoreoperation(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/member_scoreoperation.html')


# 浏览记录
class Member_record_browse(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/member_record_browse.html')


##下载记录
class Member_record_download(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/member_record_download.html')


# 分享记录
class Member_record_share(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/member_record_share.html')




# 折线图
class Charts_1(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/charts_1.html')


# 时间轴折线图
class Charts_2(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/charts_2.html')


# 区域图
class Charts_3(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/charts_3.html')


# 柱状图
class Charts_4(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/charts_4.html')


# 饼状图
class Charts_5(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/charts_5.html')


# 3D柱状图
class Charts_6(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/charts_6.html')


# 3D饼状图
class Charts_7(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/charts_7.html')


# 系统设置
class System_base(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/system_base.html')


# 栏目管理
class System_category(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/system_category.html')


# 数据字典
class System_data(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/system_data.html')


# 屏蔽词
class System_shielding(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/system_shielding.html')


# 系统日志
class System_log(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/system_log.html')


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("Hello, world123")
        # self.finish({'name':'你好'})

# class IndexHandler(BaseHandler):
#     def get(self, *args, **kwargs):
#         bill = sess.query(Bill).all()
#         self.write(json.dumps({"status": 200, "msg": "返回成功",'billcate':bill}, cls=AlchemyEncoder, ensure_ascii=False))





# class Add(BaseHandler):
#     def get(self):
#         self.render('../templates/add.html')
#     def post(self):
#         time = self.get_argument('time','')
#         start = self.get_argument('start','')
#         target = self.get_argument('target','')
#         num = self.get_argument('num','')
#         bill = Bill(time=time,start=start,target=target,num=num)
#         sess.add(bill)
#         sess.commit()
#         self.redirect('/')
