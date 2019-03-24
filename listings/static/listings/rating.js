$(function() {

  var rating_p = $(".rating").children("p");
  rating_p.hide();
  var rating = parseInt(rating_p.text().split("=")[1]);

  var star_images = $(".rating").children("img");
  star_images.each(function(){
    var star_num = parseInt($(this).attr("num"));
    if(star_num != rating){
      $(this).hide();
    }else{
      $(this).show();
    }
  });


});
