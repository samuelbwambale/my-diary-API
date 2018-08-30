function changediv(){
    let editable = document.getElementById('desc')
    editable.contentEditable = "true"
    let editbtn = document.getElementById('editbtn')
    editbtn.innerText="Save";
    editbtn.setAttribute("onclick","update_an_entry()")
}


function update_an_entry(){
    let description = document.getElementById('desc').innerText;
    let id = document.getElementById('entryid').innerText;
    console.log(description)
    
    fetch('http://127.0.0.1:5000/api/v1/entries/'+id, {
      method:'PUT',
      headers: {
        'Content-type':'application/json; charset=UTF-8',
        'authorization':'Bearer '+token
      },
      body:JSON.stringify({
        description:description})
    })
    .then(function(response) {
        return response.json()
      })
    .then(function(data) {
        if(data.message === "Entry edited successfully"){
        alert(data.message)
        window.location.href = "./entries.html"
        } else if(data.message === "Internal Server Error"){
            sessionExpired()        
      } else{
            document.getElementById('view_entries_response').innerHTML = "Error : " + data.message;
        }        
    })
    .catch(error => console.log(error))
}

function get_entries(){

    fetch('http://127.0.0.1:5000/api/v1/entries', {
      method:'GET',
      headers: {
        'Content-type':'application/json; charset=UTF-8',
        'Authorization':'Bearer '+ token
      }
    })
    .then(response => response.json())
    .then(function(data) {
        if(data.status === "success"){
        let entries_output = '<h2 style = "color: #5f044b;" class="mb-4">My Entries</h4>'
        data.entries.forEach(entry => {
            entries_output += `
            <div class="entry-div card">
                <h3><a href="#" onclick="get_an_entry(${entry.entry_id})">${entry.title}</a>
                </h3>
                <p>${entry.description}</p>
                <p>${entry.create_date}</p>
            </div>
            <p class="mb-5"></p>
            `
        })
        document.getElementById('entries_output').innerHTML = entries_output
        }
        else if(data.message === "Internal Server Error"){
            sessionExpired()
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
        'Authorization':'Bearer '+ token
      }
    })
    .then(response => {
        response.json().then(function(data) {
            if(data.status === "success"){
                let entries_output = `
                <div class="entry-div card">
                    <h2 class="entry-title">${data.entry.title}</h2>
                    <p id='entryid' style="display: none;" >${data.entry.entry_id}</p>
                    <p id="desc" contenteditable="false" >${data.entry.description}</p>
                    <button id="editbtn" class="btn-edit" onclick="changediv()">Edit</button>
                    <button onclick="delete_an_entry(${data.entry.entry_id})" class="btn-delete-entry">Delete</button>
                    <button class="btn-cancel" onclick="window.location='./entries.html'">Cancel</button>
                    <p class="mb-2"></p>
                </div>
                ` 
                document.getElementById('entries_output').innerHTML = entries_output
            }
            else if(data.message === "Internal Server Error"){
                sessionExpired()       
            } else {
                    document.getElementById('view_entries_response').innerHTML = data.message
                }
        })
    })
    .catch(error => console.log(error))
}

function delete_an_entry(id){

    fetch('http://127.0.0.1:5000/api/v1/entries/'+id, {
      method:'DELETE',
      headers: {
        'Content-type':'application/json; charset=UTF-8',
        'Authorization':'Bearer '+ token
      }
    })
    .then(response => {
        response.json().then(function(data) {
            if(data.message === "Selected entry has been deleted"){
                alert(data.message)
                window.location.href = "./entries.html"
            } else if(data.message === "Internal Server Error"){
                sessionExpired()       
            } else{
                    document.getElementById('view_entries_response').innerHTML = data.message
                }
        }) 
    })   
    .catch(error => console.log(error))
}
