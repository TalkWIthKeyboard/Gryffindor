/**
 * Created by CoderSong on 16/10/31.
 */

$(document).ready(function () {

    $('#sureBtn').click(function () {
        var account = $('#account').val() || false;
        var password = $('#password').val() || false;
        var next = $('.next-url').html() || false;
        if (!account || !password){
            $.toast('账号/密码未输入！', 'forbidden');
        } else{
            $.ajax({
                url:'/user/login',
                type: 'POST',
                data: {
                    'account' : account,
                    'password' : password,
                    'next': next
                },
                success: function (data) {
                    var message = data.message;
                    var url = '/calendar/getCalendar';
                    if (data.next != ''){
                        url = data.next;
                    }
                    if (message == 'success'){
                        window.location.href = url
                    } else {
                        $.toast('账号输入有误！', 'forbidden');
                    }
                }
            })
        }
    })

});
