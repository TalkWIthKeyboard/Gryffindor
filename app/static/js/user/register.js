/**
 * Created by CoderSong on 16/10/31.
 */

$(document).ready(function () {

    $('#sureBtn').click(function () {
        var account = $('#account').val() || false;
        var password = $('#password').val() || false;
        var repassword = $('#repassword').val() || false;
        var username = $('#username').val() || false;
        if (!account || !password || !repassword || !username){
            $.toast('请将账户信息输入完整！', 'forbidden');
        } else {
            $.ajax({
                url:'/user/register',
                type: 'POST',
                data: {
                    'account' : account,
                    'password': password,
                    'repassword' : repassword,
                    'username': username
                },
                success: function (data) {
                    var message = data.message;
                    if (message == 'success'){
                        window.location.href = '/calendar/getCalendar'
                    } else if (message == 'repeat'){
                        $.toast('账号已存在！', 'forbidden');
                    } else {
                        $.toast('出现异常！', 'forbidden');
                    }
                }
            })
        }
    })
    
    $('#exitBtn').click(function () {
        window.location.href = '/user/login';
    })

});