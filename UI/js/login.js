document.getElementById("login_form").addEventListener("submit", login)
function login(e){
    e.preventDefault();

    let email = document.getElementById('email').value
    let password = document.getElementById('password').value

    fetch('http://127.0.0.1:5000/api/v1/auth/login', {
      method:'POST',
      headers: {
        'Content-type':'application/json; charset=UTF-8'
      },
      body:JSON.stringify({
        email:email,
        password:password})
    })
    .then(function(response) {
        return response.json()
      })
    .then(function(data) {
        if(data.message === "Successfully logged in"){
            sessionStorage.setItem('token', data.token);
            window.location.href = "./home.html"
        } else{
            document.getElementById('login_response').innerHTML = "Error : " + data.message
        }        
    })
    .catch(error => console.log(error))
}

function logout() {
	sessionStorage.removeItem('token');
	window.location.href = './index.html';
}
