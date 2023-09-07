const video_database = [
    {
        title: 'Calisthenics for Beginners',
        tags: ['calisthenics','core','hybrid calisthenics'],
        url:'..\static\media\video_database\Calisthenics for Beginners (2023).mp4.crdownload'
    }
]

// Listen for the "keydown" event on the input field
searchInput.addEventListener("keydown", function(event) {
    // Check if the pressed key is Enter
    if (event.key === "Enter" || event.keyCode === 13) {
        // Execute your code here
        const searchTerm = searchInput.value.toLowerCase();
        searchvideos(searchTerm);
    }
});


// Event listener for search input
const searchInput = document.getElementById("searchInput");
searchInput.addEventListener("input", () => {
    const searchTerm = searchInput.value.toLowerCase();
    searchvideos(searchTerm);
});

function searchvideos(searchTerm) {
    const videoplacer = document.getElementById('videoplacer')
    videoplacer.innerHTML = ""; // Clear previous videos

    video_database.forEach(video => {
        // Check if the video's tags match the search term
        if (video.tags.includes(searchTerm)) {

            videoplacer.innerHTML = `
            <video id="video_background" loop muted autoplay>
                <source src="` + video_database + `">
            </video>
            `
        }
        else {
            videoplacer.innerHTML = "<h1>No videos found with the search term.</h1>"
        }
    });
}


