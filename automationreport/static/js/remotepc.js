var token = String(Date.parse(new Date()) + 86400).substring(0, 10);
var url = '/automationquery/remoteip';
var send_data = '&token=' + token;
var isshow_list = []; // 定义存放设备数组的列表
axios.defaults.timeout = 2000; // 设置请求超时时间
let config = {
    headers: {
        'Content-Type': 'multipart/form-data'
    }
}
request_function(url, send_data);
get_inferface_case();

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
                                html += "<div class=\"panel-heading\"" + "id='show_devices" + i + "'" + "style=\"font-size: 13px;\">" + item.ip_address + "<div style='margin-top: 8px;'>" + "<input style='display: inline; width: 180px; margin-bottom: 8px;' id='app_case_file" + i + "'" + "type=\"file\" name=\"casefile\"/><input type=\"submit\" value=\"上传用用例\" style='border-radius: 20px;' onclick=\"upload_case_file('app',show_devices" + i + ")\"></input>" + "<button style='border-radius: 20px;' onclick=\"get_devices(show_devices" + i + ")\">获取设备</button>" + '&nbsp' + '&nbsp' + "<button style='border-radius: 20px;' onclick=\"run_case('app',show_devices" + i + ")\">执行用例</button> </div>" + "<div style='margin-top: 3%;'>选择用例 " + "<select id='case_list" + i + "'" + " style='width: 154px;'><option value='默认'>默认</option></select></div>" + '</div>';
                                html += '</div>';
                                $('#datapaging').append(html);
                                get_run_case(item.ip_address, 'app', i);//获取测试用例
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
    var request_formmat_data = new FormData();
    var get_run_url = 'http://' + get_devices_ip + '/automationserver/devicelist';
    request_formmat_data.append('token', token)
    let config = {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }
    axios.post(get_run_url, request_formmat_data, config).then(response_data => {
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
function upload_case_file(casetype, element_content) {
    var request_formmat_data = new FormData()
    if (casetype == 'app') {
        var get_computer_ip = 'http://' + element_content.innerText.replace(/\s/g, "").split('获取设备')[0] + '/automationserver/uploadcase' //element_content 把整个元素传进来，分割字符串获取ip地址
        var case_file_id = 'app_case_file' + element_content.id.split('show_devices')[1] //获取选择文件框中的file id
        var case_file = document.getElementById(case_file_id).files // 获取上传的测试用例文件
        request_formmat_data.append('casefile', case_file[0]);
        request_formmat_data.append('token', token);
    } else {
        var get_computer_ip = 'http://127.0.0.1:8988/automationserver/uploadcase'
        var case_file = element_content.files //获取上传的测试用例文件
        request_formmat_data.append('casefile', case_file[0]);
        request_formmat_data.append('token', token);
    }
    if (case_file.length > 0) {
        // 上传django的测试用例
        axios.post(get_computer_ip, request_formmat_data, config).then(response_data => {
            if (response_data.data.code == '200') {
                show_element(response_data.data.msg);
                if (casetype == 'app') { //上传完用例后需要再次获取新的用例列表
                    get_run_case(element_content.innerText.replace(/\s/g, "").split('获取设备')[0], 'app', element_content.id.split('show_devices')[1])
                } else {
                    get_inferface_case()
                }
            } else {
                show_element(response_data.data.msg)
            }
        }).catch(res => {
        })
    } else {
        show_element('请上传测试用例')
    }
}

// 执行用例 app web interface
function run_case(casetype, element_content) {
    var runcase_type = casetype;
    var request_formmat_data = new FormData()
    if (casetype == 'app') {
        var devices_id_list = new Array();
        var get_devices_ip = element_content.innerText.replace(/\s/g, "").split('获取设备')[0] //element_content 把整个元素传进来，分割字符串获取ip地址
        var get_run_url = 'http://' + get_devices_ip + '/automationserver/runcase';
        var file_name = document.getElementById('case_list' + element_content.id.split('show_devices')[1]).value;
        var devices_list = document.getElementsByName('vehicle')
        if (devices_list.length > 0) {
            for (var i = 0; i < devices_list.length; i++) {
                if (devices_list[i].checked == true) {
                    devices_id_list[i] = devices_list[i].value; // 遍历页面input勾选的元素且加入到devices_id_list中
                }
            }
            request_formmat_data.append('token', token);
            request_formmat_data.append('filename', file_name);
            request_formmat_data.append('runcasetype', runcase_type);
            request_formmat_data.append('devicesid', devices_id_list);
            axios.post(get_run_url, request_formmat_data, config).then(response_data => {
                if (response_data.data.code != '200') {
                    show_element(response_data.data.msg)
                }

            }).catch(res => {
                show_element('请求接口失败！')
            })
        } else {
            show_element("没有任何可执行的设备!")
        }
    } else {
        var get_run_url = 'http://127.0.0.1:8988/automationserver/runcase';
        request_formmat_data.append('token', token);
        request_formmat_data.append('runcasetype', runcase_type);
        if (casetype == 'interface') {
            var file_name = document.getElementById('interface_case_option').value;
        } else {
            var file_name = document.getElementById('web_case_option').value; //web
        }
        request_formmat_data.append('filename', file_name);
        axios.post(get_run_url, request_formmat_data, config).then(response_data => {
            if (response_data.data.code != '200') {
                show_element(response_data.data.msg)
            }

        }).catch(res => {
            show_element('请求接口失败！')
        })
    }

}

// 检测数组中是否包含 某一个元素 true 是包含 false是不包含
function check_element_array(element) {
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

//获取测试用例
function get_run_case(connect_ip, casetype, number) {
    if (casetype == 'app') {
        var get_run_url = 'http://' + connect_ip + '/automationserver/getcasefile';
    } else {
        var get_run_url = connect_ip;
    }
    var request_formmat_data = new FormData()
    request_formmat_data.append('token', token);
    request_formmat_data.append('casetype', casetype);
    axios.post(get_run_url, request_formmat_data, config).then(response_data => {
        case_file_list = response_data.data.data
        if (case_file_list.length > 0) {
            if (casetype == 'app') {
                $(".appcasefilelist").remove();
                draw(case_file_list);

                function draw(displaylist) {
                    $.each(displaylist, function (i, item) {
                        var html = '<option class="appcasefilelist" value="' + item + '">';
                        html = html + item;
                        html = html + '</option>';
                        $('#case_list' + number).append(html);
                    });
                }
            } else if (casetype == 'interface') {
                $(".interfacecasefilelist").remove();
                draw(case_file_list);

                function draw(displaylist) {
                    $.each(displaylist, function (i, item) {
                        var html = '<option class="interfacecasefilelist" value="' + item + '">';
                        html = html + item;
                        html = html + '</option>';
                        $('#interface_case_option').append(html);
                    });
                }
            } else if (casetype == 'web') {
                $(".webcasefilelist").remove();
                draw(case_file_list);

                function draw(displaylist) {
                    $.each(displaylist, function (i, item) {
                        var html = '<option class="webcasefilelist" value="' + item + '">';
                        html = html + item;
                        html = html + '</option>';
                        $('#web_case_option').append(html);
                    });
                }
            }
        }
    }).catch(res => {
    })
}

// 获取接口自动化用例
function get_inferface_case() {
    var get_run_url = 'http://127.0.0.1:8988/automationserver/getcasefile';
    get_run_case(get_run_url, 'interface', '0');
    get_run_case(get_run_url, 'web', '0');
}