function showLocation1(province , city , town) {
	
	var loc	= new Location();
	var title	= ['省份' , '地级市' , '市、县、区'];
	$.each(title , function(k , v) {
		title[k]	= '<option value="">'+v+'</option>';
	})
	
	$('#pdpid').append(title[0]);
	$('#pdcid').append(title[1]);
	$('#loc_town').append(title[2]);
	
	$("#pdpid,#pdcid,#loc_town").select2()
	$('#pdpid').change(function() {
		$('#pdcid').empty();
		$('#pdcid').append(title[1]);
		loc.fillOption('pdcid' , '0,'+$('#pdpid').val());
		$('#pdcid').change()
	})
	
	$('#pdcid').change(function() {
		$('#loc_town').empty();
		$('#loc_town').append(title[2]);
		loc.fillOption('loc_town' , '0,' + $('#pdpid').val() + ',' + $('#pdcid').val());
	})
	
	$('#loc_town').change(function() {
		$('input[name=location_id]').val($(this).val());
	})
	
	if (province) {
		loc.fillOption('pdpid' , '0' , province);
		
		if (city) {
			loc.fillOption('pdcid' , '0,'+province , city);
			
			if (town) {
				loc.fillOption('loc_town' , '0,'+province+','+city , town);
			}
		}
		
	} else {
		loc.fillOption('pdpid' , '0');
	}
		
}

$(function(){
		showLocation1();
		$('#btnval').click(function(){
			alert($('#pdpid').val() + ' - ' + $('#ppcid').val() + ' - ' +  $('#loc_town').val()) 
		})
		$('#btntext').click(function(){
			alert($('#pdpid').select2('data').text + ' - ' + $('#ppcid').select2('data').text + ' - ' +  $('#loc_town').select2('data').text) 
		})
	})

function showLocation2(province , city , town) {
	
	var loc	= new Location();
	var title	= ['省份' , '地级市' , '市、县、区'];
	$.each(title , function(k , v) {
		title[k]	= '<option value="">'+v+'</option>';
	})
	
	$('#prpid').append(title[0]);
	$('#prcid').append(title[1]);
	$('#loc_town').append(title[2]);
	
	$("#prpid,#prcid,#loc_town").select2()
	$('#prpid').change(function() {
		$('#prcid').empty();
		$('#prcid').append(title[1]);
		loc.fillOption('prcid' , '0,'+$('#prpid').val());
		$('#prcid').change()
	})
	
	$('#prcid').change(function() {
		$('#loc_town').empty();
		$('#loc_town').append(title[2]);
		loc.fillOption('loc_town' , '0,' + $('#prpid').val() + ',' + $('#prcid').val());
	})
	
	$('#loc_town').change(function() {
		$('input[name=location_id]').val($(this).val());
	})
	
	if (province) {
		loc.fillOption('prpid' , '0' , province);
		
		if (city) {
			loc.fillOption('prcid' , '0,'+province , city);
			
			if (town) {
				loc.fillOption('loc_town' , '0,'+province+','+city , town);
			}
		}
		
	} else {
		loc.fillOption('prpid' , '0');
	}
		
}

$(function(){
		showLocation2();
		$('#btnval').click(function(){
			alert($('#prpid').val() + ' - ' + $('#prcid').val() + ' - ' +  $('#loc_town').val()) 
		})
		$('#btntext').click(function(){
			alert($('#prpid').select2('data').text + ' - ' + $('#prcid').select2('data').text + ' - ' +  $('#loc_town').select2('data').text) 
		})
	})

function showLocation3(province , city , town) {
	
	var loc	= new Location();
	var title	= ['省份' , '地级市' , '市、县、区'];
	$.each(title , function(k , v) {
		title[k]	= '<option value="">'+v+'</option>';
	})
	
	$('#pppid').append(title[0]);
	$('#ppcid').append(title[1]);
	$('#loc_town').append(title[2]);
	
	$("#pppid,#ppcid,#loc_town").select2()
	$('#pppid').change(function() {
		$('#ppcid').empty();
		$('#ppcid').append(title[1]);
		loc.fillOption('ppcid' , '0,'+$('#pppid').val());
		$('#ppcid').change()
	})
	
	$('#ppcid').change(function() {
		$('#loc_town').empty();
		$('#loc_town').append(title[2]);
		loc.fillOption('loc_town' , '0,' + $('#pppid').val() + ',' + $('#ppcid').val());
	})
	
	$('#loc_town').change(function() {
		$('input[name=location_id]').val($(this).val());
	})
	
	if (province) {
		loc.fillOption('pppid' , '0' , province);
		
		if (city) {
			loc.fillOption('ppcid' , '0,'+province , city);
			
			if (town) {
				loc.fillOption('loc_town' , '0,'+province+','+city , town);
			}
		}
		
	} else {
		loc.fillOption('pppid' , '0');
	}
		
}

$(function(){
		showLocation3();
		$('#btnval').click(function(){
			alert($('#pppid').val() + ' - ' + $('#ppcid').val() + ' - ' +  $('#loc_town').val()) 
		})
		$('#btntext').click(function(){
			alert($('#pppid').select2('data').text + ' - ' + $('#ppcid').select2('data').text + ' - ' +  $('#loc_town').select2('data').text) 
		})
	})