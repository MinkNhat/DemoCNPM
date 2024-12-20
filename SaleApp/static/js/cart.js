function addToCart(id, name, price) {
console.log(id, name, price)
    fetch("api/carts", {
        method: "post",
        body: JSON.stringify({
            "id": id,
            "name": name,
            "price": price
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(res => res.json()).then(data => {
        let d = document.getElementsByClassName("badge-counter");
        for(let e of d) {
            e.innerText = data.total_quantity;
        }
    })
}