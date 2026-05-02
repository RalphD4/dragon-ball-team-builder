const BASE_URL = "http://127.0.0.1:5000";
console.log("JS running")


/*fetch(`${BASE_URL}/teams`)
  .then(response => response.json())
  .then(data => {
      console.log(data); // your teams array
  });
*/




// ---------------  Teams -----------------

document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("teams-container");

    fetch("/api/teams") //send fetch request to address
        .then(response => response.json()) //raw http response object, .json() reads it
        .then(teams => {  //the actual returned data
            teams.forEach(team => {
                console.log(team); ////////////////////       DEBUG LINE
                const link = document.createElement("a");
                link.href = `${BASE_URL}/teams/${team.tag}`;
                link.textContent = team.name;
                link.classList.add("team-link");
                container.appendChild(link);
            });
        })
        .catch(error => {
            console.error("Error fetching teams:", error);
        });
});


   














