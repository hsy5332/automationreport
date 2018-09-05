var token = String(Date.parse(new Date()) + 86400).substring(0, 10);
var url = '/automationquery/remoteip';
var send_data = '&token=' + token;
var isshow_list = []; // 定义存放设备数组的列表
axios.defaults.timeout = 2000; // 设置请求超时时间
request_function(url, send_data);

function request_function(request_url, send_data) {
    var requests_value;
    send_data = send_data;
    requests_value = new XMLHttpRequest();
    requests_value.open("POST", request_url, true); // 接口地址
    requests_value.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    requests_value.send(send_data);
    requests_value.onreadystatechange = function () {
        if (requests_value.status == 200 & requests_value.readyState == 4) {
            var requests_datas = requests_value.responseText;
            if (requests_datas.length > 0) {
                try {
                    json_requests_datas = JSON.parse(requests_datas).data
                    displaylist = [];
                    if (json_requests_datas.length > 0) {
                        for (var i = 0; i < json_requests_datas.length; i++) {
                            var ip_address = json_requests_datas[i];
                            displaylist[i] = {
                                'ip_address': ip_address,
                            }
                        }
                        draw(displaylist);

                        function draw(displaylist) {
                            $.each(displaylist, function (i, item) {
                                var html = '<div class="panel panel-default" style="width: 24%; height: 270px; float:left;margin-right:14px;' +
                                    '">';
                                html += "<div class=\"panel-heading\"" + "id='show_devices" + i + "'" + "style=\"font-size: 13px;\">" + item.ip_address + "<div style='margin-top: 8px;'><button onclick=\"get_devices(show_devices" + i + ")\">获取设备</button>" + '&nbsp' + '&nbsp' + "<button onclick=\"upload_case(show_devices" + i + ")\">上传用例</button>" + '&nbsp' + '&nbsp' + "<button onclick=\"run_case(show_devices" + i + ")\">执行用例</button> </div>" + "<div style='margin-top: 3%'>选择测试用例 <select id='case_list'><option value='黄顺耀'>黄顺耀</option></select></div>" + '</div>';
                                html += '</div>';
                                $('#datapaging').append(html);
                            });
                        }
                    }
                } catch (err) {
                    console.log(err)
                }
            }
        }
    }
}

//获取设备ID
function get_devices(element_content) {
    var get_devices_ip = element_content.innerText.replace(/\s/g, "").split('获取设备')[0] //element_content 把整个元素传进来，分割字符串获取ip地址
    var request_formmat_data = new FormData()
    var get_devices_url = 'http://' + get_devices_ip + '/automationserver/devicelist';
    request_formmat_data.append('token', token)
    let config = {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }
    axios.post(get_devices_url, request_formmat_data, config).then(response_data => {
        devices_list = response_data.data.data;
        $(".device_list").remove();
        if (devices_list.length > 0) {
            if (response_data.status == 200 && response_data.request.readyState == 4) {
                draw(devices_list);

                function draw(displaylist) {
                    $.each(displaylist, function (i, item) {
                        var html = '<ol class="device_list" style="margin-left:-25px; margin-top: 8px;">';
                        html += '<li>' + "<input " + "id=\"input_check_box" + i + "\"" + "type=\"checkbox\" name=\"vehicle\" value=" + item + " checked=\"checked\"/>" + '&nbsp' + '&nbsp' + item + '</li>';
                        html = html + '</ol>';
                        isshow_list.push(item)
                        $('#' + element_content.id).append(html);
                    });
                }
            } else {
                show_element('无法连接此主机!')
            }
        } else {
            show_element('未获取到任何移动设备!')
        }
    })
        .catch(res => {
            show_element('无法连接此主机!')
        })
}

// 上传测试用例
function upload_case(element_content) {
    var get_devices_ip = element_content.innerText.replace(/\s/g, "").split('获取设备')[0] //element_content 把整个元素传进来，分割字符串获取ip地址
    // 上传django的测试用例
    show_element("上传测试用例方法")

}

// 执行用例 app web interface
function run_case(element_content) {
    var get_devices_ip = element_content.innerText.replace(/\s/g, "").split('获取设备')[0] //element_content 把整个元素传进来，分割字符串获取ip地址
    // 上传django的测试用例
    var file_name = 'app_function_case.xlsx';
    var runcase_type = 'app';
    var devices_list = document.getElementsByName('vehicle')
    var devices_id_list = new Array();
    if (devices_list.length > 0) {
        for (var i = 0; i < devices_list.length; i++) {
            if (devices_list[i].checked == true) {
                console.log(devices_list[i].value)
                devices_id_list[i] = devices_list[i].value; // 遍历页面input勾选的元素且加入到devices_id_list中
                console.log(devices_id_list[i])
            }
        }
        var request_formmat_data = new FormData()
        var get_devices_url = 'http://' + get_devices_ip + '/automationserver/runcase';
        request_formmat_data.append('token', token);
        request_formmat_data.append('filename', file_name);
        request_formmat_data.append('runcasetype', runcase_type);
        request_formmat_data.append('devicesid', devices_id_list);
        let config = {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }
        axios.post(get_devices_url, request_formmat_data, config).then(response_data => {
            console.log(response_data)

        }).catch(res => {
            show_element('请求接口失败！')
        })
    } else {
        show_element("没有任何可执行的设备!")
    }
}

// 检测数组中是否包含 某一个元素 true 是包含 false是不包含
function check_element_array(element) {
    console.log(element)
    if (isshow_list.length > 0) {
        if (isshow_list.indexOf(element) == 1 || isshow_list.indexOf(element) == 0) {
            return true
        } else {
            return false
        }
    } else {
        return false
    }
}


// 展示弹窗
function show_element(content_data) {
    document.getElementById('pop_up_windows').style.display = "block";
    document.getElementById('pop_up_data').style.display = "block";
    document.getElementById('pop_up_data').innerText = content_data;
}

//关闭弹窗
function show_close() {
    document.getElementById('pop_up_windows').style.display = "none";
    document.getElementById('pop_up_data').style.display = "none";
}

