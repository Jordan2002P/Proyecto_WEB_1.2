$("#btn-obtener").click(function (event) {
    /* Borrar las consultas */
    event.preventDefault();

    var url = "https://api.thecatapi.com/v1/images/search";
    
fetch(url)
    .then(response => response.json())
    .then(data => 
        {

        var $foto_gato = $("<p><img src='"+data[0].url+"'>");
        
        
        $("#info").empty();
        $('#info')
       
        .append ($foto_gato);
             
        
    })
   
});
//   cierre del click 

