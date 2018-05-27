var token = String(Date.parse(new Date()) + 86400).substring(0, 10)
var requestdata = 'token=' + token;
requestfunctiondatas = new XMLHttpRequest();
requestfunctiondatas.open("POST", "/automationquery/functioncount", true);
requestfunctiondatas.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
requestfunctiondatas.send(requestdata);
requestfunctiondatas.onreadystatechange = function() {
    if (requestfunctiondatas.readyState == 4 && requestfunctiondatas.status == 200){
        functiondatasjson = JSON.parse(requestfunctiondatas.responseText);
        document.getElementById("function-case-count").innerHTML = functiondatasjson.data.casecount;
    }
    else{
        document.getElementById("function-case-count").innerHTML = "0";
    }
}

appcasedata = new XMLHttpRequest();
appcasedata.open("POST", "/automationquery/appfunctioncount", true);
appcasedata.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
appcasedata.send(requestdata);
appcasedata.onreadystatechange =  function () {
    if (appcasedata.status ==200 && appcasedata.readyState == 4) {
        appcasedatajson = JSON.parse(appcasedata.responseText);
        document.getElementById("app-case-count").innerHTML = appcasedatajson.data.casecount;
    }
    else{
        document.getElementById("app-case-count").innerHTML = "0";
    }
}

webcasedata = new  XMLHttpRequest();
webcasedata.open("POST", "/automationquery/webfunctioncount", true);
webcasedata.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
webcasedata.send(requestdata);
webcasedata.onreadystatechange = function () {
    if (webcasedata.status == 200 && webcasedata.readyState == 4){
        webcasedatajson = JSON.parse(webcasedata.responseText);
        document.getElementById("web-case-count").innerHTML = webcasedatajson.data.casecount;
    }
    else{
        document.getElementById("web-case-count").innerHTML = "0";
    }
}