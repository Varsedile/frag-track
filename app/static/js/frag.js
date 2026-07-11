// Getting ID from the link
let params = new URL(document.location.toString()).searchParams;
ids = params.get("id");

// Function to capitalize every first letter of a word
function capitalizeFirstLetter(str) {
  var lower = String(str).toLowerCase().replace("-", " ");
  return lower.replace(/(^| )(\w)/g, function(x) {
    return x.toUpperCase();
  });
}

// Inserting name, photos, links and prices of the products
fetch(`/fragrances/${ids}`)
  .then(response => response.json())
  .then(data => {
    data.forEach(frag => {
    document.getElementById("name-frag").innerHTML = `${frag.name}`
    document.getElementById("photo-frag").src = `/static/assets/${frag.name}.webp`

    const container = document.getElementById("dealer-list")
    const card = `<li class="py-4 sm:py-4">
                  <div class="flex items-center gap-2">
                    <div class="flex-1 min-w-0 ms-2">
                        <p class="font-medium text-heading truncate">
                            <a href="${frag.url}">${capitalizeFirstLetter(frag.site_name)}</a>
                        </p>
                      </div>
                        <div class="inline-flex items-center font-medium text-heading">${frag.price}
                      </div>
                    </div>
                  </li>`
    container.innerHTML += card
    })
})