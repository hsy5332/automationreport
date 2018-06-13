currentpage = 1; //当前显示在第几页
// 查询数据
function queryappcase(source) {
    if (source.id == "jumpWhere" || source.id == "buttonquery" || source.id == "firstPage") {
        currentpage = 1;
    }
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
        appcasecount.open("POST", "/automationquery/cpu", true); // 接口地址
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
                    //totalCount 总页数
                    if (requestdatalength % displaynumber > 0) {
                        totalCount = Math.ceil(requestdatalength / displaynumber); //小数上进一位
                    }
                    else {
                        totalCount = requestdatalength / displaynumber;
                    }
                    document.getElementById('totalcounts').innerHTML = ' 共 ' + totalCount + ' 页';//页面显示共多少页
                    for (var i = 0; i <= requestdatalength - 1; i++) {
                        var number = JSON.parse(appcasecount.responseText).data[i].id;
                        var caseid = JSON.parse(appcasecount.responseText).data[i].caseid;
                        var cpuproportion = JSON.parse(appcasecount.responseText).data[i].cpuproportion;
                        var functionscript = JSON.parse(appcasecount.responseText).data[i].functionscript;
                        var runtime = JSON.parse(appcasecount.responseText).data[i].runtime;
                        var eventid = JSON.parse(appcasecount.responseText).data[i].eventid;
                        var createdtime = JSON.parse(appcasecount.responseText).data[i].createdtime;
                        traversedata[i] = {
                            'data': {
                                'id': number,
                                'caseid': caseid,
                                'cpuproportion': cpuproportion,
                                'functionscript' : functionscript,
                                'runtime': runtime,
                                'eventid': eventid,
                                'createdtime': createdtime
                            }
                        }

                    }
                    // 判断当前选择 每页展示的数据
                    if (source.id == "lastPage") {
                        if (requestdatalength > displaynumber) {
                            if (requestdatalength % displaynumber > 0) {
                                pagecounts = Math.ceil(requestdatalength / displaynumber); //小数上进一位
                            }
                            else {
                                pagecounts = requestdatalength / displaynumber;
                            }
                            currentpage = pagecounts;//当前在最后一页则是最后一页
                            // 判断获取的数据，是否刚好等于页数整数的倍数
                            displaylist = [];
                            lastdata = requestdatalength - ((pagecounts - 1) * displaynumber); //最后一页要显示的数据数目
                            for (var lastdatacount = 0; lastdatacount < lastdata; lastdatacount++) {
                                displaylist[lastdatacount] = traversedata[Math.floor(requestdatalength / displaynumber) * displaynumber + lastdatacount]; //取出最后一页未显示的数据
                            }
                            draw(displaylist);

                            function draw(displaylist) {
                                $.each(displaylist, function (i, item) {
                                    var html = '<tr class="listdata">';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.id + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.caseid + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.cpuproportion + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.functionscript + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.runtime + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.eventid + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.createdtime + '</td>';
                                    html += '</tr>';
                                    $('#datapaging').append(html);
                                });
                            }
                        }
                        else {
                            window.alert("最后一页没有数据了,自动跳转到首页");
                            queryappcase(firstPage)
                        }
                    }
                    else if (source.id == "nextPage") {
                        console.log(currentpage)
                        displaylist = []; // 先清空整个数组
                        if (currentpage < totalCount) {
                            startnextpagelen = currentpage * displaynumber;
                            endnextpagelen = ((currentpage + 1) * displaynumber);
                            contrastcount = endnextpagelen - startnextpagelen;
                            for (var nextcount = 0; nextcount < contrastcount; nextcount++) {
                                if (startnextpagelen < traversedata.length) {
                                    displaylist[nextcount] = traversedata[startnextpagelen]; // 把数据放入新的数组，在HTML中创建数据
                                    startnextpagelen = startnextpagelen + 1;
                                }
                            }
                            draw(displaylist);

                            function draw(displaylist) {
                                $.each(displaylist, function (i, item) {
                                    var html = '<tr class="listdata">';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.id + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.caseid + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.cpuproportion + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.functionscript + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.runtime + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.eventid + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.createdtime + '</td>';
                                    html += '</tr>';
                                    $('#datapaging').append(html);
                                });
                            }

                            currentpage = currentpage + 1;
                        }
                        else {
                            window.alert("这已经是最后一页了,自动跳转到首页");
                            currentpage = 1;
                            queryappcase(firstPage)
                        }
                    }
                    else if (source.id == "prePage") {
                        if (currentpage > 1) {
                            startnextpagelen = (currentpage - 2) * displaynumber;
                            endnextpagelen = (currentpage - 1) * displaynumber;

                            contrastcount = endnextpagelen - startnextpagelen; //上一页要显示的数据数量
                            for (var nextcount = 0; nextcount < contrastcount; nextcount++) {
                                displaylist[nextcount] = traversedata[startnextpagelen]; // 把数据放入新的数组，在HTML中创建数据
                                startnextpagelen = startnextpagelen + 1;
                            }
                            draw(displaylist);

                            function draw(displaylist) {
                                $.each(displaylist, function (i, item) {
                                    var html = '<tr class="listdata">';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.id + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.caseid + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.cpuproportion + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.functionscript + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.runtime + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.eventid + '</td>';
                                    html += '<td style="font-size: 11px;text-align: center;">' + item.data.createdtime + '</td>';
                                    html += '</tr>';
                                    $('#datapaging').append(html);
                                });
                            }

                            currentpage = currentpage - 1;

                        } else {
                            currentpage = 1;
                            queryappcase(firstPage)
                        }

                    }
                    else {
                        displaylist = []; // 先清空整个数组
                        for (var y = 0; y < displaynumber; y++) {
                            displaylist[y] = traversedata[y]; // 把数据放入新的数组，在HTML中创建数据
                        }
                        draw(displaylist);

                        function draw(displaylist) {
                            $.each(displaylist, function (i, item) {
                                var html = '<tr class="listdata">';
                                html += '<td style="font-size: 11px;text-align: center;">' + item.data.id + '</td>';
                                html += '<td style="font-size: 11px;text-align: center;">' + item.data.caseid + '</td>';
                                html += '<td style="font-size: 11px;text-align: center;">' + item.data.cpuproportion + '</td>';
                                html += '<td style="font-size: 11px;text-align: center;">' + item.data.functionscript + '</td>';
                                html += '<td style="font-size: 11px;text-align: center;">' + item.data.runtime + '</td>';
                                html += '<td style="font-size: 11px;text-align: center;">' + item.data.eventid + '</td>';
                                html += '<td style="font-size: 11px;text-align: center;">' + item.data.createdtime + '</td>';
                                html += '</tr>';
                                $('#datapaging').append(html);
                            });
                        }
                    }
                } else {
                    window.alert("没有获取到任何数据");
                }
                console.log(currentpage)
                document.getElementById('currentpage').innerHTML = '，第 ' + currentpage + ' 页';//页面显示当前页面
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

