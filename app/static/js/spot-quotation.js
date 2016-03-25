$(document).ready(function(){
	$(".top-class li").mouseover(function(){
		$(this).css("color","E4A15D");
		$(this).css("background-color","rgb(239,239,239)");
	}).mouseout(function(){
		$(this).css("color","black");
		$(this).css("background-color","rgb(216,216,216)");
	});

	// $(".top-class li").each(function(index){
	// 	$(this).click(function(){
	// 		$("li").removeClass("active");
	// 		$(this).addClass("active");
	// 		$(".information-box").removeClass("show-box");
	// 		$(".information-box").eq(index).addClass("show-box");
	// 	});
	// });
	
	$("#img-one").click(function(){
		$("#img-one").attr("src","../spot-quotation/picture/cut_change_10.png");
		$("#img-two").attr("src","../spot-quotation/picture/cut_07.png");
		$("#img-three").attr("src","../spot-quotation/picture/cut_13.png");
	});
	$("#img-two").click(function(){
		$("#img-one").attr("src","../spot-quotation/picture/cut_10.png");
		$("#img-two").attr("src","../spot-quotation/picture/cut_change_07.png");
		$("#img-three").attr("src","../spot-quotation/picture/cut_13.png");
	});
	$("#img-three").click(function(){
		$("#img-one").attr("src","../spot-quotation/picture/cut_10.png");
		$("#img-two").attr("src","../spot-quotation/picture/cut_07.png");
		$("#img-three").attr("src","../spot-quotation/picture/cut_change_13.png");
	});
});