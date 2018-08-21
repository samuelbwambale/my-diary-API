//document.getElementById("get_entries_button").addEventListener("submit", test_log_something)
function get_entries(){

    fetch('http://127.0.0.1:5000/api/v1/entries', {
      method:'GET',
      headers: {
        'Content-type':'application/json; charset=UTF-8',
        'Authorization':'Bearer '+sessionStorage.getItem('token')
      }
    })
    .then(response => response.json())
    .then(function(data) {
        if(data.status === "success"){
        alert(data.status)
        let entries_output = '<h4 style = "color: rgb(73, 35, 35);" class="display-4 mb-4">My Entries</h4>'
        data.entries.forEach(entry => {
            entries_output += `
            <div class="entry-div">
                <h2><a href="#" onclick="get_an_entry(${entry.entry_id})">Title: ${entry.title}</a></h2>
                <p>ID: ${entry.entry_id}</p>
                <p>Description: ${entry.description}</p>
            <div>
            `
        })
        document.getElementById('entries_output').innerHTML = entries_output
        }
        else if(data.message === "Internal Server Error"){
            let res = "Session has expired, please login and try again"
            alert(res)
            window.location.href = "./login.html"

        } else {
            document.getElementById('view_entries_response').innerHTML = data.message
        }      
    })
    .catch(error => console.log(error))
  }


function get_an_entry(id){

    fetch('http://127.0.0.1:5000/api/v1/entries/'+id, {
      method:'GET',
      headers: {
        'Content-type':'application/json; charset=UTF-8',
        'Authorization':'Bearer '+sessionStorage.getItem('token')
      }
    })
    .then(response => {
        console.log(response)
        response.json().then(function(data) {
            console.log(data)
            alert(data.status)
            if(data.status === "success"){
                let entries_output = '<h3 style = "color: rgb(73, 35, 35);" class="display-4 mb-4">Single Entry</h3>'
                
                entries_output += `
                <div class="entry-div">
                    <h2>Title: ${data.entry.title}</h2>
                    <p>ID: ${data.entry.entry_id}</p>
                    <p>Description: ${data.entry.description}</p>
                <div>
                ` 
                document.getElementById('entries_output').innerHTML = entries_output
            }
            else if(data.message === "Internal Server Error"){
                let res = "Session has expired, please login and try again"
                alert(res)
                window.location.href = "./login.html"        
            } else {
                    document.getElementById('view_entries_response').innerHTML = data.message
                }
        })
    })
    .catch(error => console.log(error))
  }




function test_log_something(){
    console.log(12345)
    }
