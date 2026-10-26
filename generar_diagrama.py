"""
generar_diagrama.py
===================
Genera el diagrama 'ANÁLISIS DIMENSIONAL CONFORMADO DE BUYERS' utilizando Matplotlib.
Reproduce con la máxima fidelidad visual el diseño del diagrama radial de dimensiones
y el panel lateral de indicadores y medidas, exportando en formatos PNG (300 DPI) y SVG.

Requisitos:
    pip install matplotlib

Ejecución:
    python generar_diagrama.py
"""

import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


# ==============================================================================
# CONFIGURACIÓN DE TIPOGRAFÍA Y ESTILOS GLOBALES
# ==============================================================================

# Tipografía sans-serif limpia y nítida
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans', 'Liberation Sans']
plt.rcParams['font.family'] = 'sans-serif'


# ==============================================================================
# PALETA DE COLORES
# ==============================================================================

# Colores extraídos fielmente de la captura de referencia
COLOR_BG = "#FFFFFF"               # Fondo blanco del lienzo
COLOR_TITLE = "#1B2A4A"            # Azul oscuro marino para títulos y nombres de dimensiones
COLOR_SUBTITLE = "#64748B"         # Gris azulado para subtítulo
COLOR_AXIS = "#334155"             # Color slate oscuro para líneas de eje y flechas
COLOR_TICKS = "#334155"            # Marcas transversales sobre los ejes
COLOR_ATTR_TEXT = "#5A6B82"        # Texto de los atributos de cada dimensión
COLOR_CENTER_DOT = "#1B2A4A"       # Punto central de convergencia

# Estilos del panel de indicadores y medidas (derecha)
COLOR_PANEL_BG = "#FFF8C9"         # Fondo amarillo suave del panel (#FFF8C9)
COLOR_PANEL_BORDER = "#6F7683"     # Borde gris azulado del panel
COLOR_PANEL_TITLE = "#1B2A4A"      # Título 'INDICADORES Y MEDIDAS'
COLOR_PANEL_SEP = "#6F7683"        # Separador horizontal bajo el título del panel
COLOR_CARD_BG = "#FFFFFF"          # Fondo blanco de las tarjetas interiores
COLOR_CARD_BORDER = "#E8E1BC"      # Borde sutil redondeado de las tarjetas
COLOR_CARD_TITLE = "#1B2A4A"       # Título de cada tarjeta
COLOR_MEDIDAS_LABEL = "#C5A038"    # Etiqueta 'Medidas' en tono dorado/ocre cálido
COLOR_MEASURE_ITEM = "#5A6B82"     # Texto de las medidas individuales


# ==============================================================================
# DEFINICIÓN DE DATOS DEL DIAGRAMA DIMENSIONAL
# ==============================================================================

# Coordenadas cartesianas del punto central de convergencia (x=273.3, y=477-252=225)
CENTER_X = 273.3
CENTER_Y = 225.0

