# Python Brasil 2026 slides in Markdown

[Português](README.md) · English · [Español](README.es.md)

Write the content of your [Python Brasil 2026](https://2026.pythonbrasil.org.br/) talk your own way, in plain Markdown, and let an AI agent take care of the design. Your favorite agent reads [`AGENTS.md`](AGENTS.md) and formats the slides with the event's layouts, colors and brand rules. Every push publishes the deck to GitHub Pages, with a PDF next to it.

Code blocks get syntax highlighting automatically. Write ` ```python ` and your code, and the theme applies the GitHub Light colors on a white card, in the Cascadia Mono font, on both dark and light slides. Dark text on a light background is easier to read, especially at small sizes. If you prefer code on a dark background, change the code colors in `pybr2026.css` to the Monokai colors, on `#1A1A1A`, and make the font large. You do not need to copy code from another site or paste screenshots of it.

![Dark code slide: a Palestra dataclass with GitHub Light syntax highlighting on a white card, with the wizard sticker beside it](docs/codigo.png)

The theme uses [Marp](https://marp.app/) and the event's visual identity: colors, fonts, logo and stickers.

Prefer PowerPoint, LibreOffice or Google Slides? Use the [`.pptx` template](https://github.com/rodbv/pybr2026-slides/blob/main/README.en.md). Its example slides and speaker notes are in Portuguese.

The example slides come in three languages, with the same tips:

| Language | File | View |
|---|---|---|
| Português | `slides.md` | [in the browser](https://gabubellon.github.io/2026_python_brasil_talk_iceberg_floco_de_neves/) · [PDF](https://gabubellon.github.io/2026_python_brasil_talk_iceberg_floco_de_neves/slides.pdf) |
| English | `slides.en.md` | [in the browser](https://gabubellon.github.io/2026_python_brasil_talk_iceberg_floco_de_neves/en.html) · [PDF](https://gabubellon.github.io/2026_python_brasil_talk_iceberg_floco_de_neves/slides.en.pdf) |
| Español | `slides.es.md` | [in the browser](https://gabubellon.github.io/2026_python_brasil_talk_iceberg_floco_de_neves/es.html) · [PDF](https://gabubellon.github.io/2026_python_brasil_talk_iceberg_floco_de_neves/slides.es.pdf) |

![The 38 example slides, in the dark and light versions](docs/overview.png)

## Get started

1. Click **Use this template > Create a new repository**. Keep the repository public: GitHub Pages is free for public repositories.
2. In the new repository, open **Settings > Pages** and choose **GitHub Actions** under **Source**.
3. In the **Actions** tab, open the "pages" run, which failed because Pages was not enabled yet, and click **Re-run all jobs**. From then on, every push to `main` publishes the slides and the PDFs.
4. On the repository page, click the gear next to **About** and check **Use your GitHub Pages website**. The link to your slides then shows at the top of the repository.
5. Keep only the file in the language of your talk. If your talk is in Portuguese, delete `slides.en.md` and `slides.es.md`. If it is in English or Spanish, delete the other two files and rename yours to `slides.md`. The talk is then published at the root of the site.

In your copy, the links in the table above point to your own site. The slides are at `https://YOUR-USERNAME.github.io/REPOSITORY-NAME/` and the PDF at `.../slides.pdf`. Without Pages, you can also download the PDF from each run in the Actions tab, in the **slides-pdf** artifact.

Use that address for the QR code on the closing slide, so the audience can open your slides on their phones.

The gray boxes on the example slides mark where images go and show the size that fills the space. Replace the image path in the Markdown with yours.

The template is a starting point: change anything you like. To keep the look of the event, use the brand colors and fonts listed in [Colors and fonts](#colors-and-fonts).

## Colors and fonts

| | Color | Hex | RGB | Use |
|---|---|---|---|---|
| ![Black sample](docs/cores/0F0F0F.png) | Black | `#0F0F0F` | 15, 15, 15 | Dark background, text on light background |
| ![Off-white sample](docs/cores/E8F4BA.png) | Off-white | `#E8F4BA` | 232, 244, 186 | Text on dark background |
| ![Lime green sample](docs/cores/B7FF06.png) | Lime green | `#B7FF06` | 183, 255, 6 | Highlight; as a text color, only on dark background |
| ![Violet sample](docs/cores/BF2EB2.png) | Violet | `#BF2EB2` | 191, 46, 178 | Links on light background |

| Font | Use |
|---|---|
| [Cascadia Mono](https://fonts.google.com/specimen/Cascadia+Mono) | Titles and code |
| [Roboto](https://fonts.google.com/specimen/Roboto) | Text |

## With an AI agent

The content is yours: write the outline of your talk in a file, as bullets, a rough draft or full text. Then open the repository in your editor with your agent and ask it to build the slides. For example:

```
My outline is in outline.md. Build the slides in slides.md, replacing the
examples, using the template's layouts and colors: title slide, agenda, a
section slide for each part and a closing slide. One idea per slide, code in
highlighted blocks, and what I will say in the speaker notes. Do not make up
content: if something is missing, ask me.
```

`AGENTS.md` tells the agent which layouts exist, how to write each one, and the brand and content rules: up to 8 lines of code per slide and up to 60 characters per line, alt text on every image, lime as a text color only on dark backgrounds, gender-neutral language. `CLAUDE.md` points to the same file.

After that, ask for changes the way you would ask a person: "split slide 7 into two", "replace the table with a flow", "make the notes shorter".

## In VS Code

1. Open the repository folder. VS Code suggests the **Marp for VS Code** extension: install it.
2. Open `slides.md` and click the preview button in the top-right corner. The theme is already configured.
3. To export, run **Marp: Export Slide Deck** from the Command Palette and choose HTML, PDF or PPTX. PDF and PPTX export need Chrome, Edge or Firefox installed.

You can also edit `slides.md` directly on GitHub, in the browser. The Action publishes it the same way.

## Present

Open the GitHub Pages address or the exported HTML in the browser.

- **F**: full screen.
- **P**: opens presenter view in a new window, with the speaker notes, the next slide and the timer. The two windows stay in sync: keep presenter view on your laptop screen and the slides on the big screen. To leave presenter view, close its window.
- Arrow keys or Space: next slide.

LED screen as big as a wall: use the dark version, which is not too bright for the audience. Projector, TV or monitor: use the light version (the `light` class). Code stays on a light background in both.

Bring the PDF on a USB drive too. It opens on any computer, without internet access.

## Layouts

Each slide picks its layout with a comment at the top, such as `<!-- _class: secao -->`. The examples in `slides.en.md` show all of them, and [`AGENTS.md`](AGENTS.md) gives the Markdown that each one expects. The class names are in Portuguese.

| Class | Use it for |
|---|---|
| (none) | Title and bullets, a table, code or an image |
| `capa` | Talk title, your name and the date badge |
| `frase` | One sentence, large |
| `secao` | Section divider with the number in the lime circle |
| `duas-colunas` | Before and after, problem and solution, two code snippets |
| `numeros` | Three large numbers with labels |
| `cartoes` | Three numbered cards with a title and a description |
| `fluxo` | Steps in boxes connected by arrows |
| `tres-imagens` | Three screenshots with captions |
| `palestrante` | Photo, name, role and three facts |
| `destaque` | Lime panel with the message the room should not miss |
| `imagem-cheia` | Full-screen background photo with a caption bar |
| `encerramento` | "Questions?" or "Thank you!", contact details and a QR code |
| `figurinhas` | Logo, stickers, pixelated circle and highlighter |
| `light` | Light version of any layout: `<!-- _class: frase light -->` |

For text next to an image, use the Marp syntax: `![bg right:42%](img/foto.png)`.

## Chart and QR code

Marp has no built-in charts. The scripts in `scripts/` generate the images in the brand colors, with [uv](https://docs.astral.sh/uv/):

```sh
uv run scripts/qr.py https://your-username.github.io/your-talk/
uv run scripts/grafico.py
```

`qr.py` replaces `img/qr.png`. `grafico.py` makes the example chart with matplotlib, in the theme's style: change the labels and values in the script and run it again.

## Accessibility

- Body text is 36 px on a 1280 px slide, the same as 20 pt in the `.pptx` template. So that people at the back can read it, avoid text smaller than 32 px (18 pt in the `.pptx`).
- Every color combination in the theme meets WCAG 2.1 level AA. The colors and the contrast of each one are in the [reference of the `.pptx` template](https://github.com/rodbv/pybr2026-slides/blob/main/docs/referencia.md#cores-e-contraste) (in Portuguese).
- Each slides file declares its language for screen readers in the `lang:` field at the top. `slides.en.md` uses `en`.
- Write alt text between the brackets of every image: `![Bar chart: ...](img/grafico.png)`.

## Found a problem?

Open an [issue on GitHub](https://github.com/rodbv/pybr2026-marp/issues) that says what happened and, if you can, includes a screenshot.

## Licenses

- Template, example text and code in this repository: [CC0 1.0](LICENSE) (public domain). Use, change and share them without asking for permission or giving credit.
- Logo, stickers and visual identity: Python Brasil 2026 and APyB, from the event's official brand book, created by [Ana Terhorst](https://anaterhorstdesign.com).
- Roboto and Cascadia Mono fonts: SIL Open Font License 1.1, loaded from Google Fonts.
