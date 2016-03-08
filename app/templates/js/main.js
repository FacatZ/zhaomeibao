$(document).ready(function(){
    var a = $(".ui_asideMenu").offset().left;
    var b = a+250;
    $(".action-imformation").css("left",b);
    $(".nosmoke-imformation").css("left",b);
    $(".fire-imformation").css("left",b);

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
    $(".nosmoke-imformation").css("display","block");
  });
  $(".nosmoke").mouseout(function(){
    $(".nosmoke").css("background-image","url(../main/picture/cut_29.png)");
    $(".nosmoke-imformation").css("display","none");
  });

  $(".fire").mouseover(function(){
    $(".fire").css("background-image","url(../main/picture/change_cut_30.png)");
    $(".fire-imformation").css("display","block");
  });
  $(".fire").mouseout(function(){
    $(".fire").css("background-image","url(../main/picture/cut_30.png)");
    $(".fire-imformation").css("display","none");
  });

  $(".action-imformation").mouseover(function(){
    $(".action-imformation").css("display","block");
  });
  $(".action-imformation").mouseout(function(){
    $(".action-imformation").css("display","none");
  });
  $(".nosmoke-imformation").mouseover(function(){
    $(".nosmoke-imformation").css("display","block");
  });
  $(".nosmoke-imformation").mouseout(function(){
    $(".nosmoke-imformation").css("display","none");
  });
  $(".fire-imformation").mouseover(function(){
    $(".fire-imformation").css("display","block");
  });
  $(".fire-imformation").mouseout(function(){
    $(".fire-imformation").css("display","none");
  });

  $(window).resize(function(){
    var a = $(".ui_asideMenu").offset().left;
    var b = a+250;
    $(".action-imformation").css("left",b);
  });
  $(window).resize(function(){
    var a = $(".ui_asideMenu").offset().left;
    var b = a+250;
    $(".nosmoke-imformation").css("left",b);
  });
  $(window).resize(function(){
    var a = $(".ui_asideMenu").offset().left;
    var b = a+250;
    $(".fire-imformation").css("left",b);
  });

  $("#left").mouseover(function(){
    $("#left").attr("src","../main/picture/cut_change_33.png")
  });
  $("#left").mouseout(function(){
    $("#left").attr("src","../main/picture/cut_33.png")
  });
  $("#right").mouseover(function(){
    $("#right").attr("src","../main/picture/cut_change_35.png")
  });
  $("#right").mouseout(function(){
    $("#right").attr("src","../main/picture/cut_35.png")
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
  
  $("#top_img").mouseover(function(){
    $("#top_img").css("background-image","url(../main/picture/cut_change_26.png)");
  });
  $("#top_img").mouseout(function(){
    $("#top_img").css("background-image","url(../main/picture/cut_26.png)");
  });

  $("#bottom_img").mouseover(function(){
    $("#bottom_img").css("background-image","url(../main/picture/cut_change_49.png)");
  });
  $("#bottom_img").mouseout(function(){
    $("#bottom_img").css("background-image","url(../main/picture/cut_49.png)");
  });
  
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

  $(".north-area").click(function(){
    $(".north-area").attr("src","../main/picture/cut2_change_20.png");
    $(".south-area").attr("src","../main/picture/cut2_22.png");
    $(".else-area").attr("src","../main/picture/cut2_24.png");
    $(".east-area").attr("src","../main/picture/cut2_18.png");
    $(".action-box-south").css("display","none");
    $(".action-box-else").css("display","none");
    $(".action-box-east").css("display","none");
    $(".action-box-north").css("display","block");
  });
  $(".south-area").click(function(){
    $(".south-area").attr("src","../main/picture/cut2_change_22.png");
    $(".north-area").attr("src","../main/picture/cut2_20.png");
    $(".else-area").attr("src","../main/picture/cut2_24.png");
    $(".east-area").attr("src","../main/picture/cut2_18.png");
    $(".action-box-south").css("display","block");
    $(".action-box-else").css("display","none");
    $(".action-box-east").css("display","none");
    $(".action-box-north").css("display","none");
  });
  $(".else-area").click(function(){
    $(".else-area").attr("src","../main/picture/cut2_change_24.png");
    $(".north-area").attr("src","../main/picture/cut2_20.png");
    $(".south-area").attr("src","../main/picture/cut2_22.png");
    $(".east-area").attr("src","../main/picture/cut2_18.png");
    $(".action-box-south").css("display","none");
    $(".action-box-else").css("display","block");
    $(".action-box-east").css("display","none");
    $(".action-box-north").css("display","none");
  });
  $(".east-area").click(function(){
    $(".east-area").attr("src","../main/picture/cut2_change_18.png");
    $(".else-area").attr("src","../main/picture/cut2_24.png");
    $(".north-area").attr("src","../main/picture/cut2_20.png");
    $(".south-area").attr("src","../main/picture/cut2_22.png");
    $(".action-box-south").css("display","none");
    $(".action-box-else").css("display","none");
    $(".action-box-east").css("display","block");
    $(".action-box-north").css("display","none");
  });
  






});