# Estructura modular de dimensiones:
# Permite modificar ángulos, longitudes, marcas y posición individual de cada etiqueta.
# - name: Nombre en negrita de la dimensión
# - angle_deg: Ángulo en grados respecto a la horizontal (0° derecha, 90° arriba, 180° izquierda, 270° abajo)
# - length: Longitud del eje desde el centro hasta la punta de la flecha
# - label_offset: Desplazamiento (dx, dy) de la etiqueta del nombre de la dimensión
# - label_align: Alineación horizontal ('ha') y vertical ('va')
# - ticks: Posiciones relativas (ratio 0.0 a 1.0) sobre el eje para las marcas transversales
# - attributes: Atributos individuales con posición (ratio), offset (dx, dy) y alineación
DIMENSIONS = [
    {
        "name": "DIM_FECHA",
        "angle_deg": 90.0,
        "length": 173.0,
        "label_offset": (0.0, 15.0),
        "label_align": {"ha": "center", "va": "bottom"},
        "ticks": [0.202, 0.405, 0.607, 0.809],
        "attributes": [
            {"text": "dia", "pos_ratio": 0.202, "offset": (7.0, 0.0), "ha": "left", "va": "center"},
            {"text": "mes", "pos_ratio": 0.405, "offset": (7.0, 0.0), "ha": "left", "va": "center"},
            {"text": "trimestre", "pos_ratio": 0.607, "offset": (7.0, 0.0), "ha": "left", "va": "center"},
            {"text": "año", "pos_ratio": 0.809, "offset": (7.0, 0.0), "ha": "left", "va": "center"},
        ]
    },
    {
        "name": "DIM_BUYER",
        "angle_deg": 45.0,
        "length": 173.0,
        "label_offset": (23.0, 13.0),
        "label_align": {"ha": "left", "va": "bottom"},
        "ticks": [0.38],
        "attributes": [
            {
                "text": "Tipo de Buyer (FK a DIM_TIPO_BUYER)",
                "pos_ratio": 0.38,
                "offset": (75.0, 53.0),
                "ha": "center",
                "va": "center"
            }
        ]
    },
    {
        "name": "DIM_TIPO_BUYER",
        "angle_deg": 0.0,
        "length": 224.0,
        "label_offset": (-10.0, 21.0),
        "label_align": {"ha": "center", "va": "bottom"},
        "ticks": [0.335, 0.670],
        "attributes": [
            {"text": "Código", "pos_ratio": 0.335, "offset": (26.0, -14.0), "ha": "center", "va": "top"},
            {"text": "Nombre", "pos_ratio": 0.670, "offset": (24.0, -14.0), "ha": "center", "va": "top"},
        ]
    },
    {
        "name": "DIM_CAMPANA",
        "angle_deg": -41.6,
        "length": 189.0,
        "label_offset": (14.0, -18.0),
        "label_align": {"ha": "center", "va": "top"},
        "ticks": [0.20, 0.40, 0.60, 0.80],
        "attributes": [
            {"text": "nombre", "pos_ratio": 0.20, "offset": (-8.0, -6.0), "ha": "center", "va": "top"},
            {"text": "fuente_utm", "pos_ratio": 0.40, "offset": (13.0, -13.0), "ha": "center", "va": "top"},
            {
                "text": "plato_gancho (platos.nombre)",
                "pos_ratio": 0.60,
                "offset": (41.0, -27.0),
                "ha": "center",
                "va": "top"
            },
            {
                "text": "tipo_buyer_objetivo (tipos_buyer.nombre)",
                "pos_ratio": 0.80,
                "offset": (46.0, -24.0),
                "ha": "center",
                "va": "top"
            },
        ]
    },
    {
        "name": "DIM_PRODUCTO",
        "angle_deg": -90.0,
        "length": 180.0,
        "label_offset": (35.0, -9.0),
        "label_align": {"ha": "center", "va": "top"},
        "ticks": [0.20, 0.40, 0.60, 0.80],
        "attributes": [
            # La marca en 0.20 no posee texto según la captura de referencia
            {
                "text": "categoría: platos, bebidas,\nguarniciones, postres",
                "pos_ratio": 0.40,
                "offset": (-48.0, 0.0),
                "ha": "right",
                "va": "center"
            },
            {"text": "precio_base", "pos_ratio": 0.60, "offset": (-48.0, 0.0), "ha": "right", "va": "center"},
            {"text": "es_gancho_promocional", "pos_ratio": 0.80, "offset": (-48.0, 0.0), "ha": "right", "va": "center"},
        ]
    },
    {
        "name": "DIM_PERSONAL",
        "angle_deg": 199.5,
        "length": 193.0,
        "label_offset": (-16.0, 1.0),
        "label_align": {"ha": "right", "va": "center"},
        "ticks": [0.20, 0.40, 0.60, 0.80],
        "attributes": [
            {"text": "nombre", "pos_ratio": 0.60, "offset": (0.0, 0.0), "ha": "center", "va": "center"},
        ],
        # Columna de atributos en el extremo izquierdo alineados sobre DIM_PERSONAL tal como en la captura
        "column_attributes": {
            "items": [
                {"text": "nombres", "x": 58.0, "y": 214.0, "ha": "center"},
                {"text": "apellidos", "x": 58.0, "y": 198.0, "ha": "center"},
                {"text": "cargo", "x": 54.0, "y": 182.0, "ha": "center"},
                # NOTA EDITABLE: En la captura original se observa 'área (area_empresa.nombre)'.
                # Puede modificarse fácilmente aquí a 'área (core_empresa.nombre)' si se desea.
                {"text": "área (area_empresa.nombre)", "x": 77.0, "y": 167.0, "ha": "center"}
            ]
        }
    },
    {
        "name": "DIM_CANAL",
        "angle_deg": 180.0,
        "length": 220.0,
        "label_offset": (-8.0, 21.0),
        "label_align": {"ha": "center", "va": "bottom"},
        "ticks": [0.341, 0.673],
        "attributes": [
            {"text": "Descripción", "pos_ratio": 0.341, "offset": (20.0, -14.0), "ha": "center", "va": "top"},
            {"text": "Código", "pos_ratio": 0.673, "offset": (21.0, -14.0), "ha": "center", "va": "top"},
        ]
    },
    {
        "name": "DIM_RED_SOCIAL",
        "angle_deg": 145.1,
        "length": 187.0,
        "label_offset": (-28.0, 1.0),
        "label_align": {"ha": "right", "va": "bottom"},
        "ticks": [0.25, 0.50, 0.75],
        "attributes": [
            {"text": "url_página", "pos_ratio": 0.25, "offset": (-54.0, 0.0), "ha": "center", "va": "center"},
            {"text": "nombre_página", "pos_ratio": 0.50, "offset": (-20.0, -8.0), "ha": "center", "va": "top"},
            {"text": "plataforma", "pos_ratio": 0.75, "offset": (-8.0, -14.0), "ha": "center", "va": "top"},
        ]
    },
    {
        "name": "DIM_ANUNCIO",
        "angle_deg": 121.4,
        "length": 194.5,
        "label_offset": (-20.0, -1.0),
        "label_align": {"ha": "right", "va": "bottom"},
        "ticks": [0.25, 0.45, 0.66, 0.86],
        "attributes": [
            {"text": "horario_fin", "pos_ratio": 0.25, "offset": (-4.0, -2.0), "ha": "right", "va": "center"},
            {"text": "horario_inicio", "pos_ratio": 0.45, "offset": (2.0, 0.0), "ha": "left", "va": "center"},
            {"text": "texto_cta", "pos_ratio": 0.66, "offset": (7.0, 0.0), "ha": "left", "va": "center"},
            {"text": "nombre", "pos_ratio": 0.86, "offset": (7.0, 4.0), "ha": "left", "va": "center"},
        ]
    }
]


