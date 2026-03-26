# Backend — Desarrollo local

## Requisitos

- Python 3.12+
- PostgreSQL corriendo (o usar Docker Compose)
- Redis corriendo (o usar Docker Compose)

## Entorno virtual

### Crear e instalar dependencias

```bash
cd backend
python -m venv .venv
```

**Activar el entorno:**

```bash
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

**Instalar dependencias:**

```bash
pip install -e .
```

### Ejecutar el servidor

Con el entorno activado:

```bash
uvicorn app.main:app --reload
```

Sin activar (directo al binario del venv):

```bash
# Windows
.venv\Scripts\uvicorn app.main:app --reload

# Linux / macOS
.venv/bin/uvicorn app.main:app --reload
```

El servidor levanta en `http://localhost:8000`.
Swagger UI disponible en `http://localhost:8000/docs`.

## Variables de entorno

Copia el archivo de ejemplo en la raíz del repo y edítalo:

```bash
cp ../.env.example .env
```

Variables mínimas para desarrollo local:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/jobkit
REDIS_URL=redis://localhost:6379
LLM_PROVIDER=ollama
LLM_MODEL=llama3.2
OLLAMA_BASE_URL=http://localhost:11434
```

## Con Docker Compose (recomendado)

Para levantar todos los servicios de infraestructura (DB, Redis, Ollama) sin instalar nada localmente:

```bash
docker compose up db redis ollama
```

Y luego correr el backend en local con el venv para desarrollo más rápido.

## Playwright (scraping)

Después de instalar las dependencias, instala los navegadores de Playwright:

```bash
playwright install chromium
```
