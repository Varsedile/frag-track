// Listing products in the index page
fetch("/fragrances")
  .then(response => response.json())
  .then(data => {
    try {
    data.forEach(frag => {
        const container = document.getElementById("fragrance-container");
        const card = `<li class="py-4 sm:py-4 list-none">
                        <div class="group relative">
                            <img src="/static/assets/${frag.name}.webp" alt="picture of the perfume" class="aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75 lg:aspect-auto lg:h-80" />
                            <div class="mt-4 flex justify-between">
                            <div>
                                <h3 class="text-sm text-gray-700">
                                <a href="fragrance?id=${frag.fragrance_id}">
                                <span aria-hidden="true" class="absolute inset-0"></span>
                                ${frag.name}
                            </a>
                            </h3>
                        </div>
                        </div>
                    </div>`
        container.innerHTML += card
    })
    } catch(error) {
        console.log("Could not retrieve data")
        document.getElementById("fragrance-container").remove();
    } 
})