# ==============================================================================
# DEFINICIÓN DE DATOS DEL PANEL DERECHO (INDICADORES Y MEDIDAS)
# ==============================================================================

PANEL_CONFIG = {
    "box": {"x": 569.0, "y": 19.0, "width": 211.0, "height": 409.0, "radius": 12.0},
    "title": "INDICADORES Y MEDIDAS",
    "title_pos": (674.5, 411.0),
    "separator": {"x1": 634.0, "x2": 715.0, "y": 404.0},
    "card_x": 580.0,
    "card_width": 191.0,
    "card_radius": 8.0,
    "cards": [
        {
            "id": "card_cpl",
            "title": "Costo por LEAD (CPL)",
            "y": 325.0,
            "height": 76.0,
            "measures": [
                "•  importe_gastado",
                "•  leads_convertidos"
            ]
        },
        {
            "id": "card_twf",
            "title": "Inicio de WhatsApp tras formulario (TWF)",
            "y": 241.0,
            "height": 77.0,
            "measures": [
                "•  formularios_enviados",
                # En la captura original se observa 'inicio_whatsapp'
                "•  inicio_whatsapp"
            ]
        },
        {
            "id": "card_trc",
            "title": "Rescate de conversaciones (TRC)",
            "y": 145.0,
            "height": 89.0,
            "measures": [
                "•  sesiones_iniciadas",
                "•  sesiones_abandonadas",
                "•  rescates_enviados",
                "•  sesiones_rescatadas"
            ]
        },
        {
            "id": "card_b1",
            "title": "Conversión BUYER a LEAD (B1)",
            "y": 61.0,
            "height": 77.0,
            "measures": [
                "•  buyers_captados",
                "•  leads_convertidos"
            ]
        }
    ]
}


