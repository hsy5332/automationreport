import time
import json
import datetime

from django.shortcuts import render
from automationquery import models
from django.http import HttpResponse


#登录页面
def index(request):
    return render(request, 'index.html')

#查询页面
def query(request):
    return render(request, 'query.html')

def main(request):
    return render(request,'main.html')

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
                    # 判断开始时间和结束时间是否为空
                    if request.POST['eventid'] != "":
                        # 判断eventid 是否为空
                        startdate = request.POST['startdate']
                        enddate = request.POST['enddate']
                        querydatas = models.automation_cpu_app.objects.filter(caseid=request.POST['caseid'])
                        querydatalist = []
                        for querydata in range(0, len(querydatas)):
                            if querydatas[querydata].createdtime <= enddate and querydatas[
                                querydata].createdtime >= startdate and request.POST[
                                'eventid'] in querydatas[querydata].eventid:
                                print()
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
                        startdate = request.POST['startdate']
                        enddate = request.POST['enddate']
                        querydatas = models.automation_cpu_app.objects.filter(caseid=request.POST['caseid'])
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
                    if request.POST['eventid'] != "":
                        querydatas = models.automation_cpu_app.objects.filter(caseid=request.POST['caseid'])
                        querydatalist = []
                        for querydata in range(0, len(querydatas)):
                            if request.POST['eventid'] in querydatas[querydata].eventid:
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
                        querydatas = models.automation_cpu_app.objects.filter(caseid=request.POST['caseid'])
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
                    if request.POST['eventid'] != "":
                        startdate = request.POST['startdate']
                        enddate = request.POST['enddate']
                        launchappdatas = models.automation_launch_app.objects.filter(caseid=request.POST['caseid'])
                        launchappdatalist = []
                        for launchappdata in range(0, len(launchappdatas)):
                            if launchappdatas[launchappdata].createdtime <= enddate and launchappdatas[
                                launchappdata].createdtime >= startdate and request.POST['eventid'] in launchappdatas[
                                launchappdata].eventid:
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
                        startdate = request.POST['startdate']
                        enddate = request.POST['enddate']
                        launchappdatas = models.automation_launch_app.objects.filter(caseid=request.POST['caseid'])
                        launchappdatalist = []
                        for launchappdata in range(0, len(launchappdatas)):
                            if launchappdatas[launchappdata].createdtime <= enddate and launchappdatas[
                                launchappdata].createdtime >= startdate:
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
                    if request.POST['eventid'] != "":
                        launchappdatas = models.automation_cpu_app.objects.filter(caseid=request.POST['caseid'])
                        launchappdatalist = []
                        for launchappdata in range(0, len(launchappdatas)):
                            if request.POST['eventid'] in launchappdatas[
                                launchappdata].eventid:
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
            launchapp_tokenerror = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(launchapp_tokenerror))
    else:
        launchapp_error = {"code": "-12", "msg": "请求方式错误", "data": {}}
        return HttpResponse(json.dumps(launchapp_error))


