# /// script
# dependencies = ["matplotlib"]
# ///
"""Gera o diagrama do caminho do Iceberg ao Snowflake (versão clara, fundo transparente).
As fotos ficam em img/util/iceberg_photo.jpg e img/util/snowflake_photo.jpg.

    uv run scripts/diagrama_derreteu.py
"""

from diagrama_base import *  # noqa: F403

foto("iceberg_photo.jpg", 12, 25, 11, "ICEBERG")
foto("snowflake_photo.jpg", 138, 25, 11, "SNOWFLAKE")

caixa(31, 10, 26, 30, "DUCKDB LOCAL", "Manifesto/Parquet", icone_banco)
caixa(62, 10, 26, 30, "SEM ACESSO", "Manifesto/Parquet", icone_cadeado)
caixa(93, 10, 26, 30, "CONSUMO", "direto no Snowflake", icone_floco)
seta(24, 25, 30, 25)
seta(57.5, 25, 61.5, 25)
seta(88.5, 25, 92.5, 25)
seta(119.5, 25, 125.5, 25)

# Quais caminhos usam Iceberg + Snowflake e quais só o Snowflake.
ax.text(60, 45, "ICEBERG + SNOWFLAKE", ha="center", va="center", color=VIOLETA, fontsize=12, fontweight="bold")
ax.plot([33, 86], [42.5, 42.5], color=VIOLETA, lw=3, solid_capstyle="round")
ax.text(106, 45, "SNOWFLAKE", ha="center", va="center", color=VIOLETA, fontsize=12, fontweight="bold")
ax.plot([95, 117], [42.5, 42.5], color=VIOLETA, lw=3, solid_capstyle="round")

salvar("diagrama-derreteu.png")
