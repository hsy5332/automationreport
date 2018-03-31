import time
import json

from django.shortcuts import render
from automationquery import models
from django.http import HttpResponse


def index(request):
    userinfo = models.automation_user.objects.get(id=1)
    return render(request, 'index.html',{"TEST": userinfo.username})


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
    if request.POST:
        if token(request.POST['token']):
            try:
                userinfo = models.automation_user.objects.get(username=request.POST['username'],
                                                              password=request.POST['password'])
                if userinfo.userstatus == "1":
                    print(userinfo.userstatus)
                    usermessage = {
                        "userid": userinfo.id,
                        "username": userinfo.username,
                        "nickname": userinfo.nickname,
                        "userstatus": userinfo.userstatus,
                        "createdtime": userinfo.createdtime,
                        "updatetime": userinfo.updatetime
                    }
                    login_userinfo = {"code": "200", "msg": "success", "data": usermessage}
                    return HttpResponse(json.dumps(login_userinfo))
                elif userinfo.userstatus == "0":
                    login_usererror = {"code": "100", "msg": "该用户账号已经被禁用，请联系管理员。", "data": {}}
                    return HttpResponse(json.dumps(login_usererror))
                else:
                    login_usererror = {"code": "101", "msg": "该用户账号异常，请联系管理员。", "data": {}}
                    return HttpResponse(json.dumps(login_usererror))
            except:
                login_accounterror = {"code" : "102","msg" : "账号或密码错误", "data" : {}}
                return HttpResponse(json.dumps(login_accounterror))
        else:
            login_tokenerror = {"code" : "-11", "msg" : "token过期", "data" : {}}
            return HttpResponse(json.dumps(login_tokenerror))
    else:
        login_error = {"code" : "-12", "msg" : "请求方式错误", "data" : {}}
        return HttpResponse(json.dumps(login_error))



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
