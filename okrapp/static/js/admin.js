document.addEventListener('DOMContentLoaded', function() {
    // Fetch the dropdown elements by ID
    var dropdown = document.getElementById('id_checklist');
    var categoryPointsDropdown = document.getElementById('id_category_points');

    // Function to handle the AJAX request and update category points dropdown
    function updateCategoryPointsDropdown() {
        // Check if the dropdown element exists
        if (dropdown) {
            // Get the selected option
            var selectedOption = dropdown.options[dropdown.selectedIndex];

            // Get the text of the selected option
            var selectedText = selectedOption.text;

            // Do something with the selected text
            console.log('Selected text:', selectedText);
            var url = `http://127.0.0.1:8000/get_subcategories/${encodeURIComponent(selectedText)}`;

            fetch(url)
                .then(function(response) {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(function(data) {
                    console.log("old data", data)
                    categoryPointsDropdown.innerHTML = '';
                    data = data['sub_categories']
                    console.log("new data", data)

                    // Add new options based on the response data
                    data.forEach(function(item) {
                        console.log("the item", item)
                        var option = document.createElement('option');
                        option.text = item;  
                        option.value = item; 
                        categoryPointsDropdown.add(option);
                    });
                })
                .catch(function(error) {
                    // Handle errors
                    console.error('Error fetching data:', error);
                });
        } else {
            console.log('Dropdown element with ID "id_checklist" not found.');
        }
    }

    // Call the function initially
    updateCategoryPointsDropdown();

    // Add event listener to the dropdown to trigger the function when value changes
    if (dropdown) {
        dropdown.addEventListener('change', updateCategoryPointsDropdown);
    }
});
