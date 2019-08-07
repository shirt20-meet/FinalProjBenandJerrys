function myFunction() {
	var input, filter, ul, li, a, i, txtValue;
	input = $('#searchInput'):
	filter = input.val().toUpperCase();
	ul = $("#storeList");
	li = $(".store_info").each(function(){
		txtValue = $(this).text().toUpperCase();
		if (txtValue.includes(filter)) {
			$(this).show();
		}
		else {
			$(this).hide();
		}
	});
}

$('#searchInput').on("keyup", function(){
	myFunction();
});
