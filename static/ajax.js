function AJAX(url,type,data,func){
  $.ajax({
    url: url,
    type: type,
    data: data,
    success: func
  });
}
