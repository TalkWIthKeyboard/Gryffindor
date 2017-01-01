/**
 * Created by CoderSong on 17/1/1.
 */
$(document).ready(function () {
    var loading = false;
    listenInfinite();

    // 监听滚动事件
    function listenInfinite() {
        $(document.body).infinite().on("infinite", function () {
            if (loading) return;
            loading = true;
            setTimeout(function () {
                searchEvent();
                loading = false;
            }, 1000);   //模拟延迟
        });
    }

    $('.friend-movie-btn').click(function () {
        var myId = $(this).attr('data-userid');
        var movieId = $(this).attr('data-movieid');
        var url = '/movies/friends/' + myId + '/impressions/' + movieId;
        window.location.href = url;
    })
});

function searchEvent() {
    var num = $('.search-out').attr('data-id');
    num = parseInt(num);

    if (num == 2) {
        startInfinite();
    }

    $.ajax({
        url: '/timeline/more/' + num,
        type: 'GET',
        success: function (data) {
            var list = data.list;
            $('.search-out').attr('data-id', num + 1);
            if (list.length != 0) {
                for (var index in list) {
                    var info = list[index];
                    // 添加头像的样式
                    var appendStr =
                        '<li> \
                            <div class="po-avt-wrap"> \
                                <img class="po-avt" src=' + info.user_info.headImgUrl + '> \
                            </div>'

                    var stateStr = '';
                    // 处理左边竖线的样式
                    if (info.state == 0) {
                        appendStr +=
                            '<div style="float:left;background-color:#FFB939;width:3px;height:171px"> \
                                <div style="background-color:#f8f8f8;height:40px;width:4px"></div> \
                            </div>';
                        stateStr = '观看了';
                    } else {
                        appendStr +=
                            '<div style="float:left;background-color:red;width:3px;height:171px"> \
                                <div style="background-color:#f8f8f8;height:40px;width:4px"></div> \
                            </div>';
                        stateStr = '想要观看';
                    }

                    // 剩余的样式
                    $('.search-out').append(
                        appendStr +=
                            '<div class="po-cmt"> \
                            <div class="po-hd"> \
                                <p class="po-name">' + info.user_info.nickName + '</p> \
                                <div class="post"> \
                                    <p class="time"><span>' + info.date + '</span></p> \
                                    <br> \
                                    <p class="watch">' + stateStr + '</p> \
                                    <a id="first" href="javascript:void(0);" \
                                       class="weui_media_box weui_media_appmsg order"> \
                                        <div id="fp" class=" weui_media_hd order_pic"> \
                                            <img id="fpp" class="weui_media_appmsg_thumb" src=' + info.movie_info.img + '> \
                                        </div> \
                                        <div class="weui_media_bd"> \
                                            <h4 class="weui_media_title">' + info.movie_info.cnname + '</h4> \
                                            <p style="font-family:Times New Roman,Times,serif;font-size:10px;color:gray;">' + info.movie_info.enname + '</p> \
                                            <div style="display:inline"> \
                                                <div style="float:left;font-size:15px">导演:</div> \
                                                <div style="float:left;font-size:15px;color:#0052BA;">&nbsp&nbsp' + info.director + ' </div> \
                                            </div> \
                                            <br> \
                                            <div style="display:inline"> \
                                                <div style="float:left;font-size:15px">编剧:</div> \
                                                <div style="float:left;font-size:15px;color:#0052BA;">&nbsp&nbsp' + info.writer + '</div>\
                                            </div> \
                                        </div> \
                                    </a> \
                                </div> \
                            </div> \
                        </div> \
                    </li>'
                    )
                }
            } else {
                killInfinite()
            }
        }
    })
}

function startInfinite() {
    $(document.body).infinite();
    $('#infinite').removeClass('infi-display');
}

function killInfinite() {
    $(document.body).destroyInfinite();
    $('#infinite').addClass('infi-display');
}