document.getElementById("login_form").addEventListener("submit", login)
function login(e){
    e.preventDefault();

    let email = document.getElementById('email').value
    let password = document.getElementById('password').value

    fetch(url + blueprint +'/auth/login', {
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
