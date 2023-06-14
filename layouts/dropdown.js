// Read the characters.txt file and populate the dropdown options
fetch('characters.txt')
  .then(response => response.text())
  .then(data => {
    const dropdown = document.getElementById('characterDropdown');
    const characters = data.split('\n');

    characters.forEach(character => {
      const option = document.createElement('option');
      option.text = character;
      dropdown.add(option);
    });
  })
  .catch(error => {
    console.error('Error fetching characters:', error);
  });

// Function to handle the selection change
function handleSelectionChange() {
  const selectedCharacter = document.getElementById('characterDropdown').value;
  
  // TODO: Implement code to filter and display relevant .md files based on the selected character
  // You can use the 'selectedCharacter' variable to get the selected character value
  // and perform the necessary filtering and rendering of the .md files.
}