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
			alert($('#pdpid').val() + ' - ' + $('#pdcid').val() + ' - ' +  $('#loc_town').val()) 
		})
		$('#btntext').click(function(){
			alert($('#pdpid').select2('data').text + ' - ' + $('#pdcid').select2('data').text + ' - ' +  $('#loc_town').select2('data').text) 
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

function showLocation(province , city , town) {
	
	var loc	= new Location();
	var title	= ['省份' , '地级市' , '市、县、区'];
	$.each(title , function(k , v) {
		title[k]	= '<option value="">'+v+'</option>';
	})
	
	$('#dppid').append(title[0]);
	$('#dpcid').append(title[1]);
	$('#loc_town').append(title[2]);
	
	$("#dppid,#dpcid,#loc_town").select2()
	$('#dppid').change(function() {
		$('#dpcid').empty();
		$('#dpcid').append(title[1]);
		loc.fillOption('dpcid' , '0,'+$('#dppid').val());
		$('#dpcid').change()
	})
	
	$('#dpcid').change(function() {
		$('#loc_town').empty();
		$('#loc_town').append(title[2]);
		loc.fillOption('loc_town' , '0,' + $('#dppid').val() + ',' + $('#dpcid').val());
	})
	
	$('#loc_town').change(function() {
		$('input[name=location_id]').val($(this).val());
	})
	
	if (province) {
		loc.fillOption('dppid' , '0' , province);
		
		if (city) {
			loc.fillOption('dpcid' , '0,'+province , city);
			
			if (town) {
				loc.fillOption('loc_town' , '0,'+province+','+city , town);
			}
		}
		
	} else {
		loc.fillOption('dppid' , '0');
	}
		
}

$(function(){
		showLocation();
		$('#btnval').click(function(){
			alert($('#dppid').val() + ' - ' + $('#dpcid').val() + ' - ' +  $('#loc_town').val()) 
		})
		$('#btntext').click(function(){
			alert($('#dppid').select2('data').text + ' - ' + $('#dpcid').select2('data').text + ' - ' +  $('#loc_town').select2('data').text) 
		})
	})