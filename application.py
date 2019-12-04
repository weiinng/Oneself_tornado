import tornado.web
from views import Index,adminuser,User
import config


# 路由
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            #主页面操作
            (r"/index", Index.IndexHandler),
            (r"/", Index.Index),  # 首页
            (r"/welcome", Index.Welcome),  # 我的桌面


            #管理员相关
            (r"/login", adminuser.Login),  # 登录
            (r"/admin_list", adminuser.Admin_list),  # 管理员列表
            (r"/admin_add", adminuser.Admin_add),  # 管理员添加
            (r"/admin_compile/(\d)", adminuser.Admin_compile),  # 管理员编辑
            (r"/admin_delete/(\d)", adminuser.Admin_delete),  # 管理员编辑

            (r"/admin_role", adminuser.Admin_role),  # 角色管理
            (r"/admin_permission", adminuser.Admin_permission),  # 权限管理

            #用户管理
            (r"/user_list",User.User_list),              #用户管理
            (r"/member_user_del",User.Member_user_del),     #删除的用户
            (r"/member_add",User.Member_add),             #添加用户
            (r"/user_del/(\d)", User.User_del),        #删除用户
            (r"/member_edit/(\d)",User.Member_edit),    #修改用户
            (r"/user_change_password/(\d)",User.User_change_password),    #修改密码
            (r"/member_show/(\d)",User.Member_show),   #用户详情
            (r"/upload_user/(\d+)", User.Upload_user),  # 用户头像上传


            (r"/article_list", Index.Article_list),  # 资讯管理
            (r"/picture_list", Index.Picture_list),  # 图片管理
            (r"/picture_show", Index.Picture_show),  # 图片展示
            (r"/picture_del/(\d+)", Index.Picture_del),  # 删除图片
            # (r"/picture_edit/(\d+)", Index.Picture_edit),         #修改图片


            (r"/product_brand", Index.Product_brand),  # 明星管理
            (r"/product_brand_add", Index.Product_brand_add),  # 添加明星
            (r"/active_del/(\d+)", Index.Active_del),  # 删除明星
            (r"/product_brand_edit/(\d+)", Index.Product_brand_edit),  # 修改明星
            (r"/product_show/(\d+)", Index.Product_show),  # 明星详情
            (r"/upload_brand/(\d+)", Index.Upload_brand),  # 明星图片上传



            (r"/product_category", Index.Product_category),  # 分类管理
            (r"/product_category_add", Index.Product_category_add),  # 添加分类
            (r"/category_del/(\d+)", Index.Category_del),  # 删除分类


            (r"/product_list", Index.Product_list),  # 视频管理
            (r"/product_add", Index.Product_add),  # 添加视频
            (r"/product_del/(\d+)", Index.Product_del),  # 删除视频
            (r"/product_edit/(\d+)", Index.Product_edit),  # 修改视频
            (r"/product_details/(\d+)", Index.Product_details),  # 视频详情
            (r"/upload_product/(\d+)", Index.Upload_product),  # 视频图片上传


            (r"/feedment_list", Index.Feedment_list),  # 评论列表
            (r"/feedment_del/(\d+)", Index.Feedment_del),  # 删除评论

            (r"/feedback_list", Index.Feedback_list),  # 意见反馈


            (r"/member_level", Index.Member_level),  # 等级管理
            (r"/member_scoreoperation", Index.Member_scoreoperation),  # 积分管理
            (r"/member_record_browse", Index.Member_record_browse),  # 浏览记录
            (r"/member_record_download", Index.Member_record_download),  # 下载记录
            (r"/member_record_share", Index.Member_record_share),  # 分享记录





            (r"/charts_1", Index.Charts_1),  # 折线图
            (r"/charts_2", Index.Charts_2),  # 时间轴折线图
            (r"/charts_3", Index.Charts_3),  # 区域图
            (r"/charts_4", Index.Charts_4),  # 柱状图
            (r"/charts_5", Index.Charts_5),  # 饼状图
            (r"/charts_6", Index.Charts_6),  # 3D柱状图
            (r"/charts_7", Index.Charts_7),  # 3D饼状图


            (r"/system_base", Index.System_base),  # 系统设置
            (r"/system_category", Index.System_category),  # 栏目管理
            (r"/system_data", Index.System_data),  # 数据字典
            (r"/system_shielding", Index.System_shielding),  # 屏蔽词
            (r"/system_log", Index.System_log),  # 系统日志


            (r"/article_add", Index.Article_add),  # 添加资讯
            (r"/picture_add", Index.Picture_add),  # 添加图片
            (r"/product_add", Index.Product_add),  # 添加产品


        ]
        super(Application, self).__init__(handlers, **config.setting)