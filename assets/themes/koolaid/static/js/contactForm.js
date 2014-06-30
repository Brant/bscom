$(function(){

	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	var loader = $("<img src='" + siteVars("img") + "loading.gif' alt='loading' class='contact-loading' />").hide().appendTo("body");

	var handleForm = function(form){
		formWrap.html(form);


		var submitUrl = form.attr("action");

		form.on("submit", function(event){
			event.preventDefault();

			formWrap.height(formWrap.height());

			form.hide();
			loader.appendTo(formWrap).fadeIn();

			$.ajaxSetup({
				crossDomain: false, // obviates need for sameOrigin test
				beforeSend: function(xhr, settings) {
					if (!csrfSafeMethod(settings.type)) {
						xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
					}
				}
			});

			$.ajax({
				url: submitUrl,
				type: "POST",
				data: form.serialize(),
				dataType: "json"
			}).done(function(response){
				if (typeof response == "string"){
					response = $.parseJSON(data);
				}
				handleResponse(response);
			});
		});
	};

	var handleResponse = function(response){

		if (typeof response == "string"){
			response = $.parseJSON(data);
		}

		loader.fadeOut(function(){
			formWrap.height("");
			if (response.form){
				handleForm($(response.form));
			}
			else{
				if (response.success){
					formWrap.html("<p>Thanks! I'll be in touch soon.</p>");
				}
				else{
					formWrap.html("<p>Something has gone wrong, please try in a few minutes.</p>");
				}
			}
		});
	};

	var formWrap = $("#contactFormWrap");
	var endpoint = formWrap.data("url");

	$.ajax({
		url: endpoint,
		type: "GET",
		dataType: "json"
	}).done(function(response){
		handleResponse(response);
	});

});
