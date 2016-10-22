/**
 * Created by huangrui on 2016/10/22.
 */
$(document).ready(function () {
    $("#mov_input").keyup(function () {
        var value = $(this).val();
        //判断条件之后可修改
        if (value != "") {
            $("#select").slideDown();
        }else {
            $("#select").slideUp();
        }
    });

    $("#select .weui_cell").hover(function () {
        $(this).css({"background-color":"#1ebc21","color":"white"});
        // console.log("ok");
    }, function () {
        $(this).css({"background-color":"white","color":"black"});
    });

    $("#select .weui_cell").click(function () {
        var str = $(this).attr('data-id');
        $(".input").val(str);
    });
    
    // $("#select div").on("touchstart", function (e) {
    //     $(this).css({"background-color":"#1ebc21","color":"white"});
    // });
    // $("#select div").on("touchend", function (e) {
    //     $(this).css({"background-color":"white","color":"black"});
    // });

});