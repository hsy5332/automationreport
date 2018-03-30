import time
from django.shortcuts import render
from automationquery import models
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


# token计算规则
def token(token):
    try:
        if int(token) + 86400 > int(time.time()):  # 86400是一天的时间戳
            return True
        else:
            return False
    except:
        return False


# 登录接口
def login(request):
    return render(request, 'index.html')


# cpu占有率
def cpu(request):
    return render(request, 'index.html')


# 启动App时间查询
def launchapp(request):
    return render(request, 'index.html')


# 内存占有率查询
def menapp(request):
    return render(request, 'index.html')


# 接口测试查询
def interface(request):
    return render(request, 'index.html')


# App功能测试查询
def functionapp(request):
    return render(request, 'index.html')


# Web功能测试查询
def functionweb(request):
    return render(request, 'index.html')
