/**
 * Created by huangrui on 2016/10/22.
 */
$(document).ready(function () {

    var loading = false;  //状态标记
    $("#mov_input").on('keyup',_.debounce(function(){
        var value = $(this).val();
            //判断条件之后可修改
        if (value != "") {
            searchEvent(value);
            listenInfinite();
        }else {
            searchEventClean();
        }
    },1000));

    $(".search-out").children("div").hover(function () {
        $(this).addClass("touch");
    }, function () {
        $(this).removeClass("touch");
    });

    $(".search-out").children("div").click(function () {
        var str = $(this).attr("data-id");
        $(".input").val(str);
        $("#select").slideUp();
    });

    $(".search-out").children("div").on("touchstart", function () {
        $(this).addClass("touch");
    });

    $(".search-out").children("div").on("touchend", function () {
        $(this).removeClass("touch");
    });

    // 监听滚动事件
    function listenInfinite(){
        $(document.body).infinite().on("infinite", function() {
            if(loading) return;
            loading = true;
            setTimeout(function() {
                var value = $('.search-out').attr('data-value');
                searchEvent(value);
                loading = false;
            }, 1000);   //模拟延迟
        });
    }
});

function searchEvent(value) {
    // 现在已经显示了多少个电影了
    var num = $('.search-out').attr('data-id');
    num = parseInt(num);
    if (num == 1){
        $('.search-out').empty();
        startInfinite();
    }

    console.log(num);

    $.ajax({
        url: '/movies/' + value + '/' + num,
        type: 'GET',
        success: function (data) {
            var movies = data.movieList;
            var num = data.movieNum;
            $('.search-out').attr('data-id',num);
            $('.search-out').attr('data-value',value);
            if (movies != null){
                for (var index in movies){
                    var movie = movies[index];
                    $('.search-out').append(
                    '<div id="aa" data-id="'+ movie.movieid +'"> \
                        <a href="' + '/movies/' + movie.movieid + '" class="weui_media_box weui_media_appmsg"> \
                            <div style="height:90px;width:65px;"class="weui_media_hd"> \
                                <img style="height:90px;"class="weui_media_appmsg_thumb" src="' + movie.img + '"> \
                            </div> \
                            <div class="weui_media_bd"> \
                                <h5 class="weui_media_title">'+ movie.cnname +'</h5> \
                                <p class="movie-enname">' + movie.enname + '</p> \
                                <div style="display:inline"> \
                                    <div class="table-title">导演:</div> \
                                    <div class="table-value">&nbsp&nbsp' + movie.director + '</div> \
                                </div> \
                                <br> \
                                <div style="display:inline"> \
                                    <div class="table-title">主演:</div> \
                                    <div class="table-value">&nbsp&nbsp' + movie.actor + '</div> \
                                </div> \
                            </div> \
                        </a> \
                    </div>')
                }

                if (movies.length < 5){
                    killInfinite();
                }
                $("#select").slideDown();
            } else {
                killInfinite();
            }
        }
    })
}

function searchEventClean() {
    $('.search-out').empty();
    killInfinite();
    $('.search-out').attr('data-id',"1");
    $("#select").slideUp();
}

function startInfinite() {
    $(document.body).infinite();
    $('#infinite').removeClass('infi-display');
}

function killInfinite() {
    $(document.body).destroyInfinite();
    $('#infinite').addClass('infi-display');
}


