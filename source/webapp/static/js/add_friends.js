function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequest(url, method = 'GET', data = undefined) {
    let opts = {method, headers: {}};

    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }

    let response = await fetch(url, opts);

    if (response.ok) {  // нормальный ответ
        return response;
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function add_friends(event) {
    event.preventDefault();
    console.log(event);
    let add_button_friend = event.target.parentElement;
    console.log(add_button_friend );
    let url = add_button_friend .href;
    console.log(url);

    try {
        let response = await makeRequest(url, 'POST');
        let data = await response.text();
        console.log(data);
    }
    catch (error) {
        console.log(error);
    }


}
window.addEventListener('load', function() {
    const buttons = document.getElementsByClassName('badge badge-dark')
    for (let button of buttons) {button.onclick = add_friends}

});