# /// script
# dependencies = ["matplotlib"]
# ///
"""Gera o gráfico de exemplo nas cores da Python Brasil 2026, em versão escura e clara.
Troque os rótulos e os valores pelos seus dados e rode de novo:

    uv run scripts/grafico.py
"""

from pathlib import Path

import matplotlib.pyplot as plt

PRETO = "#0F0F0F"
OFF_WHITE = "#E8F4BA"
LIMAO = "#B7FF06"

IMG = Path(__file__).resolve().parent.parent / "img"

ROTULOS = ["Python 3.10", "Python 3.11", "Python 3.12", "Python 3.13", "Python 3.14"]
VALORES = [8, 15, 29, 33, 15]


def grafico(arquivo: str, texto: str) -> None:
    plt.rcParams["font.family"] = ["Roboto", "DejaVu Sans"]
    fig, ax = plt.subplots(figsize=(11.5, 4.6), dpi=150)
    # As barras ficam limão nos dois fundos: o número sobre cada barra leva a informação.
    barras = ax.bar(ROTULOS, VALORES, color=LIMAO, width=0.5)
    ax.bar_label(barras, labels=[f"{v}%" for v in VALORES], padding=8, color=texto, fontsize=26, fontweight="bold")
    ax.tick_params(axis="x", colors=texto, labelsize=24, length=0)
    ax.set_yticks([])
    for borda in ax.spines.values():
        borda.set_visible(False)
    fig.tight_layout()
    # Fundo transparente: o gráfico pega a cor do slide, sem um retângulo em volta.
    fig.savefig(IMG / arquivo, transparent=True)


grafico("grafico-exemplo.png", OFF_WHITE)
grafico("grafico-exemplo-claro.png", PRETO)
