$(function () {
    // 添加到购物车
    $('.addToCart').click(function () {
        var $button = $(this)
        var g_id = $button.attr('goodid')
        $.getJSON(
            '/sxsdcart/addToCart/',
            {'g_id': g_id},
            function (data) {
                $button.prev().text(data.c_goods_num)
            }
        )
    })
    //从购物车中减少
    $('.reduceFromCart').click(function () {
        var $button = $(this)
        var good_num = $button.next().text()
        var g_id = $button.attr('goodid')
        if(good_num == 0){
            $button.next().text('0')
        }else {
           $.getJSON(
            '/sxsdcart/reduceFromCart/',
            {'g_id': g_id},
            function (data) {
                if(data.c_goods_num){
                    $button.next().text(data.c_goods_num)
                }else {
                    $button.next().text('0')
                }

            }
        )
        }
    })


    // 购物车中加数量
    $('.add').click(function () {
        var $button = $(this)
        var cartid = $button.attr('cartid')
        $.getJSON(
            '/sxsdcart/modifyGoodsNum/',
            {'cartid': cartid, 'add_reduce': 'add'},
            function (data) {
                $button.prev().text(data.c_goods_num)
                $('#total_price').text(data.total_price)
            }
        )

    })
    // 购物车中减数量
    $('.reduce').click(function () {
        var $button = $(this)
        var cartid = $button.attr('cartid')
        $.getJSON(
            '/sxsdcart/modifyGoodsNum/',
            {'cartid': cartid, 'add_reduce': 'reduce'},
            function (data) {
                if (data.c_goods_num) {
                    $button.next().text(data.c_goods_num)
                } else {
                    $button.parent().parent().remove()
                }
                $('#total_price').text(data.total_price)
            }
        )
    })

    //   单选
    $('.confirm').click(function () {
        var $button = $(this)
        var cartid = $button.attr('cartid')
        $.getJSON(
            '/sxsdcart/select/',
            {'cartid': cartid,},
            function (data) {
                if (data.c_is_select) {
                    $button.find('span').find('span').text('√')
                } else {
                    $button.find('span').find('span').text('')
                }
                if (data.is_not_all_select){
                    $('.all_select').find('span').find('span').text('')
                }
                else {
                    $('.all_select').find('span').find('span').text('√')
                }
                $('#total_price').text(data.total_price)
            }
        )
    })

    //  全选
    $('.all_select').click(function () {
        var select_list = []
        var unselect_list = []

        $('.confirm').each(function () {
            var cartid = $(this).attr('cartid')
            if ($(this).find('span').find('span').text()) {
                select_list.push(cartid)
            } else {
                unselect_list.push(cartid)
            }
        })
        if (unselect_list.length == 0) {
            $.getJSON(
                '/sxsdcart/allselect/',
                {'all_select_list': select_list.join('#')},
                function (data) {
                    $('.all_select').find('span').find('span').text('')
                    $('.confirm').find('span').find('span').text('');
                    $('#total_price').text(data.total_price)
                }
            )
        } else {
            $.getJSON(
                '/sxsdcart/allselect/',
                {'all_select_list': unselect_list.join('#')},
                function (data) {
                    $('.all_select').find('span').find('span').text('√')
                    $('.confirm').find('span').find('span').text('√');
                    $('#total_price').text(data.total_price)
                }
            )
        }

    })
})