// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Get a reference to the popup element
    var popup = document.getElementById("popup");

    // Check if the popup element exists
    if (popup) {
        // Set a timeout to remove the popup after 5 seconds (5000 milliseconds)
        setTimeout(function() {
            // Remove the popup by setting its style to "display: none;"
            popup.style.display = "none";
            // Alternatively, you can remove the popup from the DOM entirely
            // popup.parentNode.removeChild(popup);
        }, 5000); // 5000 milliseconds (5 seconds)
    }
});
