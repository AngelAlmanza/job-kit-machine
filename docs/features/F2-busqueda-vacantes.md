# F2. Búsqueda de Vacantes (Scraping)

> Busca vacantes en múltiples plataformas en background usando Celery workers + Playwright.

---

## F2.1 — Búsqueda híbrida

- El sistema **sugiere búsquedas** automáticas basadas en el perfil:
  - Skills principales → títulos de puesto probables
  - Ubicación y modalidad preferida
  - Keywords derivadas de la experiencia
- El usuario puede **ajustar, agregar o eliminar** sugerencias antes de ejecutar
- Parámetros de búsqueda:
  - Título del puesto (texto libre)
  - Ubicación
  - Modalidad (remoto / híbrido / presencial)
  - Keywords adicionales
  - Plataformas a buscar (selección múltiple)

## F2.2 — Scrapers por plataforma

| Plataforma | Prioridad | Notas |
|---|---|---|
| **Indeed** | Alta | Scraping más accesible, buen volumen |
| **LinkedIn** | Alta | Requiere manejo de sesión/cookies, protecciones anti-bot |
| **Computrabajo** | Media | Popular en LATAM, especialmente México |
| **OCC Mundial** | Media | Popular en México |

- Interface base (`BaseScraper`) con contrato estándar para agregar nuevas plataformas
- Cada scraper implementa: `search(params) -> list[RawJob]`
- Manejo de rate limiting y retries por plataforma

## F2.3 — Datos extraídos por vacante

Cada vacante scraped debe contener:

| Campo | Requerido | Notas |
|---|---|---|
| Título del puesto | Sí | |
| Empresa | Sí | |
| Ubicación | Sí | Ciudad/país o "Remoto" |
| Modalidad | No | remoto / híbrido / presencial (si disponible) |
| Descripción completa | Sí | Texto completo de la oferta |
| Requisitos | No | Skills, experiencia, educación requeridos |
| Rango salarial | No | Si está publicado |
| Fecha de publicación | Sí | |
| URL original | Sí | Link a la vacante en la plataforma |
| Plataforma de origen | Sí | indeed / linkedin / computrabajo / occ |

## F2.4 — Deduplicación

- Detectar vacantes duplicadas entre plataformas
- Criterio: misma empresa + título similar + ubicación similar
- Unificar en un solo registro, guardar referencia a ambas URLs
- Se ejecuta después de cada ronda de scraping

## F2.5 — Búsquedas programadas

- Configurar búsquedas para ejecutarse automáticamente:
  - Frecuencia: cada X horas, diario, personalizado
  - Parámetros guardados de una búsqueda previa
- Implementación con **Celery Beat** (ya configurado en docker-compose con profile `scheduler`)
- Al encontrar nuevas vacantes con buen match → notificación en la app (ver F6)

---

## Notas de implementación

- Interface base: `backend/app/services/scraper/base.py`
- Scrapers: `backend/app/services/scraper/{platform}.py`
- Modelo de vacante: `backend/app/models/job.py`
- Modelo de búsqueda: `backend/app/models/search.py`
- Task de Celery: `backend/app/workers/scrape_task.py`
- API routes: `backend/app/api/routes/search.py`
- UI: `frontend/src/pages/Search.tsx`
- Scraping con **Playwright** (headless Chromium)
