

$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    console.log("pid = ", id)
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            console.log("data = ", data)
            eml.innerText = data.cantidad
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalcantidad").innerText = data.totalcantidad
        }
    })
})

$('.remove-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function (data) {
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalcantidad").innerText = data.totalcantidad
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})