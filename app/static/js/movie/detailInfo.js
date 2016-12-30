/**
 * Created by huangrui on 2016/10/22.
 */
$(document).ready(function () {

    $('#time').calendar();
    $('#ftime').calendar();
    var click = 0;
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
            console.log("remove class");
        }
        else {
            $(this).children().eq(1).addClass('disvi');
            console.log("add class");
        }

        if (0 == click) {
            $(this).css({'background': 'rgba(255,255,255, 0.8)'});

            click = 1;
        } else {
            $(this).css({'background': '#fff'});

            click = 0;
        }
    });
});

