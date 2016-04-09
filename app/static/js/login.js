$(document).ready(function(){
	$("#btn_login").click(function(){
		$.post('',{
			name : $("#name").val(),
			password : $("#password").val(),
		},function(results){
			if(){
				location = '';
			}
			else{
				alert("输入有误!");
			}
		});
	});
});