# 内存占有率查询
def menapp(request):
    if request.POST:
        if token(request.POST['token']):
            try:
                if request.POST['startdate'] and request.POST['enddate'] != "":
                    if request.POST['eventid'] != "":
                        startdate = request.POST['startdate']
                        enddate = request.POST['enddate']
                        menappdatas = models.automation_mem_app.objects.filter(caseid=request.POST['caseid'])
                        menappdataslist = []
                        for menappdata in range(0, len(menappdatas)):
                            if menappdatas[menappdata].createdtime >= startdate and menappdatas[
                                menappdata].createdtime <= enddate and request.POST['eventid'] in menappdatas[
                                menappdata].eventid:
                                menapp_querydata = {
                                    "id": menappdatas[menappdata].id,
                                    "caseid": menappdatas[menappdata].caseid,
                                    "starttime": menappdatas[menappdata].starttime,
                                    "endtime": menappdatas[menappdata].endtime,
                                    "memorysize": menappdatas[menappdata].memorysize,
                                    "monkeyscript": menappdatas[menappdata].monkeyscript,
                                    "functionscript": menappdatas[menappdata].functionscript,
                                    "runtime": menappdatas[menappdata].runtime,
                                    "eventid": menappdatas[menappdata].eventid,
                                    "createdtime": menappdatas[menappdata].createdtime,
                                }
                                menappdataslist.append(menapp_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": menappdataslist}))
                    else:
                        startdate = request.POST['startdate']
                        enddate = request.POST['enddate']
                        menappdatas = models.automation_mem_app.objects.filter(caseid=request.POST['caseid'])
                        menappdataslist = []
                        for menappdata in range(0, len(menappdatas)):
                            if menappdatas[menappdata].createdtime >= startdate and menappdatas[
                                menappdata].createdtime <= enddate:
                                menapp_querydata = {
                                    "id": menappdatas[menappdata].id,
                                    "caseid": menappdatas[menappdata].caseid,
                                    "starttime": menappdatas[menappdata].starttime,
                                    "endtime": menappdatas[menappdata].endtime,
                                    "memorysize": menappdatas[menappdata].memorysize,
                                    "monkeyscript": menappdatas[menappdata].monkeyscript,
                                    "functionscript": menappdatas[menappdata].functionscript,
                                    "runtime": menappdatas[menappdata].runtime,
                                    "eventid": menappdatas[menappdata].eventid,
                                    "createdtime": menappdatas[menappdata].createdtime,
                                }
                                menappdataslist.append(menapp_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": menappdataslist}))
                else:
                    if request.POST['eventid'] != "":
                        menappdatas = models.automation_mem_app.objects.filter(caseid=request.POST['caseid'])
                        menappdataslist = []
                        for menappdata in range(0, len(menappdatas)):
                            if request.POST['eventid'] in menappdatas[menappdata].eventid:
                                menapp_querydata = {
                                    "id": menappdatas[menappdata].id,
                                    "caseid": menappdatas[menappdata].caseid,
                                    "starttime": menappdatas[menappdata].starttime,
                                    "endtime": menappdatas[menappdata].endtime,
                                    "memorysize": menappdatas[menappdata].memorysize,
                                    "monkeyscript": menappdatas[menappdata].monkeyscript,
                                    "functionscript": menappdatas[menappdata].functionscript,
                                    "runtime": menappdatas[menappdata].runtime,
                                    "eventid": menappdatas[menappdata].eventid,
                                    "createdtime": menappdatas[menappdata].createdtime,
                                }
                                menappdataslist.append(menapp_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": menappdataslist}))
                    else:
                        menappdatas = models.automation_mem_app.objects.filter(caseid=request.POST['caseid'])
                        menappdataslist = []
                        for menappdata in range(0, len(menappdatas)):
                            menapp_querydata = {
                                "id": menappdatas[menappdata].id,
                                "caseid": menappdatas[menappdata].caseid,
                                "starttime": menappdatas[menappdata].starttime,
                                "endtime": menappdatas[menappdata].endtime,
                                "memorysize": menappdatas[menappdata].memorysize,
                                "monkeyscript": menappdatas[menappdata].monkeyscript,
                                "functionscript": menappdatas[menappdata].functionscript,
                                "runtime": menappdatas[menappdata].runtime,
                                "eventid": menappdatas[menappdata].eventid,
                                "createdtime": menappdatas[menappdata].createdtime,
                            }
                            menappdataslist.append(menapp_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": menappdataslist}))
            except:
                return HttpResponse(json.dumps({"code": "-13", "msg": "查询数据出错，请检查参数。", "data": {}}))
        else:
            menapp_tokenerror = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(menapp_tokenerror))
    else:
        menapp_error = {"code": "-12", "msg": "请求方式错误", "data": {}}
        return HttpResponse(json.dumps(menapp_error))


# 接口测试查询
def interface(request):
    if request.POST:
        if token(request.POST['token']):
            try:
                if request.POST['startdate'] and request.POST['enddate'] != "":
                    if request.POST['eventid'] != "":
                        startdate = request.POST['startdate']
                        enddate = request.POST['enddate']
                        interfacedatas = models.automation_interface.objects.filter(caseid=request.POST['caseid'])
                        interfacedatalist = []
                        for interfacedata in range(0, len(interfacedatas)):
                            if interfacedatas[interfacedata].createdtime >= startdate and interfacedatas[
                                interfacedata].createdtime <= enddate and request.POST['eventid'] in interfacedatas[
                                interfacedata].eventid:
                                interface_querydata = {
                                    "id": interfacedatas[interfacedata].id,
                                    "caseid": interfacedatas[interfacedata].caseid,
                                    "interfaceurl": interfacedatas[interfacedata].interfaceurl,
                                    "requestparameter": interfacedatas[interfacedata].id,
                                    "returnparameter": interfacedatas[interfacedata].requestparameter,
                                    "requesttype": interfacedatas[interfacedata].requesttype,
                                    "casestatus": interfacedatas[interfacedata].casestatus,
                                    "remark": interfacedatas[interfacedata].remark,
                                    "eventid": interfacedatas[interfacedata].eventid,
                                    "createdtime": interfacedatas[interfacedata].createdtime,
                                }
                                interfacedatalist.append(interface_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": interfacedatalist}))
                    else:
                        startdate = request.POST['startdate']
                        enddate = request.POST['enddate']
                        interfacedatas = models.automation_interface.objects.filter(caseid=request.POST['caseid'])
                        interfacedatalist = []
                        for interfacedata in range(0, len(interfacedatas)):
                            if interfacedatas[interfacedata].createdtime >= startdate and interfacedatas[
                                interfacedata].createdtime <= enddate:
                                interface_querydata = {
                                    "id": interfacedatas[interfacedata].id,
                                    "caseid": interfacedatas[interfacedata].caseid,
                                    "interfaceurl": interfacedatas[interfacedata].interfaceurl,
                                    "requestparameter": interfacedatas[interfacedata].id,
                                    "returnparameter": interfacedatas[interfacedata].requestparameter,
                                    "requesttype": interfacedatas[interfacedata].requesttype,
                                    "casestatus": interfacedatas[interfacedata].casestatus,
                                    "remark": interfacedatas[interfacedata].remark,
                                    "eventid": interfacedatas[interfacedata].eventid,
                                    "createdtime": interfacedatas[interfacedata].createdtime,
                                }
                                interfacedatalist.append(interface_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": interfacedatalist}))
                else:
                    if request.POST['eventid'] != "":
                        interfacedatas = models.automation_interface.objects.filter(caseid=request.POST['caseid'])
                        interfacedatalist = []
                        for interfacedata in range(0, len(interfacedatas)):
                            if request.POST['eventid'] in interfacedatas[interfacedata].eventid:
                                interface_querydata = {
                                    "id": interfacedatas[interfacedata].id,
                                    "caseid": interfacedatas[interfacedata].caseid,
                                    "interfaceurl": interfacedatas[interfacedata].interfaceurl,
                                    "requestparameter": interfacedatas[interfacedata].id,
                                    "returnparameter": interfacedatas[interfacedata].requestparameter,
                                    "requesttype": interfacedatas[interfacedata].requesttype,
                                    "casestatus": interfacedatas[interfacedata].casestatus,
                                    "remark": interfacedatas[interfacedata].remark,
                                    "eventid": interfacedatas[interfacedata].eventid,
                                    "createdtime": interfacedatas[interfacedata].createdtime,
                                }
                                interfacedatalist.append(interface_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": interfacedatalist}))
                    else:
                        interfacedatas = models.automation_interface.objects.filter(caseid=request.POST['caseid'])
                        interfacedatalist = []
                        for interfacedata in range(0, len(interfacedatas)):
                            interface_querydata = {
                                "id": interfacedatas[interfacedata].id,
                                "caseid": interfacedatas[interfacedata].caseid,
                                "interfaceurl": interfacedatas[interfacedata].interfaceurl,
                                "requestparameter": interfacedatas[interfacedata].id,
                                "returnparameter": interfacedatas[interfacedata].requestparameter,
                                "requesttype": interfacedatas[interfacedata].requesttype,
                                "casestatus": interfacedatas[interfacedata].casestatus,
                                "remark": interfacedatas[interfacedata].remark,
                                "eventid": interfacedatas[interfacedata].eventid,
                                "createdtime": interfacedatas[interfacedata].createdtime,
                            }
                            interfacedatalist.append(interface_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": interfacedatalist}))
            except:
                return HttpResponse(json.dumps({"code": "-13", "msg": "查询数据出错，请检查参数。", "data": {}}))
        else:
            interface_tokenerror = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(interface_tokenerror))
    else:
        interface_error = {"code": "-12", "msg": "请求方式错误", "data": {}}
        return HttpResponse(json.dumps(interface_error))


# App功能测试查询
def functionapp(request):
    if request.POST:
        if token(request.POST['token']):
            try:
                if request.POST['startdate'] and request.POST['enddate'] != "":
                    if request.POST['eventid'] != "":
                        startdate = request.POST['startdate']
                        enddate = request.POST['enddate']
                        functionappdatas = models.automation_function_app.objects.filter(caseid=request.POST['caseid'])
                        functionappdatalist = []
                        for functionappdata in range(0, len(functionappdatas)):
                            if functionappdatas[functionappdata].createdtime >= startdate and functionappdatas[
                                functionappdata].createdtime <= enddate and request.POST['eventid'] in functionappdatas[
                                functionappdata].eventid:
                                functionapp_querydata = {
                                    "id": functionappdatas[functionappdata].id,
                                    "caseid": functionappdatas[functionappdata].caseid,
                                    "devicesinfos": functionappdatas[functionappdata].devicesinfos,
                                    "appiumport": functionappdatas[functionappdata].appiumport,
                                    "devicesexecute": functionappdatas[functionappdata].devicesexecute,
                                    "operatetype": functionappdatas[functionappdata].operatetype,
                                    "parameter": functionappdatas[functionappdata].parameter,
                                    "waittime": functionappdatas[functionappdata].waittime,
                                    "element": functionappdatas[functionappdata].element,
                                    "rundescribe": functionappdatas[functionappdata].rundescribe,
                                    "casereport": functionappdatas[functionappdata].casereport,
                                    "caseexecute": functionappdatas[functionappdata].caseexecute,
                                    "runcasetime": functionappdatas[functionappdata].runcasetime,
                                    "eventid": functionappdatas[functionappdata].eventid,
                                    "createdtime": functionappdatas[functionappdata].createdtime,
                                }
                                functionappdatalist.append(functionapp_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": functionappdatalist}))
                    else:
                        startdate = request.POST['startdate']
                        enddate = request.POST['enddate']
                        functionappdatas = models.automation_function_app.objects.filter(caseid=request.POST['caseid'])
                        functionappdatalist = []
                        for functionappdata in range(0, len(functionappdatas)):
                            if functionappdatas[functionappdata].createdtime >= startdate and functionappdatas[
                                functionappdata].createdtime <= enddate:
                                functionapp_querydata = {
                                    "id": functionappdatas[functionappdata].id,
                                    "caseid": functionappdatas[functionappdata].caseid,
                                    "devicesinfos": functionappdatas[functionappdata].devicesinfos,
                                    "appiumport": functionappdatas[functionappdata].appiumport,
                                    "devicesexecute": functionappdatas[functionappdata].devicesexecute,
                                    "operatetype": functionappdatas[functionappdata].operatetype,
                                    "parameter": functionappdatas[functionappdata].parameter,
                                    "waittime": functionappdatas[functionappdata].waittime,
                                    "element": functionappdatas[functionappdata].element,
                                    "rundescribe": functionappdatas[functionappdata].rundescribe,
                                    "casereport": functionappdatas[functionappdata].casereport,
                                    "caseexecute": functionappdatas[functionappdata].caseexecute,
                                    "runcasetime": functionappdatas[functionappdata].runcasetime,
                                    "eventid": functionappdatas[functionappdata].eventid,
                                    "createdtime": functionappdatas[functionappdata].createdtime,
                                }
                                functionappdatalist.append(functionapp_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": functionappdatalist}))
                else:
                    if request.POST['eventid'] != "":
                        functionappdatas = models.automation_function_app.objects.filter(caseid=request.POST['caseid'])
                        functionappdatalist = []
                        for functionappdata in range(0, len(functionappdatas)):
                            if request.POST['eventid'] in functionappdatas[functionappdata].eventid:
                                functionapp_querydata = {
                                    "id": functionappdatas[functionappdata].id,
                                    "caseid": functionappdatas[functionappdata].caseid,
                                    "devicesinfos": functionappdatas[functionappdata].devicesinfos,
                                    "appiumport": functionappdatas[functionappdata].appiumport,
                                    "devicesexecute": functionappdatas[functionappdata].devicesexecute,
                                    "operatetype": functionappdatas[functionappdata].operatetype,
                                    "parameter": functionappdatas[functionappdata].parameter,
                                    "waittime": functionappdatas[functionappdata].waittime,
                                    "element": functionappdatas[functionappdata].element,
                                    "rundescribe": functionappdatas[functionappdata].rundescribe,
                                    "casereport": functionappdatas[functionappdata].casereport,
                                    "caseexecute": functionappdatas[functionappdata].caseexecute,
                                    "runcasetime": functionappdatas[functionappdata].runcasetime,
                                    "eventid": functionappdatas[functionappdata].eventid,
                                    "createdtime": functionappdatas[functionappdata].createdtime,
                                }
                                functionappdatalist.append(functionapp_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": functionappdatalist}))
                    else:
                        functionappdatas = models.automation_function_app.objects.filter(caseid=request.POST['caseid'])
                        functionappdatalist = []
                        for functionappdata in range(0, len(functionappdatas)):
                            functionapp_querydata = {
                                "id": functionappdatas[functionappdata].id,
                                "caseid": functionappdatas[functionappdata].caseid,
                                "devicesinfos": functionappdatas[functionappdata].devicesinfos,
                                "appiumport": functionappdatas[functionappdata].appiumport,
                                "devicesexecute": functionappdatas[functionappdata].devicesexecute,
                                "operatetype": functionappdatas[functionappdata].operatetype,
                                "parameter": functionappdatas[functionappdata].parameter,
                                "waittime": functionappdatas[functionappdata].waittime,
                                "element": functionappdatas[functionappdata].element,
                                "rundescribe": functionappdatas[functionappdata].rundescribe,
                                "casereport": functionappdatas[functionappdata].casereport,
                                "caseexecute": functionappdatas[functionappdata].caseexecute,
                                "runcasetime": functionappdatas[functionappdata].runcasetime,
                                "eventid": functionappdatas[functionappdata].eventid,
                                "createdtime": functionappdatas[functionappdata].createdtime,
                            }
                            functionappdatalist.append(functionapp_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": functionappdatalist}))
            except:
                return HttpResponse(json.dumps({"code": "-13", "msg": "查询数据出错，请检查参数。", "data": {}}))
        else:
            functionapp_tokenerror = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(functionapp_tokenerror))
    else:
        functionapp_error = {"code": "-12", "msg": "请求方式错误", "data": {}}
        return HttpResponse(json.dumps(functionapp_error))


# Web功能测试查询
def functionweb(request):
    if request.POST:
        if token(request.POST['token']):
            try:
                if request.POST['startdate'] and request.POST['enddate'] != "":
                    if request.POST['eventid'] != "":
                        startdate = request.POST['startdate']
                        enddate = request.POST['enddate']
                        functionwebdatas = models.automation_function_web.objects.filter(caseid=request.POST['caseid'])
                        functionwebdatalist = []
                        for functionwebdata in range(0, len(functionwebdatas)):
                            if functionwebdatas[functionwebdata].createdtime >= startdate and functionwebdatas[
                                functionwebdata].createdtime <= enddate and request.POST['eventid'] in functionwebdatas[
                                functionwebdata].eventid:
                                functionweb_querydata = {
                                    "id": functionwebdatas[functionwebdata].id,
                                    "caseid": functionwebdatas[functionwebdata].caseid,
                                    "browsername": functionwebdatas[functionwebdata].browsername,
                                    "browserconfigure": functionwebdatas[functionwebdata].browserconfigure,
                                    "browserstatus": functionwebdatas[functionwebdata].browserstatus,
                                    "operatetype": functionwebdatas[functionwebdata].operatetype,
                                    "element": functionwebdatas[functionwebdata].element,
                                    "parameter": functionwebdatas[functionwebdata].parameter,
                                    "waittime": functionwebdatas[functionwebdata].waittime,
                                    "rundescribe": functionwebdatas[functionwebdata].rundescribe,
                                    "casereport": functionwebdatas[functionwebdata].casereport,
                                    "caseexecute": functionwebdatas[functionwebdata].caseexecute,
                                    "runcasetime": functionwebdatas[functionwebdata].runcasetime,
                                    "eventid": functionwebdatas[functionwebdata].eventid,
                                    "createdtime": functionwebdatas[functionwebdata].createdtime,
                                }
                                functionwebdatalist.append(functionweb_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": functionwebdatalist}))
                    else:
                        startdate = request.POST['startdate']
                        enddate = request.POST['enddate']
                        functionwebdatas = models.automation_function_web.objects.filter(caseid=request.POST['caseid'])
                        functionwebdatalist = []
                        for functionwebdata in range(0, len(functionwebdatas)):
                            if functionwebdatas[functionwebdata].createdtime >= startdate and functionwebdatas[
                                functionwebdata].createdtime <= enddate:
                                functionweb_querydata = {
                                    "id": functionwebdatas[functionwebdata].id,
                                    "caseid": functionwebdatas[functionwebdata].caseid,
                                    "browsername": functionwebdatas[functionwebdata].browsername,
                                    "browserconfigure": functionwebdatas[functionwebdata].browserconfigure,
                                    "browserstatus": functionwebdatas[functionwebdata].browserstatus,
                                    "operatetype": functionwebdatas[functionwebdata].operatetype,
                                    "element": functionwebdatas[functionwebdata].element,
                                    "parameter": functionwebdatas[functionwebdata].parameter,
                                    "waittime": functionwebdatas[functionwebdata].waittime,
                                    "rundescribe": functionwebdatas[functionwebdata].rundescribe,
                                    "casereport": functionwebdatas[functionwebdata].casereport,
                                    "caseexecute": functionwebdatas[functionwebdata].caseexecute,
                                    "runcasetime": functionwebdatas[functionwebdata].runcasetime,
                                    "eventid": functionwebdatas[functionwebdata].eventid,
                                    "createdtime": functionwebdatas[functionwebdata].createdtime,
                                }
                                functionwebdatalist.append(functionweb_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": functionwebdatalist}))
                else:
                    if request.POST['eventid'] != "":
                        functionwebdatas = models.automation_function_web.objects.filter(caseid=request.POST['caseid'])
                        functionwebdatalist = []
                        for functionwebdata in range(0, len(functionwebdatas)):
                            if request.POST['eventid'] in functionwebdatas[functionwebdata].eventid:
                                functionweb_querydata = {
                                    "id": functionwebdatas[functionwebdata].id,
                                    "caseid": functionwebdatas[functionwebdata].caseid,
                                    "browsername": functionwebdatas[functionwebdata].browsername,
                                    "browserconfigure": functionwebdatas[functionwebdata].browserconfigure,
                                    "browserstatus": functionwebdatas[functionwebdata].browserstatus,
                                    "operatetype": functionwebdatas[functionwebdata].operatetype,
                                    "element": functionwebdatas[functionwebdata].element,
                                    "parameter": functionwebdatas[functionwebdata].parameter,
                                    "waittime": functionwebdatas[functionwebdata].waittime,
                                    "rundescribe": functionwebdatas[functionwebdata].rundescribe,
                                    "casereport": functionwebdatas[functionwebdata].casereport,
                                    "caseexecute": functionwebdatas[functionwebdata].caseexecute,
                                    "runcasetime": functionwebdatas[functionwebdata].runcasetime,
                                    "eventid": functionwebdatas[functionwebdata].eventid,
                                    "createdtime": functionwebdatas[functionwebdata].createdtime,
                                }
                                functionwebdatalist.append(functionweb_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": functionwebdatalist}))
                    else:
                        functionwebdatas = models.automation_function_web.objects.filter(caseid=request.POST['caseid'])
                        functionwebdatalist = []
                        for functionwebdata in range(0, len(functionwebdatas)):
                            functionweb_querydata = {
                                "id": functionwebdatas[functionwebdata].id,
                                "caseid": functionwebdatas[functionwebdata].caseid,
                                "browsername": functionwebdatas[functionwebdata].browsername,
                                "browserconfigure": functionwebdatas[functionwebdata].browserconfigure,
                                "browserstatus": functionwebdatas[functionwebdata].browserstatus,
                                "operatetype": functionwebdatas[functionwebdata].operatetype,
                                "element": functionwebdatas[functionwebdata].element,
                                "parameter": functionwebdatas[functionwebdata].parameter,
                                "waittime": functionwebdatas[functionwebdata].waittime,
                                "rundescribe": functionwebdatas[functionwebdata].rundescribe,
                                "casereport": functionwebdatas[functionwebdata].casereport,
                                "caseexecute": functionwebdatas[functionwebdata].caseexecute,
                                "runcasetime": functionwebdatas[functionwebdata].runcasetime,
                                "eventid": functionwebdatas[functionwebdata].eventid,
                                "createdtime": functionwebdatas[functionwebdata].createdtime,
                            }
                            functionwebdatalist.append(functionweb_querydata)
                        return HttpResponse(json.dumps({"code": "200", "msg": "succes", "data": functionwebdatalist}))
            except:
                return HttpResponse(json.dumps({"code": "-13", "msg": "查询数据出错，请检查参数。", "data": {}}))
        else:
            functionapp_tokenerror = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(functionapp_tokenerror))
    else:
        functionapp_error = {"code": "-12", "msg": "请求方式错误", "data": {}}
        return HttpResponse(json.dumps(functionapp_error))
