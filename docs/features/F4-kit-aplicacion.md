# F4. Kit de Aplicación

> Por cada vacante seleccionada, genera un paquete completo de materiales de aplicación personalizados.

---

## F4.1 — CV optimizado

- Toma el perfil completo del usuario y lo **adapta/reordena** para la vacante específica
- **Enfatiza** skills y experiencia relevantes para el puesto
- **Minimiza** información irrelevante sin eliminarla
- Usa el **template de CV del usuario** (diseño replicado de un PDF estático existente)
- El diseño es fijo, solo cambia el contenido/texto

**Output:**
- **PDF** listo para enviar al reclutador
- **HTML editable** para que el usuario pueda hacer ajustes manuales antes de exportar

## F4.2 — Mensaje al reclutador (email formal)

Genera un email profesional con:
- **Asunto** relevante y atractivo
- **Saludo** personalizado (nombre del reclutador si está disponible)
- **Cuerpo** argumentativo: por qué eres buen fit para el puesto
- **Cierre** con call-to-action
- Tono: profesional pero cercano
- Personalizado con nombre de la empresa y puesto específico

## F4.3 — Mensaje corto (LinkedIn/InMail)

- Mensaje breve y directo (~300 caracteres)
- Para usar como:
  - Nota en solicitud de conexión de LinkedIn
  - InMail
- Debe captar atención y generar interés en tu perfil

## F4.4 — Análisis de fortalezas y debilidades

- **Puntos a favor**: qué aspectos de tu perfil hacen buen match con la vacante
  - Skills técnicos relevantes
  - Experiencia aplicable
  - Certificaciones/educación que piden
- **Puntos en contra**: qué falta o es débil respecto a lo que piden
  - Skills que no tienes
  - Experiencia insuficiente en algo específico
  - Requisitos que no cumples
- Presentación clara y accionable (no solo listar, sino contextualizar)

## F4.5 — Guía de estudio / cierre de brechas

Por cada gap identificado en F4.4, generar:

| Campo | Descripción |
|---|---|
| **Tema** | Qué necesitas aprender/mejorar |
| **Prioridad** | Crítico para el puesto / nice-to-have / diferenciador |
| **Recursos sugeridos** | Temas y áreas de estudio (no URLs específicas) |
| **Tiempo estimado** | Estimación de tiempo para cubrir la brecha |
| **Impacto** | Cómo mejora tu candidatura al cubrir este gap |

---

## Notas de implementación

- Chain CV: `backend/app/services/ai/chains/cv_chain.py`
- Chain mensajes: `backend/app/services/ai/chains/message_chain.py`
- Chain gaps: `backend/app/services/ai/chains/gap_chain.py`
- Modelo kit: `backend/app/models/kit.py`
- Task de Celery: `backend/app/workers/kit_task.py`
- API: `backend/app/api/routes/kit.py`
- UI: `frontend/src/pages/Kit.tsx`
- Generación PDF: replicar diseño del PDF estático del usuario programáticamente (weasyprint, puppeteer, o similar)
