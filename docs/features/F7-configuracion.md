# F7. Configuración

> Ajustes del sistema accesibles desde la UI.

---

## F7.1 — Proveedor de IA

- Switch entre proveedores sin reiniciar la app:
  - **Ollama** (local, gratis) — default para desarrollo
  - **Anthropic** (Claude)
  - **OpenAI** (GPT)
  - **Google** (Gemini)
- Modelo específico por proveedor
- Validación de API key al cambiar a proveedor cloud
- Ya diseñado en `.env` + `llm_factory.py`, exponer en UI

## F7.2 — Umbrales de matching

- Configurar los rangos de clasificación automática:
  - "Aplica ya": score mínimo (default: 80)
  - "Buen match": score mínimo (default: 60)
  - "Estudia primero": score mínimo (default: 40)
  - "Descarta": todo lo que quede debajo
- Configurar pesos de cada categoría en el score global:
  - Skills técnicos (default: 35%)
  - Experiencia (default: 25%)
  - Educación (default: 15%)
  - Idiomas (default: 10%)
  - Preferencias (default: 15%)

## F7.3 — Template de CV

- Subir / cambiar el PDF base que se usa como referencia de diseño
- Preview del template actual
- El sistema replica el diseño visual y solo modifica el contenido

---

## Notas de implementación

- Modelo de configuración en DB o archivo JSON persistente
- API: `backend/app/api/routes/config.py`
- UI: página o sección de settings
