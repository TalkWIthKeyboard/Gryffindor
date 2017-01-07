$(document).ready(function () {

   // 确认按钮点击事件
   $('#sure-btn').click(function () {
       var message = $('#input-text').val() || false
       if (!message) {
           $.toast('请填写评论后再提交！', 'forbidden');
       } else {
           var eventId = $(this).attr('data-id');
           var url = '/movies/message/' + eventId;
           $.ajax({
               url: url,
               type: 'POST',
               data: {
                   'message': message
               },
               success: function (data) {
                   if (data.message == 'success') {
                       window.location.href = url;
                   } else {
                       alert('保存评论出现错误!');
                   }
               }
           })
       }
   })

});