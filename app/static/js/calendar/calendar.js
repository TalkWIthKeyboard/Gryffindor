/**
 * Created by CoderSong on 16/10/21.
 */


$(function () {
    startCalendar();
});

startEventDay = function () {
    var firstObj = $('tbody.event-calendar tr:first td:first');
    var lastObj = $('tbody.event-calendar tr:last td:last');
    var firstDay = getDate(firstObj);
    var lastDay = getDate(lastObj);

    function getDate(obj) {
        var day = obj.attr('date-day');
        var month = parseInt(obj.attr('date-month')) + 1;
        var year = obj.attr('date-year');
        var date = year + '-' + month + '-' + day;
        return date;
    }

    $.showLoading();
    $.showLoading("正在加载数据...");

    $.ajax({
        url:'/calendar',
        type:'POST',
        data:{
            'firstDay': firstDay,
            'lastDay': lastDay
        },
        traditional: true,
        success:function (data) {
            var dict = data.dateDict;
            $('tbody.event-calendar tr td').each(function () {
                var year = $(this).attr('date-year');
                var month = addZero(parseInt($(this).attr('date-month')) + 1);
                var day = addZero($(this).attr('date-day'));

                var dateStr = year + '-' + month + '-' + day;
                if (dict[dateStr] > 0){
                    $(this).addClass('has-event');
                }
            })
            var event = data.event;
            for (var i = 0; i < event.length; i++){
                $('.event-list').append(
                        '<div class="weui_panel"> \
                            <div class="weui_panel_bd"> \
                                <div class="weui_media_box weui_media_small_appmsg event-btn event-hidden" data-id=' + event[i].id + ' data-date=' + event[i].date + '> \
                                    <div class="weui_cells weui_cells_access"> \
                                        <a class="weui_cell" href="javascript:;"> \
                                            <div class="weui_cell_hd"> \
                                                <img class="box-img" src="'+ event[i].img +'"> \
                                            </div> \
                                            <div class="weui_media_bd"> \
                                                <h4 class="weui_media_title">' + event[i].cnname + '</h4> \
                                                <p class="weui_media_desc">观影日期：' + event[i].date + '</p> \
                                                <p class="weui_media_desc">观影地址：' + event[i].address + '</p> \
                                            </div> \
                                        </a> \
                                    </div> \
                                </div> \
                            </div> \
                        </div>'
                )
            }

             $('.event-list').append(
//                     '<div class="panel m-t-sm p-t p-b empty event-hidden" style="margin-top: 0px"> \
//                         <img src="/assets/images/common/empty.png" alt="" class="empty_img"> \
//                         <p class="p-t-sm empty_text">空空如也</p> \
//                     </div>'
                                  '<div  id ="remind_div" class="weui_panel_bd">\
          <a id="remind_btn"  href="javascript:void(0);" class="weui_media_box weui_media_appmsg order">\
              <div  id="remind_pic_div" class=" weui_media_hd order_pic">\
                  <img id="remind_pic" class="weui_media_appmsg_thumb" src="/image/icons/Bitmap.png" alt="">\
              </div>\
             <div id = "remind_text" class="weui_media_bd">\
                  <h4 class="weui_media_title">关于莉莉周的一切(2010)</h4>\
                  <p class="movie_title_e" >All About Lily Chou-Chou</p>\
                  <div style="display:inline">\
                      <div  class="dw_title" >导演:</div>\
                      <div  class="dw_name" >&nbsp&nbsp岩井俊二</div>\
                  </div>\
                  <br>\
                  <div style="display:inline">\
                      <div class="dw_title" >编剧:</div>\
                      <div class="dw_name" >&nbsp&nbsp岩井俊二</div>\
                  </div>\
              </div>\
          </a>\
        </div>\
        <div  id ="record_div" class="weui_panel_bd">\
          <a id="record_btn"  href="javascript:void(0);" class="weui_media_box weui_media_appmsg order">\
              <div  id="record_pic_div" class=" weui_media_hd order_pic">\
                  <img id="record_pic" class="weui_media_appmsg_thumb" src="/image/icons/Bitmap.png" alt="">\
              </div>\
             <div id = "record_text" class="weui_media_bd">\
                  <h4 class="weui_media_title">关于莉莉周的一切(2010)</h4>\
                  <p class="movie_title_e" >All About Lily Chou-Chou</p>\
                  <div style="display:inline">\
                      <div  class="dw_title" >导演:</div>\
                      <div  class="dw_name" >&nbsp&nbsp岩井俊二</div>\
                  </div>\
                  <br>\
                  <div style="display:inline">\
                      <div class="dw_title">编剧:</div>\
                      <div class="dw_name">&nbsp&nbsp岩井俊二</div>\
                  </div>\
              </div>\
          </a>\
        </div>'
             )

            $('.event-btn').click(function () {
                var id = $(this).attr('data-id');
                window.location.href = '/movies/impressions/' + id;
            })

            $.hideLoading();
            startEventHeader();
        }
    })
}

