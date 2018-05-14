
function automationlogin() {
    var usernmae = document.getElementById("username");
    var password = document.getElementById("password");
    console.log(usernmae)
    if (usernmae.value == "123") {
        alert("请输入用户名");
        return false;
    }
}