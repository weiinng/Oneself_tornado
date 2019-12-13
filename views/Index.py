from .base import BaseHandler
from models import *
import json
from qiniu_stk.qiniuupload_img import qiniu_upload,gitVideoTime

# 后台首页


#登录
class Login(BaseHandler):
    def get(self,*args,**kwargs):
        self.render('../templates/login.html')
    def post(self,*args,**kwargs):
        account = self.get_argument('account','')
        password = self.get_argument('password','')

        admin = sess.query(AdminUser).filter(AdminUser.account==account).first()
        if admin:
            if admin.password == password:
                self.redirect('/')
            else:
                self.write('密码错误')
        else:
            self.write('账号不存在')



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
            c_dict['director'] = i.director
            c_dict['nation'] = i.nation
            c_list.append(c_dict)
        self.render('../templates/product_brand.html', celebrity=c_list, lens=lens)




#明星详情
class Product_show(BaseHandler):
    def get(self,id):
        big_v = sess.query(Big_V).filter(Big_V.id == id ).one()
        picture = sess.query(Picture).filter(Picture.big_v_id == id ).one()
        self.render('../templates/product_show.html',big_v=big_v,picture=picture)



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
        if not all([name,year,english_name,nation,graduate_academy,blood_type,
        stature,weight,constellation,main_achievements,in_work,region,gender,
        profession,nationality,director]):
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

                qiniu_upload(filename, file_path)

                g_img = Picture(picture_name="http://q2cbcbetl.bkt.clouddn.com/"+filename,
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
        picture = sess.query(Picture).filter(Picture.video_id == id ).one()
        self.render('../templates/product_details.html',video=video,picture=picture)




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
        tag = self.get_argument('tag', '')
        types = self.get_argument('types', '')
        if not all([name,region,year,director,intro,english_name,
        cinemanufacturer,protagonist,cost,scriptwriter,release_date,
        box_office,tag,types]):
            mes['data'] = "参数不能为空,请重新输入"
            self.render('../templates/product_add.html', classify=classify,**mes)
        else:
            try:
                sess.query(Video).filter(Video.name==name).one()
            except:
                movie = Video(
                    name=name,region=region, year=year,director=director,types=types,
                    intro=intro,english_name=english_name,cinemanufacturer=cinemanufacturer,
                    protagonist=protagonist,cost=cost,scriptwriter=scriptwriter,
                    release_date=release_date,box_office=box_office,tag=tag)
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
        tag = self.get_argument('tag', '')
        types = self.get_argument('types', '')
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
        p.tag = tag
        p.types = types
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
                
                qiniu_upload(filename, file_path)

                g_img = Picture(picture_name="http://q2cbcbetl.bkt.clouddn.com/"+filename,
                                video_id = goods
                                )
                sess.add(g_img)
                sess.commit()
        self.write(json.dumps({'status': 'ok'}, ensure_ascii=False))



 
# 微视频管理
class Product_micro(BaseHandler):
    def get(self, *args, **kwargs):
        micro_video = sess.query(Micro_video).all()
        lens = len(micro_video)
        m_list = []
        for i in micro_video:
            m_dict = {}
            m_dict['id'] = i.id
            m_dict['name'] = i.name
            m_dict['is_show'] = i.is_show
            m_list.append(m_dict)
        self.render('../templates/product_micro.html', micro_video=m_list, lens=lens)
    def post(self, *args, **kwargs):
        title = self.get_argument('title', '')
        micro_video = sess.query(Micro_video).filter(Micro_video.name.like('%' + title + '%')).all()
        lens = len(micro_video)
        m_list = []
        for i in micro_video:
            m_dict = {}
            m_dict['id'] = i.id
            m_dict['name'] = i.name
            m_dict['is_show'] = i.is_show
            m_list.append(m_dict)
        self.render('../templates/product_micro.html', micro_video=m_list, lens=lens)




# 添加微视频
class Product_video_add(BaseHandler):
    def get(self, *args, **kwargs):
        mes = {}
        mes['data'] = ''
        self.render('../templates/product_video_add.html',**mes)
    def post(self, *args, **kwargs):
        mes = {}
        mes['data'] = ''
        name = self.get_argument('name', '')
        if not all([name]):
            mes['data'] = "参数不能为空,请重新输入"
            self.render('../templates/product_video_add.html',**mes)
        else:
            try:
                sess.query(Micro_video).filter(Micro_video.name==name).one()
            except:
                micro_video = Micro_video(
                    name=name)
                sess.add(micro_video)
                sess.commit()
                self.redirect('/product_micro')
            else:
                mes['data'] = "此商品已存在，可添加其他"
                self.render('../templates/product_video_add.html',**mes)
        self.render('../templates/product_video_add.html',**mes)




# 栏目列表
class Product_column(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/product_column.html')




# # 添加栏目
class Product_column_add(BaseHandler):
    def get(self, *args, **kwargs):
        columns = sess.query(Columns).all()
        mes = {}
        mes['data'] = ''
        self.render('../templates/product_column_add.html', columns=columns,**mes)
    def post(self, *args, **kwargs):
        columns = sess.query(Columns).all()
        mes = {}
        name = self.get_argument('name', '')
        if not name:
            mes['data'] = '参数不能为空，请重新输入'
            self.render('../templates/product_column_add.html',columns=columns,**mes)
        else:
            try:
                sess.query(Columns).filter(Columns.name==name).one()
            except:
                columns = Columns(name=name)
                sess.add(columns)
                sess.commit()
                self.redirect('/product_column_add')
            else:
                 mes['data'] = '此分类已存在，可添加其他'
                 self.render('../templates/Product_column_add.html',columns=columns,**mes)




# 删除栏目
class Column_del(BaseHandler):
    def get(self, id):
        columns = sess.query(Columns).filter(Columns.id == id).one()
        sess.delete(columns)
        sess.commit()
        self.redirect('/product_column_add')




# 标签列表
class Product_label(BaseHandler):
    def get(self, *args, **kwargs):

        self.render('../templates/product_label.html')




# 添加标签
class Product_label_add(BaseHandler):
    def get(self, *args, **kwargs):
        label = sess.query(Label).all()
        mes = {}
        mes['data'] = ''
        self.render('../templates/product_label_add.html', label=label,**mes)
    def post(self, *args, **kwargs):
        label = sess.query(Label).all()
        mes = {}
        name = self.get_argument('name', '')
        if not name:
            mes['data'] = '参数不能为空，请重新输入'
            self.render('../templates/product_label_add.html',label=label,**mes)
        else:
            try:
                sess.query(Label).filter(Label.name==name).one()
            except:
                label = Label(name=name)
                sess.add(label)
                sess.commit()
                self.redirect('/product_label_add')
            else:
                 mes['data'] = '此分类已存在，可添加其他'
                 self.render('../templates/product_label_add.html',label=label,**mes)




# 删除标签
class Label_del(BaseHandler):
    def get(self, id):
        label = sess.query(Label).filter(Label.id == id).one()
        sess.delete(label)
        sess.commit()
        self.redirect('/product_label_add')




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
        self.render('../templates/system_add.html')
    def post(self, *srgs, **kwsrgs):
        site_name = self.get_argument('site_name', '')
        domain_name = self.get_argument('domain_name', '')
        describe = self.get_argument('describe', '')
        copyrights = self.get_argument('copyrights', '')
        number = self.get_argument('number', '')
        SMTP_server = self.get_argument('SMTP_server', '')
        SMTP_port = self.get_argument('SMTP_port', '')
        mail_account = self.get_argument('mail_account', '')
        email_password = self.get_argument('email_password', '')
        email_address = self.get_argument('email_address', '')
        system = System(site_name=site_name,domain_name=domain_name,describe=describe,
                number=number,copyrights=copyrights,SMTP_server=SMTP_server,SMTP_port=SMTP_port,
                mail_account=mail_account,email_password=email_password,email_address=email_address
                )
        sess.add(system)
        sess.commit()
        self.redirect('/system_base')




# # 系统设置（修改）
# class System_base(BaseHandler):
#     def get(self, *args, **kwargs):
#         system = sess.query(System).filter_by(id=1).first()
#         self.render('../templates/system_base.html',system=system)
#     def post(self, *args, **kwargs):
#         p = sess.query(System).filter_by(id=1).first()
#         site_name = self.get_argument('site_name', '')
#         domain_name = self.get_argument('domain_name', '')
#         describe = self.get_argument('describe', '')
#         copyrights = self.get_argument('copyrights', '')
#         number = self.get_argument('number', '')
#         SMTP_server = self.get_argument('SMTP_server', '')
#         SMTP_port = self.get_argument('SMTP_port', '')
#         mail_account = self.get_argument('mail_account', '')
#         email_password = self.get_argument('email_password', '')
#         email_address = self.get_argument('email_address', '')
#         p.site_name = site_name
#         p.domain_name = domain_name
#         p.describe = describe
#         p.copyrights = copyrights
#         p.SMTP_server = SMTP_server
#         p.SMTP_port = SMTP_port
#         p.email_password = email_password
#         p.email_address = email_address
#         p.number = number
#         p.mail_account = mail_account
#         sess.commit()
#         self.redirect('/system_base')



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



# 修改微视频信息
class Product_micro_edit(BaseHandler):
    def get(self, id):
        micro_video = sess.query(Micro_video).filter_by(id=id).first()
        self.render('../templates/product_micro_edit.html', micro_video=micro_video)
    def post(self, id):
        p = sess.query(Micro_video).filter_by(id=id).first()
        name = self.get_argument('name', '')
        p.name = name
        sess.commit()
        self.redirect('/product_micro')



#微视频详情
class Product_micro_details(BaseHandler):
    def get(self,id):
        micro_video = sess.query(Micro_video).filter(Micro_video.id == id ).one()
        movie = sess.query(Movie).filter(Movie.micro_video_id == id ).one()
        picture = sess.query(Picture).filter(Picture.micro_video_id == id ).one()

        self.render('../templates/Product_micro_details.html',micro_video=micro_video,movie=movie,picture=picture)



# 删除微视频
class Micro_del(BaseHandler):
    def get(self, id):
        micro_video = sess.query(Micro_video).filter(Micro_video.id == id ).one()
        sess.delete(micro_video)
        sess.commit()
        self.redirect('/product_micro')




import os 
#微视频上传图片
class Upload_micro(BaseHandler):
    async def get(self,id):
        micro_video = sess.query(Micro_video).filter_by(id=id).first()
        self.render('../templates/upload_micro.html', micro_video=micro_video)

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
            print(filename)
            print(file_path)
            with open(file_path, 'wb') as up:
                up.write(meta['body'])

                qiniu_upload(filename, file_path)

                g_img = Picture(picture_name= "http://q2cbcbetl.bkt.clouddn.com/"+filename,
                                micro_video_id = goods
                                )
                sess.add(g_img)
                sess.commit()
                print(g_img)

        self.write(json.dumps({'status': 'ok'}, ensure_ascii=False))




#微视频 上传视频
class Upload_video(BaseHandler):
    def get(self,id):
        micro_video = sess.query(Micro_video).filter_by(id=id).first()
        self.render('../templates/upload_video.html',micro_video=micro_video)

    def post(self,id):
        ret = {'result': 'OK'}

        upload_path = os.path.dirname(os.path.dirname(__file__))+"/static/files/"      #文件的暂存路径

        file_metas = self.request.files.get('file', None)  # 提取表单中‘name’为‘file’的文件元数据
        goods = self.get_argument('goods')

        if not file_metas:
            ret['result'] = 'Invalid Args'
            return ret

        for meta in file_metas:
            filename = meta['filename']
            file_path = os.path.join(upload_path,filename)
            print(file_path)
            with open(file_path, 'wb') as up:
                up.write(meta['body'])
            qiniu_upload(filename,file_path)

            
            print(filename)
            g_img = Movie(movie_name="http://q2cbcbetl.bkt.clouddn.com/"+filename,
            micro_video_id=goods)
            sess.add(g_img)
            sess.commit()
            print(g_img)

            self.redirect('/product_micro')





# 视频列表
class Movie_list(BaseHandler):
    def get(self, *args, **kwargs):
        movie = sess.query(Movie).all()
        self.render('../templates/movie_list.html', movie=movie)



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
 

import os 
#微视频上传图片
class Upload(BaseHandler):
    async def get(self):
        self.render('../templates/zaqxsw.html')

    async def post(self):

        # 接收文件，以对象的形式
        img = self.request.files.get('file', None)
        # 获取jquery传来的值
        print(img)

        # 写入本地
        for meta in img:
            filename = meta['filename']

            file_path = 'http://q2cbcbetl.bkt.clouddn.com/'+filename

            print(filename)
            print(file_path)
            
            qiniu_upload(filename, file_path)


            # with open(file_path, 'wb') as up:
            #     up.write(meta['body'])


            g_img = Picture(picture_name= "http://q2cbcbetl.bkt.clouddn.com/"+filename
                            )
            sess.add(g_img)
            sess.commit()
            print(g_img)
            # with open(file_path, 'wb') as up:
            #     up.write(meta['body'])

                # qiniu_upload(filename, file_path)

                # g_img = Picture(picture_name= "http://q2cbcbetl.bkt.clouddn.com/"+filename,
                #                 micro_video_id = goods
                #                 )
                # sess.add(g_img)
                # sess.commit()
                # print(g_img)

        self.write(json.dumps({'status': 'ok'}, ensure_ascii=False))



###################################################################
import json
import re

class RegisterHanler(BaseHandler):
    async def get(self, *args, **kwargs):
        self.write(json.dumps({"status":200,"msg":"返回成功"},ensure_ascii=False,indent=4))
    async def post(self ,*args ,**kwargs):
        phoneno = self.get_argument('phoneno')
        password = self.get_argument('password')
        code = self.get_argument('code')
        if not all([phoneno,password,code]):
            self.write(json.dumps({'status':10010,'msg':'内容输入不全'},ensure_ascii=False,index=4))
        else:
            if re.match('^1[3578]\d{9}$',phoneno):
                user = sess.query(User).filter(User.phone == phoneno).first()
                if not user:
                    user = User(phone=phoneno,password=password)
                    sess.add(user)
                    sess.commit()
                    self.write(json.dumps({'status':200,'msg':'注册成功'},ensure_ascii=False,indent=4))
                else:
                    self.write(json.dumps({'status':10011,'msg':'手机号已注册'},ensure_ascii=False,indent=4))
            else:
                self.write(json.dumps({'status':10012,'msg':'手机号格式不正确'},ensure_ascii=False,indent=4))




class LoginHanler(BaseHandler):
    async def get(self, *args, **kwargs):
        self.write(json.dumps({'status':200,'msg':'返回成功'},ensure_ascii=False,indent=4))
    async def post(self, *args, **kwargs):
        phoneno = self.get_argument('phoneno')
        password = self.get_argument('password')
        if not all([phoneno,password]):
            self.write(json.dumps({'status':10010,'msg':'内容输入不全'},ensure_ascii=False,indent=4))
        else:
            user = sess.query(User).filter(User.phone==phoneno).first()
            if user:
                if user.password == password:
                    self.write(json.dumps({'status':200,'msg':'登录成功'},ensure_ascii=False,indent=4))
                else:
                    self.write(json.dumps({'status':10010,'msg':'密码错误，请重新输入'},ensure_ascii=False,indent=4))
            else:
                self.write(json.dumps({'status':10011,'msg':'用户名不存在，请注册'},ensure_ascii=False,indent=4))

            

     

class IndexHanler(BaseHandler):
    async def get(self, *args, **kwargs):
        self.write(json.dumps({'status':200,'msg':'返回成功'},ensure_ascii=False,indent=4))
    async def post(self, *args, **kwargs):
        pass


