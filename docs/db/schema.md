# Database Schema — Job Kit Machine

> PostgreSQL · SQLModel (SQLAlchemy) · Single-user

---

## Diagrama de relaciones

```
profile (1) ─┬── (N) work_experience
              ├── (N) skill
              ├── (N) education
              ├── (N) certification
              ├── (N) course
              ├── (N) language
              └── (1) job_preference

search (1) ──── (N) search_job ──── (N) job

job (1) ─┬── (1) match_result     (scores + explicación)
         └── (N) kit

config (singleton)
notification (N) ── job
```

---

## Tablas

### `profile`

Singleton (siempre `id = 1`). Información personal del usuario (F1.1).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | Siempre 1 |
| `full_name` | `VARCHAR(200)` | |
| `email` | `VARCHAR(200)` | |
| `phone` | `VARCHAR(50)` | Nullable |
| `city` | `VARCHAR(100)` | Nullable |
| `state` | `VARCHAR(100)` | Nullable |
| `country` | `VARCHAR(100)` | Default "México" |
| `linkedin_url` | `VARCHAR(500)` | Nullable |
| `github_url` | `VARCHAR(500)` | Nullable |
| `portfolio_url` | `VARCHAR(500)` | Nullable |
| `other_links` | `JSON` | `[]` — lista de `{label, url}` |
| `created_at` | `TIMESTAMPTZ` | |
| `updated_at` | `TIMESTAMPTZ` | |

---

### `work_experience`

Experiencia laboral del usuario (F1.2).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `profile_id` | `INTEGER FK → profile.id` | |
| `company` | `VARCHAR(200)` | |
| `job_title` | `VARCHAR(200)` | |
| `start_date` | `DATE` | |
| `end_date` | `DATE` | Null = puesto actual |
| `is_current` | `BOOLEAN` | Default false |
| `description` | `TEXT` | Responsabilidades y logros |
| `technologies` | `JSON` | `["React", "Python", ...]` |
| `sort_order` | `INTEGER` | Para ordenamiento manual |
| `created_at` | `TIMESTAMPTZ` | |
| `updated_at` | `TIMESTAMPTZ` | |

---

### `skill`

Skills técnicos del usuario (F1.3).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `profile_id` | `INTEGER FK → profile.id` | |
| `name` | `VARCHAR(100)` | |
| `level` | `VARCHAR(20)` | `básico / intermedio / avanzado / experto` |
| `years_experience` | `SMALLINT` | Nullable |
| `category` | `VARCHAR(50)` | `lenguaje / framework / base_de_datos / herramienta / cloud / otro` |
| `created_at` | `TIMESTAMPTZ` | |

---

### `education`

Títulos académicos (F1.4).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `profile_id` | `INTEGER FK → profile.id` | |
| `institution` | `VARCHAR(200)` | |
| `degree` | `VARCHAR(200)` | Título obtenido |
| `start_date` | `DATE` | Nullable |
| `end_date` | `DATE` | Nullable |
| `created_at` | `TIMESTAMPTZ` | |

---

### `certification`

Certificaciones profesionales (F1.4).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `profile_id` | `INTEGER FK → profile.id` | |
| `name` | `VARCHAR(200)` | |
| `issuer` | `VARCHAR(200)` | |
| `obtained_date` | `DATE` | Nullable |
| `verification_url` | `VARCHAR(500)` | Nullable |
| `created_at` | `TIMESTAMPTZ` | |

---

### `course`

Cursos relevantes (F1.4).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `profile_id` | `INTEGER FK → profile.id` | |
| `name` | `VARCHAR(200)` | |
| `platform` | `VARCHAR(200)` | Plataforma o emisor |
| `created_at` | `TIMESTAMPTZ` | |

---

### `language`

Idiomas del usuario (F1.5).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `profile_id` | `INTEGER FK → profile.id` | |
| `name` | `VARCHAR(100)` | Ej: "Español", "English" |
| `level` | `VARCHAR(20)` | `A1 / A2 / B1 / B2 / C1 / C2 / nativo` |
| `created_at` | `TIMESTAMPTZ` | |

---

### `job_preference`

Preferencias laborales — 1:1 con profile (F1.6).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `profile_id` | `INTEGER FK → profile.id` | UNIQUE |
| `salary_min` | `INTEGER` | Nullable |
| `salary_max` | `INTEGER` | Nullable |
| `salary_currency` | `VARCHAR(10)` | Default "MXN" |
| `modalities` | `JSON` | `["remoto", "híbrido"]` |
| `preferred_locations` | `JSON` | `["CDMX", "Guadalajara"]` |
| `contract_types` | `JSON` | `["tiempo_completo", "freelance"]` |
| `willing_to_relocate` | `BOOLEAN` | Default false |
| `created_at` | `TIMESTAMPTZ` | |
| `updated_at` | `TIMESTAMPTZ` | |

