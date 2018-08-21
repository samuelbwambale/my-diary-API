document.getElementById("add_entry_form").addEventListener("submit", signup)
function signup(e){
    e.preventDefault();

    let title = document.getElementById('title').value
    let description = document.getElementById('description').value

    fetch('http://127.0.0.1:5000/api/v1/entries', {
      method:'POST',
      headers: {
        'Content-type':'application/json; charset=UTF-8',
        'authorization':'Bearer '+sessionStorage.getItem('token')
      },
      body:JSON.stringify({
        title:title, 
        description:description})
    })
    .then(function(response) {
        return response.json()
      })
    .then(function(data) {
        if(data.message === "Entry successfully created"){
        alert(data.message)
        window.location.href = "./entries.html"
        } else if(data.message === "Internal Server Error"){
          let res = "Session has expired, please login and try again"
          alert(res)
          window.location.href = "./login.html"        
      } else{
            document.getElementById('add_entry_response').innerHTML = "Error : " + data.message;
        }        
    })
    .catch(error => console.log(error))
  }
