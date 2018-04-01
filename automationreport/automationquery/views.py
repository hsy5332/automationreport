import time
import json
import datetime

from django.shortcuts import render
from automationquery import models
from django.http import HttpResponse


def index(request):
    userinfo = models.automation_user.objects.get(id=1)
    return render(request, 'index.html', {"TEST": userinfo.username})


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
                login_accounterror = {"code": "102", "msg": "账号或密码错误", "data": {}}
                return HttpResponse(json.dumps(login_accounterror))
        else:
            login_tokenerror = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(login_tokenerror))
    else:
        login_error = {"code": "-12", "msg": "请求方式错误", "data": {}}
        return HttpResponse(json.dumps(login_error))


# cpu占有率
def cpu(request):
    if request.POST:
        if token(request.POST['token']):
            try:
                if request.POST['startdate'] and request.POST['enddate'] != "":
                    startdate = request.POST['startdate']
                    enddate = request.POST['enddate']
                    querydatas = models.automation_launch_app.objects.filter(caseid=request.POST['caseid'])
                    querydatalist = []
                    for querydata in range(0, len(querydatas)):
                        if querydatas[querydata].createdtime <= enddate and querydatas[
                            querydata].createdtime >= startdate:
                            cpu_querydata = {
                                "id": querydatas[querydata].id,
                                "caseid": querydatas[querydata].caseid,
                                "cpuproportion": querydatas[querydata].cpuproportion,
                                "starttime": querydatas[querydata].starttime,
                                "endtime": querydatas[querydata].endtime,
                                "monkeyscript": querydatas[querydata].monkeyscript,
                                "functionscript": querydatas[querydata].functionscript,
                                "runtime": querydatas[querydata].runtime,
                                "eventid": querydatas[querydata].eventid,
                                "createdtime": querydatas[querydata].createdtime
                            }
                            querydatalist.append(cpu_querydata)
                    return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": querydatalist}))
                else:
                    querydatas = models.automation_launch_app.objects.filter(caseid=request.POST['caseid'])
                    querydatalist = []
                    for querydata in range(0, len(querydatas)):
                        cpu_querydata = {
                            "id": querydatas[querydata].id,
                            "caseid": querydatas[querydata].caseid,
                            "cpuproportion": querydatas[querydata].cpuproportion,
                            "starttime": querydatas[querydata].starttime,
                            "endtime": querydatas[querydata].endtime,
                            "monkeyscript": querydatas[querydata].monkeyscript,
                            "functionscript": querydatas[querydata].functionscript,
                            "runtime": querydatas[querydata].runtime,
                            "eventid": querydatas[querydata].eventid,
                            "createdtime": querydatas[querydata].createdtime
                        }
                        querydatalist.append(cpu_querydata)
                    return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": querydatalist}))
            except:
                return HttpResponse(json.dumps({"code": "-13", "msg": "查询数据出错，请检查参数。", "data": {}}))
        else:
            cpu_tokenerror = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(cpu_tokenerror))
    else:
        cpu_error = {"code": "-12", "msg": "请求方式错误", "data": {}}
        return HttpResponse(json.dumps(cpu_error))


# 启动App时间查询
def launchapp(request):
    if request.POST:
        if token(request.POST['token']):
            try:
                if request.POST['startdate'] and request.POST['enddate'] != "":
                    startdate = request.POST['startdate']
                    enddate = request.POST['enddate']
                    launchappdatas = models.automation_launch_app.objects.filter(caseid=request.POST['caseid'])
                    launchappdatalist = []
                    for launchappdata in range(0, len(launchappdatas)):
                        if launchappdatas[launchappdata].createdtime <= enddate and launchappdatas[
                            launchappdata].createdtime >= startdate:
                            print(launchappdatas[0].id)
                            cpu_querydata = {
                                "id": launchappdatas[launchappdata].id,
                                "starttime": launchappdatas[launchappdata].starttime,
                                "launchtime": launchappdatas[launchappdata].launchtime,
                                "endtime": launchappdatas[launchappdata].endtime,
                                "launchtype": launchappdatas[launchappdata].launchtype,
                                "eventid": launchappdatas[launchappdata].eventid,
                                "caseid": launchappdatas[launchappdata].caseid,
                                "createdtime": launchappdatas[launchappdata].createdtime
                            }
                            launchappdatalist.append(cpu_querydata)
                    return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": launchappdatalist}))
                else:
                    launchappdatas = models.automation_cpu_app.objects.filter(caseid=request.POST['caseid'])
                    launchappdatalist = []
                    for launchappdata in range(0, len(launchappdatas)):
                        cpu_querydata = {
                            "id": launchappdatas[launchappdata].id,
                            "starttime": launchappdatas[launchappdata].starttime,
                            "launchtime": launchappdatas[launchappdata].launchtime,
                            "endtime": launchappdatas[launchappdata].endtime,
                            "launchtype": launchappdatas[launchappdata].launchtype,
                            "launchtime": launchappdatas[launchappdata].launchtime,
                            "eventid": launchappdatas[launchappdata].eventid,
                            "caseid": launchappdatas[launchappdata].caseid,
                            "createdtime": launchappdatas[launchappdata].createdtime
                        }
                        launchappdatalist.append(cpu_querydata)
                    return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": launchappdatalist}))
            except:
                return HttpResponse(json.dumps({"code": "-13", "msg": "查询数据出错，请检查参数。", "data": {}}))
        else:
            launchapp = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(launchapp))
    else:
        launchapp_error = {"code": "-12", "msg": "请求方式错误", "data": {}}
        return HttpResponse(json.dumps(launchapp_error))


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
