from django.contrib import admin
from .models import *
# Register your models here.


# inline 内部嵌套
class UserInline(admin.StackedInline):
    '''
    继承StackedInline就是多个表单
    如果继承TabularInline的话就是表格形式
    '''
    # 选择你要选择哪个模型类 嵌套进去
    model = UserInfo
    # 额外添加几个数据
    extra = 3


#定义一个类 可以对后台显示的界面显示的字段进行编辑
class UserInfoAdmin(admin.ModelAdmin):
    # #定义显示的字段 可以点击列头进行排序
    # list_display = ['user','gender','image','blood','start_workout_data']
    # #定义一个过滤器 过滤框会显示在右侧
    # list_filter = ['start_workout_data']
    # # 查找
    # search_fields = ['user']
    # # 显示多少页 分页框会显示在下侧
    # list_per_page = 10
    #
    # # [添加页和修改页]可以设置修改数据页面的分类
    # fieldsets = [
    #     ('一个分类',{'fields':['gender']}),
    #     ('另一个分类',{'fields':['blood']})
    # ]

    # 定义要嵌入的 列表内可以写多个
    inlines = [UserInline]

admin.site.register(User,UserInfoAdmin)
admin.site.register(UserInfo)
admin.site.register(WorkoutPlan)