startEventHeader = function () {

    var d = new Date();
    var dayNumber = d.getDate();
    var monthNumber = d.getMonth();
    var yearNumber = d.getFullYear();
    writeByTime(yearNumber,monthNumber,dayNumber);
};

writeByTime = function (year,month,day) {

    var weekName = ['星期日','星期一','星期二','星期三','星期四','星期五','星期六'];
    var date = new Date(year,month,day);
    var realMonth = parseInt(month) + 1;
    $('.dayInfo').text(weekName[date.getDay()] + '  ' + day)

    var num = 0;

    if (!$('.empty').hasClass('event-hidden')){
        $('.empty').addClass('event-hidden');
    }
    $('.event-btn').each(function () {
        if (!$(this).hasClass('event-hidden')){
            $(this).addClass('event-hidden');
        }
        var e_date = $(this).attr('data-date');
        e_date = new Date(e_date);
        if (isEqual(e_date,date)){
            num++;
            $(this).removeClass('event-hidden');
        }
    })

    if (num == 0){
        $('.activeInfo').text("没有记录提醒!");
        $('.empty').removeClass('event-hidden')
    }
    else{
        $('.activeInfo').text("这一天有" + num + "个记录提醒！");
    }


    function isEqual(day1,day2) {
        if (day1.getFullYear() != day2.getFullYear() || day1.getMonth() != day2.getMonth() || day1.getDate() != day2.getDate()) {
            return false;
        }
        return true;
    }
}

function addZero(num) {
    if (parseInt(num) < 10){
        return('0' + num);
    } else{
        return num;
    }
}

