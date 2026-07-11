// Getting ID from the link

let params = new URL(document.location.toString()).searchParams;
ids = params.get("id");

// Inserting name, photos, links and prices of the products

fetch(`/fragrances/${ids}`)
  .then(response => response.json())
  .then(data => {
    data.forEach(frag => {
    document.getElementById("name-frag").innerHTML = `${frag.name}`
    document.getElementById("photo-frag").src = `/static/assets/${frag.name}.webp`
    document.getElementById(`${frag.site_name}-link`).href = `${frag.url}`
    document.getElementById(`${frag.site_name}-price`).innerHTML = `${frag.price}`
})})