function automationlogin() {
    var usernmae = String(document.getElementById("username").value);
    var password = String(document.getElementById("password").value);
    var token = String(Date.parse(new Date()) + 86400).substring(0, 10)
    var requestlogin;
    var requestdata = 'username=' + usernmae + '&password=' + password + '&token=' + token
    requestlogin = new XMLHttpRequest();
    requestlogin.open("POST", "/automationquery/login", true);
    requestlogin.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    requestlogin.send(requestdata);
    requestlogin.onreadystatechange = function () {
        if (requestlogin.readyState == 4 && requestlogin.status == 200) {
            loginresponsejson = JSON.parse(requestlogin.responseText);
            if (loginresponsejson != "") {
                if (loginresponsejson.code == '200') {
                    document.getElementById("request_tooltip").innerText = "登录成功";
                }
                else if (loginresponsejson.code == '100') {
                    document.getElementById("request_tooltip").innerText = "该用户账号已经被禁用，请联系管理员。";
                }
                else if (loginresponsejson.code == '102') {
                    document.getElementById("request_tooltip").innerText = "账号或密码错误";
                }
                else if (loginresponsejson.code == '-11') {
                    document.getElementById("request_tooltip").innerText = "token过期";
                }
                else {
                    document.getElementById("request_tooltip").innerText = "登录失败";
                }
            }
        }
        else {
        }
    }
}