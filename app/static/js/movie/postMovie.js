/**
 * Created by huangrui on 2016/10/22.
 */
$(document).ready(function () {

    $('#time').calendar();
    $('#ftime').calendar();
    init();
    postMovie();
});

// 初始化页面信息
function init() {
    var date = new Date();
    var month = date.getMonth() + 1;
    if (month < 10){
        month = '0' + month;
    }
    var day = date.getDate();
    if (day < 10){
        day = '0' + day;
    }
    var dateStr = date.getFullYear() + '-' + month + '-' + day;
    $('#time').val(dateStr);

    getLocation()
}

// 获取地理位置
function getLocation() {

    var map = new BMap.Map("bdMapBox");
    var nowCity = new BMap.LocalCity();
    nowCity.get(bdGetPosition);
    function bdGetPosition(result){
        var cityName = result.name; //当前的城市名
        $('#where').val(cityName);
    }
}

//提交表单
function postMovie() {

    $('.foot-btn').click(function () {
        $.ajax({
            url: '/postMovieInfo',
            type: 'POST',
            data: {
                'impression': $('#impression').val(),
                'date': $('#time').val(),
                'featureDate': $('#ftime').val(),
                'movieId': $(this).attr('data-id'),
                'address': $('#where').val()
            },
            success: function (data) {
                window.location.href = '/';
            }
        })
    })
}