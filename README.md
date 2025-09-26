# Actividad: API sencilla de Login con FastAPI

## Objetivo

Implementar una API REST mínima con FastAPI que permita realizar el proceso de login contra una base de datos embebida (db "quemada" en código) usando SQLModel. El objetivo es comprender la estructura básica de una API de autenticación (sin complejidades como tokens obligatorios).

## Requisitos

- Python 3.10+ recomendado.
- Usar SQLModel.
- No es necesario implementar JWT o sesiones; basta validar usuario/contraseña y devolver resultado apropiado.
- Mantener la DB "quemada" en código (crear un usuario de ejemplo al iniciar).

## Instalación

1. Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_PROYECTO>
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

Ejecuta la aplicación con Uvicorn:
```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`.

## Documentación de la API

Accede a la documentación interactiva en `http://127.0.0.1:8000/docs` (Swagger UI).

### Endpoint de Login

- **URL**: `/login`
- **Método**: POST
- **Cuerpo de la solicitud** (JSON):
  ```json
  {
     "username": "usuario_ejemplo",
     "password": "password_ejemplo"
  }
  ```
- **Respuesta exitosa** (200):
  ```json
  {
     "message": "Login exitoso"
  }
  ```
- **Respuesta de error** (401):
  ```json
  {
     "detail": "Credenciales inválidas"
  }
  ```

## Ejemplos de Ejecución

### Ejemplo 1: Login exitoso
```bash
curl -X POST "http://127.0.0.1:8000/login" \
      -H "Content-Type: application/json" \
      -d '{"username": "usuario_ejemplo", "password": "password_ejemplo"}'
```
Respuesta:
```json
{"message": "Login exitoso"}
```

### Ejemplo 2: Login fallido
```bash
curl -X POST "http://127.0.0.1:8000/login" \
      -H "Content-Type: application/json" \
      -d '{"username": "usuario_invalido", "password": "password_invalido"}'
```
Respuesta:
```json
{"detail": "Credenciales inválidas"}
```

## Archivos Principales

- `main.py`: Código principal de la API.
- `requirements.txt`: Dependencias del proyecto.
- `README.md`: Este archivo.

## Entregables

- Repositorio en GitHub/GitLab con el código.
- Archivos principales: main.py, requirements.txt, README.md.
- Ejemplos de ejecución en README.md.