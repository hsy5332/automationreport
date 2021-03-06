# -*- coding: UTF-8 -*-
from django.db import models


# 用户信息表
class automation_user(models.Model):
    username = models.CharField(max_length=40);
    password = models.CharField(max_length=40);
    nickname = models.CharField(max_length=40);
    userstatus = models.CharField(max_length=4);
    createdtime = models.DateTimeField(default='auto_now_add');
    updatetime = models.DateTimeField(default='auto_now');


# Cpu数据表
class automation_cpu_app(models.Model):
    cpuproportion = models.CharField(max_length=100);
    starttime = models.CharField(max_length=20);
    endtime = models.CharField(max_length=20);
    monkeyscript = models.CharField(max_length=200);
    functionscript = models.CharField(max_length=4);
    runtime = models.CharField(max_length=50);
    createdtime = models.DateTimeField(default='auto_now_add');
    updatetime = models.DateTimeField(default='auto_now');
    caseid = models.CharField(max_length=10);
    eventid = models.CharField(max_length=100);


# APP启动数据
class automation_launch_app(models.Model):
    starttime = models.CharField(max_length=50);
    launchtime = models.CharField(max_length=50);
    endtime = models.CharField(max_length=50);
    launchtype = models.CharField(max_length=10);
    createdtime = models.DateTimeField(default='auto_now_add');
    updatetime = models.DateTimeField(default='auto_now');
    caseid = models.CharField(max_length=10);
    eventid = models.CharField(max_length=100);


# APP内存使用数据
class automation_mem_app(models.Model):
    memorysize = models.CharField(max_length=50);
    starttime = models.CharField(max_length=50);
    endtime = models.CharField(max_length=50);
    monkeyscript = models.CharField(max_length=200);
    functionscript = models.CharField(max_length=200);
    runtime = models.CharField(max_length=50);
    createdtime = models.DateTimeField(default='auto_now_add');
    updatetime = models.DateTimeField(default='auto_now');
    caseid = models.CharField(max_length=50);
    eventid = models.CharField(max_length=50);


# 接口数据
class automation_interface(models.Model):
    interfaceurl = models.CharField(max_length=200);
    requestparameter = models.CharField(max_length=200);
    returnparameter = models.CharField(max_length=200);
    requesttype = models.CharField(max_length=10);
    casestatus = models.CharField(max_length=4);
    caseid = models.CharField(max_length=10);
    remark = models.CharField(max_length=200);
    eventid = models.CharField(max_length=50);
    createdtime = models.DateTimeField(default='auto_now_add');
    updatetime = models.DateTimeField(default='auto_now');


# 自动化APP功能测试结果
class automation_function_web(models.Model):
    browsername = models.CharField(max_length=200);
    browserconfigure = models.CharField(max_length=10);
    browserstatus = models.CharField(max_length=5);
    operatetype = models.CharField(max_length=50);
    element = models.CharField(max_length=200);
    parameter = models.CharField(max_length=50);
    waittime = models.CharField(max_length=50);
    rundescribe = models.CharField(max_length=300);
    caseexecute = models.CharField(max_length=5);
    runcasetime = models.CharField(max_length=100);
    caseid = models.CharField(max_length=100);
    eventid = models.CharField(max_length=100);
    casereport = models.CharField(max_length=100);
    createdtime = models.DateTimeField(default='auto_now_add');
    updatetime = models.DateTimeField(default='auto_now');


# 自动化web功能测试结果
class automation_function_app(models.Model):
    devicesinfos = models.CharField(max_length=200);
    appiumport = models.CharField(max_length=10);
    devicesexecute = models.CharField(max_length=5);
    operatetype = models.CharField(max_length=50);
    element = models.CharField(max_length=200);
    parameter = models.CharField(max_length=50);
    waittime = models.CharField(max_length=50);
    rundescribe = models.CharField(max_length=300);
    caseexecute = models.CharField(max_length=5);
    runcasetime = models.CharField(max_length=50);
    caseid = models.CharField(max_length=100);
    eventid = models.CharField(max_length=100);
    casereport = models.CharField(max_length=100);
    createdtime = models.DateTimeField(default='auto_now_add');
    updatetime = models.DateTimeField(default='auto_now');


# 远程服务端IP配置
class automation_remote_ip(models.Model):
    ipaddress = models.CharField(max_length=20);
    status = models.CharField(max_length=4);
    createdtime = models.DateTimeField(default='auto_now_add');


# 执行monkey数据存取记录
class automation_monkey_app(models.Model):
    monkeyscript = models.CharField(max_length=255);
    status = models.CharField(max_length=4);
    createdtime = models.DateTimeField(default='auto_now_add');
