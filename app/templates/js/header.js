$(document).ready(function(){
  $("#shift").click(function(){
    $(".shift-hide").css("display","block");
    $(".help-hide").css("display","none");
  });
  $("#shift-img").click(function(){
    $(".shift-hide").css("display","block");
    $(".help-hide").css("display","none");
  });
  $("#help-img").click(function(){
    $(".help-hide").css("display","block");
    $(".shift-hide").css("display","none");
  });
  $("#help").click(function(){
    $(".help-hide").css("display","block");
    $(".shift-hide").css("display","none");
  });
  
  $("#main").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"5px",
      "width":"80px"
    },{
    	duration:500
    });
  });

  $("#resource").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"100px",
      "width":"140px"
    },{
    	duration:500
    });
  });
  
  $("#purchase").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"260px",
      "width":"140px"
    },{
    	duration:500
    });
  });

  $("#logistics").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"417px",
      "width":"80px"
    },{
    	duration:500
    });
  });

  $("#price").mouseover(function(){
    $("#slide-act").animate({
      "margin-left":"515px",
      "width":"140px"
    },{
    	duration:500
    });
  });

  // $(".top-out").mouseover(function(){
  //   $("#slide-act").animate({
  //     "margin-left":"5px",
  //     "width":"80px"
  //   },{
  //   	duration:500
  //   });
  // });
});

