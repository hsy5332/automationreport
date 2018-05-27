function queryappcase() {
    var token = String(Date.parse(new Date()) + 86400).substring(0, 10);
    var startdate = document.getElementById("starttime").value.replace(/[^0-9]/ig, "");
    var enddate = document.getElementById("endtime").value.replace(/[^0-9]/ig, "");
    var caseid = document.getElementById("caseid").value.replace(/[^0-9]/ig, "");
    var eventid = document.getElementById("eventid").value.replace(/[^0-9]/ig, "");
    if (document.getElementById("caseid").value.replace(/[^0-9]/ig, "") !=""){
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
