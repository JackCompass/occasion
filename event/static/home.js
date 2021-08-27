async function togglePreference(x) {
	data = JSON.stringify({
		id: x.id,
	})
	var csrftoken = getCookie('csrftoken');
	if (x.style.color == 'red') {
		x.style.color = 'white';
		fetch("/postdata", {
			method: 'DELETE',
			body: data,
			headers: { 'Accept': 'application/json, text/plain, */*',
				'Content-Type': 'application/json',
				"X-CSRFToken": csrftoken },
		})
	}
	else {
		x.style.color = 'red';
		fetch("/postdata", {
			method: 'POST',
			body: data,
			headers: { 'Accept': 'application/json, text/plain, */*',
				'Content-Type': 'application/json',
				"X-CSRFToken": csrftoken },
		})
	}
	/*
	TESTING THE GET REQEUST
	const response = await fetch('/getdata');
	console.log(response);
	const data = await response.json();
	console.log(data);
	*/
}

function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim();
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}