$(document).ready(function(){
	$(".stockButton").click(function(){
		var $this = $(this);
		var url = $this.attr("url");
		if (url != undefined){
			window.location.href = url;
		}
	});
});