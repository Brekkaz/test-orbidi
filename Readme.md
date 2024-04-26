# Descripción del Proyecto
Este proyecto está construido utilizando Python con FastAPI e incorpora varias bibliotecas para la creación de una aplicación web. Sigue el patrón de arquitectura hexagonal, utiliza dataloaders e implementa federación GraphQL.

## Requerimientos
- asyncpg==0.29.0
- fastapi==0.110.2
- graphql-core==3.2.3
- pydantic==2.7.1
- pydantic-settings==2.2.1
- pydantic_core==2.18.2
- starlette==0.37.2
- strawberry-graphql==0.227.2
- uvicorn==0.29.0

## Instalacion
1. Clone este repositorio en tu maquina local.
```bash
git clone git@github.com:Brekkaz/test-oribi.git
```

2. Navegue hasta la carpeta del proyecto.
```bash
cd test-oribi
```

3. Cree un entorno virtual (opcional pero recomendado).
```bash
python -m venv venv
```

4. Active el entorno virtual.
    - En Windows:
    ```bash
    venv\Scripts\activate
    ```
    - En macOS y Linux:
    ```bash
    source venv/bin/activate
    ```

5. Instale las dependencias.
```bash
pip install -r requirements.txt
```

6. Configuracion
Cree un archivo .env en la raiz del proyecto y configure las variables de entorno basandose en el archivo .env.example

7. Ejecucion
Ejecute la aplicacion utilizando uvicorn.
```bash
uvicorn main:app --reload
```

8. Docker
Ejecute la aplicacion utilizando docker.
```bash
docker compose up --build
```

9. Uso
Navegue hasta la ruta `http://localhost:8000/graphql` donde podra encontrar el playground de la aplicaciom.

## Arquitectura Hexagonal
Este proyecto sigue el patrón de arquitectura hexagonal. La arquitectura hexagonal, también conocida como puertos y adaptadores, separa la lógica principal del negocio de las preocupaciones externas como bases de datos, interfaces de usuario y frameworks. Promueve la flexibilidad, la capacidad de realizar pruebas y la facilidad de mantenimiento al mantener la lógica central del dominio independiente de las dependencias externas.

## GraphQL Federation
La Federación GraphQL es un método para componer múltiples servicios GraphQL en una sola API coherente. Permite crear un gráfico de datos distribuido, donde cada servicio administra su propio dominio y expone su esquema a una pasarela que une los esquemas. Este enfoque posibilita una arquitectura escalable y flexible para construir APIs complejas.

## Dataloaders

Los Dataloaders son un patrón utilizado en GraphQL para realizar de manera eficiente operaciones de carga de datos en lotes y caché. Ayudan a reducir el número de consultas realizadas a una base de datos u otras fuentes de datos al agrupar las solicitudes de datos. Esto mejora el rendimiento y reduce la probabilidad de cargar datos innecesarios.

## Contribuidores
Breyner Mola - (<breyner.mola.9@gmail.com>)

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.