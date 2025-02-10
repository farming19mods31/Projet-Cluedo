// Fonction pour récupérer les suspects
function afficherSuspects() {
    fetch("suspects.json")
        .then(response => response.json())
        .then(data => {
            let container = document.getElementById("suspects-container");
            container.innerHTML = "";
            data.forEach(suspect => {
                let div = document.createElement("div");
                div.innerHTML = `<h2>${suspect.nom}</h2><p>${suspect.role} - ${suspect.description}</p>`;
                container.appendChild(div);
            });
        });
}

// Fonction pour récupérer les objets
function afficherObjets() {
    fetch("objets.json")
        .then(response => response.json())
        .then(data => {
            let container = document.getElementById("objets-container");
            container.innerHTML = "";
            data.forEach(objet => {
                let div = document.createElement("div");
                div.innerHTML = `<h2>${objet.nom}</h2><p>${objet.description}</p>`;
                container.appendChild(div);
            });
        });
}

// Fonction pour récupérer les énigmes avec input de réponse
function afficherEnigmes() {
    fetch("enigmes.json")
        .then(response => response.json())
        .then(data => {
            let container = document.getElementById("enigmes-container");
            container.innerHTML = "";
            data.forEach(enigme => {
                let div = document.createElement("div");
                div.innerHTML = `
                    <h2>${enigme.question}</h2>
                    <input type="text" id="reponse-${enigme.id}" placeholder="Votre réponse">
                    <button onclick="verifierReponse(${enigme.id}, '${enigme.reponse}')">Vérifier</button>
                    <p id="resultat-${enigme.id}"></p>
                `;
                container.appendChild(div);
            });
        });
}

// Vérifier la réponse de l'utilisateur
function verifierReponse(id, bonneReponse) {
    let input = document.getElementById(`reponse-${id}`);
    let resultat = document.getElementById(`resultat-${id}`);
    
    if (input.value.trim().toLowerCase() === bonneReponse.toLowerCase()) {
        resultat.innerHTML = "✅ Bonne réponse !";
        resultat.style.color = "lightgreen";
    } else {
        resultat.innerHTML = "❌ Mauvaise réponse, essayez encore.";
        resultat.style.color = "red";
    }
}

