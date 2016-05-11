$(document).ready(function(){
  var a = $(".top").offset().left;
  var b = a+730;
  var c = a+895;
  $(".shift-hide").css("left",b);
  $(".help-hide").css("left",c);

  $(window).resize(function(){
    var d = $(".top").offset().left;
    var e = d+730;
    var f = d+895;
    // console.log(e);
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
    for(var i = 0;i < 5;i ++){
      if($(".nav-link a").eq(i).hasClass("active")){
        if(i==0){
          $("#slide-act").animate({
            "margin-left":"30px",
            "width":"52px"
          },{
            duration:100
          });
        }else if(i==1){
          $("#slide-act").animate({
            "margin-left":"130px",
            "width":"110px"
          },{
            duration:100
          });
        }else if(i==2){
          $("#slide-act").animate({
            "margin-left":"278px",
            "width":"110px"
          },{
            duration:100
          });
        }else if(i==3){
          $("#slide-act").animate({
            "margin-left":"436px",
            "width":"52px"
          },{
            duration:100
          });
        }else if(i==4){
          $("#slide-act").animate({
            "margin-left":"535px",
            "width":"110px"
          },{
            duration:100
          });
        }

      }
    }
    
  });
  
  $(".nav-link a").click(function(){
    $(".nav-link a").removeClass();
    $(this).addClass("active");
  });
  
  if($(".nav-link").attr("activeid")=="0"){
    $("#slide-act").css("margin-left","30px");
    $("#slide-act").css("width","52px");
  }else if($(".nav-link").attr("activeid")=="1"){
    $("#slide-act").css("margin-left","130px");
    $("#slide-act").css("width","110px");
  }else if($(".nav-link").attr("activeid")=="2"){
    $("#slide-act").css("margin-left","278px");
    $("#slide-act").css("width","110px");
  }else if($(".nav-link").attr("activeid")=="3"){
    $("#slide-act").css("margin-left","436px");
    $("#slide-act").css("width","52px");
  }else if($(".nav-link").attr("activeid")=="4"){
    $("#slide-act").css("margin-left","535px");
    $("#slide-act").css("width","110px");
  }

});

