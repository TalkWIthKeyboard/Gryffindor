/**
 * Created by huangrui on 2016/10/22.
 */
$(document).ready(function () {

    $('#time').calendar();
    $('#ftime').calendar();
    init();
    postMovie();
    var click = 0;
    $('.info').click(function () {
        $('.about').slideToggle();
        $('.record').slideToggle();
        if (0 == click) {
            $(this).css({'background': 'rgba(255,255,255, 0.8)'});
            click = 1;
        } else {
            $(this).css({'background': '#fff'});
            click = 0;
        }
    });
});

// 初始化页面信息
function init() {
    var date = new Date();
    var month = date.getMonth() + 1;
    if (month < 10) {
        month = '0' + month;
    }
    var day = date.getDate();
    if (day < 10) {
        day = '0' + day;
    }
    var dateStr = date.getFullYear() + '-' + month + '-' + day;

    // 这边暂时不提供默认的今天日期
    $('#time').val("请选择日期");
    getLocation();
    $('#where').click(function () {
        getLocation();
    });
}

// 获取地理位置
function getLocation() {

    var geolocation = new BMap.Geolocation();
    geolocation.getCurrentPosition(function (r) {
        if (this.getStatus() == BMAP_STATUS_SUCCESS) {
            var mk = new BMap.Marker(r.point);
            var myGeo = new BMap.Geocoder();
            myGeo.getLocation(new BMap.Point(r.point.lng, r.point.lat),
                function (rs) {
                    var addComp = rs.addressComponents;
                    var data = '';
                    if (addComp.province != addComp.city) {
                        data = addComp.province + addComp.city + addComp.district + addComp.street
                    } else {
                        data = addComp.city + addComp.district + addComp.street
                    }
                    $('#where').val(data);
                });

        } else {
            $.toast('获取地理位置失败！', 'forbidden');
        }
    });
}

//提交表单
function postMovie() {

    $('.foot-btn').click(function () {
        var date = $('#time').val() || false;
        var impression = $('#impression').val() || false;
        var featureDate = $('#ftime').val() || false;


        if (date.isEqual("请选择日期") && featureDate.isEqual("请选择日期")) {
            $.toast('请至少填写一个观影日期！', 'forbidden');
        }
        else {
            if (date.isEqual("请选择日期")) {
                date = '';
            }

            if (featureDate.isEqual("请选择日期")) {
                featureDate = '';
            }

            $.ajax({
                url: '/movies',
                type: 'POST',
                data: {
                    'impression': $('#impression').val(),
                    'date': date,
                    'featureDate': featureDate,
                    'movieId': $(this).attr('data-id'),
                    'address': $('#where').val()
                },
                success: function (data) {
                    if (data.message == 'success') {
                        window.location.href = '/movies';
                    }
                }
            })
        }
    })
}
