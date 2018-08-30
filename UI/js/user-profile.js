
  function get_user_profile(){
    fetch(url + blueprint +'/user', {
      method:'GET',
      headers: {
        'Content-type':'application/json; charset=UTF-8',
        'Authorization':'Bearer '+ token
      }
    })
    .then(response => {
        response.json().then(function(data) {
            if(data.status === "success"){
                let profile_output = `
                <div class="entry-div">
                    <h2 class="entry-title mt-3">${data.profile.first_name} ${data.profile.last_name}</h2>
                    <p>${data.profile.email}</p>
                    <p id="desc" contenteditable="false" >${data.profile.entries_count} Entries</p>
                    <button id="editbtn" class="btn-edit">Edit Profile</button>
                <div>
                ` 
                document.getElementById('profile_output').innerHTML = profile_output
            }
            else if(data.message === "Internal Server Error"){
                sessionExpired()       
            } else {
                    document.getElementById('profile_response').innerHTML = data.message
                }
        })
    })
    .catch(error => console.log(error))
}
