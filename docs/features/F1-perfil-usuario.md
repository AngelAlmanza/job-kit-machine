# F1. Perfil de Usuario

> Un solo perfil persistente que alimenta todo el sistema: búsquedas, matching y generación de kit.

App single-user (sin autenticación). El perfil es el input principal para todo el flujo.

---

## F1.1 — Información personal

- Nombre completo
- Email
- Teléfono
- Ubicación (ciudad / estado / país)
- Links: LinkedIn, GitHub, portafolio, otros

## F1.2 — Experiencia laboral

- Lista de posiciones con:
  - Empresa
  - Título del puesto
  - Periodo (fecha inicio — fecha fin, o "actual")
  - Descripción de responsabilidades y logros
  - Tecnologías/herramientas usadas en ese puesto
- Ordenadas cronológicamente (más reciente primero)

## F1.3 — Skills técnicos

- Lista de tecnologías/herramientas con:
  - Nivel de dominio: básico / intermedio / avanzado / experto
  - Años de experiencia
  - Categoría: lenguaje, framework, base de datos, herramienta, cloud, etc.

## F1.4 — Educación y certificaciones

- **Títulos académicos**: institución, título obtenido, periodo
- **Certificaciones**: nombre, emisor, fecha de obtención, URL de verificación (opcional)
- **Cursos relevantes**: nombre, plataforma/emisor

## F1.5 — Idiomas

- Lista de idiomas con nivel:
  - Escala CEFR (A1, A2, B1, B2, C1, C2) o equivalente (básico / intermedio / avanzado / nativo)

## F1.6 — Preferencias laborales

- Salario deseado: rango mínimo — máximo, moneda (MXN, USD, etc.)
- Modalidad (selección múltiple): remoto / híbrido / presencial
- Ubicaciones preferidas (si no es 100% remoto)
- Tipo de contrato: tiempo completo, freelance, contrato temporal, medio tiempo
- Disposición a reubicarse: sí / no

---

## Notas de implementación

- Modelo SQLModel en `backend/app/models/profile.py`
- CRUD API en `backend/app/api/routes/profile.py`
- UI en `frontend/src/pages/Profile.tsx`
- Al ser single-user, siempre hay un solo registro de perfil (ID = 1 o singleton)
