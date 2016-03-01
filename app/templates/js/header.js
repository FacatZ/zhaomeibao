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