startCalendar = function() {
    //获得现在的日期
    var d = new Date();
    var dayNumber = d.getDate();
    var monthNumber = d.getMonth() + 1;
    var yearNumber = d.getFullYear();
    setMonth(yearNumber,monthNumber);

    //左翻按钮事件
    $('.btn-prev').click(function () {
        var monthNumber = $('.month').attr('data-month');
        if (monthNumber < 2){
            $('.month').attr('data-month','13');
            var monthNumber = 13;
            yearNumber = yearNumber - 1;
            setMonth(yearNumber,parseInt(monthNumber) - 1);
        }
        else{
            setMonth(yearNumber,parseInt(monthNumber) - 1);
        }
    });

    //右翻按钮事件
    $('.btn-next').click(function () {
        var monthNumber = $('.month').attr('data-month');
        if (monthNumber > 11){
            $('.month').attr('data-month', '0');
            var monthNumber = 0;
            yearNumber = yearNumber + 1;
            setMonth(yearNumber,parseInt(monthNumber) + 1);
        }
        else {
            setMonth(yearNumber,parseInt(monthNumber) + 1);
        }
    });

    function getWeekWord(monthNumber) {
        var months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'];
        return months[monthNumber - 1];
    }

    //通过月数来填数据
    function setMonth(yearNumber,monthNumber) {
        $('.month').text(yearNumber + '年 ' + getWeekWord(monthNumber));
        $('.month').attr('data-month', monthNumber);
        setDay(monthNumber)
    };

    function setDay(monthNumber) {

        //清空天数栏
        $($('tbody.event-calendar tr')).each(function (index) {
            $(this).empty();
        });

        //清空星期数栏
        $($('thead.event-days tr')).each(function (index) {
            $(this).empty();
        });

        //清空活动栏
        $('.event-list').empty();

        printWeek(monthNumber);
        printDay(monthNumber);
        var date = new Date();
        var month = date.getMonth() + 1;
        var thisyear = new Date().getFullYear();
        setCurrentDay(month,thisyear);
        startEventDay();

        function getAllDays(month,year) {
            var days = getDaysInMonth(month,year);
            var realDays = [];
            //填列表前的空
            var weekNum = days[0].getDay();
            var date = new Date(days[0]);
            date.setDate(days[0].getDate() - weekNum - 1);
            for (var i = 0; i < weekNum; i++){
                date.setDate(date.getDate() + 1);
                realDays.push(new Date(date));
            }
            //填中间内容
            for (var i = 0; i < days.length; i++){
                realDays.push(days[i]);
            }
            //填列表后的空
            var date = new Date(days[days.length - 1]);
            for (var i = days.length - 1; i < 41; i++){
                date.setDate(date.getDate() + 1);
                realDays.push(new Date(date));
            }
            return realDays;
        }

        //准备天的数组
        function getDaysInMonth(month,year) {
            var date = new Date(year,month,1);
            var days = [];
            while (date.getMonth() == month){
                days.push(new Date(date));
                date.setDate(date.getDate() + 1);
            }
            return days;
        }

        //填星期数栏
        function printWeek() {
            $('thead.event-days tr').append('<td>日</td><td>一</td><td>二</td><td>三</td><td>四</td><td>五</td><td>六</td>');
        }

        //填天数栏
        function printDay(monthNumber) {
            var days = getAllDays(monthNumber - 1, yearNumber);
            for (var index = 0 ; index < days.length; index++){
                var each = new Date(days[index]);
                if (index < 7) {
                    $('tbody.event-calendar tr.1').append('<td date-month="' + each.getMonth() + '" date-day="' + each.getDate() + '" date-year="' + each.getFullYear() + '"class="first-line">' + each.getDate() + '</td>');
                } else if (index < 14) {
                    $('tbody.event-calendar tr.2').append('<td date-month="' + each.getMonth() + '" date-day="' + each.getDate() + '" date-year="' + each.getFullYear() + '">' + each.getDate() + '</td>');
                } else if (index < 21) {
                    $('tbody.event-calendar tr.3').append('<td date-month="' + each.getMonth() + '" date-day="' + each.getDate() + '" date-year="' + each.getFullYear() + '">' + each.getDate() + '</td>');
                } else if (index < 28) {
                    $('tbody.event-calendar tr.4').append('<td date-month="' + each.getMonth() + '" date-day="' + each.getDate() + '" date-year="' + each.getFullYear() + '">' + each.getDate() + '</td>');
                } else if (index < 35) {
                    $('tbody.event-calendar tr.5').append('<td date-month="' + each.getMonth() + '" date-day="' + each.getDate() + '" date-year="' + each.getFullYear() + '">' + each.getDate() + '</td>');
                } else if (index < 42){
                    $('tbody.event-calendar tr.6').append('<td date-month="' + each.getMonth() + '" date-day="' + each.getDate() + '" date-year="' + each.getFullYear() + '"class="last-line">' + each.getDate() + '</td>');
                }
            }

            $('tbody.event-calendar tr td').each(function (index) {
                if ($(this).attr('date-month') != monthNumber - 1){
                    $(this).addClass('not-month-day');
                }

                $(this).click(function () {
                    var day = $(this).attr('date-day');
                    var month = $(this).attr('date-month');
                    var year = $(this).attr('date-year');
                    writeByTime(year,month,day);
                })
            })
        }

        //对今天特殊的样式处理
        function setCurrentDay(month, year) {
            var viewMonth = $('.month').attr('data-month');
            if (parseInt(year) === yearNumber) {
                if (parseInt(month) === parseInt(viewMonth)) {
                    $('tbody.event-calendar td[date-day="' + d.getDate() + '"]').addClass('current-day');
                }
            }
        };
    }
};
