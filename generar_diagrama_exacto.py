"""
generar_diagrama_exacto.py
===========================
Genera el diagrama dimensional con el nuevo diseño idéntico a las Capturas 2, 3 y 4:
- Título principal centrado en azul (#5b9bd5).
- Gráfico estrella con flechas estilizadas dobles (#4f81bd) y puntas triangulares.
- Cuadros de dimensión en la punta con borde cian (#4bacc6) y texto centrado.
- Cuadro de medidas inferior central en azul suave (#d3dfee) con viñetas ✔ (máximo 3).
"""

import math
import os

def generar_svg(
    titulo="SERVICIO SIN INCIDENCIA",
    medidas=None,
    ruta_salida="diagrama_exacto.svg"
):
    if medidas is None:
        medidas = ["Servicios finalizados", "Servicios sin incidencia"]

    # Limitado a máximo 3 medidas según especificación
    medidas = medidas[:3]

    w = 820
    h = 540
    cx = 410.0
    cy = 232.0
    axis_len = 175.0

    arrow_color = "#4f81bd"
    inner_color = "#ffffff"
    box_border = "#4bacc6"
    title_color = "#5b9bd5"
    measures_bg = "#d3dfee"

    # Preset 1: Servicio sin Incidencia (Captura 2)
    axes = [
        {
            "name": "FECHA",
            "angle": 140,
            "ticks": [
                {"r": 48, "text": "Día", "ox": -14, "oy": 12, "anchor": "end"},
                {"r": 78, "text": "Mes", "ox": -14, "oy": 12, "anchor": "end"},
                {"r": 108, "text": "Trimestre", "ox": -14, "oy": 12, "anchor": "end"},
                {"r": 138, "text": "Semestre", "ox": -14, "oy": 12, "anchor": "end"},
                {"r": 168, "text": "Año", "ox": -14, "oy": 12, "anchor": "end"}
            ]
        },
        {
            "name": "LEAD",
            "angle": 40,
            "ticks": [
                {"r": 60, "text": "Nombre", "ox": 14, "oy": 12, "anchor": "start"},
                {"r": 110, "text": "Tipo de lead", "ox": 14, "oy": 12, "anchor": "start"},
                {"r": 160, "text": "Interés principal", "ox": 14, "oy": 12, "anchor": "start"}
            ]
        },
        {
            "name": "SERVICIO",
            "angle": 0,
            "ticks": [
                {"r": 75, "text": "Tipo de servicio", "ox": 0, "oy": 20, "anchor": "middle"},
                {"r": 145, "text": "Estado", "ox": 0, "oy": 20, "anchor": "middle"}
            ]
        },
        {
            "name": "MESA",
            "angle": 315,
            "ticks": [
                {"r": 65, "text": "N° mesa", "ox": -14, "oy": 12, "anchor": "end"},
                {"r": 115, "text": "Zona", "ox": -14, "oy": 12, "anchor": "end"},
                {"r": 165, "text": "Capacidad", "ox": -14, "oy": 12, "anchor": "end"}
            ]
        },
        {
            "name": "PERSONAL",
            "angle": 225,
            "ticks": [
                {"r": 55, "text": "Nombres", "ox": 14, "oy": 12, "anchor": "start"},
                {"r": 95, "text": "Apellidos", "ox": 14, "oy": 12, "anchor": "start"},
                {"r": 135, "text": "Cargo", "ox": 14, "oy": 12, "anchor": "start"},
                {"r": 170, "text": "Área", "ox": 14, "oy": 12, "anchor": "start"}
            ]
        }
    ]

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">')
    svg.append(f'<rect width="{w}" height="{h}" fill="#ffffff" />')

    # Título principal
    svg.append(f'<text x="{cx}" y="46" text-anchor="middle" font-family="Arial, Segoe UI, sans-serif" font-size="25px" font-weight="bold" fill="{title_color}" letter-spacing="0.5px">{titulo}</text>')

    head_len = 16.0
    head_w = 14.0

    for ax in axes:
        rad = math.radians(ax["angle"])
        ux = math.cos(rad)
        uy = -math.sin(rad)
        px = -uy
        py = ux

        bw = max(72.0, len(ax["name"]) * 8.6 + 26.0)
        bh = 30.0

        bcx = cx + (axis_len + (bw / 2.0) * abs(ux) + 6.0) * ux
        bcy = cy + (axis_len + (bh / 2.0) * abs(uy) + 6.0) * uy

        hw = bw / 2.0
        hh = bh / 2.0
        dx = bcx - cx
        dy = bcy - cy
        dist = math.hypot(dx, dy)
        nux = dx / dist
        nuy = dy / dist

        tx = hw / abs(nux) if abs(nux) > 1e-5 else 1e9
        ty = hh / abs(nuy) if abs(nuy) > 1e-5 else 1e9
        t = min(tx, ty)

        tip_x = bcx - t * nux
        tip_y = bcy - t * nuy

        base_x = tip_x - head_len * nux
        base_y = tip_y - head_len * nuy

        # Tallo doble
        svg.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{base_x:.1f}" y2="{base_y:.1f}" stroke="{arrow_color}" stroke-width="4.5" stroke-linecap="butt" />')
        svg.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{base_x:.1f}" y2="{base_y:.1f}" stroke="{inner_color}" stroke-width="2.2" stroke-linecap="butt" />')

        # Punta
        c1x = base_x + (head_w / 2.0) * px
        c1y = base_y + (head_w / 2.0) * py
        c2x = base_x - (head_w / 2.0) * px
        c2y = base_y - (head_w / 2.0) * py
        svg.append(f'<polygon points="{tip_x:.1f},{tip_y:.1f} {c1x:.1f},{c1y:.1f} {c2x:.1f},{c2y:.1f}" fill="{arrow_color}" stroke="{arrow_color}" stroke-width="1" stroke-linejoin="round" />')

        # Ticks
        for tk in ax["ticks"]:
            ax_x = cx + tk["r"] * ux
            ax_y = cy + tk["r"] * uy
            t1x = ax_x + 7.0 * px
            t1y = ax_y + 7.0 * py
            t2x = ax_x - 7.0 * px
            t2y = ax_y - 7.0 * py
            svg.append(f'<line x1="{t1x:.1f}" y1="{t1y:.1f}" x2="{t2x:.1f}" y2="{t2y:.1f}" stroke="{arrow_color}" stroke-width="1.8" />')

            lbl_x = ax_x + tk["ox"]
            lbl_y = ax_y + tk["oy"]
            svg.append(f'<text x="{lbl_x:.1f}" y="{lbl_y:.1f}" text-anchor="{tk["anchor"]}" dominant-baseline="middle" font-family="Arial, Segoe UI, sans-serif" font-size="11.5px" fill="#222222" paint-order="stroke fill" stroke="#ffffff" stroke-width="3.5px" stroke-linejoin="round">{tk["text"]}</text>')

        # Cuadro dimensión
        bx = bcx - hw
        by = bcy - hh
        svg.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="#ffffff" stroke="{box_border}" stroke-width="2" />')
        svg.append(f'<text x="{bcx:.1f}" y="{bcy:.1f}" text-anchor="middle" dominant-baseline="central" font-family="Arial, Segoe UI, sans-serif" font-size="12.5px" font-weight="bold" fill="#111827" letter-spacing="0.3px">{ax["name"]}</text>')

    # Cuadro inferior central de medidas
    max_len = max(len(m) for m in medidas) if medidas else 10
    mb_w = max(220.0, min(380.0, max_len * 8.2 + 58.0))
    line_h = 22.0
    mb_h = 16.0 + len(medidas) * line_h
    mb_x = cx - mb_w / 2.0
    mb_y = 442.0

    svg.append(f'<rect x="{mb_x:.1f}" y="{mb_y:.1f}" width="{mb_w:.1f}" height="{mb_h:.1f}" fill="{measures_bg}" rx="2" ry="2" />')

    for idx, m in enumerate(medidas):
        row_y = mb_y + 14.0 + idx * line_h + 2.0
        ck_x = mb_x + 18.0
        svg.append(f'<path d="M {ck_x:.1f} {row_y-2.0:.1f} L {ck_x+4.5:.1f} {row_y+3.5:.1f} L {ck_x+12.0:.1f} {row_y-6.0:.1f}" fill="none" stroke="#000000" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />')
        svg.append(f'<text x="{ck_x+20.0:.1f}" y="{row_y:.1f}" dominant-baseline="middle" font-family="Arial, Segoe UI, sans-serif" font-size="13px" font-weight="bold" fill="#111827">{m}</text>')

    svg.append('</svg>')

    with open(ruta_salida, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    print(f"Diagrama guardado en: {ruta_salida}")

if __name__ == '__main__':
    generar_svg()
