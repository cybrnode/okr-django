window.onload = function() {
    console.log("window.onload");

    var dropdown = document.getElementById('id_checklist');
    console.log(dropdown)

    var selectedOption = dropdown.options[dropdown.selectedIndex];

    var selectedText = selectedOption.text;
    console.log(selectedText)

    var url = `http://127.0.0.1:8000/get_subcategories/${encodeURIComponent(selectedText)}`;
    document.getElementById("content").innerHTML = ""
    fetch(url)
    .then(function(response) {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(function(data) {
        var table = document.createElement("table");
        var header = document.createElement("h1");
        header.innerText = "Checklist Table"
        
        var subCategories = data['sub_categories'];
        var date = data['date'];
        var status = data['status'];

        // Create a new row above all subcategories for 'checklist'
        var checklistRow = table.insertRow();
        var checklistCell = checklistRow.insertCell(0);
        checklistCell.colSpan = 3; // Span across all columns
        checklistCell.textContent = "Checklist";

        // Create the first row for the date columns
        var dateRow = table.insertRow();
        
        // Set the date column texts
        var dateCell1 = dateRow.insertCell(0);
        dateCell1.textContent = selectedText;

        // Add date column based on the provided date
        var dateCell2 = dateRow.insertCell(1);
        dateCell2.textContent = date;

        // Create a checkbox for the status
        var statusCell = dateRow.insertCell(2);
        var statusCheckbox = document.createElement('input');
        statusCheckbox.type = 'checkbox';
        statusCheckbox.disabled = true;
        statusCheckbox.checked = status;
        // statusCell.appendChild(statusCheckbox);

        // Loop through the sub-categories array to create rows
        subCategories.forEach(function(subCategory) {
            var row = table.insertRow();
            var cell1 = row.insertCell(0);
            cell1.textContent = subCategory[0]; // Assuming subCategory is a tuple and the name is at index 0

            // Create a checkbox for each sub-category and make it checked
            var subCategoryCell = row.insertCell(1);
            var subCategoryCheckbox = document.createElement('input');
            subCategoryCheckbox.type = 'checkbox';
            subCategoryCheckbox.checked = true;
            subCategoryCheckbox.disabled = true;
            subCategoryCell.appendChild(subCategoryCheckbox);
        });

        // Append the table to the body
        document.getElementById("content").appendChild(header);
        document.getElementById("content").appendChild(table);
    })
    .catch(function(error) {
        // Handle errors
        console.error('Error fetching data:', error);
    });
};
