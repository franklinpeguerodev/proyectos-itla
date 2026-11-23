# Práctica 6 — API REST de productos

API en Node.js y Express para listar, consultar, crear, actualizar y eliminar productos. El catálogo empieza con seis productos y se guarda en memoria. Al reiniciar el servidor, se recupera el catálogo inicial.

## Cómo ejecutar

```bash
npm ci
npm run dev
```

Ejecuta los comandos desde `programacion-web/practica-6`. La API responde en `http://localhost:3000`. Ejecuta `npm start` para iniciar el servidor sin recarga automática.

## Endpoints

| Método | Ruta | Acción | Respuestas |
|---|---|---|---|
| GET | `/productos` | Listar los productos | `200` |
| GET | `/productos/:id` | Consultar un producto | `200`, `404` |
| POST | `/productos` | Crear un producto con ID automático | `201`, `400` |
| PUT | `/productos/:id` | Actualizar un producto conservando su ID | `200`, `400`, `404` |
| DELETE | `/productos/:id` | Eliminar un producto y devolver sus datos | `200`, `404` |

Para `POST` y `PUT`, envía `Content-Type: application/json` y un cuerpo con `nombre`, `descripcion` y `precio`. Si falta un campo obligatorio, la API devuelve `400`. Si el ID consultado, actualizado o eliminado no existe, devuelve `404`.
