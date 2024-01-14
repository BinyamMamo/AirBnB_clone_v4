document.addEventListener('DOMContentLoaded', function () {
	setInterval(() => {
		$.ajax({
			url: 'http://172.19.92.242:5001/api/v1/status/',
			method: 'GET',
			success: (response) => {
				if (response.status === 'OK') {
					$('#api_status').addClass('available');
				} else {
					$('#api_status').removeClass('available');
				}
			},
			error: (err) => {
				$('#api_status').removeClass('available');
			}
		})
	}, 1);
});
