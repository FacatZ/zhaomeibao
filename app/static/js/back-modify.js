$(document).ready(function(){
	// var infor_ctgid = "0";
	// var paytype = "0";
	// var pdtype = "0";
	// var onsale = "0";
	if($("#infor_ctgid").html() == "0"){
		$(".txt_type").html("支付类型");
		$("#paytype0").css("display","block");
		$("#paytype1").css("display","block");
		$("#paytype2").css("display","block");
		$(".txt_paytype").css("display","block");
		$("#pdtype0").css("display","none");
		$("#pdtype1").css("display","none");
		$(".txt_pdtype").css("display","none");
		$(".if_onsale").css("display","none");
		$("#if_onsale").html("");
		$("#if_count").html("数量");
		$("#count").css("display","block");
		$("#stock").css("display","none");
		$("#infor_ctgid").text("0");
	} else {
		$(".txt_type").html("供货类型");
		$("#paytype0").css("display","none");
		$("#paytype1").css("display","none");
		$("#paytype2").css("display","none");
		$(".txt_paytype").css("display","none");
		$("#pdtype0").css("display","block");
		$("#pdtype1").css("display","block");
		$(".txt_pdtype").css("display","block");
		$(".if_onsale").css("display","block");
		$("#if_onsale").html("特价");
		$("#if_count").html("库存");
		$("#count").css("display","none");
		$("#stock").css("display","block");
		$("#infor_ctgid").text("1");
	}

	$("#paytype0").click(function(){
		$("#paytype").text("0");
	});
	$("#paytype1").click(function(){
		$("#paytype").text("1");
	});
	$("#paytype2").click(function(){
		$("#paytype").text("2");
	});
	$("#pdtype0").click(function(){
		$("#pdtype").text("0");
	});
	$("#pdtype1").click(function(){
		$("#pdtype").text("1");
	});
	$("#onsale0").click(function(){
		$("#onsale").text("0");
	});
	$("#onsale1").click(function(){
		$("#onsale").text("1");
	});

	$("#btn-publish").click(function(){
		$.post('/api/admin/publish/product',{
			'typeid' : $("#infor_ctgid").text(),
			'paytype' : $("#paytype").text(),
			'pdtype' : $("#pdtype").text(),
			'onsale' : $("#onsale").text(),
			ctgid : $("#ctgid").val(),
			indid : $("#indid").val(),
			stock : $("#stock").val(),
			vldterm : $("#vldterm").val(),
			dppid : $("#dppid").val(),
			dpcid : $("#dpcid").val(),
			pdpid : $("#pdpid").val(),
			pdcid : $("#pdcid").val(),
			dpaddr : $("#dpaddr").val(),
			prtype : $("#prtype").val(),
			prpid : $("#prpid").val(),
			prcid : $("#prcid").val(),
			coal : $("#coal").val(),
			count : $("#count").val(),
			price : $("#price").val(),
			remark : $("#remark").val(),
			mt : $("#mt").val(),
			aar : $("#aar").val(),
			star : $("#star").val(),
			mad : $("#mad").val(),
			aad : $("#aad").val(),
			stad : $("#stad").val(),
			varr : $("#varr").val(),
			fcar : $("#fcar").val(),
			qnetar : $("#qnetar").val(),
			vad : $("#vad").val(),
			fcad : $("#fcad").val(),
			qnetad : $("#qnetad").val(),
			vdaf : $("#vdaf").val(),
			szuplm : $("#szuplm").val(),
			szlowlm : $("#szlowlm").val(),
			szppt : $("#szppt").val(),
		},function(result){
			console.log(result);
		});
	});

	$(".change_p1").click(function(){
		$(".span_add1").css("display","none");
		$(".change_p1").css("display","none");
		$("#hide1").css("display","block");
	});

});