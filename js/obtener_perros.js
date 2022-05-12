function getRandomImage()
{
  // get the data from the server
  $.get( "https://dog.ceo/api/breeds/image/random", function( data ) {
    // set the source of the image
    $('#dogImage').attr('src', data.message)
  });
}