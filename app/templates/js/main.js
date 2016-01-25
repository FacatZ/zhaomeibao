$(document).ready(function(){
  $(".action").mouseover(function(){
    $(".action").css("background-image","url(style/picture/change_cut_23.png)");
  });
  $(".action").mouseout(function(){
    $(".action").css("background-image","url(style/picture/cut_23.png)");
  });

  $(".nosmoke").mouseover(function(){
    $(".nosmoke").css("background-image","url(style/picture/change_cut_29.png)");
  });
  $(".nosmoke").mouseout(function(){
    $(".nosmoke").css("background-image","url(style/picture/cut_29.png)");
  });

  $(".fire").mouseover(function(){
    $(".fire").css("background-image","url(style/picture/change_cut_30.png)");
  });
  $(".fire").mouseout(function(){
    $(".fire").css("background-image","url(style/picture/cut_30.png)");
  });
});