// objeto.metodo(json)

$("#peluqueria").validate({
    rules: {
        "txtEmail": {
            required: true,
            email: true
        },
        "txtEmail": {
            required: true,
            minlength: 5
        },
        "txtSolicitud": {
            required: true,
            equalTo: '#id_txtSolicitud'
        }
    }, // --> Fin de reglas
    messages: {
        "txtEmail": {
            required: 'Ingrese email!!!',
            email: 'No cumple formato'
        },
        "txtSolicitud": {
            required: 'Detalles de la agenda',
            minlength: 'Min. 5 caract'
        },
     
    } //-->Fin de mensajes

});
