$('.button').each(function(){
	console.log('clicked1');
    var toggle_div_id = 'description_' + $(this).attr('id');
    $(this).click(function(){
        $('#' + toggle_div_id).toggle();
        console.log('clicked');
    });
});