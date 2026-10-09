# /// script
# dependencies = ["matplotlib"]
# ///
"""Gera o diagrama da orquestração Airflow + Kubernetes (versão clara, fundo transparente).

    uv run scripts/diagramas/orquestracao.py
"""

from base import *  # noqa: F403

caixa(2, 10, 28, 30, "TASK", "@task.kubernetes", icone_pod)
caixa(41, 10, 28, 30, "COPY INTO", "com BATCH", icone_copiar)
caixa(80, 10, 28, 30, "DBT", "KubernetesPodOperator", icone_dbt)
caixa(119, 10, 28, 30, "TESTES", "DBT Tests isolados", icone_teste)
seta(31, 25, 40, 25)
seta(70, 25, 79, 25)
seta(109, 25, 118, 25)

salvar("orquestracao.png")
