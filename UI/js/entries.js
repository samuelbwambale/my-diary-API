document.getElementById("get_entries_button").addEventListener("submit", test_log_something)
function view_entries(){

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
        let entry_output = '<h2 style = "color: rgb(73, 35, 35);" class="display-4 mb-4">My Entries</h2>'
        data.entries.forEach(entry => {
            entry_output += `
            <div class="entry-div">
                <h2>Title: ${entry.title}</h2>
                <p>ID: ${entry.entry_id}</p>
                <p>Description: ${entry.description}</p>
            <div>
            `
        })
        document.getElementById('entry_output').innerHTML = entry_output
        }
        else if(data.message === "Internal Server Error"){
            let res = "Session has expired, please login and try again"
            //document.getElementById('view_entry_response').innerHTML = res
            alert(res)
            window.location.href = "./login.html"

        } else {
            document.getElementById('view_entry_response').innerHTML = data.message
        }      
    })
    .catch(error => console.log(error))
  }

function test_log_something(){
    console.log(12345)
    }
