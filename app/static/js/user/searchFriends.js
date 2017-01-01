/**
 * Created by CoderSong on 16/12/31.
 */
$(document).ready(function () {

    $("#mov_input").keydown(function (e) {
        if (e.which == 13) {
            var value = $(this).val();
            if (value != "") {
                $('.search-out').empty();
                $("#select").slideDown();
                searchEvent(value);
            } else {
                $('.search-out').empty();
                $("#select").slideUp();
            }
        }
    });
});

function searchEvent(value) {
    $.ajax({
        url: '/friends/friend/' + value,
        type: 'GET',
        success: function (data) {
            var friends = data.userList;
            if (friends != null) {
                for (var index in friends) {
                    var friend = friends[index];
                    var address = friend.province + ' ' + friend.city;
                    var sex = "";
                    if (friend.sex == 0) {
                        sex = 'female'
                    } else {
                        sex = 'male'
                    }

                    var appendString =
                        '<div class="weui_media_box weui_media_appmsg"> \
                            <div class="weui_media_hd"> \
                                <img class="weui_media_appmsg_thumb head-image" src="' + friend.headImgUrl + '"> \
                            </div> \
                            <div class="weui_media_bd"> \
                                <div class="weui_media_title"> \
                                    <img src="image/photo/' + sex + '.png" /><div>' + friend.nickName + '</div> \
                                </div> \
                                <p class="weui_media_desc">' + address + '</p> \
                            </div>';

                    // 添加好友按钮
                    if (friend.isMy == 0) {
                        appendString +=
                            '   <div class="weui_cell_ft"> \
                                    <h4 class="me">我</h4>\
                                </div>\
                            </div>'
                    } else {
                        if (friend.isFriend == 0 || friend.isFriend == 2) {
                            appendString +=
                                '   <div class="weui_cell_ft">\
                                        <img data-id="' + friend.myid + '" class="friends-add-btn" src="image/photo/friends_add.png"/> \
                                    </div>\
                                </div>'
                        } else {
                            appendString +=
                                '   <div class="weui_cell_ft">\
                                        <h4>好友</h4> \
                                    </div>\
                                </div>'
                        }
                    }

                    $('.search-out').append(
                        appendString
                    )
                }

                $('.friends-add-btn').click(function () {
                    var id = $(this).attr('data-id');
                    $.ajax({
                        url: '/friends/one/' + id,
                        type: 'GET',
                        success: function (data) {
                            if (data.message == 'success') {
                                window.location.href = '/';
                            } else {
                                alert('添加好友失败!')
                            }
                        }
                    })
                })
            }
        }
    })
}