---

### `search`

Búsquedas de vacantes ejecutadas o programadas (F2.1, F2.5).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `job_title` | `VARCHAR(200)` | Título buscado |
| `location` | `VARCHAR(200)` | Nullable |
| `modality` | `VARCHAR(20)` | `remoto / híbrido / presencial` — Nullable |
| `keywords` | `JSON` | `["python", "senior"]` |
| `platforms` | `JSON` | `["indeed", "linkedin"]` |
| `is_scheduled` | `BOOLEAN` | Default false |
| `schedule_cron` | `VARCHAR(100)` | Expresión cron — Nullable |
| `schedule_active` | `BOOLEAN` | Default false |
| `last_run_at` | `TIMESTAMPTZ` | Nullable |
| `next_run_at` | `TIMESTAMPTZ` | Nullable |
| `status` | `VARCHAR(20)` | `pending / running / completed / failed` |
| `jobs_found` | `INTEGER` | Conteo de resultados — Default 0 |
| `created_at` | `TIMESTAMPTZ` | |
| `updated_at` | `TIMESTAMPTZ` | |

---

### `job`

Vacantes encontradas por scraping (F2.3, F5.1).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `title` | `VARCHAR(300)` | Título del puesto |
| `company` | `VARCHAR(200)` | |
| `location` | `VARCHAR(200)` | Ciudad/país o "Remoto" |
| `modality` | `VARCHAR(20)` | `remoto / híbrido / presencial` — Nullable |
| `description` | `TEXT` | Descripción completa de la oferta |
| `requirements` | `TEXT` | Skills, experiencia, educación requeridos — Nullable |
| `salary_min` | `INTEGER` | Nullable |
| `salary_max` | `INTEGER` | Nullable |
| `salary_currency` | `VARCHAR(10)` | Nullable |
| `published_at` | `DATE` | Fecha de publicación en la plataforma |
| `platform` | `VARCHAR(20)` | Plataforma principal: `indeed / linkedin / computrabajo / occ` |
| `source_url` | `VARCHAR(1000)` | URL original de la vacante |
| `status` | `VARCHAR(20)` | Ver estados abajo — Default `nueva` |
| `found_at` | `TIMESTAMPTZ` | Cuándo se encontró por scraping |
| `seen_at` | `TIMESTAMPTZ` | Cuándo el usuario la vio — Nullable |
| `created_at` | `TIMESTAMPTZ` | |
| `updated_at` | `TIMESTAMPTZ` | |

**Estados de `job.status`** (F5.1):

| Estado | Descripción |
|---|---|
| `nueva` | Recién encontrada, sin revisar |
| `vista` | El usuario la vio pero no tomó acción |
| `kit_generado` | Se generó un kit de aplicación |
| `aplicada` | El usuario aplicó a esta vacante |
| `descartada` | El usuario decidió no aplicar |
| `entrevista` | Recibió respuesta / tiene entrevista |
| `rechazada` | No fue seleccionado |

**Índices:**
- `ix_job_status` — filtro por estado
- `ix_job_platform` — filtro por plataforma
- `ux_job_source_url` — UNIQUE en `source_url`, previene duplicados por URL
- `ux_job_company_title` — UNIQUE en `(company, title)`, previene duplicados por empresa+título

---

### `search_job`

Tabla puente: qué vacantes se encontraron en cada búsqueda (N:N).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `search_id` | `INTEGER FK → search.id` | ON DELETE CASCADE |
| `job_id` | `INTEGER FK → job.id` | ON DELETE CASCADE |

**Unique constraint:** `(search_id, job_id)`

---

### `match_result`

