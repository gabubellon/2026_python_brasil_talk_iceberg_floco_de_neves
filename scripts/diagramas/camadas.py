# /// script
# dependencies = ["matplotlib"]
# ///
"""Gera o diagrama das camadas do dbt (versão clara, fundo transparente).

    uv run scripts/diagramas/camadas.py
"""

from base import *  # noqa: F403

caixa(2, 10, 36, 30, "STAGING", "Limpeza e tipo", icone_filtro)
caixa(57, 10, 36, 30, "INTEGRATION", "Regras de negócio\ne filtros (SQL)", icone_engrenagem)
caixa(112, 10, 36, 30, "PUBLICATION", "Views de consulta", icone_olho)
seta(39, 25, 56, 25)
seta(94, 25, 111, 25)

salvar("camadas.png")
