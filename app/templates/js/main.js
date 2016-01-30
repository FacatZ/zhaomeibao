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
  
  // $(".top_img").mouseover(function(){
  //   $(".top_img").css(("background-image","url(../main/picture/cut_change_26.png)");
  // });
  // $(".top_img").mouseout(function(){
  //   $(".top_img").css("background-image","url(../main/picture/cut_26.png)");
  // });

  // $(".bottom_img").mouseover(function(){
  //   $(".bottom_img").css(("background-image","url(../main/picture/cut_change_49.png)");
  // });
  // $(".bottom_img").mouseout(function(){
  //   $(".bottom_img").css("background-image","url(../main/picture/cut_49.png)");
  // });
  
  jQuery(".txtScroll-top").slide({titCell:".hd ul",mainCell:".bd ul",autoPage:true,effect:"top",autoPlay:true,vis:15});

  $(".pic1").mouseover(function(){
    $(".pic1").attr("src","../main/picture/cut2_change_06.png");
  });
  $(".pic1").mouseout(function(){
    $(".pic1").attr("src","../main/picture/cut2_09.png");
  });
  $(".pic2").mouseover(function(){
    $(".pic2").attr("src","../main/picture/cut2_change_06.png");
  });
  $(".pic2").mouseout(function(){
    $(".pic2").attr("src","../main/picture/cut2_09.png");
  });
  $(".pic3").mouseover(function(){
    $(".pic3").attr("src","../main/picture/cut2_change_06.png");
  });
  $(".pic3").mouseout(function(){
    $(".pic3").attr("src","../main/picture/cut2_09.png");
  });
  $(".pic4").mouseover(function(){
    $(".pic4").attr("src","../main/picture/cut2_change_06.png");
  });
  $(".pic4").mouseout(function(){
    $(".pic4").attr("src","../main/picture/cut2_09.png");
  });
  $(".pic5").mouseover(function(){
    $(".pic5").attr("src","../main/picture/cut2_change_06.png");
  });
  $(".pic5").mouseout(function(){
    $(".pic5").attr("src","../main/picture/cut2_09.png");
  });
  $(".pic6").mouseover(function(){
    $(".pic6").attr("src","../main/picture/cut2_change_06.png");
  });
  $(".pic6").mouseout(function(){
    $(".pic6").attr("src","../main/picture/cut2_09.png");
  });
  $(".pic7").mouseover(function(){
    $(".pic7").attr("src","../main/picture/cut2_change_06.png");
  });
  $(".pic7").mouseout(function(){
    $(".pic7").attr("src","../main/picture/cut2_09.png");
  });
});



