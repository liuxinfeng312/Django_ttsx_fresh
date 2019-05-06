$(function () {

    var num=parseInt($('.num_show').val())
    // var num=$('.num_show').val()
    console.log(num)
    $('.add').click(function () {
        console.log('点击成功')
        console.log(num)
        num=parseInt($('.num_show').val())+1
        console.log($('.num_show').val())


        $('.num_show').val(num)


    })
      $('.minus').click(function () {
        console.log('点击成功')
        num=parseInt($('.num_show').val())-1
          if (num < 1) {
              num=1

          }

        $('.num_show').val(num)

    })
    $('.add_cart').click(function () {
        console.log('点击购物车成功')
        var goodnum=parseInt($('.num_show').val())
        console.log(goodnum)
        var goodid=$('.add_cart').attr('data-id')
        console.log(goodid)
        request_data={
            'goodid':goodid,
            'goodnum':goodnum

        }

        $.get('/fresh/addcart/', request_data, function (response) {
            console.log(response)
            // console.log(response.status)


            if (response.statue==1){
                //
                console.log(response.goodsnum)
                $('#show_count').html(response.goodsnum)

            }

        })

    })





})