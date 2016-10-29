/**
 * Created by huangrui on 2016/10/22.
 */
$(document).ready(function () {
    $('#time').calendar();
    $('#ftime').calendar();
    getLocation();
});

// 获取地理位置
function getLocation()  {
    var map = new BMap.Map("bdMapBox");
    var nowCity = new BMap.LocalCity();
    nowCity.get(bdGetPosition);
    function bdGetPosition(result){
        var cityName = result.name; //当前的城市名
        $('#where').val(cityName);
    }
}