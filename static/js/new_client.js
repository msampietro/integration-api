$(document).ready(function(){
    $( "#register-submit" ).on('click',function() {

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });

    $.ajax({
        type : "POST",
        url : "/mad/new_client", // the endpoint,commonly same url // http method
        data : {'empresa':$('#empresa').val(),
                'db':$('#db').val()}, // data sent with the post request
        success : function(resp) {
            if(resp.status!=200){
                $('#response').text(resp.details)
                setTimeout(function(){ $('#response').text(""); }, 2000);
            }
            else{
                $('#response').text(resp.details)
                 setTimeout(function(){window.location.href = window.location;}, 2000);
            }

    },
        error : function(xhr,errmsg,err) {
        $('#response').text(err.details)
             setTimeout(function(){ $('#response').text(""); }, 2000);
}
});

});

    $( "#password-submit" ).on('click',function() {

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });

    $.ajax({
        type : "POST",
        url : "/mad/change", // the endpoint,commonly same url // http method
        data : {'user_now':$('#user_now').val(),
                'password_now':$('#password_now').val(),
                'new_password':$('#new_password').val(),
                'new_password2':$('#new_password2').val()}, // data sent with the post request
        success : function(resp) {
            if(resp.status!=200){
                $('#password-response').text(resp.details)
                setTimeout(function(){ $('#response').text(""); }, 2000);
            }
            else{
                $('#password-response').text(resp.details)
                 setTimeout(function(){window.location.href = window.location;}, 2000);
            }

    },
        error : function(xhr,errmsg,err) {
        $('#password-response').text(err.details)
             setTimeout(function(){ $('#response').text(""); }, 2000);
}
});

});

    $( "#create-submit" ).on('click',function() {

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });

    $.ajax({
        type : "POST",
        url : "/mad/create", // the endpoint,commonly same url // http method
        data : {'user_new':$('#user_new').val(),
                'new_password_create':$('#new_password_create').val(),
                'new_password2_create':$('#new_password2_create').val()}, // data sent with the post request
        success : function(resp) {
            if(resp.status!=200){
                $('#user-response').text(resp.details)
                setTimeout(function(){ $('#response').text(""); }, 2000);
            }
            else{
                $('#user-response').text(resp.details)
                 setTimeout(function(){window.location.href = window.location;}, 2000);
            }

    },
        error : function(xhr,errmsg,err) {
        $('#password-response').text(err.details)
             setTimeout(function(){ $('#response').text(""); }, 2000);
}
});

});


    $( "#logout" ).on('click',function() {
        window.location.replace('/mad/logout')
});

    $( "#change" ).on('click',function() {
        window.location.replace('/mad/change')
});

     $( "#back" ).on('click',function() {
        window.location.replace('/mad/clients')
});



});

    function actualizar(id) {
    res = id.match('(client_list-[0-9]{1,}-)');
    empresa_id = res[0]+'empresa';
    codigo_id = res[0]+'codigo';
    codigo = $('#'+codigo_id).val()
    empresa = $('#'+empresa_id).val();
    db_id = res[0]+'db';
    db = $('#'+db_id).val();
    usuario_id = res[0]+'usuario_lead';
    usuario_lead = $('#'+usuario_id).val();

      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });



     $.ajax({
        type : "POST",
        url : "/mad/update_client", // the endpoint,commonly same url // http method
        data : {'empresa':empresa, 'db':db,'usuario_lead':usuario_lead, 'id':codigo}, // data sent with the post request
        success : function(resp) {
             $('#response').text(resp.details)
            if(resp.status==200){
                 setTimeout(function(){ window.location.href = window.location.href; }, 2000);
            } else {
                setTimeout(function(){ window.location.href = window.location.href; }, 2000);
            }

    },
        error : function(xhr,errmsg,err) {
        $('#response').text(err)
}
});
}


  function eliminar(id) {
    res = id.match('(client_list-[0-9]{1,}-)');
    empresa_id = res[0]+'empresa';
    codigo_id = res[0]+'codigo';
    codigo = $('#'+codigo_id).val()

      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });


     $.ajax({
        type : "POST",
        url : "/mad/delete_client", // the endpoint,commonly same url // http method
        data : {'id':codigo}, // data sent with the post request
        success : function(resp) {
            $('#response').text(resp.details)
            if(resp.status==200){
                 setTimeout(function(){ window.location.href = window.location.href; }, 2000);
            }
            else {
                 setTimeout(function(){  window.location.href = window.location.href; }, 2000);
            }
    },
        error : function(xhr,errmsg,err) {
        $('#response').text(err)
}
});
}


  function eliminar_usuario(id) {

      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });


     $.ajax({
        type : "POST",
        url : "/mad/delete_user", // the endpoint,commonly same url // http method
        data : {'id':id}, // data sent with the post request
        success : function(resp) {
            $('#delete-response').text(resp.details)
            if(resp.status==200){
                 setTimeout(function(){ window.location.href = window.location.href; }, 2000);
            }
            else {
                 setTimeout(function(){  window.location.href = window.location.href; }, 2000);
            }
    },
        error : function(xhr,errmsg,err) {
        $('#delete-response').text(err)
}
});
}



