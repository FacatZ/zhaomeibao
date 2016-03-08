$(document).ready(function(){
  var a = $(".top").offset().left;
  var b = a+730;
  var c = a+840;
  $(".shift-hide").css("left",b);
  $(".help-hide").css("left",c);

  $(window).resize(function(){
    var d = $(".top").offset().left;
    var e = d+730;
    var f = d+840;
    console.log(e);
    $(".shift-hide").css("left",e);
    $(".help-hide").css("left",f);
  });

  $(".move-box").mouseover(function(){
    $(".shift-hide").css("display","block");
  });
  $(".move-box").mouseout(function(){
    $(".shift-hide").css("display","none");
  });
  $(".shift-hide").mouseover(function(){
    $(".shift-hide").css("display","block");
    $(".help-hide").css("display","none");
  });
  $(".shift-hide").mouseout(function(){
    $(".shift-hide").css("display","none");
  });

  $(".help-box").mouseover(function(){
    $(".help-hide").css("display","block");
  });
  $(".help-box").mouseout(function(){
    $(".help-hide").css("display","none");
  });
  $(".help-hide").mouseover(function(){
    $(".help-hide").css("display","block");
    $(".shift-hide").css("display","none");
  });
  $(".help-hide").mouseout(function(){
    $(".help-hide").css("display","none");
  });

  $("#main").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"30px",
      "width":"52px"
    },{
    	duration:100
    });
  });

  $("#resource").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"130px",
      "width":"110px"
    },{
    	duration:100
    });
  });
  
  $("#purchase").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"278px",
      "width":"110px"
    },{
    	duration:100
    });
  });

  $("#logistics").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"436px",
      "width":"52px"
    },{
    	duration:100
    });
  });

  $("#price").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"535px",
      "width":"110px"
    },{
    	duration:100
    });
  });
  
  $(".nav-link").mouseleave(function(){
    $("#slide-act").animate({
      "margin-left":"30px",
      "width":"52px"
    },{
      duration:100
    });
  });

});

