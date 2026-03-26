# F3. Matching con IA

> Analiza cada vacante contra el perfil del usuario y genera un score desglosado de compatibilidad.

---

## F3.1 — Score desglosado

Cada vacante recibe un análisis con los siguientes scores (0-100):

| Categoría | Qué evalúa |
|---|---|
| **Score global** | Ponderación de todas las categorías |
| **Skills técnicos** | Match entre skills del perfil vs skills requeridos en la vacante |
| **Experiencia** | Años de experiencia y nivel de seniority vs lo solicitado |
| **Educación** | Títulos y certificaciones vs requisitos académicos |
| **Idiomas** | Idiomas del perfil vs idiomas requeridos |
| **Preferencias** | Salario ofrecido vs deseado, modalidad, ubicación |

Los pesos de cada categoría en el score global son configurables (ver F7.2).

## F3.2 — Clasificación automática

Basada en el score global, cada vacante se clasifica en:

| Clasificación | Rango default | Significado |
|---|---|---|
| **Aplica ya** | 80 — 100 | Excelente match, no esperes |
| **Buen match** | 60 — 79 | Buen fit, vale la pena |
| **Estudia primero** | 40 — 59 | Hay gaps pero es alcanzable |
| **Descarta** | 0 — 39 | No es buen fit actualmente |

Los umbrales son configurables (ver F7.2).

## F3.3 — Explicación del match

Para cada vacante analizada, la IA genera:

- **Resumen**: explicación breve (2-3 oraciones) de por qué el score es alto o bajo
- **Skills que hacen match**: tecnologías/herramientas que tienes y que piden
- **Gaps**: skills que piden y no tienes (input para la guía de estudio F4.5)
- **Diferenciadores**: skills que tienes y no piden (bonus que te destacan)

---

## Notas de implementación

- Chain de LangChain: `backend/app/services/ai/chains/match_chain.py`
- Input: perfil del usuario + datos de la vacante
- Output: JSON estructurado con scores, clasificación y explicación
- Se ejecuta como parte del scrape task o como task independiente
- Usa el LLM configurado en `.env` via `llm_factory.py`
