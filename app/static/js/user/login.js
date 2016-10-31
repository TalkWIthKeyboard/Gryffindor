/**
 * Created by CoderSong on 16/10/31.
 */

$(document).ready(function () {

    $('#sureBtn').click(function () {
        var account = $('#account').val() || false;
        var password = $('#password').val() || false;
        if (!account || !password){
            $.toast('账号/密码未输入！', 'forbidden');
        } else{
            $.ajax({
                url:'/user/login',
                type: 'POST',
                data: {
                    'account' : account,
                    'password' : password
                },
                success: function (data) {
                    var message = data.message;
                    if (message == 'success'){
                        window.location.href = '/calendar/getCalendar'
                    } else {
                        $.toast('账号输入有误！', 'forbidden');
                    }
                }
            })
        }
    })

});
