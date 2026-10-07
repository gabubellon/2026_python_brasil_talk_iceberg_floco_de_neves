# Instruções para agentes

Este repositório é um modelo de slides da Python Brasil 2026 em Markdown, com o [Marp](https://marp.app/). A pessoa palestrante escreve a palestra em `slides.md`; o tema `pybr2026.css` aplica a identidade visual do evento.

## Arquivos

- `slides.md`: a apresentação em português. `slides.en.md` e `slides.es.md` são a mesma apresentação em inglês e em espanhol. A pessoa fica só com o arquivo do idioma da palestra, renomeado para `slides.md`, para a palestra sair na raiz do site. Os slides de exemplo mostram todos os layouts, cada um com dicas nas anotações.
- `pybr2026.css`: o tema. Não mude o tema para resolver um slide: use as classes abaixo. Mude o tema só quando a pessoa pedir.
- `img/`: logos, figurinhas, imagens de exemplo, o gráfico e o QR code. As imagens dos slides ficam aqui. As imagens `*-exemplo*.png` são caixas cinza que marcam o lugar de uma imagem: troque pela imagem da pessoa, nunca use uma delas na palestra.
- `scripts/grafico.py` e `scripts/qr.py`: geram o gráfico e o QR code nas cores da marca (`uv run scripts/qr.py https://endereco`). Para um gráfico com os dados da pessoa, troque `ROTULOS` e `VALORES` no script, ou copie o script para um gráfico novo.

## Como um slide é escrito

Os slides são separados por `---`. O layout vem de um comentário no topo do slide; o `_` faz a diretiva valer só para aquele slide:

```markdown
<!-- _class: duas-colunas light -->
```

As anotações são comentários HTML no fim do slide, com dois ou três tópicos curtos:

```markdown
<!--
- Uma dica por linha.
-->
```

## Layouts

| Classe | Markdown esperado |
|---|---|
| (nenhuma) | `## Título` e uma lista de 3 a 5 tópicos, uma tabela, um bloco de código ou uma imagem |
| `capa` | `<div class="selo">...</div>`, `# Título`, subtítulo, `**Nome** · @usuario`. Use `_paginate: false` e `_footer: ""` |
| `frase` | Só um `# Frase`, em até duas linhas |
| `secao` | `# _01_ Título da seção`. Use `_paginate: false` e `_footer: ""` |
| `duas-colunas` | `## Título`, depois `### Coluna` + conteúdo, duas vezes. Com `miuda`, o código da esquerda fica pequeno de propósito |
| `numeros` | `## Título` e três itens `- **18** rótulo` |
| `cartoes` | `## Título` e três itens `1. **Título** Descrição curta.` |
| `fluxo` | `## Título` e uma lista numerada de 3 a 5 passos curtos; vira caixas com setas |
| `tres-imagens` | `## Título` e três itens `- ![alt](img/x.png) Legenda` |
| `palestrante` | `![Foto de ...](img/foto.png)`, `# Nome`, `### Cargo`, lista de até três fatos |
| `destaque` | `## Mensagem` (vai no painel limão) e até quatro tópicos curtos |
| `imagem-cheia` | `![bg](img/foto.png)` e um parágrafo de legenda com o crédito |
| `encerramento` | `# Perguntas?`, contatos (`_@usuario_`), `![QR code para ...](img/qr.png)` e o endereço na linha seguinte. Use `_paginate: false` e `_footer: ""` |
| `figurinhas` | Imagens com largura, como `![w:200](img/sticker-witch.png)` |
| `light` | Combina com qualquer outra: `<!-- _class: frase light -->` |

Texto ao lado de uma imagem usa a sintaxe do Marp: `![bg right:42%](img/x.png)` ou `![bg left:42%](img/x.png)`.

## Regras da marca

- Cores: preto `#0F0F0F` (RGB 15, 15, 15), off-white `#E8F4BA` (232, 244, 186), verde limão `#B7FF06` (183, 255, 6), violeta `#BF2EB2` (191, 46, 178). O tema já aplica as cores; não escreva cores no Markdown. Use estas cores em imagens, gráficos e diagramas que você criar.
- Fontes: Cascadia Mono nos títulos e no código, Roboto no texto. O tema já carrega as duas.
- Verde limão como cor de texto, só no fundo escuro. No fundo claro, destaque com o marca-texto: `<mark>palavra</mark>`.
- Código: o tema aplica as cores do GitHub Light num cartão branco, nos slides escuros e nos claros. Monokai com fundo `#1A1A1A` é a alternativa para quem pedir código no fundo escuro; nesse caso, use fonte grande.
- Tela de LED do tamanho de uma parede: versão escura, que não ofusca o público. Projetor, TV ou monitor: versão clara, com a classe `light`. O código fica em fundo claro nas duas.
- Use as figurinhas de `img/` como estão: sem distorcer e sem recolorir. Uma figurinha por slide costuma bastar.
- A identidade visual é de Ana Terhorst; mantenha o crédito no slide de figurinhas.

## Regras de conteúdo

- O conteúdo é da pessoa palestrante. Organize o que ela escreveu em slides, encurte e escolha os layouts, mas não invente fatos, exemplos, números nem opiniões. Se faltar alguma coisa, pergunte.
- Uma ideia por slide. De 3 a 5 tópicos curtos, de uma linha cada quando possível.
- Código: até 8 linhas e 60 colunas por slide (30 colunas em `duas-colunas`). Marque a linguagem do bloco, como ` ```python `, para o realce de sintaxe.
- Toda imagem que não seja de fundo tem texto alternativo entre os colchetes. Gráficos levam os números no texto alternativo.
- O Marp lê algumas palavras soltas do texto alternativo como filtros de imagem: `blur`, `brightness`, `contrast`, `drop-shadow`, `grayscale`, `hue-rotate`, `invert`, `opacity`, `saturate` e `sepia`. Em inglês, troque essas palavras por outras no texto alternativo: "contrast" muda as cores do gráfico.
- O que não cabe no slide vai para as anotações.
- Escreva no idioma do arquivo, indicado em `lang:` no topo: `pt-BR`, `en` ou `es`. Use linguagem neutra de gênero quando possível ("pessoa palestrante", "o público", "quem assiste"; "the speaker", "people"; "la persona que presenta", "el público").
- Nas versões em inglês e em espanhol, as imagens com texto têm o sufixo do idioma, como `img/imagem-exemplo-en.png`. O gráfico de exemplo é o mesmo nos três idiomas. O lema `Pessoas > Tecnologia` e a saudação "Dazumbanho!" ficam em português nos três idiomas.
- O tom é de dica, não de regra: apoio, sem cobrança e sem prometer resultado. Evite "é só", "é fácil" e "todo mundo sabe".
- Conte mais ou menos 1 minuto por slide, depois de separar uns 5 minutos para perguntas. Pergunte a duração da palestra se não souber.

## Conferir o resultado

Gere o PDF e olhe os slides que mudaram:

```sh
npx @marp-team/marp-cli --theme-set pybr2026.css --html --allow-local-files --pdf slides.md
```

Texto que passa do rodapé ou some atrás de uma imagem quer dizer que o slide tem conteúdo demais: divida em dois.
