# Uso: make help
MARP = npx @marp-team/marp-cli --theme-set pybr2026.css --html --allow-local-files

.PHONY: help html pdf diagramas grafico qr clean

help: ## Lista os comandos
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-10s %s\n", $$1, $$2}'

html: ## Salva slides.md em slides.html
	$(MARP) slides.md -o slides.html

pdf: ## Salva slides.md em slides.pdf
	$(MARP) --pdf slides.md -o slides.pdf

diagramas: ## Regera os diagramas em img/diagramas/
	cd scripts/diagramas && for f in camadas derreteu ingestao orquestracao; do uv run $$f.py; done

grafico: ## Regera o gráfico em img/graficos/
	uv run scripts/grafico.py

qr: ## Regera img/qr.png (make qr URL=https://endereco)
	uv run scripts/qr.py $(URL)

clean: ## Apaga slides.html e slides.pdf
	rm -f slides.html slides.pdf
