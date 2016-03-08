$(document).ready(function(){
	$(".meishi-box").mouseover(function(){
		$(this).css("color","E4A15D");
	});
	$(".meishi-box").mouseout(function(){
		$(this).css("color","black");
	});
	$(".meishi-quotation").click(function(){
		$(this).css("border-bottom","none");
		$(this).css("background-color","white");
		$(".meishi-know").css("border-bottom","1px solid");
		$(".meishi-storage").css("border-bottom","1px solid");
		$(".meishi-index").css("border-bottom","1px solid");
		$(".meishi-know").css("background-color","rgb(216,216,216)");
		$(".meishi-storage").css("background-color","rgb(216,216,216)");
		$(".meishi-index").css("background-color","rgb(216,216,216)");
		$(".information-box-one").css("display","block");
		$(".information-box-two").css("display","none");
		$(".information-box-three").css("display","none");
		$(".information-box-four").css("display","none");
	});
	$(".meishi-know").click(function(){
		$(this).css("border-bottom","none");
		$(this).css("background-color","white");
		$(".meishi-quotation").css("border-bottom","1px solid");
		$(".meishi-storage").css("border-bottom","1px solid");
		$(".meishi-index").css("border-bottom","1px solid");
		$(".meishi-quotation").css("background-color","rgb(216,216,216)");
		$(".meishi-storage").css("background-color","rgb(216,216,216)");
		$(".meishi-index").css("background-color","rgb(216,216,216)");
		$(".information-box-one").css("display","none");
		$(".information-box-two").css("display","block");
		$(".information-box-three").css("display","none");
		$(".information-box-four").css("display","none");
	});
	$(".meishi-storage").click(function(){
		$(this).css("border-bottom","none");
		$(this).css("background-color","white");
		$(".meishi-know").css("border-bottom","1px solid");
		$(".meishi-quotation").css("border-bottom","1px solid");
		$(".meishi-index").css("border-bottom","1px solid");
		$(".meishi-know").css("background-color","rgb(216,216,216)");
		$(".meishi-quotation").css("background-color","rgb(216,216,216)");
		$(".meishi-index").css("background-color","rgb(216,216,216)");
		$(".information-box-one").css("display","none");
		$(".information-box-two").css("display","none");
		$(".information-box-three").css("display","block");
		$(".information-box-four").css("display","none");
	});
	$(".meishi-index").click(function(){
		$(this).css("border-bottom","none");
		$(this).css("background-color","white");
		$(".meishi-know").css("border-bottom","1px solid");
		$(".meishi-storage").css("border-bottom","1px solid");
		$(".meishi-quotation").css("border-bottom","1px solid");
		$(".meishi-know").css("background-color","rgb(216,216,216)");
		$(".meishi-storage").css("background-color","rgb(216,216,216)");
		$(".meishi-quotation").css("background-color","rgb(216,216,216)");
		$(".information-box-one").css("display","none");
		$(".information-box-two").css("display","none");
		$(".information-box-three").css("display","none");
		$(".information-box-four").css("display","block");
	});

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