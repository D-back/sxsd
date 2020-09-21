$(function () {
    var name_flag = false
    var password_flag = false
    var confirm_password_flag = false
    var email_flag = false
    var head_flag = false

    // 判断用户名是否存在和是否符合要求
    $('#username').mouseout(function () {
        var username = $('#username').val()
        if (username.length >8 | username.length < 5  ) {
            $('#username_err').text('用户名格式错误')
            name_flag = false
        }
        else {
            $('#username_err').text('')
            name_flag = true
            // $('#button').removeAttr('disabled')   自己的逻辑(是否能够注册)
            $.ajax({
                url:'/sxsduser/ajax_username/',
                type:'POST',
                data:{'username':username},
                success:function (msg) {
                    if ( msg.flag ) {
                        $('#username_err').text('用户名已存在')
                        name_flag = false
                    }
                    else {
                        $('#username_err').text('')
                        // $('#button').removeAttr('disabled') 自己的逻辑(是否能够注册)
                        name_flag = true
                    }
                }
            })
        }

    })
    // 密码格式的判断
    $('#password').mouseout(function () {
        var check_password = '^[A-Za-z0-9]+$'
        var password = $('#password').val()
        if (password.length > 16 | password.length < 8 |  password.match(check_password)){
            $('#password_err').text('密码格式错误')
            password_flag = false
        }
        else {
            $('#password_err').text('')
            // $('#button').removeAttr('disabled')  自己的逻辑(是否能够注册)
            password_flag = true
        }

    })
        //确认密码的判断
    $('#confirm_password').mouseout(function () {
        var password = $('#password').val()
        var confirm_password = $('#confirm_password').val()
        if (password != confirm_password ){
            $('#confirm_password_err').text('密码不一致')
            confirm_password_flag = false
        }
        else {
            $('#confirm_password_err').text('')
            // $('#button').removeAttr('disabled')  自己的逻辑(是否能够注册)
            confirm_password_flag = true
        }
    })
    //    判断邮箱格式
    $('#email').mouseout(function () {
        var check_email = /^([A-z0-9]{6,18})(\w|\-)+@[A-z0-9]+\.([A-z]{2,3})$/;
        var email = $('#email').val()
        if (check_email.test(email)){
            $('#email_err').text('')
            // $('#button').removeAttr('disabled')    自己的逻辑(是否能够注册)
            email_flag = true
        }
        else {
            $('#email_err').text('请输入正确的邮箱')
            email_flag = false
        }
    })

    // 判断头像存在不存在
    $('#head').mouseout(function () {
        if ($('#head').val()){
             // $('#button').removeAttr('disabled')   自己的逻辑(是否能够注册)
            head_flag = true
        }
        else {
            head_flag = false
        }
    })

    // // 注册按钮是否能够点击    自己的逻辑(是否能够注册)
    // $('#button').click(function () {
    //     if ($('#head').val() && !$('#email_err').text() && !$('#confirm_password_err').text() &&  !$('#password_err').text() && !$('#username_err').text()){
    //        if($('#username').val() && $('#password').val() && $('#confirm_password').val() && $('#email').val()){
    //             var password = $('#password').val()
    //             var confirm_password = $('#confirm_password').val()
    //             var hash_password = MD5(password)
    //             var hash_confirm_password = MD5(confirm_password)
    //             $('#password').val(hash_password)
    //             $('#confirm_password').val(hash_confirm_password)
    //        }
    //     }
    //     else {
    //         $('#button').attr('disabled','disabled')
    //     }
    //
    // })

        // 授课逻辑
    $('form').submit(function () {
        var flag = name_flag && password_flag && confirm_password_flag && email_flag && head_flag
        var password = $('#password').val()
        var confirm_password = $('#confirm_password').val()
        var hash_password = MD5(password)
        var hash_confirm_password = MD5(confirm_password)
        $('#password').val(hash_password)
        $('#confirm_password').val(hash_confirm_password)

        if (flag){
            return true
        }else {
            return false
        }
    })





})