# ==============================================================================
# FUNCIONES DE RENDERIZADO MODULARES
# ==============================================================================

def draw_dimension_axis(ax, dim, center_x=CENTER_X, center_y=CENTER_Y, tick_half_length=3.5):
    """
    Dibuja un eje radial completo con:
    1. Flecha con punta triangular desde el centro hacia afuera.
    2. Marcas transversales perpendiculares en cada posición relativa.
    3. Etiquetas de atributos colocadas horizontalmente y con ajustes individuales.
    4. Nombre de la dimensión en negrita cerca de la punta.
    """
    angle_rad = math.radians(dim["angle_deg"])
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    length = dim["length"]

    tip_x = center_x + length * cos_a
    tip_y = center_y + length * sin_a

    # Vector normal unitario perpendicular a la dirección del eje (-sin(a), cos(a))
    norm_x = -sin_a
    norm_y = cos_a

    # 1. Flecha principal del eje
    arrow = FancyArrowPatch(
        (center_x, center_y), (tip_x, tip_y),
        arrowstyle="-|>",
        mutation_scale=12.0,
        color=COLOR_AXIS,
        linewidth=1.3,
        zorder=2
    )
    ax.add_patch(arrow)

    # 2. Marcas transversales perpendiculares
    for ratio in dim.get("ticks", []):
        tx = center_x + ratio * length * cos_a
        ty = center_y + ratio * length * sin_a
        x0 = tx - tick_half_length * norm_x
        y0 = ty - tick_half_length * norm_y
        x1 = tx + tick_half_length * norm_x
        y1 = ty + tick_half_length * norm_y

        ax.plot([x0, x1], [y0, y1], color=COLOR_TICKS, linewidth=1.1, zorder=3)

    # 3. Etiquetas de atributos
    for attr in dim.get("attributes", []):
        ratio = attr["pos_ratio"]
        base_x = center_x + ratio * length * cos_a
        base_y = center_y + ratio * length * sin_a
        dx, dy = attr.get("offset", (0.0, 0.0))

        ax.text(
            base_x + dx,
            base_y + dy,
            attr["text"],
            fontsize=8.5,
            color=COLOR_ATTR_TEXT,
            ha=attr.get("ha", "center"),
            va=attr.get("va", "center"),
            zorder=4
        )

    # Columna de atributos especiales en el margen izquierdo (DIM_PERSONAL)
    if "column_attributes" in dim:
        for item in dim["column_attributes"]["items"]:
            ax.text(
                item["x"],
                item["y"],
                item["text"],
                fontsize=8.5,
                color=COLOR_ATTR_TEXT,
                ha=item.get("ha", "center"),
                va="center",
                zorder=4
            )

    # 4. Nombre de la dimensión cerca de la punta de la flecha
    off_x, off_y = dim.get("label_offset", (0.0, 10.0))
    align = dim.get("label_align", {"ha": "center", "va": "bottom"})
    ax.text(
        tip_x + off_x,
        tip_y + off_y,
        dim["name"],
        fontsize=10.5,
        fontweight="bold",
        color=COLOR_TITLE,
        ha=align.get("ha", "center"),
        va=align.get("va", "center"),
        zorder=5
    )


