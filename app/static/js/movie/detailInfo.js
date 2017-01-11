/**
 * Created by huangrui on 2016/10/22.
 */
$(document).ready(function () {

    var click = 1;
    $('.info').click(function () {
        $('.about').slideToggle();
        if (0 == click) {
            $(this).css({'background': 'rgba(255,255,255, 0.8)'});
            click = 1;
        } else {
            $(this).css({'background': '#fff'});
            click = 0;
        }
    });

    $('.record_click').click(function () {
        $(this).next().slideToggle();

        if ($(this).children().eq(1).hasClass('disvi')) {
            $(this).children().eq(1).removeClass('disvi');
        } else {
            $(this).children().eq(1).addClass('disvi');
        }

        // 收起来
        if (!$(this).children().eq(1).hasClass('disvi')) {
            $(this).css({'background': 'rgba(255,255,255, 0.8)'});
            $(this).children().eq(1).show();
            $(this).children().eq(2).hide();
        } else {
            // 放下去
            $(this).css({'background': '#fff'});
            $(this).children().eq(1).hide();
            $(this).children().eq(2).show();
        }
    })
});

