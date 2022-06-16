// objeto.metodo(json)
// $("#formulario1").click(function (event) {
//     /* Borrar las consultas */
//     event.preventDefault();
// });
btnGuardar.preventDefault();

$("#formulario1").validate({
    rules: {
        "id_txtNombre": {
            required: true,
            
        },
        "id_txtEmail": {
            required: true,
            email: true
        },
        "id_txtSolicitud": {
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
            minlength: 'le'
        },
     
    } //-->Fin de mensajes


});



