$(function(){
	if ($("body").hasClass("blog-index")){
		$("#content").jaxy({"fromBottom": 500});		
	}
	
	if ($("body").hasClass("blog-single")){
		hljs.tabReplace = "  ";
		hljs.initHighlightingOnLoad();
	}
});