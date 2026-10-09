@AGENTS.md

## Contexto da palestra

- Os slides de acesso ao catálogo (PyIceberg, Spark, DuckDB, Trino, Snowflake) usam uma URI de catálogo REST como exemplo.
- Há também um slide "PyIceberg: Disco Local", com `SqlCatalog` (SQLite) e warehouse em `file://`, para mostrar a leitura de um caminho de disco e não de uma URL. Ele fica logo depois do slide do PyIceberg; mantenha-o.
- Se a pessoa pedir a versão de disco de outra ferramenta (Spark, DuckDB ou Trino), pergunte qual antes de editar.

## Estrutura do projeto (reorganizada em 2026-10-09)

- `slides.md` é o único arquivo de slides. As versões `slides.en.md`, `slides.es.md`, `slides copy.md` e `slides_v1.md` foram apagadas de propósito: não recrie.
- Os 3 READMEs (`README.md`, `README.en.md`, `README.es.md`) ficam. Eles vêm do modelo original e ainda falam dos "slides de exemplo"; mantenha os três em sincronia quando mudar um.
- `img/` por pasta: `marca/`, `figurinhas/`, `logos/`, `diagramas/`, `fotos/`, `graficos/`, mais `qr.png`. Nomes em português e kebab-case, sem `_`. Toda imagem nova entra na pasta certa, e imagem que nenhum slide usa é apagada.
- Os diagramas de `img/diagramas/` (`camadas`, `derreteu`, `ingestao`, `orquestracao`) saem de `scripts/diagramas/`; edite o script e regere, não o PNG.
- `Makefile`: `make html`, `make pdf`, `make diagramas`, `make grafico`, `make qr URL=...`, `make clean`. `slides.html` e `slides.pdf` ficam na raiz (ignorados pelo git) para as imagens funcionarem. O `npx` pode não estar no PATH da shell do agente; no nvm está em `~/.nvm/versions/node/`.

## Histórico de pedidos da pessoa palestrante

Mantenha esta lista atualizada: ao fim de cada pedido que mude o projeto ou as preferências, acrescente uma linha curta (data, pedido, decisão). Só registre o que a pessoa pediu neste repositório; não invente.

- Antes de 2026-10-09: slides do PyIceberg com catálogo REST e o slide "PyIceberg: Disco Local" (ver acima); diagramas gerados por script.
- 2026-10-09: pediu para organizar o projeto: só `slides.md` como slide, renomear e organizar imagens e caminhos, apagar imagens sem uso, organizar e renomear scripts, manter os 3 READMEs e criar um Makefile para salvar o slide em HTML ou PDF. Feito como descrito em "Estrutura do projeto".
- 2026-10-09: pediu para manter este `CLAUDE.md` sempre atualizado com o histórico de pedidos, e para conferir se o `AGENTS.md` precisava de ajustes após a limpeza (ajustado: projeto de uma palestra só, em português, pastas de `img/`, `make pdf`).
