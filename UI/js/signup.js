document.getElementById("register_form").addEventListener("submit", signup)
function signup(e){
    e.preventDefault()
    //prevents from submitting to a file

    let firstname = document.getElementById('first_name').value
    let lastname = document.getElementById('last_name').value
    let email = document.getElementById('email').value
    let password = document.getElementById('password').value

    fetch(url + blueprint +'/auth/signup', {
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
        alert(data.message)
        window.location.href = "./index.html"
        } else{
            document.getElementById('signup_response').innerHTML = "Error : " + data.message;
        }        
    })
    .catch(error => console.log(error))
  }
