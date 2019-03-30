from django.conf.urls import url
from django.urls import path
from . import views

# 应用命名空间
app_name = 'user'

urlpatterns = [
    path('login',views.login)

]