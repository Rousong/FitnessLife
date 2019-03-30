from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
    context = {
        'haha':'哈哈哈',
    }

    return render(response,'index.html',context)


def login(response):
    return HttpResponse("注册页面")