Score de matching IA — 1:1 con job (F3.1, F3.2, F3.3).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `job_id` | `INTEGER FK → job.id` | UNIQUE, ON DELETE CASCADE |
| `score_overall` | `SMALLINT` | 0–100 |
| `score_skills` | `SMALLINT` | 0–100 |
| `score_experience` | `SMALLINT` | 0–100 |
| `score_education` | `SMALLINT` | 0–100 |
| `score_languages` | `SMALLINT` | 0–100 |
| `score_preferences` | `SMALLINT` | 0–100 |
| `classification` | `VARCHAR(20)` | `aplica_ya / buen_match / estudia_primero / descarta` |
| `summary` | `TEXT` | Explicación breve del score |
| `matching_skills` | `JSON` | `["React", "Python", ...]` |
| `gap_skills` | `JSON` | `["Kubernetes", "AWS", ...]` |
| `differentiators` | `JSON` | `["Docker", "CI/CD", ...]` |
| `raw_response` | `JSON` | Respuesta completa del LLM (debug) — Nullable |
| `created_at` | `TIMESTAMPTZ` | |

**Índices:**
- `ix_match_score_overall` — ordenar por score
- `ix_match_classification` — filtro por clasificación

---

### `kit`

Kit de aplicación generado para una vacante (F4, F5.2).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `job_id` | `INTEGER FK → job.id` | ON DELETE CASCADE |
| `version` | `SMALLINT` | Default 1 — incrementa al regenerar |
| `cv_html` | `TEXT` | CV optimizado en HTML |
| `cv_pdf_path` | `VARCHAR(500)` | Ruta al archivo PDF generado — Nullable |
| `email_subject` | `VARCHAR(300)` | Asunto del email — Nullable |
| `email_body` | `TEXT` | Mensaje al reclutador — Nullable |
| `short_message` | `TEXT` | Mensaje corto LinkedIn/InMail — Nullable |
| `strengths` | `JSON` | Puntos a favor — Nullable |
| `weaknesses` | `JSON` | Puntos en contra — Nullable |
| `study_guide` | `JSON` | Lista de gaps con prioridad, recursos, tiempo, impacto — Nullable |
| `raw_response` | `JSON` | Respuesta completa del LLM (debug) — Nullable |
| `created_at` | `TIMESTAMPTZ` | |

**Índice:**
- `ix_kit_job_version` — `(job_id, version)` para historial de versiones

---

### `notification`

Notificaciones in-app (F6.1).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | |
| `job_id` | `INTEGER FK → job.id` | Nullable, ON DELETE SET NULL |
| `search_id` | `INTEGER FK → search.id` | Nullable — búsqueda que originó la notificación |
| `type` | `VARCHAR(30)` | `new_match / search_completed / kit_ready` |
| `title` | `VARCHAR(200)` | |
| `message` | `TEXT` | Nullable |
| `is_read` | `BOOLEAN` | Default false |
| `created_at` | `TIMESTAMPTZ` | |

---

### `config`

Configuración del sistema — singleton (F7).

| Columna | Tipo | Notas |
|---|---|---|
| `id` | `INTEGER PK` | Siempre 1 |
| `llm_provider` | `VARCHAR(20)` | `ollama / anthropic / openai / google` — Default `ollama` |
| `llm_model` | `VARCHAR(100)` | Modelo específico del proveedor |
| `llm_api_key` | `VARCHAR(500)` | Encrypted — Nullable (no aplica para Ollama) |
| `threshold_apply_now` | `SMALLINT` | Default 80 |
| `threshold_good_match` | `SMALLINT` | Default 60 |
| `threshold_study_first` | `SMALLINT` | Default 40 |
| `weight_skills` | `SMALLINT` | Default 35 (porcentaje) |
| `weight_experience` | `SMALLINT` | Default 25 |
| `weight_education` | `SMALLINT` | Default 15 |
| `weight_languages` | `SMALLINT` | Default 10 |
| `weight_preferences` | `SMALLINT` | Default 15 |
| `cv_template_path` | `VARCHAR(500)` | Ruta al PDF base — Nullable |
| `created_at` | `TIMESTAMPTZ` | |
| `updated_at` | `TIMESTAMPTZ` | |

---

## Notas generales

- **Motor**: PostgreSQL 16+
- **ORM**: SQLModel (combina SQLAlchemy + Pydantic)
- **Migraciones**: Alembic
- **Timestamps**: Todos los `created_at` usan `server_default=func.now()`, los `updated_at` usan `onupdate=func.now()`
- **JSON columns**: Se usa `JSON` de PostgreSQL nativo para listas simples que no necesitan queries complejas. Si en el futuro se necesitan queries sobre estos campos, se pueden normalizar en tablas separadas
- **Soft delete**: No se implementa en MVP. Los registros se eliminan directamente
- **Fase 4 (pgvector)**: Cuando se implemente búsqueda semántica, se agrega una columna `embedding VECTOR(1536)` a la tabla `job` y se crea un índice `ivfflat` o `hnsw`
