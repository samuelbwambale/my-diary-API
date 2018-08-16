function signup(e){
    e.preventDefault()

    let firstname = document.getElementById('first_name').value
    let lastname = document.getElementById('last_name').value
    let email = document.getElementById('email').value
    let password = document.getElementById('password').value

    fetch('http://127.0.0.1:5000/api/v1/auth/signup', {
      method:'POST',
      headers: {
        'Content-type':'application/json; charset=UTF-8'
      },
      body:JSON.stringify({
        first_name:firstname, 
        last_name:lastname,
        email:email,
        password:password})
    })
    .then(function(response) {
        return response.json()
      })
    .then(function(data) {
        if(data.message === "Account successfully created"){
            window.location.href = "./home.html"
        }
        else{
            document.getElementById('signup-response').innerHTML = data.message
        }
        //console.log(data)
        
    })
    .catch(error => console.log(error))
  }

function test_log_something(){
    console.log(12345)
}