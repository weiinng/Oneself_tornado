from .base import BaseHandler
from models import AdminUser,sess,User
import json

# 用户列表
class User_list(BaseHandler):
    def get(self, *args, **kwargs):
        user = sess.query(User).all()
        len_user = len(user)
        self.render('../templates/user-list.html',len_user=len_user,userlist=user)
    def post(self, *args, **kwargs):
        # user = sess.query(User).filter(User.name.like('%' + title + '%')).all()
        pass


#有bug
# 添加用户
class User_add(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/user-add.html')
    def post(self):
        name = self.get_argument('name','')
        password = self.get_argument('password','')
        phone = self.get_argument('phone','')
        gender = self.get_argument('gender')
        age = self.get_argument('age')
        is_member =  self.get_argument('is_member')
        is_activate =  self.get_argument('is_activate')
        email = self.get_argument('email','')
        birthplace = self.get_argument('birthplace','')
        add_user = User(name=name,password=password,phone=phone,email=email,age=age,gender=gender,is_member =is_member,is_activate=is_activate,birthplace=birthplace)
        sess.add(add_user)
        sess.commit()
        self.write("添加完成！")


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



# 修改用户
class Member_edit(BaseHandler):
    def get(self, id):
        user = sess.query(User).filter_by(id=id).first()
        self.render('../templates/member-update.html', user=user)

    def post(self, id):
        p = sess.query(User).filter_by(id=id).first()
        name = self.get_argument('name')
        gender = self.get_argument('gender')
        birthplace = self.get_argument('birthplace')
        phone = self.get_argument('phone')
        p.name = name
        p.gender = gender
        p.birthplace = birthplace
        p.phone = phone
        sess.commit()
        self.redirect('/member_list')


# 删除的会员
class Member_user_del(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/member_del.html')