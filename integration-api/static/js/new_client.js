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
        $('#response').text(resp.details)

    },
        error : function(xhr,errmsg,err) {
        $('#response').text(err.details)
}
});

});

});


