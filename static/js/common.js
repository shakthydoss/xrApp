$(".mobile-menu-btn").click(function(){
	console.log($(".side-menu-wrapper").css("display"));
	if($(".side-menu-wrapper").css("display") == "none"){
	    console.log("setting block")
		$(".side-menu-wrapper").css("display", "block")
	}else{
		$(".side-menu-wrapper").css("display", "none")
	}
});


// go to app page.
$(".goto-app-page").click(function(){
	console.log("I am here")
	window.location.href = "/";
});

// go to Exit page.
$(".goto-exit-page").click(function(){
	console.log("I am here in exit")
	window.location.href = "/auth/logout/";
});


