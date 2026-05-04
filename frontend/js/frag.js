let params = new URL(document.location.toString()).searchParams;
let ids = params.get("id");

fetch(`http://127.0.0.1:5001/fragrances/${ids}`)
  .then(response => response.json())
  .then(datas => {
    data = datas[0]
    document.getElementById("name-frag").innerHTML = data[1]
    document.getElementById("photo-frag").src = `assets/${data[1]}.webp`

    document.getElementById("belvish-link").href = data[2]
    document.getElementById("whiff-culture-link").href = data[3]
    document.getElementById("aar-fragrances-link").href = data[4]
    document.getElementById("perfume-palace-link").href = data[5]
    document.getElementById("fragrance-haven-link").href = data[6]

    document.getElementById("belvish-price").innerHTML = `₹${data[10]}`
    document.getElementById("whiff-culture-price").innerHTML = `₹${data[11]}`
    document.getElementById("aar-fragrances-price").innerHTML = `₹${data[12]}`
    document.getElementById("perfume-palace-price").innerHTML = `₹${data[13]}`
    document.getElementById("fragrance-haven-price").innerHTML = `₹${data[14]}`
})
