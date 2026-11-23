const express = require('express')
const app = express()

app.use(express.json())

// Catálogo inicial en memoria
const productos = [
    {
        id: 1,
        nombre: 'Teclado inalambrico',
        descripcion: 'Teclado 101 teclas idioma ingles',
        precio: 1500.00
    },
    {
        id: 2,
        nombre: 'Mouse inalambrico',
        descripcion: 'Mouse optico inalambrico.',
        precio: 600.00
    },
    {
        id: 3,
        nombre: 'Monitor 23.5 pulgadas full hd',
        descripcion: 'Monitor Full HD panel IPS',
        precio: 6500.00
    },
    {
        id: 4,
        nombre: 'Webcam Full HD',
        descripcion: 'Camara USB con microfono integrado',
        precio: 2800.00
    },
    {
        id: 5,
        nombre: 'Memoria USB de 64 GB',
        descripcion: 'Unidad de almacenamiento USB 3.0',
        precio: 750.00
    },
    {
        id: 6,
        nombre: 'Base para laptop',
        descripcion: 'Soporte ajustable de aluminio',
        precio: 1350.00
    }
]

let siguienteId = Math.max(...productos.map(producto => producto.id)) + 1

// GET - Consultar el catálogo completo
app.get('/productos', (req, res) => {
    res.json(productos)
})

// GET - Buscar un producto por su ID
app.get('/productos/:id', (req, res) => {
    const id = parseInt(req.params.id)
    const producto = productos.find(p => p.id === id)

    if (!producto) {
        return res.status(404).json({ mensaje: 'Producto no encontrado' })
    }

    res.json(producto)
})


// POST - Registrar un producto y asignarle un ID
app.post('/productos', (req, res) => {
    const { nombre, descripcion, precio } = req.body || {}

    if (!nombre || !descripcion || precio == null || precio === '') {
        return res.status(400).json({ mensaje: 'nombre, descripcion y precio son obligatorios' })
    }

    const producto = { id: siguienteId, nombre, descripcion, precio: parseFloat(precio) }
    siguienteId++
    productos.push(producto)

    res.status(201).json(producto)
})

// PUT - Actualizar todos los campos y conservar el ID
app.put('/productos/:id', (req, res) => {
    const id = Number(req.params.id)
    const indice = productos.findIndex(producto => producto.id === id)

    if (indice === -1) {
        return res.status(404).json({ mensaje: 'Producto no encontrado' })
    }

    const { nombre, descripcion, precio } = req.body || {}

    if (!nombre || !descripcion || precio == null || precio === '') {
        return res.status(400).json({ mensaje: 'nombre, descripcion y precio son obligatorios' })
    }

    const producto = { id, nombre, descripcion, precio: parseFloat(precio) }
    productos[indice] = producto

    res.status(200).json(producto)
})

// DELETE - Retirar un producto y devolver el registro eliminado
app.delete('/productos/:id', (req, res) => {
    const id = Number(req.params.id)
    const indice = productos.findIndex(producto => producto.id === id)

    if (indice === -1) {
        return res.status(404).json({ mensaje: 'Producto no encontrado' })
    }

    const [producto] = productos.splice(indice, 1)
    res.status(200).json({ mensaje: 'Producto eliminado', producto })
})


app.listen(3000, () => {
    console.log('Servidor corriendo en http://localhost:3000')
})
