const video_database = [
    {
        title: 'Video 1',
        tags: ['tag1','tag2'],
        url:''
    }
]

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
            videoplacer.innerHTML = ''
        }
        else {
            videoplacer.innerHTML = "<h1>No videos found with the search term.</h1>"
        }
    });
}


