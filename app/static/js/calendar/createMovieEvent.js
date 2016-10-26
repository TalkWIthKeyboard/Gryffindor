/**
 * Created by huangrui on 2016/10/22.
 */
$(document).ready(function () {
    $("#mov_input").keyup(function () {
        var value = $(this).val();
        //判断条件之后可修改
        if (value != "") {
            $("#select").find("p.content").text(function () {
                return $(this).parents().attr("data-id");
            });
            $("#select").slideDown();
        }else {
            $("#select").slideUp();
        }
    });

    $("#select").children("div").hover(function () {
        $(this).addClass("touch");
    }, function () {
        $(this).removeClass("touch");
    });

    $("#select").children("div").click(function () {
        var str = $(this).attr("data-id");
        $(".input").val(str);
        $("#select").slideUp();
    });

    $("#select").children("div").on("touchstart", function () {
        $(this).addClass("touch");
    });

    $("#select").children("div").on("touchend", function () {
        $(this).removeClass("touch");
    });
});