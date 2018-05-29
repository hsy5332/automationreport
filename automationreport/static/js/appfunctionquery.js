// 查询数据
function queryappcase(source) {
    var token = String(Date.parse(new Date()) + 86400).substring(0, 10);
    var startdate = document.getElementById("starttime").value.replace(/[^0-9]/ig, "");
    if (startdate.length > 6) {
        startdate = startdate.substring(0, 4) + '-' + startdate.substring(4, 6) + '-' + startdate.substring(6, 8) + ' 00:00:00';
    }
    var enddate = document.getElementById("endtime").value.replace(/[^0-9]/ig, "");
    if (enddate.length > 6) {
        enddate = enddate.substring(0, 4) + '-' + enddate.substring(4, 6) + '-' + enddate.substring(6, 8) + ' 23:59:59';
    }
    var caseid = document.getElementById("caseid").value.replace(/[^0-9]/ig, "");
    var eventid = document.getElementById("eventid").value.replace(/[^0-9]/ig, "");
    if (document.getElementById("caseid").value.replace(/[^0-9]/ig, "") != "") {
        var appcasecount;
        senddata = 'startdate=' + startdate + '&enddate=' + enddate + '&token=' + token + '&caseid=' + caseid + '&eventid=' + eventid
        appcasecount = new XMLHttpRequest();
        appcasecount.open("POST", "/automationquery/functionapp", true);
        appcasecount.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        appcasecount.send(senddata);
        appcasecount.onreadystatechange = function () {
            if (appcasecount.status == 200 & appcasecount.readyState == 4) {
                requestdatalength = JSON.parse(appcasecount.responseText).data.length; // 获取接口返回的数据长度
                if (requestdatalength > 0) {
                    if (document.getElementsByClassName('listdata').length > 0) {
                        $('.listdata').remove();
                    }
                    var traversedata = []; //新增一个数组，把接口数据存入
                    var displaylist = [];
                    displaynumber = document.getElementById('jumpWhere').value;
                    if (displaynumber > requestdatalength) {
                        displaynumber = requestdatalength;
                    }
                    for (var i = 0; i <= requestdatalength - 1; i++) {
                        var number = JSON.parse(appcasecount.responseText).data[i].id;
                        var caseid = JSON.parse(appcasecount.responseText).data[i].caseid;
                        var devicesinfos = JSON.parse(appcasecount.responseText).data[i].devicesinfos;
                        var devicesexecute = JSON.parse(appcasecount.responseText).data[i].devicesexecute;
                        var runcasetime = JSON.parse(appcasecount.responseText).data[i].runcasetime;
                        var appiumport = JSON.parse(appcasecount.responseText).data[i].appiumport;
                        var caseexecute = JSON.parse(appcasecount.responseText).data[i].caseexecute;
                        var casereport = JSON.parse(appcasecount.responseText).data[i].casereport;
                        var eventid = JSON.parse(appcasecount.responseText).data[i].eventid;
                        var createdtime = JSON.parse(appcasecount.responseText).data[i].createdtime;
                        traversedata[i] = {
                            'data': {
                                'id': number,
                                'caseid': caseid,
                                'devicesinfos': devicesinfos,
                                'devicesexecute': devicesexecute,
                                'runcasetime': runcasetime,
                                'appiumport': appiumport,
                                'caseexecute': caseexecute,
                                'casereport': casereport,
                                'eventid': eventid,
                                'createdtime': createdtime
                            }
                        }
                    }
                    if (source.id == "lastPage") {
                        if (requestdatalength > displaynumber) {


                        }
                    }
                    else {
                        for (var y = 0; y < displaynumber; y++) {
                            displaylist[y] = traversedata[y]; // 把数据放入新的数组，在HTML中创建数据
                        }
                    }
                    // 判断当前选择 每页展示的数据
                    draw(displaylist);

                    function draw(displaylist) {
                        $.each(displaylist, function (i, item) {
                            var html = '<tr class="listdata">';
                            html += '<td style="font-size: 11px;text-align: center;">' + item.data.id + '</td>';
                            html += '<td style="font-size: 11px;text-align: center;">' + item.data.caseid + '</td>';
                            html += '<td style="font-size: 11px;text-align: center;">' + item.data.devicesinfos + '</td>';
                            html += '<td style="font-size: 11px;text-align: center;">' + item.data.devicesexecute + '</td>';
                            html += '<td style="font-size: 11px;text-align: center;">' + item.data.runcasetime + 's' + '</td>';
                            html += '<td style="font-size: 11px;text-align: center;">' + item.data.appiumport + '</td>';
                            html += '<td style="font-size: 11px;text-align: center;">' + item.data.caseexecute + '</td>';
                            html += '<td style="font-size: 11px;text-align: center;">' + item.data.casereport + '</td>';
                            html += '<td style="font-size: 11px;text-align: center;">' + item.data.eventid + '</td>';
                            html += '<td style="font-size: 11px;text-align: center;">' + item.data.createdtime + '</td>';
                            html += '</tr>';
                            $('#datapaging').append(html);
                        });
                    }
                } else {
                    window.alert("没有获取到任何数据");
                }
            }
        }
    }
    else {
        if (document.getElementsByClassName('listdata').length > 0) {
            $('.listdata').remove();
        }
        else {
            if (source.id == "buttonquery") {
                window.alert("请输入用例编号！")
            }
        }
    }

}

// 获取当前 数据选中的行数
function jumpWhereChange() {
    var displaynumber = document.getElementById('jumpWhere').options[jumpWhere.selectedIndex].value;
    queryappcase('jumpWhere');
}

