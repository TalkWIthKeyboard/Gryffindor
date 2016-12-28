/**
 * Created by CoderSong on 16/10/31.
 */

$(document).ready(function () {

    var url = '/calendar';
    $('#sureBtn').click(function () {
        var account = $('#account').val() || false;
        var password = $('#password').val() || false;
        var next = $('.next-url').html() || false;
        if (!account || !password) {
            $.toast('账号/密码未输入！', 'forbidden');
        } else {
            $.showLoading();
            $.showLoading("正在加载...");
            $.ajax({
                url: '/users/user',
                type: 'POST',
                data: {
                    'account': account,
                    'password': password,
                    'next': next
                },
                success: function (data) {
                    var message = data.message;
                    var img = data.img;
                    if (data.next != '') {
                        url = data.next;
                    }
                    if (message == 'success') {
                        if (img != '') {
                            $('.head-image').attr('src', img);
                        }
                        setTimeout(jumpUrl, 1000);
                        function jumpUrl() {
                            $.hideLoading();
                            window.location.href = url;
                        }
                    } else {
                        $.toast('账号输入有误！', 'forbidden');
                    }
                }
            })
        }
    })

    $('#register').click(function () {
        window.location.href = '／users'
    })

});
