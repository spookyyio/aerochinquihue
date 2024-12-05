# Aero Chinquihue

Proyecto 2024 POO

## Integrantes

- Felipe Sanchez
- Kassandra Fuentes

## Descripción

Aero Chinquihue es una aplicacion ficticia creada para el proyecto de POO 2024 de 2-SEM.

## Funcionalidades

- **Agendar un vuelo**: Los empleados pueden seleccionar un destino, ingresar sus datos y agendar un vuelo. También pueden optar por agregar un paquete y el precio se ajustará en consecuencia.
- **Gestionar encomiendas**: Los empleados pueden crear encomiendas seleccionando un destino y proporcionando los detalles del paquete.
- **Vuelos actuales**: Los empleados pueden ver una lista de los vuelos actuales.
- **Administrar vuelos**: Los administradores pueden agregar pasajeros a los vuelos existentes, aplicar descuentos y eliminar vuelos.
- **Administrar paquetes**: Los administradores pueden gestionar los paquetes asociados a los vuelos.

## Estructura del Proyecto

- `app.py`: Archivo principal que inicia la aplicación.
- `controller_agendar.py`: Controlador para la gestión de vuelos y encomiendas.
- `model_agendar.py`: Modelo que maneja la lógica de negocio y la interacción con los archivos CSV.
- `vista_agendar.py`: Vista para agendar vuelos.
- `vista_encomiendas.py`: Vista para gestionar encomiendas.
- `vista_vuelosact.py`: Vista para mostrar los vuelos actuales.
- `vista_admin.py`: Vista para administrar vuelos y agregar pasajeros.
- `vista_adminpackages.py`: Vista para administrar paquetes.
- `vista_adminvuelos.py`: Vista para gestionar y eliminar vuelos.

## Archivos CSV

- `vuelos.csv`: Almacena los detalles de los vuelos.
- `destinations.csv`: Almacena los destinos disponibles y sus detalles.
- `packages.csv`: Almacena los detalles de los paquetes.
- `passwords.csv`: Almacena las contraseñas de los usuarios.

## Uso

1. Ejecuta la aplicación:
    ```bash
    python app.py
    ```
2. Interactúa con la interfaz gráfica para agendar vuelos, gestionar encomiendas y administrar vuelos.
