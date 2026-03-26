# F6. Notificaciones

> Alertas cuando hay vacantes nuevas relevantes encontradas por búsquedas programadas.

---

## F6.1 — Notificación en la app

- Badge / indicador visual de nuevas vacantes con score alto
- Lista de "nuevas desde tu última visita"
- Filtrable por umbral mínimo de score
- Se activa cuando una búsqueda programada (F2.5) encuentra resultados

## F6.2 — Notificación por email (V2 — segunda fase)

- Enviar resumen por email con nuevas vacantes de buen match
- Configurable:
  - Frecuencia (inmediata, resumen diario, semanal)
  - Umbral mínimo de score para notificar
- *No es parte del MVP, se implementa después*

---

## Notas de implementación

- F6.1: estado de "visto/no visto" en el modelo de vacante, badge en el frontend
- F6.2: integración con servicio de email (SendGrid, SES, o SMTP directo) — fase posterior
