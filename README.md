## The script for the scrape is in .backend/utils/scrape_judicial_processes
# Web Scraping de Procesos Judiciales

Este script de Python está diseñado para realizar web scraping de los procesos judiciales a partir de un número de identificación (CI o RUC) desde el sitio web de la Función Judicial del Ecuador. Utiliza Selenium para navegar y extraer la información de los procesos judiciales, y luego guarda esos datos en un archivo CSV.

## Requisitos

Para ejecutar este script, necesitarás Python 3 y algunas dependencias. Asegúrate de tener instalado Python 3.6 o superior. Puedes instalar las dependencias necesarias usando `pip`:

```bash
pip install selenium pandas beautifulsoup4
Además, necesitarás el WebDriver para Chrome. Asegúrate de descargar la versión correcta del WebDriver que corresponda a la versión de tu navegador Chrome desde aquí.

Configuración
Antes de ejecutar el script, asegúrate de colocar el ejecutable del WebDriver en tu PATH o modificar el script para que apunte a la ubicación del ejecutable.

Uso
Para ejecutar el script, simplemente navega al directorio donde se encuentra el archivo y ejecuta:

bash
Copy code
python nombre_del_archivo.py
El script iniciará varias solicitudes paralelas para raspar los datos judiciales de los números de identificación especificados en el método test_parallel_requests.

Funciones Principales
scrape_judicial_processes(id_number): Realiza el web scraping de los procesos judiciales para el número de identificación proporcionado.

save_data(data, name): Guarda los datos recopilados en un archivo CSV.

test_parallel_requests(): Prueba el web scraping con múltiples solicitudes paralelas, utilizando threading para mejorar la eficiencia.

## Technology Stack and Features

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the Python backend API.
    - 🧰 [SQLModel](https://sqlmodel.tiangolo.com) for the Python SQL database interactions (ORM).
    - 🔍 [Pydantic](https://docs.pydantic.dev), used by FastAPI, for the data validation and settings management.
    - 💾 [PostgreSQL](https://www.postgresql.org) as the SQL database.
- 🚀 [React](https://react.dev) for the frontend.
    - 💃 Using TypeScript, hooks, Vite, and other parts of a modern frontend stack.
    - 🎨 [Chakra UI](https://chakra-ui.com) for the frontend components.
    - 🤖 An automatically generated frontend client.
    - 🦇 Dark mode support.
- 🐋 [Docker Compose](https://www.docker.com) for development and production.
- 🔒 Secure password hashing by default.
- 🔑 JWT token authentication.
- 📫 Email based password recovery.
- ✅ Tests with [Pytest](https://pytest.org).
- 📞 [Traefik](https://traefik.io) as a reverse proxy / load balancer.
- 🚢 Deployment instructions using Docker Compose, including how to set up a frontend Traefik proxy to handle automatic HTTPS certificates.
- 🏭 CI (continuous integration) and CD (continuous deployment) based on GitHub Actions.

### Dashboard Login

[![API docs](img/login.png)](https://github.com/tiangolo/full-stack-fastapi-template)

### Dashboard - Admin

[![API docs](img/dashboard.png)](https://github.com/tiangolo/full-stack-fastapi-template)

### Dashboard - Create User

[![API docs](img/dashboard-create.png)](https://github.com/tiangolo/full-stack-fastapi-template)

### Dashboard - Items

[![API docs](img/dashboard-items.png)](https://github.com/tiangolo/full-stack-fastapi-template)

### Dashboard - User Settings

[![API docs](img/dashboard-user-settings.png)](https://github.com/tiangolo/full-stack-fastapi-template)

### Dashboard - Dark Mode

[![API docs](img/dashboard-dark.png)](https://github.com/tiangolo/full-stack-fastapi-template)

### Interactive API Documentation

[![API docs](img/docs.png)](https://github.com/tiangolo/full-stack-fastapi-template)

## How To Use It

You can **just fork or clone** this repository and use it as is.

✨ It just works. ✨

### Configure

You can then update configs in the `.env` files to customize your configurations.

Before deploying it, make sure you change at least the values for:

- `SECRET_KEY`
- `FIRST_SUPERUSER_PASSWORD`
- `POSTGRES_PASSWORD`

### Generate Secret Keys

Some environment variables in the `.env` file have a default value of `changethis`.

You have to change them with a secret key, to generate secret keys you can run the following command:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

## Backend Development

Backend docs: [backend/README.md](./backend/README.md).

## Frontend Development

Frontend docs: [frontend/README.md](./frontend/README.md).

## Deployment

Deployment docs: [deployment.md](./deployment.md).

## Development

General development docs: [development.md](./development.md).

This includes using Docker Compose, custom local domains, `.env` configurations, etc.

## Release Notes

Check the file [release-notes.md](./release-notes.md).

## License

The Full Stack FastAPI Template is licensed under the terms of the MIT license.
