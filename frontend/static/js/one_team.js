console.log("js running?")

/*core */
document.querySelectorAll(".slot").forEach((slot, index) => {
    slot.addEventListener("click", () => {
        console.log("Clicked slot:", index+1);
    });
});

/*bench */
document.querySelectorAll(".b-slot").forEach((slot, index) => {
    slot.addEventListener("click", () => {
        console.log("Clicked bench slot:", index+1);
    });
});

/*choice */
document.querySelectorAll(".choice-slot").forEach((slot, index) => {
    slot.addEventListener("click", () => {
        console.log("Clicked choice slot:", index+1);
    });
});


const tag = window.location.pathname.split("/").pop();

// TEAM NAME BASED ON TAG NAME RECEIVED
fetch(`/api/teams/${tag}`)
  .then(response => response.json())
  .then(data => { //data should be the TEAM of Tag x
    const team_name = data.name;
    document.getElementById("team-title").textContent = team_name;
    document.getElementById("team-name").textContent = team_name;
  });


