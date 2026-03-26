# Job Kit Machine 🧰

Aplicación que automatiza la búsqueda de empleo mediante web scraping en múltiples plataformas, análisis de compatibilidad con IA y generación de un kit de aplicación personalizado por vacante.

---

## ¿Qué hace?

1. **Scraping** — Busca vacantes en LinkedIn, Indeed y otras plataformas en base a tu perfil
2. **Matching con IA** — Analiza cada vacante contra tus habilidades y experiencia
3. **Genera tu kit** por vacante:
   - CV optimizado para la oferta
   - Mensaje/correo para el reclutador
   - Puntos a favor y en contra de tu perfil
   - Guía de estudio para cerrar brechas

---

## Stack

| Capa | Tecnología |
|---|---|
| Frontend | React + TypeScript + Vite + Shadcn/ui |
| Backend | FastAPI + SQLModel |
| IA | LangChain (Ollama / Anthropic / OpenAI / Google) |
| Workers | Celery + Redis |
| Base de datos | PostgreSQL |
| Scraping | Playwright |
| Modelos locales | Ollama |
| Infraestructura | Docker Compose |

---

## Requisitos

- Docker y Docker Compose instalados
- 8 GB de RAM mínimo para correr modelos locales con Ollama
- (Opcional) API keys de Anthropic, OpenAI o Google para usar modelos en la nube

---

## Inicio rápido

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/job-kit.git
cd job-kit
```

### 2. Configurar variables de entorno

```bash
cp .env.example .env
```

Edita `.env` con tu configuración. Por defecto usa Ollama con `llama3.2` para desarrollo local sin costo.

### 3. Levantar el proyecto

```bash
docker compose up --build
```

Esto levanta:
- Frontend en `http://localhost:5173`
- Backend/API en `http://localhost:8000`
- API Docs (Swagger) en `http://localhost:8000/docs`
- Redis en puerto `6379`
- PostgreSQL en puerto `5432`
- Ollama en `http://localhost:11434`

### 4. Descargar modelos locales (primera vez)

```bash
docker compose exec ollama ollama pull llama3.2
docker compose exec ollama ollama pull nomic-embed-text
```

O todos los recomendados de una vez:

```bash
cat ollama/models.txt | xargs -I {} docker compose exec ollama ollama pull {}
```

---

## Cambiar de modelo

El switch de proveedor/modelo se hace exclusivamente en el `.env`, sin tocar código:

```env
# Desarrollo local (gratis)
LLM_PROVIDER=ollama
LLM_MODEL=llama3.2

# Producción con Anthropic
LLM_PROVIDER=anthropic
LLM_MODEL=claude-sonnet-4-20250514
ANTHROPIC_API_KEY=sk-ant-...

# OpenAI
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o
OPENAI_API_KEY=sk-...

# Google
LLM_PROVIDER=google
LLM_MODEL=gemini-1.5-pro
GOOGLE_API_KEY=...
```

---

## Estructura del proyecto

```
job-kit-machine/
├── docker-compose.yml
├── .env.example
├── README.md
│
├── backend/
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── app/
│       ├── main.py
│       ├── core/
│       │   ├── config.py           # Settings y variables de entorno
│       │   └── database.py
│       ├── api/
│       │   └── routes/
│       │       ├── profile.py
│       │       ├── search.py
│       │       └── kit.py
│       ├── services/
│       │   ├── scraper/
│       │   │   ├── base.py         # Interface base para scrapers
│       │   │   ├── indeed.py
│       │   │   └── linkedin.py
│       │   └── ai/
│       │       ├── llm_factory.py  # Switch de modelos por .env
│       │       └── chains/
│       │           ├── match_chain.py      # Análisis fit perfil/vacante
│       │           ├── cv_chain.py         # CV optimizado
│       │           ├── message_chain.py    # Mensaje al reclutador
│       │           └── gap_chain.py        # Brechas + guía de estudio
│       ├── workers/
│       │   ├── celery_app.py
│       │   ├── scrape_task.py
│       │   └── kit_task.py
│       └── models/
│           ├── profile.py
│           ├── job.py
│           └── kit.py
│
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/
│       ├── pages/
│       │   ├── Profile.tsx
│       │   ├── Search.tsx
│       │   ├── Jobs.tsx
│       │   └── Kit.tsx
│       ├── components/
│       ├── hooks/
│       │   └── useJobSearch.ts     # Polling del job de Celery
│       └── api/
│           └── client.ts
│
└── ollama/
    └── models.txt                  # Modelos recomendados para 8GB RAM
```

---

## Variables de entorno

Ver `.env.example` para la lista completa. Las principales:

| Variable | Descripción | Default |
|---|---|---|
| `LLM_PROVIDER` | Proveedor de IA: `ollama`, `anthropic`, `openai`, `google` | `ollama` |
| `LLM_MODEL` | Nombre del modelo a usar | `llama3.2` |
| `DATABASE_URL` | Conexión a PostgreSQL | `postgresql://...` |
| `REDIS_URL` | Conexión a Redis | `redis://redis:6379` |
| `ANTHROPIC_API_KEY` | API key Anthropic (opcional) | — |
| `OPENAI_API_KEY` | API key OpenAI (opcional) | — |
| `GOOGLE_API_KEY` | API key Google (opcional) | — |

---

## Flujo de uso

```
1. Completa tu perfil (skills, experiencia, idiomas, preferencias)
        ↓
2. Inicia una búsqueda (título, ubicación, modalidad)
        ↓
3. El worker de scraping recolecta vacantes en background
        ↓
4. La IA filtra y puntúa cada vacante contra tu perfil
        ↓
5. Seleccionas una vacante que te interese
        ↓
6. La IA genera tu kit: CV + mensaje + análisis + guía
        ↓
7. Descargas o copias los documentos generados
```

---

## Roadmap

- [ ] Scraper LinkedIn
- [ ] Scraper Indeed
- [ ] Perfil de usuario con historial
- [ ] Match chain con puntuación 0-100
- [ ] Generación de CV en PDF
- [ ] Mensaje personalizado al reclutador
- [ ] Análisis de brechas + guía de estudio
- [ ] Historial de vacantes aplicadas
- [ ] Búsqueda semántica en historial (pgvector — v2)

---

## Licencia

MIT

## Comentarios

Si eres un reclutador y estás leyendo esto, quizás este proyecto me ayudo a que llegaras aquí. Esto funciona... y me gustaría que me contrataran. 😁