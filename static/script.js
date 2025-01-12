const dropArea = document.getElementById("drop-area");
const preview = document.getElementById("preview");
const descriptionArea = document.getElementById("description-area");

dropArea.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropArea.style.borderColor = "#005ea6"; // Highlight the drop area
});

dropArea.addEventListener("dragleave", () => {
    dropArea.style.borderColor = "#0078d4"; // Revert drop area highlight
});

dropArea.addEventListener("drop", (event) => {
    event.preventDefault();
    dropArea.style.borderColor = "#0078d4"; // Revert border after drop

    const file = event.dataTransfer.files[0];
    if (file && file.type.startsWith("image/")) {
        const reader = new FileReader();
        reader.onload = (e) => {
            preview.src = e.target.result; // Show the image preview
            preview.style.display = "block"; // Display the image
            dropArea.querySelector("p").style.display = "none"; // Hide drop message

            // Update description area
            descriptionArea.innerHTML = `<p>Image description is being generated...</p>`;

            // Send the file to the backend
            const formData = new FormData();
            formData.append("image", file);

            fetch("/upload", {
                method: "POST",
                body: formData,
            })
                .then((response) => {
                    if (!response.ok) {
                        throw new Error("Failed to generate description.");
                    }
                    return response.json(); // Parse the JSON response
                })
                .then((data) => {
                    // Render Markdown to HTML
                    const html = marked.parse(data.description);
                    descriptionArea.innerHTML = `<div>${html}</div>`; // Update description area with rendered HTML
                    descriptionArea.classList.add("has-content");
                })
                .catch((error) => {
                    console.error("Error:", error);
                    descriptionArea.innerHTML = `<p>Failed to generate description. Please try again.</p>`;
                });
        };
        reader.readAsDataURL(file); // Read the image file for preview
    }
});