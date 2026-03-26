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

**Desactivar el entorno:**

```bash
# Windows
.venv\Scripts\deactivate

# Linux / macOS
source .venv/bin/deactivate
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

## Migraciones (Alembic)

Los comandos se ejecutan desde `backend/` con la variable `DATABASE_URL` apuntando a la DB local.
Si usas Docker Compose, la DB expone el puerto `5434` en local.

```bash
export DATABASE_URL=postgresql://jobkit:jobkit@localhost:5434/jobkit
```

### Aplicar migraciones pendientes

```bash
alembic upgrade head
```

### Generar una migración nueva

Después de modificar o agregar un modelo en `app/models/`:

```bash
alembic revision --autogenerate -m "descripcion del cambio"
```

Alembic compara los modelos contra el schema actual de la DB y genera el archivo en `alembic/versions/`.
Revisa el archivo generado antes de aplicarlo.

### Revertir la última migración

```bash
alembic downgrade -1
```

### Ver el historial de migraciones

```bash
alembic history
```

### Ver en qué migración está la DB actualmente

```bash
alembic current
```

---

## Playwright (scraping)

Después de instalar las dependencias, instala los navegadores de Playwright:

```bash
playwright install chromium
```
