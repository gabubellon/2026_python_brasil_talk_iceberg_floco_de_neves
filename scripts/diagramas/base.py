"""Peças comuns dos diagramas (cores da Python Brasil 2026, versão clara, fundo transparente).

Cada diagrama importa este módulo, desenha as caixas e chama salvar().
"""

from math import cos, pi, sin
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

PRETO = "#0F0F0F"
OFF_WHITE = "#E8F4BA"
LIMAO = "#B7FF06"
VIOLETA = "#BF2EB2"

IMG = Path(__file__).resolve().parent.parent.parent / "img"

plt.rcParams["font.family"] = ["Roboto", "DejaVu Sans"]
fig, ax = plt.subplots(figsize=(15, 5), dpi=150)
ax.set_xlim(0, 150)
ax.set_ylim(0, 50)
ax.set_aspect("equal")
ax.axis("off")


def traco(**kw):
    return dict(ec=PRETO, lw=2.2, joinstyle="round", **kw)


# Ícones desenhados em torno de (cx, cy), cabem num quadrado de ~9 unidades.
def icone_nuvem(cx, cy):
    for dx, dy, r in [(-2.6, -0.8, 2.4), (0.2, 0.9, 3.0), (2.8, -0.8, 2.3)]:
        ax.add_patch(Circle((cx + dx, cy + dy), r, fc="white", zorder=5, **traco()))
    ax.add_patch(Rectangle((cx - 2.6, cy - 3.2), 5.4, 2.4, fc="white", ec="none", zorder=6))
    ax.plot([cx - 2.6, cx + 2.8], [cy - 3.2, cy - 3.2], color=PRETO, lw=2.2, zorder=7)
    ax.add_patch(FancyArrowPatch((cx, cy + 2.4), (cx, cy - 2.4), arrowstyle="-|>", mutation_scale=22, lw=2.2, color=VIOLETA, zorder=8))


def icone_arquivo(cx, cy):
    ax.add_patch(Rectangle((cx - 4, cy - 3.8), 8, 5.6, fc="white", zorder=5, **traco()))
    ax.add_patch(Rectangle((cx - 4.6, cy + 1.8), 9.2, 2.2, fc=VIOLETA, zorder=6, **traco()))
    ax.add_patch(Rectangle((cx - 1.2, cy - 1.0), 2.4, 1.2, fc=PRETO, ec="none", zorder=6))


def icone_banco(cx, cy):
    ax.add_patch(Rectangle((cx - 3.8, cy - 3), 7.6, 6, fc="white", ec="none", zorder=5))
    for y in (cy - 3, cy):
        ax.add_patch(Ellipse((cx, y), 7.6, 2.6, fc="white", zorder=5, **traco()))
    ax.plot([cx - 3.8, cx - 3.8], [cy - 3, cy + 3], color=PRETO, lw=2.2, zorder=6)
    ax.plot([cx + 3.8, cx + 3.8], [cy - 3, cy + 3], color=PRETO, lw=2.2, zorder=6)
    ax.add_patch(Ellipse((cx, cy + 3), 7.6, 2.6, fc=VIOLETA, zorder=7, **traco()))


def icone_bucket(cx, cy):
    ax.add_patch(Polygon([(cx - 3.8, cy + 2.6), (cx + 3.8, cy + 2.6), (cx + 2.6, cy - 3.6), (cx - 2.6, cy - 3.6)], fc="white", zorder=5, **traco()))
    ax.add_patch(Ellipse((cx, cy + 2.6), 7.6, 2.2, fc=VIOLETA, zorder=6, **traco()))


def icone_filtro(cx, cy):
    ax.add_patch(Polygon([(cx - 4.2, cy + 3.4), (cx + 4.2, cy + 3.4), (cx + 0.9, cy - 0.4), (cx + 0.9, cy - 3.6), (cx - 0.9, cy - 2.6), (cx - 0.9, cy - 0.4)], fc="white", zorder=5, **traco()))
    ax.add_patch(Rectangle((cx - 4.2, cy + 2.4), 8.4, 1.0, fc=VIOLETA, ec="none", zorder=6))


def icone_engrenagem(cx, cy):
    pts = []
    for i in range(16):
        r = 4.6 if i % 2 == 0 else 3.4
        for a in (i * pi / 8 - pi / 32, i * pi / 8 + pi / 32):
            pts.append((cx + r * cos(a), cy + r * sin(a)))
    ax.add_patch(Polygon(pts, fc="white", zorder=5, **traco()))
    ax.add_patch(Circle((cx, cy), 1.5, fc=VIOLETA, zorder=6, **traco()))


