$(document).ready(function(){
	$("#btn_login").click(function(){
		$.post('/api/admin/login',{
			name : $("#name").val(),
			password : $("#password").val(),
		},function(results){
			if(results.statecode == 200){
				location = results.url;
			}
			else{
				alert("输入有误!");
			}
		});
	});
});