const base_url = "https://simple-app-my-diary.herokuapp.com"
//const base_url = "http://127.0.0.1:5000"
const blueprint = "/api/v1"
const token = sessionStorage.getItem('token')


function sessionExpired() {
    let res = "Please login to proceed"
    alert(res)
    window.location.href = "index.html"
}

function checkToken() {
        if (token == null) {
        sessionExpired()
    }
}


function logout() {
	sessionStorage.removeItem('token');
	window.location.href = './index.html';
}
