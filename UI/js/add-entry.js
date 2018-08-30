document.getElementById("add_entry_form").addEventListener("submit", add_entry)
function add_entry(e){
    e.preventDefault();

    let title = document.getElementById('title').value
    let description = document.getElementById('description').value

    fetch(url + blueprint +'/entries', {
      method:'POST',
      headers: {
        'Content-type':'application/json; charset=UTF-8',
        'authorization':'Bearer '+ token
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
          sessionExpired()       
      } else{
            document.getElementById('add_entry_response').innerHTML = "Error : " + data.message;
        }        
    })
    .catch(error => console.log(error))
  }
