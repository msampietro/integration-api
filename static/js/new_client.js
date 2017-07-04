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
        url : "/new_client", // the endpoint,commonly same url // http method
        data : {'empresa':$('#empresa').val(),
                'db':$('#db').val(),
                'usuario_lead':$('#usuario_lead').val()}, // data sent with the post request
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


    $( "#logout" ).on('click',function() {
        window.location.replace('/logout')
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
        url : "/update_client", // the endpoint,commonly same url // http method
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
        url : "/delete_client", // the endpoint,commonly same url // http method
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




