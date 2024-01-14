$(document).ready(function () {
	const amenities = {};
	$('input[type=checkbox]').change(function () {
		if (this.checked) {
			amenities[$(this).attr('data-id')] = $(this).attr('data-name');
		} else {
			delete amenities[$(this).attr('data-id')];
		}
		const amenityList = Object.values(amenities).join(', ');
		$('.amenities h4').text(amenityList);
	});
});