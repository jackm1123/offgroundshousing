$(function() {

  var rating_p = $(".rating").children("p")
  rating_p.hide()
  var rating = parseInt(rating_p.text().split("=")[1])

  var star = $("#star")
  var star2 = star.clone()
  var star3 = star.clone()
  var star4 = star.clone()
  var star5 = star.clone()
  star.parent().append(star2)
  star.parent().append(star3)
  star.parent().append(star4)
  star.parent().append(star5)

  stars = [];
  stars.push(star);
  stars.push(star2);
  stars.push(star3);
  stars.push(star4);
  stars.push(star5);

  var empty_star = $("#empty_star")
  var empty_star2 = empty_star.clone()
  var empty_star3 = empty_star.clone()
  var empty_star4 = empty_star.clone()
  var empty_star5 = empty_star.clone()
  empty_star.parent().append(empty_star2)
  empty_star.parent().append(empty_star3)
  empty_star.parent().append(empty_star4)
  empty_star.parent().append(empty_star5)

  empty_stars = [];
  empty_stars.push(empty_star);
  empty_stars.push(empty_star2);
  empty_stars.push(empty_star3);
  empty_stars.push(empty_star4);
  empty_stars.push(empty_star5);

  for(var i = 0; i < 5-rating; i++){
    stars[i].hide()
  }

  for(var i = 0; i < rating; i++){
    empty_stars[i].hide()
  }



});
