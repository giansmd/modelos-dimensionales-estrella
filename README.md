# 🎯 Generador de Modelos Dimensionales en Estrella (Constelación)

Aplicación interactiva y generador de gráficos vectoriales en SVG y PNG de alta definición. Permite diseñar, personalizar y exportar diagramas radiales con el nuevo diseño profesional inspirado en presentaciones corporativas (Capturas 2, 3 y 4).

---

## 🎨 Características del Nuevo Diseño

1. **Sin panel lateral**: Se elimina el cuadro lateral amarillo de versiones previas.
2. **Cuadro Inferior Central de Medidas**:
   - Ubicado directamente debajo del centro de la estrella.
   - Fondo en azul suave corporativo (`#d3dfee`).
   - Admite hasta un **máximo de 3 medidas**, con viñetas de verificación nítidas (`✔`).
3. **Flechas estilizadas con relieve / doble trazo**:
   - Color azul acero (`#4f81bd`), tallo compuesto hueco y puntas triangulares prominentes.
4. **Etiquetas de Dimensiones en Cuadros Delimitados**:
   - Cuadros blancos con borde cian / turquesa (`#4bacc6`) y texto en mayúsculas negrita.
5. **Título Principal Centrado**:
   - En azul brillante (`#5b9bd5`), tipografía moderna y limpia.
6. **Plantillas Rápidas Preconfiguradas (1-Click)**:
   - **Servicio sin Incidencia** (Captura 2).
   - **Aceptación de Consumo Adicional** (Captura 3).
   - **Satisfacción del Cliente** (Captura 4).
   - **Análisis Dimensional de Buyers**.

---

## 🚀 Cómo Usar la Aplicación

### Opción 1: Directo en el Navegador
Abre el archivo **`index.html`** directamente en Chrome, Edge o Firefox. Funciona 100% offline.

### Opción 2: Servidor Local
Haz doble clic en **`iniciar_app.bat`** o ejecuta:
```bash
python server.py
```
Se abrirá automáticamente en `http://localhost:8000/index.html`.

### Opción 3: Generación por Script de Consola
```bash
python generar_diagrama_exacto.py
```
Genera `diagrama_exacto.svg`.

---

## 🖱️ Interactividad y Edición en Tiempo Real

- **Arrastre directo en el lienzo**: Haz clic y arrastra cualquier cuadro de dimensión, etiqueta de marca o el cuadro de medidas.
- **Pestaña Dimensiones**: Añade o elimina dimensiones, cambia ángulos, agrega marcas/atributos jerárquicos y ajústalos con los botones de micro-desplazamiento (◀ ▶ ▲ ▼).
- **Pestaña Medidas**: Añade, edita o elimina medidas (con tope automático en 3 medidas).
- **Pestaña Estilos y Calco**: Compara con el slider de opacidad contra las capturas originales (2, 3 y 4).
- **Exportación**:
  - 📋 **Copiar Imagen**: Copia en 300 DPI al portapapeles para pegar en PowerPoint/Word (`Ctrl+V`).
  - 📥 **Descargar PNG**: Descarga imagen HD.
  - 📐 **Descargar SVG**: Descarga archivo vectorial editable.
