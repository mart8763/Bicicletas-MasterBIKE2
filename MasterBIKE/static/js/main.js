const productos = [
    {
        id: "asiento",
        titulo: "Asiento",
        imagen: "static/imgProductos/asiento.png",
        precio: 20000
    },
    {
        id: "campana",
        titulo: "Campana",
        imagen: "static/imgProductos/campana.jpg",
        precio: 20000
    },
    {
        id: "casco",
        titulo: "Casco",
        imagen: "static/imgProductos/casco.jpg",
        precio: 20000
    },
    {
        id: "chaqueta",
        titulo: "Chaqueta",
        imagen: "static/imgProductos/chaqueta.jpg",
        precio: 20000
    },
    {
        id: "llantas",
        titulo: "Llantas",
        imagen: "static/imgProductos/llanta.png",
        precio: 20000
    },
    {
        id: "manillar",
        titulo: "Manillar",
        imagen: "static/imgProductos/manillar.png",
        precio: 20000
    },
    {
        id: "marco",
        titulo: "Marco",
        imagen: "static/imgProductos/marco.jpg",
        precio: 20000
    },
    {
        id: "puños",
        titulo: "Puños",
        imagen: "static/imgProductos/puños.png",
        precio: 20000
    },
    {
        id: "rueda",
        titulo: "Rueda",
        imagen: "static/imgProductos/rueda.png",
        precio: 20000
    },
    {
        id: "disco",
        titulo: "Disco",
        imagen: "static/imgProductos/disco.png",
        precio: 20000
    },
    {
        id: "frenos",
        titulo: "Frenos",
        imagen: "static/imgProductos/frenos.jpg",
        precio: 20000
    }
];


const contenedorProductos = document.querySelector("#contenedor-productos");
let botonesAgregar = document.querySelectorAll(".producto-agregar");
const numerito = document.querySelector("#numerito");

function cargarProductos() {

    contenedorProductos.innerHTML = "";

    productos.forEach(producto => {

        const div = document.createElement("div");
        div.classList.add("producto");
        div.innerHTML = `
            <img class="producto-imagen" src="${producto.imagen}" alt="${producto.titulo}">
            <div class="producto-detalles">
                <h3 class="producto-titulo">${producto.titulo}</h3>
                <p class="producto-precio">$${producto.precio}</p>
                <button class="producto-agregar" id="${producto.id}">Agregar</button>
            </div>
        `;

        contenedorProductos.append(div);
    })

    actualizarBotonesAgregar();
}

cargarProductos(productos);


function actualizarBotonesAgregar() {
    botonesAgregar = document.querySelectorAll(".producto-agregar");

    botonesAgregar.forEach(boton => {
        boton.addEventListener("click", agregarAlCarrito);
    });
}

let productosEnCarrito;

const productosEnCarritoLS = localStorage.getItem("productos-en-carrito");

if (productosEnCarritoLS) {
    productosEnCarrito = JSON.parse(productosEnCarritoLS);
    actualizarNumerito();
} else {
    productosEnCarrito = [];
}


function agregarAlCarrito(e) {

    const idBoton = e.currentTarget.id;
    const productoAgregado = productos.find(producto => producto.id === idBoton);

    if (productosEnCarrito.some(producto => producto.id === idBoton)) {
        const index = productosEnCarrito.findIndex(producto => producto.id === idBoton);
        productosEnCarrito[index].cantidad++;
    } else {
        productoAgregado.cantidad = 1;
        productosEnCarrito.push(productoAgregado);
    }

    actualizarNumerito();

    localStorage.setItem("productos-en-carrito", JSON.stringify(productosEnCarrito));
};

function actualizarNumerito() {
    let nuevoNumerito = productosEnCarrito.reduce((acc, producto) => acc + producto.cantidad, 0);
    numerito.innerText = nuevoNumerito;
}