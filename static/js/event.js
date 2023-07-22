var notFavorite = "favorite-btn bi bi-star";
var favorite = "favorite-btn bi bi-star-fill"

function addFavorite(event) {
    if (event.target.className == notFavorite) {
        event.target.className = favorite;
        window.location.href = `/events/add_favorite/`;
    } else {
        event.target.className = notFavorite;
    }
}

function displayDetails(id) {
    //console.log(JSON.stringify(id));
    window.location.href = `/events/${id}/`;
    //alert('Container clicked!');
}
