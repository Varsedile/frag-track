// Getting ID from the link

let params = new URL(document.location.toString()).searchParams;
ids = params.get("id");

// Inserting name, photos, links and prices of the products

fetch(`https://frag-track-app.onrender.com/fragrances/${ids}`)
  .then(response => response.json())
  .then(data => {
    data.forEach(frag => {

    let minAmt = frag[10];

    const elements = [
    { id: 10, element: "belvish-price"},
    { id: 11, element: "whiff-culture-price"},
    { id: 12, element: "aar-fragrances-price"},
    { id: 13, element: "perfume-palace-price"},
    { id: 14, element: "fragrance-haven-price"}
    ]
    
    for (let i = 10; i < 15; i++) {
        if (frag[i] == "null" || frag[item.id] == null) {
            continue
        }
        if (minAmt > frag[i]) {
            minAmt = frag[i]
        }
    }
    
    document.getElementById("name-frag").innerHTML = frag[1]
    document.getElementById("photo-frag").src = `/static/assets/${frag[1]}.webp`

    document.getElementById("belvish-link").href = frag[2]
    document.getElementById("whiff-culture-link").href = frag[3]
    document.getElementById("aar-fragrances-link").href = frag[4]
    document.getElementById("perfume-palace-link").href = frag[5]
    document.getElementById("fragrance-haven-link").href = frag[6]

    elements.forEach(item => {

        console.log(minAmt)
        console.log(frag[item.id])
        
        if (frag[item.id] == "null" || frag[item.id] == null) {
            document.getElementById(item.element).innerHTML = "N/A"
            document.getElementById(item.element).classList.add("text-gray-400")
            return
        }
        if (minAmt == frag[item.id]) {
            document.getElementById(item.element).innerHTML = `₹${frag[item.id]}`
            document.getElementById(item.element).classList.add("text-black")
        }
        else {
            document.getElementById(item.element).innerHTML = `₹${frag[item.id]}`
            document.getElementById(item.element).classList.add("text-gray-400")
        }
        })
    })
})