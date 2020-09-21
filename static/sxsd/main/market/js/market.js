$(function () {
    $('#all_type').click(function () {

        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down')
        $('#all_product_type').toggle()

    })
    $('#comprehensive_sort').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down')
        $('#sort').toggle()
    })


})