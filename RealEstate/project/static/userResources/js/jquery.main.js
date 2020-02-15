$(document).ready(function() {

  "use strict"; 

  	jQuery("#contactForm").validator().on("submit", function (event) {

		"use strict";

		if (event.isDefaultPrevented()) {
			// handle the invalid form...
			formError();
			submitMSG(false, "Please Follow Error Messages and Complete as Required");
		} else {
			// everything looks good!
			event.preventDefault();
			submitForm();
		}
	});

	function submitForm(){
		
		"use strict";

		// Initiate Variables With Form Content
		var txtname = $("#txtname").val();
		var txtemail = $("#txtemail").val();
		var txtmessage = $("#txtmessage").val();

		$.ajax({
			type: "POST",
			url: "php/form-process.php",
			data: "txtname=" + txtname + "&txtemail=" + txtemail + "&txtmessage=" + txtmessage,
			success : function(text){
				if (text == "success"){
					formSuccess();
				} else {
					formError();
					submitMSG(false,text);
				}
			}
		});
	}

	function formSuccess(){
		
		"use strict";

		$("#contactForm")[0].reset();
		submitMSG(true, "Thank you for your submission :)")
	}

	function formError(){
		
		"use strict";

		$("#contactForm").removeClass().addClass('shake animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
			$(this).removeClass();
		});
	}

	function submitMSG(valid, msg){
		
		"use strict";

		if(valid){
			var msgClasses = "success form-message";
		} else {
			var msgClasses = "error form-message";
		}
		$("#msgSubmit").removeClass().addClass(msgClasses).text(msg);
	}

	initSlickCarousel();
	// slick init
	function initSlickCarousel() {
		jQuery('.slick-fade').slick({
			slidesToScroll: 1,
			rows: 0,
			prevArrow: '<a href="#" class="slick-prev"><i class="fi flaticon-back"></i><span class="sr-only">Previous</span></a>',
			nextArrow: '<a href="#" class="slick-next"><i class="fi flaticon-right-arrow"></i><span class="sr-only">Next</span></a>',
			fade: true,
			dots: false,
			arrows: true,
			adaptiveHeight: true,
			speed: 1500,
			responsive: [
				{
					breakpoint: 768,
					settings: {
						dots: true,
						arrows: false
					}
				}
			]
		});

		jQuery('.slick-fade2').slick({
			slidesToScroll: 1,
			rows: 0,
			prevArrow: '<a href="#" class="slick-prev"><i class="fi flaticon-arrows-1 readMoreIcn"></i><span class="sr-only">Previous</span></a>',
			nextArrow: '<a href="#" class="slick-next"><i class="fi flaticon-arrows readMoreIcn"></i><span class="sr-only">Next</span></a>',
			fade: true,
			dots: false,
			arrows: true,
			adaptiveHeight: true,
			speed: 1500,
			responsive: [
				{
					breakpoint: 768,
					settings: {
						dots: true,
						arrows: false
					}
				}
			]
		});

		jQuery('.slick-carousel').slick({
			slidesToScroll: 1,
			rows: 0,
			prevArrow: '<a href="#" class="slick-prev"><i class="fi flaticon-back"></i><span class="sr-only">Previous</span></a>',
			nextArrow: '<a href="#" class="slick-next"><i class="fi flaticon-right-arrow"></i><span class="sr-only">Next</span></a>',
			adaptiveHeight: true,
			speed: 800
		});

		$('.slick-thumbnailslider').slick({
		  slidesToShow: 1,
		  slidesToScroll: 1,
		  arrows: true,
		  prevArrow: '<a href="#" class="slick-prev"><i class="fi flaticon-back"></i><span class="sr-only">Previous</span></a>',
		  nextArrow: '<a href="#" class="slick-next"><i class="fi flaticon-right-arrow"></i><span class="sr-only">Next</span></a>',
		  fade: true,
		  asNavFor: '.slick-carouselnav'
		});
		$('.slick-carouselnav').slick({
		  slidesToShow: 6,
		  slidesToScroll: 1,
		  asNavFor: '.slick-thumbnailslider',
		  dots: false,	  
		  arrows: false,
		  centerMode: true,
		  focusOnSelect: true
		});

		jQuery('.four-slider').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 4,
			prevArrow: '<a href="#" class="slick-prev"><i class="fi flaticon-back"></i><span class="sr-only">Previous</span></a>',
			nextArrow: '<a href="#" class="slick-next"><i class="fi flaticon-right-arrow"></i><span class="sr-only">Next</span></a>',
			adaptiveHeight: true,
			speed: 800,

			responsive: [{
				breakpoint: 1199,
				settings: {
					slidesToShow: 3
				}
			}, {
				breakpoint: 991,
				settings: {
					slidesToShow: 2
				}
			}, {
				breakpoint: 639,
				settings: {
					slidesToShow: 1
				}
			}, {
				breakpoint: 575,
				settings: {
					slidesToShow: 1,
					dots: true,
					arrows: false
				}
			}]
		});

		jQuery('.profilesSlider2').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 4,
			prevArrow: '<a href="#" class="slick-prev"><i class="fi flaticon-arrows-1 readMoreIcn"></i><span class="sr-only">Previous</span></a>',
			nextArrow: '<a href="#" class="slick-next"><i class="fi flaticon-arrows readMoreIcn"></i><span class="sr-only">Next</span></a>',
			adaptiveHeight: true,
			speed: 800,

			responsive: [{
				breakpoint: 1199,
				settings: {
					slidesToShow: 3
				}
			}, {
				breakpoint: 991,
				settings: {
					slidesToShow: 2
				}
			}, {
				breakpoint: 639,
				settings: {
					slidesToShow: 1
				}
			}, {
				breakpoint: 575,
				settings: {
					slidesToShow: 1,
					dots: true,
					arrows: false
				}
			}]
		});

		jQuery('.three-slider').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 3,
			prevArrow: '<a href="#" class="slick-prev"><i class="fi flaticon-arrows-1 readMoreIcn"></i><span class="sr-only">Previous</span></a>',
			nextArrow: '<a href="#" class="slick-next"><i class="fi flaticon-arrows readMoreIcn"></i><span class="sr-only">Next</span></a>',
			adaptiveHeight: true,
			dots: false,
			arrows: true,
			speed: 800,

			responsive: [
			{
				breakpoint: 991,
				settings: {
					slidesToShow: 2
				}
			}, {
				breakpoint: 639,
				settings: {
					slidesToShow: 1
				}
			}, {
				breakpoint: 575,
				settings: {
					slidesToShow: 1,
					arrows: false
				}
			}]
		});
		jQuery('.banner-slider').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 3,
			prevArrow: '<a href="#" class="slick-prev"><i class="fi flaticon-arrows-1 readMoreIcn"></i><span class="sr-only">Previous</span></a>',
			nextArrow: '<a href="#" class="slick-next"><i class="fi flaticon-arrows readMoreIcn"></i><span class="sr-only">Next</span></a>',
			adaptiveHeight: true,
			dots: false,
			arrows: true,
			speed: 800,

			responsive: [
			{
				breakpoint: 991,
				settings: {
					slidesToShow: 2
				}
			}, {
				breakpoint: 639,
				settings: {
					slidesToShow: 1
				}
			}, {
				breakpoint: 575,
				settings: {
					slidesToShow: 1,
					arrows: false
				}
			}]
		});

		jQuery('.testimonial-carousel').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 1,
			arrows: false,
			dots: true,
			adaptiveHeight: true,
			speed: 800
		});

		jQuery('.testimonial-carousel2').slick({
			slidesToScroll: 1,
			rows: 0,
			prevArrow: '<a href="#" class="slick-prev"><i class="fi flaticon-arrows-1 readMoreIcn"></i><span class="sr-only">Previous</span></a>',
			nextArrow: '<a href="#" class="slick-next"><i class="fi flaticon-arrows readMoreIcn"></i><span class="sr-only">Next</span></a>',
			dots: false,
			arrows: true,
			adaptiveHeight: true,
			speed: 800,
		});

		jQuery('.news-posts-carousel').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 2,
			arrows: false,
			dots: false,
			adaptiveHeight: true,
			speed: 800,

			responsive: [{
				breakpoint: 767,
				settings: {
					slidesToShow: 1
				}
			}]
		});

		jQuery('.news-posts-carousel2').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 3,
			arrows: false,
			dots: true,
			adaptiveHeight: true,
			speed: 800,

			responsive: [{
				breakpoint: 767,
				settings: {
					slidesToShow: 1
				}
			}]
		});

		jQuery('.news-posts-carousel3').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 2,
			prevArrow: '<a href="#" class="slick-prev"><i class="fi flaticon-arrows-1 readMoreIcn"></i><span class="sr-only">Previous</span></a>',
			nextArrow: '<a href="#" class="slick-next"><i class="fi flaticon-arrows readMoreIcn"></i><span class="sr-only">Next</span></a>',
			dots: false,
			arrows: true,
			adaptiveHeight: true,
			speed: 800,

			responsive: [{
				breakpoint: 767,
				settings: {
					slidesToShow: 1
				}
			}]
		});

		jQuery('.news-posts-carousel4').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 2,
			arrows: false,
			dots: true,
			adaptiveHeight: true,
			speed: 800,

			responsive: [{
				breakpoint: 767,
				settings: {
					slidesToShow: 1
				}
			}]
		});

		jQuery('.logos-slider').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 5,
			arrows: false,
			dots: false,
			adaptiveHeight: true,
			speed: 800,

			responsive: [{
				breakpoint: 991,
				settings: {
					slidesToShow: 3
				}
			},{
				breakpoint: 575,
				settings: {
					slidesToShow: 2
				}
			}]
		});

		jQuery('.bannerImageSlideshow').slick({
			slidesToScroll: 1,
			rows: 0,
			arrows: false,
			dots: true,
			dotsClass: 'switcherDotsVertical',
			fade: true,
			autoplay: true,
			autoplaySpeed: 10000,
			speed: 1500
		});
	}

	initCustomFormSlider();

	// custom collapse init
	function initCustomFormSlider() {

		"use strict"; 

		$(".span2").slider();
		$(".span2").on("slide", function(slideEvt) {
			var valueS = slideEvt.value;
			$(".startValue").text(valueS[0]);
			$(".endValue").text(valueS[1]);
		});
	}

	initCustomCollapse();

	// custom collapse init
	function initCustomCollapse() {

		"use strict";

		jQuery('body').bind('click', function(e) {
			if(jQuery(e.target).closest('.searchFormcollapse').length == 0) {
					// click happened outside of .navbar, so hide
					var opened = jQuery('.searchFormcollapse').hasClass('collapse in');
					if ( opened === true ) {
							jQuery('.searchFormcollapse').collapse('hide');
							jQuery('body').removeClass('searchIsActive');
					}
				}
		});

		jQuery('body').bind('click', function(e) {
			if(jQuery(e.target).closest('.navbar-collapse').length == 0) {
					// click happened outside of .navbar, so hide
					var opened = jQuery('.navbar-collapse').hasClass('collapse in');
					if ( opened === true ) {
							jQuery('.navbar-collapse').collapse('hide');
							jQuery('body').removeClass('menuIsActive');
					}
				}
		});

		jQuery('.navbar-toggle').on('click', function(){

			if(jQuery('body').hasClass('menuIsActive')){
				jQuery('body').removeClass('menuIsActive');
			} else{
				jQuery('body').addClass('menuIsActive');
			}
		});

		jQuery('.headerSearchForm .activeClassOnBody').on('click', function(){

			if(jQuery('body').hasClass('searchIsActive')){
				jQuery('body').removeClass('searchIsActive');
			} else{
				jQuery('body').addClass('searchIsActive');
			}
		});
	}

	initHoverClass();

	// add classes on hover/touch
	function initHoverClass() {

		"use strict"; 

		jQuery('.hasOver').touchHover();
	}

	initAnchors();

	// initialize smooth anchor links
	function initAnchors() {

		"use strict"; 

		new SmoothScroll({
			anchorLinks: 'a.smooth[href^="#"]:not([href="#"])',
			extraOffset: 0,
			wheelBehavior: 'none'
		});

		new SmoothScroll({
			anchorLinks: '.anchorNavigationList a[href^="#"]:not([href="#"])',
			extraOffset: function() {
				var totalHeight = 0;
				jQuery('.anchorNav').each(function() {
					var $box = jQuery(this);
					var stickyInstance = $box.data('StickyScrollBlock');
					if (stickyInstance) {
						stickyInstance.stickyFlag = false;
						stickyInstance.stickyOn();
						totalHeight += $box.outerHeight();
						stickyInstance.onResize();
					} else {
						totalHeight += $box.css('position') === 'fixed' ? $box.outerHeight() : 0;
					}
				});
				return totalHeight += 25;
			},
			activeClasses: 'parent',
			anchorActiveClass: 'active',
			wheelBehavior: 'none'
		});
	}

	initMobileNavigation();

	function initMobileNavigation() {

		"use strict";

		jQuery('#pageNav').mobileNavigation({
			slider:'.pageMainNav',
			nextLevel:'> .frame-wrap > .frame',
			title: '#menu-title'
		});
	}

	initTouchNav();

	// handle dropdowns on mobile devices
	function initTouchNav() {

		"use strict";

		jQuery('.pageMainNav').each(function() {
			new TouchNav({
				navBlock: this,
				menuDrop: '.frame-wrap'
			});
		});
	}

	initTabs();	
	// content tabs init
	function initTabs() {

		"use strict";
		
		jQuery('.tabset').tabset({
			tabLinks: 'a',
			addToParent: true,
			defaultTab: true
		});
		jQuery('.popupTabsetList').tabset({
			tabLinks: 'a',
			addToParent: true,
			defaultTab: true
		});
	}

	initStickyScrollBlock();

	// initialize fixed blocks on scroll
	function initStickyScrollBlock() {
		jQuery('.anchorNav').stickyScrollBlock({
			setBoxHeight: true,
			activeClass: 'fixed-position',
			container: '#main',
			positionType: 'fixed',
			extraTop: function() {
				var totalHeight = 0;
				jQuery('0').each(function() {
					totalHeight += jQuery(this).outerHeight();
				});
				return totalHeight;
			}
		});
	}
	
	initFancybox();
	// lightbox init
	function initFancybox() {
		jQuery('a.lightbox, [data-fancybox]').fancybox({
			parentEl: 'body',
			margin: [50, 0]
		});
	}


});



jQuery(window).on('load', function() {

	initIsoTop();

	// IsoTop init
	function initIsoTop() {
		"use strict";

		var isotopeHolder = jQuery('.isoContentHolder'),
			win = jQuery(window);
		jQuery('.isoFiltersList a').on( "click", function(e){
			e.preventDefault();
			
			jQuery('.isoFiltersList li').removeClass('active');
			jQuery(this).parent('li').addClass('active');
			var selector = jQuery(this).attr('data-filter');
			isotopeHolder.isotope({ filter: selector });
		});
		jQuery('.isoContentHolder').isotope({
			itemSelector: '.isoCol',
			transitionDuration: '0.6s',
			masonry: {
				columnWidth: '.isoCol'
			}
		});
	}

	initPreLoader();
	// PreLoader init
	function initPreLoader() {
	    "use strict";

	    jQuery('#loader').delay(1000).fadeOut();
	}

});