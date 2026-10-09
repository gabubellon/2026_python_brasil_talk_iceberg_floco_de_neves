# /// script
# dependencies = ["matplotlib"]
# ///
"""Gera o diagrama da ingestão no dp_batch (versão clara, fundo transparente).

    uv run scripts/diagramas/ingestao.py
"""

from base import *  # noqa: F403


caixa(1, 10, 26, 30, "CARGA", "Sftp/API\nCliente/Fonte", icone_nuvem)
caixa(42, 10, 26, 30, "RAW", "Compactado (HIVE)\nS3", icone_arquivo)
caixa(83, 10, 26, 30, "INGESTÃO", "Descentralizada\ne independente\n(Metadata)", icone_banco)
seta(28, 25, 41, 25)
seta(69, 25, 82, 25)

caixa(131, 27, 18, 22, "DEV", "bucket separado", icone_bucket, compacta=True)
caixa(131, 1, 18, 22, "PROD", "bucket separado", icone_bucket, compacta=True)
seta(110, 28, 130, 36)
seta(110, 22, 130, 14)

salvar("ingestao.png")
