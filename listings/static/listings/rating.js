function hide_stars(rating){
  var rating = parseInt(rating);

  var star_images = $(".rating").children("img");
  star_images.each(function(){
    var star_num = parseInt($(this).attr("num"));
    if(!$(this).hasClass("done")){
      if(star_num != rating){
        $(this).hide();
      }else{
        $(this).show();
      }
      $(this).addClass("done");
    }

  });
}
