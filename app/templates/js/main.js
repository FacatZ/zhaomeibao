$(document).ready(function(){
  $(".action").mouseover(function(){
    $(".action").css("background-image","url(../main/picture/change_cut_23.png)");
    $(".action-imformation").css("display","block");
  });
  $(".action").mouseout(function(){
    $(".action").css("background-image","url(../main/picture/cut_23.png)");
    $(".action-imformation").css("display","none");
  });

  $(".nosmoke").mouseover(function(){
    $(".nosmoke").css("background-image","url(../main/picture/change_cut_29.png)");
    $(".action-imformation").css("display","block");
  });
  $(".nosmoke").mouseout(function(){
    $(".nosmoke").css("background-image","url(../main/picture/cut_29.png)");
    $(".action-imformation").css("display","none");
  });

  $(".fire").mouseover(function(){
    $(".fire").css("background-image","url(../main/picture/change_cut_30.png)");
    $(".action-imformation").css("display","block");
  });
  $(".fire").mouseout(function(){
    $(".fire").css("background-image","url(../main/picture/cut_30.png)");
    $(".action-imformation").css("display","none");
  });

  $(".action-imformation").mouseover(function(){
    $(".action-imformation").css("display","block");
  });
  $(".action-imformation").mouseout(function(){
    $(".action-imformation").css("display","none");
  });

  $(".carousel").carousel({
    interval:4000
  })

  $(".left-img").mouseover(function(){
    $(".left-img").css("background-image","url(../main/picture/cut_change_40.png)");
  });
  $(".left-img").mouseout(function(){
    $(".left-img").css("background-image","url(../main/picture/cut_40.png)");
  });

  $(".right-img").mouseover(function(){
    $(".right-img").css("background-image","url(../main/picture/cut_change_42.png)");
  });
  $(".right-img").mouseout(function(){
    $(".right-img").css("background-image","url(../main/picture/cut_42.png)");
  });
});