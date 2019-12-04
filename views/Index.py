from .base import BaseHandler
from models import *
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
        movie = sess.query(Video).all()
        self.render('../templates/article_add.html', movie=movie)


# 图片管理
class Picture_list(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/picture_list.html')


# 添加图片
class Picture_add(BaseHandler):
    def get(self, *args, **kwargs):
        movie = sess.query(Video).all()
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
        celebrity = sess.query(Big_V).all()
        lens = len(celebrity)
        c_list = []
        for i in celebrity:
            c_dict = {}
            c_dict['id'] = i.id
            c_dict['name'] = i.name
            c_dict['year'] = i.year
            c_dict['profession'] = i.profession
            c_dict['gender'] = i.gender
            c_dict['region'] = i.region
            c_dict['nationality'] = i.nationality
            c_dict['director'] = i.director
            c_dict['nation'] = i.nation
            c_list.append(c_dict)
        self.render('../templates/product_brand.html', celebrity=c_list, lens=lens)

    def post(self, *args, **kwargs):
        title = self.get_argument('title', '')
        celebrity = sess.query(Big_V).filter(Big_V.name.like('%' + title + '%')).all()
        lens = len(celebrity)
        lens = len(celebrity)
        c_list = []
        for i in celebrity:
            c_dict = {}
            c_dict['id'] = i.id
            c_dict['name'] = i.name
            c_dict['year'] = i.year
            c_dict['profession'] = i.profession
            c_dict['gender'] = i.gender
            c_dict['region'] = i.region
            c_dict['nationality'] = i.nationality
            c_dict['director'] = i.directornation
            c_dict['nation'] = i.nation
            c_list.append(c_dict)
        self.render('../templates/product_brand.html', celebrity=c_list, lens=lens)




#明星详情
class Product_show(BaseHandler):
    def get(self,id):
        big_v = sess.query(Big_V).filter(Big_V.id == id ).one()
        self.render('../templates/product_show.html',big_v=big_v)




# 添加明星
class Product_brand_add(BaseHandler):
    def get(self, *args, **kwargs):
        mes = {}
        mes['data'] = ''
        self.render('../templates/product_brand_add.html',**mes)

    def post(self, *args, **kwargs):
        mes = {}
        name = self.get_argument('name', '')
        year = self.get_argument('year', '')
        english_name = self.get_argument('english_name', '')
        nation = self.get_argument('nation', '')
        graduate_academy = self.get_argument('graduate_academy', '')
        blood_type = self.get_argument('blood_type', '')
        stature = self.get_argument('stature', '')
        weight = self.get_argument('weight', '')
        constellation = self.get_argument('constellation', '')
        main_achievements = self.get_argument('main_achievements', '')
        in_work = self.get_argument('in_work', '')
        region = self.get_argument('region', '')
        gender = self.get_argument('gender', '')
        profession = self.get_argument('profession', '')
        nationality = self.get_argument('nationality', '')
        director = self.get_argument('director', '')
        if not all([name,year,english_name,nation,graduate_academy,blood_type,stature,weight,constellation,main_achievements,in_work,region,gender,nationality,profession,director]):
            mes['data'] = '参数不能为空，请重新输入'
            self.render('../templates/product_brand_add.html',**mes)
        else:
            try:
                sess.query(Big_V).filter(Big_V.name==name).one()
            except:
                celebrity = Big_V(name=name, year=year, region=region, 
                                nationality=nationality,gender=gender,profession=profession,
                                director=director,english_name=english_name,nation=nation,    
                                graduate_academy=graduate_academy,blood_type=blood_type,stature=stature,
                                weight=weight,constellation=constellation,main_achievements=main_achievements,
                                in_work=in_work)
                sess.add(celebrity)
                sess.commit()
                self.redirect('/product_brand')
            else:
                mes['data'] = '此明星已存在，可添加其他'
                self.render('../templates/product_brand_add.html',**mes)    



# 删除明星
class Active_del(BaseHandler):
    def get(self, id):
        celebrity = sess.query(Big_V).filter(Big_V.id == id).one()
        sess.delete(celebrity)
        sess.commit()
        self.redirect('/product_brand')


# 修改明星
class Product_brand_edit(BaseHandler):
    def get(self, id):
        celebrity = sess.query(Big_V).filter_by(id=id).first()
        self.render('../templates/product_brand_edit.html', celebrity=celebrity)
    def post(self, id):
        p = sess.query(Big_V).filter_by(id=id).first()
        name = self.get_argument('name', '')
        year = self.get_argument('year', '')
        region = self.get_argument('region', '')
        gender = self.get_argument('gender', '')
        director = self.get_argument('director', '')
        nationality = self.get_argument('nationality', '')
        p.name = name
        p.year = year
        p.region = region
        p.gender = gender
        p.nationality = nationality
        p.director = director
        sess.commit()
        self.redirect('/product_brand')


import os 
#明星上传图片
class Upload_brand(BaseHandler):
    async def get(self,id):
        big_v = sess.query(Big_V).filter_by(id=id).first()
        self.render('../templates/upload_brand.html', big_v=big_v)

    async def post(self,id):
        # 上传路径
        upload_path = os.path.dirname(os.path.dirname(__file__))+"/static/upload/"
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
                            big_v_id = goods
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
        mes = {}
        mes['data'] = ''
        self.render('../templates/product_category_add.html', classify=classify,**mes)
    def post(self, *args, **kwargs):
        classify = sess.query(Classify).all()
        mes = {}
        name = self.get_argument('name', '')
        if not name:
            mes['data'] = '参数不能为空，请重新输入'
            self.render('../templates/product_category_add.html',classify=classify,**mes)
        else:
            try:
                sess.query(Classify).filter(Classify.name==name).one()
            except:
                classify = Classify(name=name)
                sess.add(classify)
                sess.commit()
                self.redirect('/product_category_add')
            else:
                 mes['data'] = '此分类已存在，可添加其他'
                 self.render('../templates/product_category_add.html',classify=classify,**mes)


# 删除分类
class Category_del(BaseHandler):
    def get(self, id):
        classify = sess.query(Classify).filter(Classify.id == id).one()
        sess.delete(classify)
        sess.commit()
        self.redirect('/product_category_add')



# 视频管理
class Product_list(BaseHandler):
    def get(self, *args, **kwargs):
        video = sess.query(Video).all()
        lens = len(video)
        m_list = []
        for i in video:
            m_dict = {}
            m_dict['id'] = i.id
            m_dict['name'] = i.name
            m_dict['year'] = i.year
            m_dict['region'] = i.region
            m_dict['director'] = i.director
            m_dict['intro'] = i.intro
            m_dict['types'] = i.types
            m_dict['tag'] = i.tag
            m_dict['protagonist'] = i.protagonist 
            m_dict['box_office'] = i.box_office 
            m_dict['is_show'] = i.is_show 
            m_list.append(m_dict)
        self.render('../templates/product_list.html', video=m_list, lens=lens)
    def post(self, *args, **kwargs):
        title = self.get_argument('title', '')
        video = sess.query(Video).filter(Video.name.like('%' + title + '%')).all()
        lens = len(video)
        m_list = []
        for i in video:
            m_dict = {}
            m_dict['id'] = i.id
            m_dict['name'] = i.name
            m_dict['year'] = i.year
            m_dict['region'] = i.region
            m_dict['director'] = i.director
            m_dict['intro'] = i.intro
            m_dict['types'] = i.types
            m_dict['tag'] = i.tag
            m_dict['protagonist'] = i.protagonist
            m_dict['box_office'] = i.box_office
            m_dict['is_show'] = i.is_show 
            m_list.append(m_dict)
        self.render('../templates/product_list.html', video=m_list, lens=lens)




#视频详情
class Product_details(BaseHandler):
    def get(self,id):
        video = sess.query(Video).filter(Video.id == id ).one()
        self.render('../templates/product_details.html',video=video)




# 添加视频
class Product_add(BaseHandler):
    def get(self, *args, **kwargs):
        classify = sess.query(Classify).all()
        mes = {}
        mes['data'] = ''
        self.render('../templates/product_add.html', classify=classify,**mes)
    def post(self, *args, **kwargs):
        classify = sess.query(Classify).all()
        mes = {}
        name = self.get_argument('name', '')
        region = self.get_argument('region', '')
        year = self.get_argument('year', '')
        director = self.get_argument('director', '')
        intro = self.get_argument('intro', '')
        english_name = self.get_argument('english_name', '')
        cinemanufacturer = self.get_argument('cinemanufacturer', '')
        protagonist = self.get_argument('protagonist', '')
        cost = self.get_argument('cost', '')
        scriptwriter = self.get_argument('scriptwriter', '')
        release_date = self.get_argument('release_date', '')
        box_office = self.get_argument('box_office', '')
        length = self.get_argument('length', '')
        tag = self.get_argument('tag', '')
        if not all([name,region,year,director,intro,english_name,cinemanufacturer,protagonist,cost,scriptwriter,release_date,box_office,length,tag]):
            mes['data'] = "参数不能为空,请重新输入"
            self.render('../templates/product_add.html', classify=classify,**mes)
        else:
            try:
                sess.query(Video).filter(Video.name==name).one()
            except:
                movie = Video(
                    name=name,region=region, year=year,director=director,
                    intro=intro,english_name=english_name,cinemanufacturer=cinemanufacturer,
                    protagonist=protagonist,cost=cost,scriptwriter=scriptwriter,
                    release_date=release_date,box_office=box_office,length=length,
                    tag=tag)
                sess.add(movie)
                sess.commit()
                self.redirect('/product_list')
            else:
                mes['data'] = "此商品已存在，可添加其他"
                self.render('../templates/product_add.html', classify=classify,**mes)


# 删除视频
class Product_del(BaseHandler):
    def get(self, id):
        movie = sess.query(Video).filter(Video.id == id).one()
        sess.delete(movie)
        sess.commit()
        self.redirect('/product_list')


# #修改视频
class Product_edit(BaseHandler):
    def get(self, id):
        classify = sess.query(Classify).all()
        video = sess.query(Video).filter_by(id=id).first()
        self.render('../templates/product_edit.html', classify=classify, video=video)

    def post(self, id):
        p = sess.query(Video).filter_by(id=id).first()
        name = self.get_argument('name', '')
        region = self.get_argument('region', '')
        year = self.get_argument('year', '')
        director = self.get_argument('director', '')
        intro = self.get_argument('intro', '')
        english_name = self.get_argument('english_name', '')
        cinemanufacturer = self.get_argument('cinemanufacturer', '')
        protagonist = self.get_argument('protagonist', '')
        cost = self.get_argument('cost', '')
        scriptwriter = self.get_argument('scriptwriter', '')
        release_date = self.get_argument('release_date', '')
        box_office = self.get_argument('box_office', '')
        length = self.get_argument('length', '')
        tag = self.get_argument('tag', '')
        p.name = name
        p.region = region
        p.year = year
        p.director = director
        p.intro = intro
        p.english_name = english_name
        p.cinemanufacturer = cinemanufacturer
        p.protagonist = protagonist
        p.cost = cost
        p.scriptwriter = scriptwriter
        p.release_date = release_date
        p.box_office = box_office
        p.length = length
        p.tag = tag
        sess.commit()
        self.redirect('/product_list')



import os
#电影上传图片
class Upload_product(BaseHandler):
    async def get(self,id):
        video= sess.query(Video).filter_by(id=id).first()
        self.render('../templates/upload_product.html', video=video)

    async def post(self,id):
        # 上传路径
        upload_path = os.path.dirname(os.path.dirname(__file__))+"/static/upload/"
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
                            video_id = goods
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


#意见反馈
class Feedback_list(BaseHandler):
    def get(self,*args,**kwargs):
        opinion = sess.query(Opinion).all()
        lens = len(opinion)
        self.render('../templates/feedback_list.html',opinion=opinion,lens=lens)






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


# 系统设置（添加）
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
