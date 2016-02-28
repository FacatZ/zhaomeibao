$(document).ready(function(){
  $("#shift").click(function(){
    $(".shift-hide").toggle();
    $(".help-hide").css("display","none");
  });
  $("#shift-img").click(function(){
    $(".shift-hide").toggle();
    $(".help-hide").css("display","none");
  });
  $("#help-img").click(function(){
    $(".help-hide").toggle();
    $(".shift-hide").css("display","none");
  });
  $("#help").click(function(){
    $(".help-hide").toggle();
    $(".shift-hide").css("display","none");
  });

  $("#main").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"5px",
      "width":"80px"
    },{
    	duration:100
    });
  });

  $("#resource").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"100px",
      "width":"140px"
    },{
    	duration:100
    });
  });
  
  $("#purchase").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"260px",
      "width":"140px"
    },{
    	duration:100
    });
  });

  $("#logistics").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"417px",
      "width":"80px"
    },{
    	duration:100
    });
  });

  $("#price").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"515px",
      "width":"140px"
    },{
    	duration:100
    });
  });
  
  $(".nav-link").mouseleave(function(){
    $("#slide-act").animate({
      "margin-left":"5px",
      "width":"80px"
    },{
      duration:100
    });
  });

});

