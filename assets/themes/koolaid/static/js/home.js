$(window).load(function(){
	if ($("body").hasClass("home")){

		var slideReveal = function(container, num){
			$(container.find("img").get(num)).animate({"zIndex": num, "left":(num * 40 + 5)}, ((num + 2) * 150), "easeInOutExpo", function(){
				slideReveal(container, num + 1);
			});
		};

		$.get(siteVars("home") + "api/v1/portfolioimage/?format=json&limit=3", function(data){

			var entries = data.objects;

			var curCount = 0;
			var count = entries.length;

			var container = $("<div class='home-folio-image-container home-image-container' />");

			for (var i = entries.length - 1; i >= 0; i--){
				var src = entries[i].thumbnail;

				var img = $("<a href='#'><img src='" + src + "' /></a>"); //.css({"zIndex": (count - i)});

				img.appendTo(container);

				img.find("img").load(function(){

					curCount++;

					if (curCount == count){
						container.appendTo($("#home-folio"));
						var href = $("#home-folio h2 a").attr("href");
						container.find("a").attr("href", href);
						if ($.cookie("slidden")){
							$("#home-folio").addClass("slidden");
						}
						else{
							var t = setTimeout(function(){
							slideReveal(container, 0);
							}, 200);
							$.cookie("slidden", "1");
						}
					}
				});
			}
		});
	}
});
