function populateDropdown() {
  const dropdown = document.getElementById("characterDropdown");

  fetch("characters.txt")
      .then(response => response.text())
      .then(data => {
          const characters = data.split("\n");
          characters.forEach(character => {
              const option = document.createElement("option");
              option.value = character.trim();
              option.textContent = character.trim();
              dropdown.appendChild(option);
          });
      })
      .catch(error => {
          console.error("Error occurred while fetching data:", error);
      });
}

function searchFiles() {
  const characterName = document.getElementById("characterDropdown").value;
  const resultsContainer = document.getElementById("results");
  resultsContainer.innerHTML = "";

  fetch("characters.txt")
      .then(response => response.text())
      .then(data => {
          const characters = data.split("\n");
          const filesWithCharacter = characters.filter(character => character.trim() === characterName);

          if (filesWithCharacter.length === 0) {
              resultsContainer.innerHTML = "No files found.";
          } else {
              const ul = document.createElement("ul");
              filesWithCharacter.forEach(filename => {
                  const li = document.createElement("li");
                  const link = document.createElement("a");
                  link.href = "content/notes/" + filename;
                  link.textContent = filename;
                  li.appendChild(link);
                  ul.appendChild(li);
              });
              resultsContainer.appendChild(ul);
          }
      })
      .catch(error => {
          resultsContainer.innerHTML = "Error occurred while fetching data.";
          console.error("Error occurred while fetching data:", error);
      });
}

// Call the function to populate the dropdown when the page loads
window.addEventListener("DOMContentLoaded", populateDropdown);