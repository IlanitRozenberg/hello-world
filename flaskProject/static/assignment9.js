function load(search) {
    fetch("https://reqres.in/api/users?page=2").then(response => response.json())
        .then(resJSON => extractData(resJSON.data, search)).catch(err => console.log(err));
}

function extractData (users, search_term){
    const mainDiv = document.querySelector("main");
    let empty = true;

    for (let user of users){
        if (search_term == "" || search_term.toLowerCase() === user.first_name.toLowerCase()) {
            empty = false;
            const userDiv = document.createElement("section");
            userDiv.innerHTML = `
            <div class="user">    
                <img src ="${user.avatar}">
                <br>
                <span class="first_name">${user.id}. ${user.first_name}</span>
                <span class="last_name">${user.last_name}</span>
                <br>
                <a href="mailto:${user.email}">${user.first_name}'s mail</a><br>
            </div
            `
            mainDiv.appendChild(userDiv);
        }
    }

    if (empty){
        const emptyDiv = document.createElement("section");
        emptyDiv.innerHTML = "<h1> No result found </h1>";
        mainDiv.appendChild(emptyDiv);
    }
}