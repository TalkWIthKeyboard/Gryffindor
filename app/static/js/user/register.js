/**
 * Created by CoderSong on 16/10/31.
 */

$(document).ready(function () {

    $('#sureBtn').click(function () {
        var account = $('#account').val() || false;
        var password = $('#password').val() || false;
        var repassword = $('#repassword').val() || false;
        var username = $('#username').val() || false;
        var img = $('.image-input')[0].files[0];

        if (!account || !password || !repassword || !username){
            $.toast('请将账户信息输入完整！', 'forbidden');
        } else {
            var fd = new FormData();
            fd.append('file', img);
            fd.append('account',account);
            fd.append('password',password);
            fd.append('repassword',repassword);
            fd.append('username',username);
            $.ajax({
                url:'/user/register',
                type: 'POST',
                data: fd,
                processData: false,
                contentType: false,
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
    });
    
    $('#exitBtn').click(function () {
        window.location.href = '/user/login';
    });

    $(".head-image").click(function () {
        $(".image-input").click();
    });

    $('.image-input').on('change', function ajaxUploadNewAvatar() {
        var file = this.files[0];
        var reader = new FileReader();
        reader.onloadend = function (e) {
            $(".head-image").attr('src', e.target.result);
        };
        reader.readAsDataURL(file);
    });
});