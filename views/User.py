from .base import BaseHandler
from models import *
import json


#用户列表
class User_list(BaseHandler):
    def get(self,*args,**kwargs):
        user = sess.query(User).all()
        lens = len(user)
        u_list = []
        for i in user:
            u_dict = {}
            u_dict['id'] = i.id
            u_dict['name'] = i.name
            u_dict['phone'] = i.phone
            u_dict['age'] = i.age
            u_dict['gender'] = i.gender
            u_dict['is_member'] = i.is_member
            u_dict['email'] = i.email
            u_dict['create_time'] = i.create_time   
            u_dict['is_activate'] = i.is_activate
            u_list.append(u_dict)
        self.render('../templates/member_list.html',user=u_list,lens=lens)
    def post(self,*args,**kwargs):
        title = self.get_argument('title','')
        user = sess.query(User).filter(User.name.like('%' + title + '%')).all()
        lens = len(user)
        u_list = []
        for i in user:
            u_dict = {}
            u_dict['id'] = i.id
            u_dict['name'] = i.name
            u_dict['phone'] = i.phone
            u_dict['age'] = i.age
            u_dict['gender'] = i.gender
            u_dict['is_member'] = i.is_member
            u_dict['email'] = i.email
            u_dict['create_time'] = i.create_time   
            u_dict['is_activate'] = i.is_activate
            u_list.append(u_dict)
        self.render('../templates/member_list.html',user=u_list,lens=lens)



# #有bug
# # 添加用户
# class User_add(BaseHandler):
#     def get(self, *args, **kwargs):
#         self.render('../templates/user-add.html')
#     def post(self, *args, **kwargs):
#         name = self.get_argument('name','')
#         password = self.get_argument('password','')
#         phone = self.get_argument('phone','')
#         gender = self.get_argument('gender')
#         age = self.get_argument('age')
#         is_member =  self.get_argument('is_member')
#         is_activate =  self.get_argument('is_activate')
#         email = self.get_argument('email','')
#         birthplace = self.get_argument('birthplace','')
#         add_user = User(name=name,password=password,phone=phone,email=email,age=age,gender=gender,is_member =is_member,is_activate=is_activate,birthplace=birthplace)
#         sess.add(add_user)
#         sess.commit()
#         self.redirect('/user_list')




# 添加用户
class Member_add(BaseHandler):
    def get(self,*args,**kwargs):
        mes = {}
        mes['data'] = ''
        self.render('../templates/member_add.html',**mes)
    def post(self):
        mes = {}
        name = self.get_argument('name','')
        gender = self.get_argument('gender','')
        phone = self.get_argument('phone','')
        email = self.get_argument('email','')
        age = self.get_argument('age','')
        birthplace = self.get_argument('birthplace','')
        if not all([name,gender,phone,email,age,birthplace]):
            mes['data'] = '参数不能为空,请重新输入'
            self.render('../templates/member_add.html',**mes)
        else:
            try:
                sess.query(User).filter(User.name==name).one()
            except:
                user = User(name=name,gender=gender,phone=phone,birthplace=birthplace,email=email,age=age)
                sess.add(user)
                sess.commit()
                self.redirect('/user_list')
            else:
                mes['data'] = '此用户名已被占用'
                self.render('../templates/member_add.html',**mes)




# 删除用户
class User_del(BaseHandler):
    def get(self, id):
        user = sess.query(User).filter(User.id == id).one()
        sess.delete(user)
        sess.commit()
        self.redirect('/user_list')


class User_change_password(BaseHandler):
    def get(self,id, *args, **kwargs):
        user = sess.query(User).filter(User.id==id).one()
        self.render('../templates/user-change-password.html',user=user)
    def post(self,id, *args, **kwargs):
        user = sess.query(User).filter(User.id==id).one()
        newpassword = self.get_argument("newpassword2",'')
        print(newpassword)
        user.password = newpassword
        sess.commit()
        self.redirect("/user_list")




import os
#用户上传头像
class Upload_user(BaseHandler):
    async def get(self,id):
        user = sess.query(User).filter_by(id=id).first()
        self.render('../templates/upload_user.html', user=user)

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
                            user_id = goods
                            )
            sess.add(g_img)
            sess.commit()
        self.write(json.dumps({'status': 'ok'}, ensure_ascii=False))



# 修改用户
class Member_edit(BaseHandler):
    def get(self, id):
        user = sess.query(User).filter_by(id=id).first()
        self.render('../templates/member-update.html', user=user)
    def post(self, id):
        p = sess.query(User).filter_by(id=id).first()
        name = self.get_argument('name','')
        gender = self.get_argument('gender','')
        phone = self.get_argument('phone','')
        email = self.get_argument('email','')
        age = self.get_argument('age','')
        birthplace = self.get_argument('birthplace','')
        p.name = name
        p.gender = gender
        p.birthplace = birthplace
        p.phone = phone
        p.age = age
        p.email = email
        p.birthplace = birthplace
        sess.commit()
        self.redirect('/user_list')



# 删除的用户
class Member_user_del(BaseHandler):
    def get(self, *args, **kwargs):
        user = sess.query(User).filter(User.is_activate==1).all()
        lens = len(user)
        self.render('../templates/member_del.html',user=user,lens=lens)



#用户详情
class Member_show(BaseHandler):
    def get(self,id):
        user = sess.query(User).filter(User.id == id ).one()
        self.render('../templates/member_show.html',user=user)


        