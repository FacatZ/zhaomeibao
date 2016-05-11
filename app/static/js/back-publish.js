$(document).ready(function(){
	// var infor_ctgid = "0";
	// var paytype = "0";
	// var pdtype = "0";
	// var onsale = "0";
	$("#infor_ctgid0").click(function(){
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
	});
	$("#infor_ctgid1").click(function(){
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
	});

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
		if(arr.eq(14).val()<arr.eq(13).val()){
			alert('数据错误:颗度极大值不能小于极小值');
		}else{
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
				if(result.statecode == 200 ){
					alert("提交成功！");
					window.location.href = result.url;
				} else {
					alert("提交失败！错误代码："+result.statecode);
				}
			});
		}
	});

	var is_checked = $("#infor_ctgid1").checked;

	var arr = $('.value_checked');
	arr.eq(0).change(function(){
		if(0>arr.eq(0).val()||arr.eq(0).val()>60){
			alert('数据错误:全水份(Mt) 0.00% ~ 60.00%');
			arr.eq(0).val('0');
		}
	});
	arr.eq(1).change(function(){
		if(0>arr.eq(1).val()||arr.eq(1).val()>60){
			alert('数据错误:收到基(Aar) 0.00% ~ 60.00%');
			arr.eq(1).val('0');
		}
	});
	arr.eq(2).change(function(){
		if(0>arr.eq(2).val()||arr.eq(2).val()>10){
			alert('数据错误:收到基(Star) 0.00% ~ 10.00%');
			arr.eq(2).val('0');
		}
	});
	arr.eq(3).change(function(){
		if(0>arr.eq(3).val()||arr.eq(3).val()>20){
			alert('数据错误:内水(Mad) 0.00% ~ 20.00%');
			arr.eq(3).val('0');
		}
	});
	arr.eq(4).change(function(){
		if(0>arr.eq(4).val()||arr.eq(4).val()>60){
			alert('数据错误:空干基(Aad) 0.00% ~ 60.00%');
			arr.eq(4).val('0');
		}
	});
	arr.eq(5).change(function(){
		if(0>arr.eq(5).val()||arr.eq(5).val()>10){
			alert('数据错误:空干基(Stad) 0.00% ~ 10.00%');
			arr.eq(5).val('0');
		}
	});
	arr.eq(6).change(function(){
		if(0>arr.eq(6).val()||arr.eq(6).val()>60){
			alert('数据错误:收到基(Var) 0.00% ~ 60.00%');
			arr.eq(6).val('0');
		}
	});
	arr.eq(7).change(function(){
		if(0>arr.eq(7).val()||arr.eq(7).val()>100){
			alert('数据错误:收到基(Fcar) 0.00% ~ 100.00%');
			arr.eq(7).val('0');
		}
	});
	arr.eq(8).change(function(){
		if(2000>arr.eq(8).val()||arr.eq(8).val()>9000){
			alert('数据错误:收到基(Qnetar) 2000 ~ 9000');
			arr.eq(8).val('2000');
		}
	});
	arr.eq(9).change(function(){
		if(0>arr.eq(9).val()||arr.eq(9).val()>60){
			alert('数据错误:空干基(Vad) 0.00% ~ 60.00%');
			arr.eq(9).val('0');
		}
	});
	arr.eq(10).change(function(){
		if(0>arr.eq(10).val()||arr.eq(10).val()>100){
			alert('数据错误:空干基(Fcad) 0.00% ~ 100.00%');
			arr.eq(10).val('0');
		}
	});
	arr.eq(11).change(function(){
		if(0>arr.eq(11).val()||arr.eq(11).val()>9000){
			alert('数据错误:空干基(Qnetad) 0 ~ 9000');
			arr.eq(11).val('0');
		}
	});
	arr.eq(12).change(function(){
		if(0>arr.eq(12).val()||arr.eq(12).val()>60){
			alert('数据错误:干燥无灰基(Vdaf) 0.00% ~ 60.00%');
			arr.eq(12).val('0');
		}
	});
	arr.eq(13).change(function(){
		if(0>arr.eq(13).val()||arr.eq(13).val()>9000){
			alert('数据错误:颗度极小值 0 ~ 9000');
			arr.eq(13).val('0');
		}
	});
	arr.eq(14).change(function(){
		if(0>arr.eq(14).val()||arr.eq(14).val()>9000){
			alert('数据错误:颗度极大值 0 ~ 9000');
			arr.eq(14).val('0');
		}
	});
	arr.eq(15).change(function(){
		if(0>arr.eq(15).val()||arr.eq(15).val()>100){
			alert('数据错误:颗度极大值 0.00% ~ 100.00%');
			arr.eq(15).val('0');
		}
	});
});