


function deleteNote(noteId)
{
    // Way to send requests in vanilla JS
    /**
     *  Sends a POST request to the delete-note endpoint
     * After receiving a response, it reloads the window by changing the location
     * to the same home page, "/", using window.location.href="/".
     * */ 
    fetch("/delete_note", {
        method: "POST",
        body: JSON.stringify({noteId: noteId})
    }).then((_res) => {
        // 
        window.location.href = "/";
    });
}