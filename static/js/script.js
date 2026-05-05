// Listing products in the index page

fetch("https://frag-track-app.onrender.com/fragrances")
  .then(response => response.json())
  .then(data => {
    data.forEach(frag => {
    const container = document.getElementById("fragrance-container")
    const card = `<div class="group relative">
                    <img src="/static/assets/${frag[1]}.webp" alt="picture of the perfume" class="aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75 lg:aspect-auto lg:h-80" />
                    <div class="mt-4 flex justify-between">
                    <div>
                        <h3 class="text-sm text-gray-700">
                        <a href="fragrance?id=${frag[0]}">
                            <span aria-hidden="true" class="absolute inset-0"></span>
                            ${frag[1]}
                        </a>
                        </h3>
                    </div>
                    </div>
                </div>`
    container.innerHTML += card
    })
})
