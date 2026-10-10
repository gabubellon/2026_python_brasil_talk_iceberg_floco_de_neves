# /// script
# dependencies = ["pillow"]
# ///
"""Junta logos de img/logo-*.png em uma imagem só (faixa horizontal, fundo transparente), salva como img/logo-<combinação>.png.
Edite COMBINACOES e rode de novo:

    uv run scripts/logos.py
"""

from pathlib import Path

from PIL import Image

IMG = Path(__file__).resolve().parent.parent / "img"

COMBINACOES = {
    "python-snowflake": ["python", "snowflake"],
    "airflow-snowflake-dbt": ["airflow", "snowflake", "dbt"],
}

CELULA = 500  # tamanho de cada logo
MARGEM = 80


def combinar(nome: str, logos: list[str]) -> None:
    # Uma faixa horizontal: os logos combinados ficam no canto inferior do slide.
    largura = len(logos) * CELULA + (len(logos) - 1) * MARGEM
    tela = Image.new("RGBA", (largura, CELULA), (0, 0, 0, 0))
    x = 0
    for logo in logos:
        img = Image.open(IMG / f"logo-{logo}.png").convert("RGBA")
        img.thumbnail((CELULA, CELULA))
        tela.paste(img, (x + (CELULA - img.width) // 2, (CELULA - img.height) // 2), img)
        x += CELULA + MARGEM
    tela.save(IMG / f"logo-{nome}.png")


for nome, logos in COMBINACOES.items():
    combinar(nome, logos)
    print(IMG / f"logo-{nome}.png")