def icone_olho(cx, cy):
    ax.add_patch(Ellipse((cx, cy), 10, 6.4, fc="white", zorder=5, **traco()))
    ax.add_patch(Circle((cx, cy), 2.0, fc=VIOLETA, zorder=6, **traco()))


def icone_pod(cx, cy):
    pts = [(cx + 4.4 * cos(pi / 6 + i * pi / 3), cy + 4.4 * sin(pi / 6 + i * pi / 3)) for i in range(6)]
    ax.add_patch(Polygon(pts, fc="white", zorder=5, **traco()))
    ax.add_patch(Circle((cx, cy), 1.5, fc=VIOLETA, zorder=6, **traco()))


def icone_copiar(cx, cy):
    ax.add_patch(Rectangle((cx - 4, cy - 1.5), 5.4, 5, fc="white", zorder=5, **traco()))
    ax.add_patch(Rectangle((cx - 1.4, cy - 4), 5.4, 5, fc=VIOLETA, zorder=6, **traco()))


def icone_dbt(cx, cy):
    ax.add_patch(FancyBboxPatch((cx - 4.4, cy - 3), 8.8, 6, boxstyle="round,pad=0,rounding_size=1.2", fc="white", zorder=5, **traco()))
    ax.text(cx, cy - 0.1, "dbt", ha="center", va="center", color=VIOLETA, fontsize=12, fontweight="bold", zorder=6)


def icone_teste(cx, cy):
    ax.add_patch(Polygon([(cx - 4, cy + 3.6), (cx + 4, cy + 3.6), (cx + 4, cy - 0.6), (cx, cy - 4), (cx - 4, cy - 0.6)], fc="white", zorder=5, **traco()))
    ax.plot([cx - 2, cx - 0.4, cx + 2.4], [cy, cy - 1.6, cy + 1.8], color=VIOLETA, lw=3.2, zorder=6, solid_capstyle="round", solid_joinstyle="round")


def icone_cadeado(cx, cy):
    ax.add_patch(Ellipse((cx, cy + 1.6), 5.6, 7.2, fc="none", zorder=5, **traco()))
    ax.add_patch(FancyBboxPatch((cx - 3.8, cy - 3.8), 7.6, 5.6, boxstyle="round,pad=0,rounding_size=0.8", fc=VIOLETA, zorder=6, **traco()))


def icone_floco(cx, cy):
    for i in range(3):
        a = i * pi / 3
        ax.plot([cx - 4.4 * cos(a), cx + 4.4 * cos(a)], [cy - 4.4 * sin(a), cy + 4.4 * sin(a)], color=PRETO, lw=2.2, zorder=5, solid_capstyle="round")
    ax.add_patch(Circle((cx, cy), 1.3, fc=VIOLETA, zorder=6, **traco()))


def foto(arquivo, cx, cy, r, legenda):
    """Foto quadrada (recorte central) num círculo com contorno preto."""
    img = plt.imread(IMG / f"foto-{arquivo}")
    h, w = img.shape[:2]
    lado = min(h, w)
    img = img[(h - lado) // 2 : (h + lado) // 2, (w - lado) // 2 : (w + lado) // 2]
    xlim, ylim = ax.get_xlim(), ax.get_ylim()
    im = ax.imshow(img, extent=[cx - r, cx + r, cy - r, cy + r], zorder=3)
    corte = Circle((cx, cy), r, transform=ax.transData)
    im.set_clip_path(corte)
    ax.add_patch(Circle((cx, cy), r, fc="none", ec=PRETO, lw=3, zorder=4))
    ax.text(cx, cy - r - 3, legenda, ha="center", va="center", color=PRETO, fontsize=15, fontweight="bold")
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)


def caixa(x, y, w, h, titulo, detalhe, icone, fundo=OFF_WHITE, compacta=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=2", fc=fundo, ec=PRETO, lw=3))
    cx = x + w / 2
    ty, dy, cy = (y + 6.8, y + 2.8, y + h - 7) if compacta else (y + h - 17, y + 5.2, y + h - 8)
    ax.add_patch(Circle((cx, cy), 5.2 if compacta else 6.2, fc=LIMAO, ec=PRETO, lw=2.2, zorder=4))
    icone(cx, cy)
    ax.text(cx, ty, titulo, ha="center", va="center", color=PRETO, fontsize=15, fontweight="bold")
    ax.text(cx, dy, detalhe, ha="center", va="center", color=PRETO, fontsize=10 if compacta else 11)


def seta(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=28, lw=3.5, color=VIOLETA))


def salvar(nome):
    fig.savefig(IMG / f"diagrama-{nome}", transparent=True, bbox_inches="tight", pad_inches=0.1)
