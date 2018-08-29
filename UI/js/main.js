var base_url = "https://simple-app-my-diary.herokuapp.com"
//var base_url = "http://127.0.0.1:5000"
var blueprint = "/api/v1"

function sessionExpired() {
    let res = "Please login to proceed";
    alert(res);
    window.location.href = "./index.html";
}