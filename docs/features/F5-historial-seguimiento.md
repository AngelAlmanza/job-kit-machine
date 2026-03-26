# F5. Historial y Seguimiento

> Registro completo de todas las vacantes encontradas y kits generados para consulta y seguimiento.

---

## F5.1 — Historial de vacantes

- Almacenar **todas** las vacantes encontradas en cada búsqueda
- Por cada vacante se guarda:
  - Datos del scraping (ver F2.3)
  - Score de matching desglosado (ver F3.1)
  - Clasificación automática (ver F3.2)
  - Estado de seguimiento

**Estados de una vacante:**

| Estado | Descripción |
|---|---|
| `nueva` | Recién encontrada, sin revisar |
| `vista` | El usuario la vio pero no tomó acción |
| `kit_generado` | Se generó un kit de aplicación |
| `aplicada` | El usuario aplicó a esta vacante |
| `descartada` | El usuario decidió no aplicar |
| `entrevista` | Recibió respuesta / tiene entrevista |
| `rechazada` | No fue seleccionado |

**Filtros disponibles:**
- Por plataforma de origen
- Por rango de score
- Por estado
- Por fecha de publicación / fecha de hallazgo
- Por búsqueda de texto (título, empresa)

## F5.2 — Historial de kits

- Cada kit generado queda asociado a su vacante
- Poder **regenerar** un kit (con datos actualizados del perfil)
- Poder **descargar** materiales generados previamente (CV PDF, textos)
- Ver historial de versiones si se regeneró

## F5.3 — Dashboard / vista resumen

Estadísticas y vista rápida:

- Total de vacantes encontradas
- Total de kits generados
- Tasa de match promedio
- Distribución por clasificación (cuántas "Aplica ya", "Buen match", etc.)
- Vacantes recientes con buen match (top 5-10)
- Estado de búsquedas programadas (activas, última ejecución, próxima)

---

## Notas de implementación

- Modelos: `backend/app/models/job.py` (campo `status`), `backend/app/models/kit.py`
- API: endpoints de listado con filtros, paginación
- UI: `frontend/src/pages/Jobs.tsx` (lista + filtros), dashboard en página principal
