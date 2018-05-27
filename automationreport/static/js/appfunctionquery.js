function queryappcase() {
    var token = String(Date.parse(new Date()) + 86400).substring(0, 10);
    var startdate = document.getElementById("starttime").value.replace(/[^0-9]/ig, "");
    var enddate = document.getElementById("endtime").value.replace(/[^0-9]/ig, "");
    var caseid = document.getElementById("caseid").value.replace(/[^0-9]/ig, "");
    var eventid = document.getElementById("eventid").value.replace(/[^0-9]/ig, "");
    if (document.getElementById("caseid").value.replace(/[^0-9]/ig, "") != "") {
        var appcasecount;
        senddata = 'startdate=' + startdate + '&enddate=' + enddate + '&token=' + token + '&caseid=' + caseid + '&eventid=' + eventid
        console.log(senddata)
        appcasecount = new XMLHttpRequest();
        appcasecount.open("POST", "/automationquery/functionapp", true);
        appcasecount.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        appcasecount.send(senddata);
        appcasecount.onreadystatechange = function () {
            if (appcasecount.status == 200 & appcasecount.readyState == 4) {
                if (JSON.parse(appcasecount.responseText).data.length > 0) {
                    console.log(JSON.parse(appcasecount.responseText));
                    console.log(JSON.parse(appcasecount.responseText).data[0]);
                    console.log(JSON.parse(appcasecount.responseText).data.length)
                    var number = JSON.parse(appcasecount.responseText).data[0].id;
                    var caseid = JSON.parse(appcasecount.responseText).data[0].caseid;
                    var devicesinfos = JSON.parse(appcasecount.responseText).data[0].devicesinfos;
                    var devicesexecute = JSON.parse(appcasecount.responseText).data[0].devicesexecute;
                    var runcasetime = JSON.parse(appcasecount.responseText).data[0].runcasetime;
                    var appiumport = JSON.parse(appcasecount.responseText).data[0].appiumport;
                    var caseexecute = JSON.parse(appcasecount.responseText).data[0].caseexecute;
                    var casereport = JSON.parse(appcasecount.responseText).data[0].casereport;
                    var eventid = JSON.parse(appcasecount.responseText).data[0].eventid;
                    var createdtime = JSON.parse(appcasecount.responseText).data[0].createdtime;
                    var lablelist = document.getElementById('datapaging').innerHTML = '<td>' + number + '</td>' + '<td>' + caseid + '</td>' + '<td>' + devicesinfos + '</td>' + '<td>' + devicesexecute + '</td>' + '<td>' + runcasetime + '</td>' + '<td>' + appiumport + '</td>' + '<td>' + caseexecute + '</td>' + '<td>' + casereport + '</td>' + '<td>' + eventid + '</td>' + '<td>' + createdtime + '</td>';
                }
            }
            else {
                console.log("黄顺耀");
            }
        }
    }
    else {
        window.alert("请输入正确的用例编号！")
    }

}
