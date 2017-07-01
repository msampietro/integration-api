$(document).ready(function(){
    $( "#register-submit" ).click(function() {

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
        $('#response').text(resp)

    },
        error : function(xhr,errmsg,err) {
        $('#response').text(err)
}
});

});

});

function actualizar(id) {
    res = id.match('(client_list-[0-9]{1,}-)')
    empresa_id = res[0]+'empresa'
    empresa = $('#'+empresa_id).val()
    db_id = res[0]+'db'
    db = $('#'+db_id).val()
    usuario_id = res[0]+'usuario_lead'
    usuario_lead = $('#'+usuario_id).val()
    alert(empresa);
   /*  $.ajax({
        type : "POST",
        url : "/delete_client", // the endpoint,commonly same url // http method
        data : {'value':res}, // data sent with the post request
        success : function(resp) {
        $('#response').text(resp)

    },
        error : function(xhr,errmsg,err) {
        $('#response').text(err)
}
});*/
}


