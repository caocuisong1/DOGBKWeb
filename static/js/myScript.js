
var isNight = false;
function toggleTheme() {  
if (isNight)
{ document.body.classList.remove("night");
 document.body.classList.add("day");
isNight = false;  
}
else {
	document.body.classList.remove("day");    
	document.body.classList.add("night");    
	isNight = true;  }
}
document.addEventListener("DOMContentLoaded", 
	function(event) {
	var theme = localStorage.getItem("theme");  
		if (theme === "night") {    
			toggleTheme();  
		}   
		var btn = document.getElementById("btn-toggle-theme");  
		btn.addEventListener("click", function() {toggleTheme();  
		localStorage.setItem("theme", isNight ? "night" : "day"); 
		});});


		$(document).ready(function() {
			var carousel = $('.carousel-items');
			var carouselItemWidth = $('.carousel-item').outerWidth(true);
			var carouselScrollWidth = carouselItemWidth * $('.carousel-item').length;
			var currentScrollLeft = 0;
		  
			$('.carousel-container::before').click(function() {
			  currentScrollLeft -= carouselItemWidth;
			  carousel.animate({ scrollLeft: currentScrollLeft }, 500);
			});
		  
			$('.carousel-container::after').click(function() {
			  currentScrollLeft += carouselItemWidth;
			  carousel.animate({ scrollLeft: currentScrollLeft }, 500);
			});
		  });