def draw_indicators_panel(ax, config=PANEL_CONFIG):
    """
    Dibuja el panel lateral derecho con las cuatro tarjetas de indicadores y medidas:
    - Rectángulo exterior con esquinas redondeadas, fondo amarillo suave y borde gris azulado.
    - Título 'INDICADORES Y MEDIDAS' centrado con separador horizontal.
    - Cuatro tarjetas con bordes redondeados y sus medidas correspondientes.
    """
    box = config["box"]

    # Fondo y borde del panel exterior
    panel_patch = FancyBboxPatch(
        (box["x"], box["y"]),
        box["width"],
        box["height"],
        boxstyle=f"round,pad=0,rounding_size={box['radius']}",
        facecolor=COLOR_PANEL_BG,
        edgecolor=COLOR_PANEL_BORDER,
        linewidth=1.3,
        zorder=1
    )
    ax.add_patch(panel_patch)

    # Título principal del panel
    tx, ty = config["title_pos"]
    ax.text(
        tx, ty,
        config["title"],
        fontsize=10.5,
        fontweight="bold",
        color=COLOR_PANEL_TITLE,
        ha="center",
        va="center",
        zorder=3
    )

    # Separador horizontal bajo el título
    sep = config["separator"]
    ax.plot([sep["x1"], sep["x2"]], [sep["y"], sep["y"]], color=COLOR_PANEL_SEP, linewidth=1.0, zorder=3)

    cx = config["card_x"]
    cw = config["card_width"]
    cr = config["card_radius"]

    for card in config["cards"]:
        cy = card["y"]
        ch = card["height"]

        # Tarjeta blanca redondeada
        card_patch = FancyBboxPatch(
            (cx, cy),
            cw,
            ch,
            boxstyle=f"round,pad=0,rounding_size={cr}",
            facecolor=COLOR_CARD_BG,
            edgecolor=COLOR_CARD_BORDER,
            linewidth=1.0,
            zorder=2
        )
        ax.add_patch(card_patch)

        # Título de la tarjeta
        ax.text(
            cx + 10.0,
            cy + ch - 14.0,
            card["title"],
            fontsize=9.0,
            fontweight="bold",
            color=COLOR_CARD_TITLE,
            ha="left",
            va="center",
            zorder=3
        )

        # Etiqueta 'Medidas'
        ax.text(
            cx + 10.0,
            cy + ch - 27.0,
            "Medidas",
            fontsize=7.8,
            fontweight="bold",
            color=COLOR_MEDIDAS_LABEL,
            ha="left",
            va="center",
            zorder=3
        )

        # Lista de medidas con viñetas
        item_y_start = cy + ch - 39.0
        line_step = 12.0
        for idx, measure in enumerate(card["measures"]):
            ax.text(
                cx + 14.0,
                item_y_start - idx * line_step,
                measure,
                fontsize=8.0,
                color=COLOR_MEASURE_ITEM,
                ha="left",
                va="center",
                zorder=3
            )


def generar_diagrama():
    """
    Función principal que genera el diagrama dimensional y lo guarda en PNG (300 DPI) y SVG.
    """
    # Proporción exacta correspondiente a 803 x 477 píxeles
    fig_w = 803.0 / 50.0
    fig_h = 477.0 / 50.0
    fig = plt.figure(figsize=(fig_w, fig_h), facecolor=COLOR_BG)

    # Eje que abarca todo el lienzo sin marcos ni escalas cartesianas visibles
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
    ax.set_xlim(0.0, 803.0)
    ax.set_ylim(0.0, 477.0)
    ax.set_aspect("equal")
    ax.axis("off")

    # 1. Título y subtítulo en la esquina superior izquierda
    ax.text(
        34.0, 452.0,
        "ANÁLISIS DIMENSIONAL CONFORMADO DE BUYERS",
        fontsize=13.5,
        fontweight="bold",
        color=COLOR_TITLE,
        ha="left",
        va="top"
    )
    ax.text(
        34.0, 436.0,
        "Dimensiones como ejes que convergen en un punto central",
        fontsize=9.0,
        color=COLOR_SUBTITLE,
        ha="left",
        va="top"
    )

    # 2. Trazado de los 9 ejes radiales con marcas y etiquetas
    for dim in DIMENSIONS:
        draw_dimension_axis(ax, dim)

    # 3. Punto central donde convergen todas las dimensiones
    ax.plot(
        [CENTER_X], [CENTER_Y],
        marker="o",
        markersize=7.0,
        color=COLOR_CENTER_DOT,
        zorder=10
    )

    # 4. Panel lateral de indicadores y medidas
    draw_indicators_panel(ax)

    # Guardar en alta fidelidad
    png_filename = "diagrama_dimensional.png"
    svg_filename = "diagrama_dimensional.svg"

    plt.savefig(png_filename, dpi=300, facecolor=COLOR_BG, edgecolor="none")
    plt.savefig(svg_filename, facecolor=COLOR_BG, edgecolor="none")
    plt.close(fig)

    print("Archivos generados exitosamente:")
    print(f"  - {png_filename} (resolución 300 DPI)")
    print(f"  - {svg_filename} (formato vectorial SVG)")


if __name__ == "__main__":
    generar_diagrama()
