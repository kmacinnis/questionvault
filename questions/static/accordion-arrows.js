$('.collapse').on('shown.bs.collapse', function(){
$(this).parent().find(".glyphicon-menu-right").removeClass("glyphicon-menu-right").addClass("glyphicon-menu-down");
}).on('hidden.bs.collapse', function(){
$(this).parent().find(".glyphicon-menu-down").removeClass("glyphicon-menu-down").addClass("glyphicon-menu-right");
});
