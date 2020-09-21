$(function () {
    $('#icode').click(function () {
        var code_src = document.getElementById('icode')
        code_src.src = '/sxsduser/get_code/'+Math.random()
    })

    $('form').submit(function () {
        var password = $('#password').val()
        var password2 = MD5(password)
        $('#password').val(password2)
    })

})