var $SCRIPT_ROOT = "";
var userandpcname;
var Path;
function isnull(str) {

	
	for (var i = 0;i < str.length - 1; ++i) {
		if (str[i]!= ' ') {
			return false;
		}
	}
	return true;
		
}
document.onkeydown=function(e){
	e=e||event;
	//屏蔽向左的方向键
	if(e.keyCode==37){
	
		return false;
	}
	//屏蔽向上的方向键
	if(e.keyCode==38){

		return false;
	}
	//屏蔽向右的方向键
	if(e.keyCode==39){

		return false;
	}
	//屏蔽向下的方向键
	if(e.keyCode==40){

		return false;
	}
}


function html2Escape(sHtml) {
 return sHtml.replace(/[<>&"]/g,function(c){return {'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'}[c];});
}

function space2Nbsp(str) {
 return str.replace(/\s/ig, '&nbsp;');
}






function myFunction() {
		var linetext = $("#test").val();
		if(linetext[$("#test").val().length - 1] == '\n'){
			var fun = function(e) {
      	$.getJSON($SCRIPT_ROOT + '/_add_numbers', {
      	  text_line: $("#test").val()
      	  
      	}, function(data) {
      	});
      		return false;
      	};
      	fun();
      

      
      	var Text;
      	$(".cursor").eq(0).remove();
      	$(".linetext").eq(0).removeClass("linetext");
      	$.getJSON($SCRIPT_ROOT + '/cmd',{line: $("#test").val(),path:Path},function (data) {
				Path = data.path;
				Text = data.Text;
				if (data.isroot) {
					$(".active").eq(0).after($("<div class = \"line active\"><span class=\"bold fg-color-10 bg-color-256\">"+userandpcname+"</span>:<span class=\"bold fg-color-12 bg-color-256\">"+Path+"</span><span class=\"root\">#</span><span class=\"linetext\"></span><span class=\"cursor reverse-video\">&nbsp;</span></div>"));
				}else {
					$(".active").eq(0).after($("<div class = \"line active\"><span class=\"bold fg-color-10 bg-color-256\">"+userandpcname+"</span>:<span class=\"bold fg-color-12 bg-color-256\">"+Path+"</span><span class=\"root\">$</span><span class=\"linetext\"></span><span class=\"cursor reverse-video\">&nbsp;</span></div>"));
				}
				
				if (!isnull($("#test").val())&& Text != "" ) {

					$(".active").eq(0).after("<pre>" + Text + "</pre>");     
				}
     			$(".active").eq(0).removeClass("active");
				$("#test").val("");
			});
      

		
		
		
			return;
		}	
		document.getElementsByClassName("linetext")[0].innerHTML = space2Nbsp(html2Escape(linetext));	
}




$(document).ready(function(){ 
	$('#test').focus();
	$(function () { $('#test').blur(function () { var that = this;  setTimeout(function () { $(that).focus(); },100); }); });
	$('#test').width(0)
	$('#test').height(0)

      
	$.getJSON($SCRIPT_ROOT + '/user_and_pcname',{},function (data) {
    	userandpcname = data.result;
    	$(".bg-color-256").eq(0).text(data.result);
	});
	$.getJSON($SCRIPT_ROOT + '/cmd',{},function (data) {
		Path = "~";
		$(".bg-color-256").eq(1).text("~");
		if (data.isroot) {
			$(".root").eq(0).text("#")
		}else {
			$(".root").eq(0).text("$")
		}
	});
	

	

});




function f(){
	var temp = $(".reverse-video")
	function a(){
		temp.addClass("reverse-video")
	}
	function rem(){
		$(".reverse-video").removeClass("reverse-video");
		setTimeout(a,1000)
	}

	rem()
}

setInterval(f,1000);

