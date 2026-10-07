---
marp: true
theme: pybr2026
lang: en
paginate: true
footer: Python Brasil 2026
title: Python Brasil 2026
---

<!-- _class: capa -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="selo">October<br>14 to 19<br>2026<br>{Floripa/SC}</div>

# Your talk title

Python Brasil 2026 slide template

**Your name here** · @your_username

<!--
- We're glad you're speaking! Your own style matters more than any tip in this template.
- This file is a template: each example slide shows a layout and has tips in the speaker notes. Use the ones that work for you.
- To get started: keep an unchanged copy, choose the dark or the light version, and copy the slides you want to use. The _class comment at the top of each slide sets the layout.
- When you reuse a slide, delete these notes and write your own.
-->

---

<!-- _class: frase -->

# The room is cheering for you.

Every slide in this template has tips in the speaker notes: press P to see them.

<!--
- One idea per slide, in two lines at most. What sentence should the audience take home?
- Almost every speaker feels nervous. If you feel nervous, speak to one friendly face in the audience.
-->

---

<!-- _class: palestrante -->

![Example photo](img/foto-exemplo-en.png)

# Your name here

### What you do · where

- The session chair often introduces you
- If time is short, you can skip this slide
- Describing yourself helps people who cannot see

<!--
- To use your photo, replace img/foto-exemplo-en.png with its path.
- The session chair often introduces you; if time is short, you can skip this slide.
- Describing yourself helps people who cannot see. For example: “I'm Maria. I'm 1.60 m tall and have black hair worn down. I wear green-framed glasses and a PyLadies T-shirt.”
-->

---

> Readability counts.

The Zen of Python, PEP 20

Tips, <mark>not rules</mark>: use the ones that work for you.

<!--
- Up to three lines, with who said it and where. It helps to check the attribution in a primary source.
- The green quotation marks come from the theme: start the quote line with > and write the quote without quotation marks.
-->

---

## When you start

- Breathe out slowly before your first sentence
- The audience is on your side
- Speak calmly and breathe between sentences
- The talk is yours, at your own pace

<!--
- Three to five bullets per slide. If the text does not fit, split the content into two slides.
-->

---

## Agenda

1. The agenda shows where the talk is going
2. Three to five parts are usually enough
3. Come back to this slide between parts
4. Each part can open with a section slide
5. Optional: you can skip it if time is short

<!--
- The numbering is automatic.
- Coming back to the agenda between parts helps the audience know where they are.
-->

---

<!-- _class: secao -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# _01_ One section for each part of the agenda

<!--
- The number between underscores goes into the lime circle: # _01_ Title. The number follows the order of the agenda.
-->

---

<!-- _class: duas-colunas -->

## Text on the slide

### Instead of

- Whole paragraphs
- Reading the slide aloud
- Shrinking the font to fit
- A cheat sheet on the slide

### Try

- One idea per slide
- Saying what the slide does not say
- Splitting the content into two slides
- The cheat sheet in the speaker notes

<!--
- Each column has its own heading: before and after, problem and solution.
- The details and your cheat sheet go in the speaker notes, which only you see.
-->

---

## Images that explain

![bg right:42%](img/imagem-exemplo-en.png)

- A diagram instead of a paragraph
- One image per idea
- Describe it for people who cannot see

<!--
- The gray box marks the place for your image: replace img/imagem-exemplo-en.png with the path to yours. With ![bg right:42%](file.png), the text fills the rest of the slide.
- Write alt text between the brackets of every image that is not a background.
- When you speak, say what the image shows, for people who cannot see it and for people who listen to the recording.
-->

---

## License and credit

![bg left:42%](img/imagem-exemplo-en.png)

- Your own photos or openly licensed ones
- Does the license allow this use?
- Credit the author on the slide
- At least 1080 px tall

<!--
- A portrait photo fills this space; a landscape photo is cropped at the sides. Change left to right to put the image on the right.
- Check that the photo's license allows use in a recorded talk, and credit it in the format “Photo: name, license, site”.
-->

---

<!-- _class: tres-imagens -->

## Readable screenshots

- ![Example screenshot](img/captura-exemplo-en.png) Only the part that matters
- ![Example screenshot](img/captura-exemplo-en.png) Increase the font size first
- ![Example screenshot](img/captura-exemplo-en.png) No passwords, tokens or emails

<!--
- Replace each gray box with your screenshot: replace img/captura-exemplo-en.png with the path to the screenshot, and describe the screenshot between the brackets.
- Before you take the screenshot, zoom in on the browser or increase the terminal font size.
- Check that the screenshot does not show passwords, tokens, emails, open tabs or notifications.
-->

---

## Code in color

```python
@dataclass
class Talk:
    title: str
    duration_min: int = 25

    def fits_in_slot(self, slot_min: int) -> bool:
        # Keep 5 minutes for questions
        return self.duration_min + 5 <= slot_min
```

![bg right:22% 70%](img/sticker-mago.png)

<!--
- If your talk has no code, you can skip this slide.
- Up to 8 lines, with up to 60 characters per line. If the snippet is longer, split it across slides or show only what matters.
- Marp adds syntax highlighting for you: open the block with ```python, or with the language of the snippet.
- The code sits on a light card, even on the dark slide. Legibility studies show that dark text on a light background is easier to read, especially at small sizes such as code (Piepenbrock, Mayr and Buchner, 2014).
- If you prefer a dark background for code, replace the code colors in pybr2026.css with the Monokai theme on #1A1A1A, and make the font large.
-->

---

<!-- _class: duas-colunas miuda -->

## A smaller example teaches too

### Too small to read 😟

```python
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Talk:
    title: str
    start: datetime
    duration_min: int = 25

    @property
    def end(self) -> datetime:
        return self.start + timedelta(minutes=self.duration_min)

    def overlaps(self, other: "Talk") -> bool:
        return self.start < other.end and other.start < self.end

    def fits_in_slot(self, slot_min: int) -> bool:
        # Keep 5 minutes for questions
        return self.duration_min + 5 <= slot_min
```

### Readable from the back 😊

```python
def fits(talk, slot):
    # 5 min for questions
    needed = talk.duration + 5
    return needed <= slot
```

<!--
- Before and after a refactoring, or two ways to solve the same problem.
- Each code block fits lines of up to 30 characters. The miuda class on the slide makes the left code small on purpose, to show how tiny text looks on the big screen.
- Emoji are a tool too: a sad or a happy face shows immediately which side is the example to avoid. The heading says the same in words, for people who cannot see the emoji.
-->

---

<!-- _class: numeros -->

## Three numbers that help

- **18** point text: you can read it from the back row
- **1** rehearsal out loud shows how long the talk takes
- **5** minutes for questions at the end

<!--
- Up to three numbers, each with a label for what it measures.
- The number goes in bold at the start of the item: - **18** label.
-->

---

<!-- _class: cartoes -->

## Before you go on stage

1. **Live coding** Plan B: screenshots or a video of the demo.
2. **Internet** With videos and pages downloaded, you do not depend on the network.
3. **PDF** Bring the slides as a PDF on a USB drive.

<!--
- Choose the plan B that fits your talk, and rehearse the switch to it on your computer.
- When talks follow each other with no break, there is not always time for a sound check. A video with captions works without audio.
-->

---

## The day of your talk

| When | Suggestion |
|---|---|
| Before the event | Ask questions in the speakers' Telegram group |
| The day before | Go easy on the karaoke :P Rest your voice and sleep well |
| On the day | Arrive early and look around the room |
| 15 min before | Say hello to the room volunteers |
| During the talk | Keep the mic close to your mouth, even when you look at the screen |
| After | Publish your slides at the address in your QR code |

<!--
- Markdown tables get the lime header from the theme.
- Testing your video adapter and screen mirroring at home usually makes the day calmer.
- Every room has a volunteer. Projector, microphone, courage: whatever you need, we will help.
-->

---

## Which Python version do you use? (%)

![Bar chart with sample data: Python 3.10 8%, 3.11 15%, 3.12 29%, 3.13 33% and 3.14 15%](img/grafico-exemplo.png)

Sample data. To change the data, see the notes on this slide.

<!--
- Marp has no built-in charts: the chart is an image made with matplotlib. Change the labels and values in scripts/grafico.py, then run the command uv run scripts/grafico.py.
- Write the chart numbers in the alt text, for screen readers.
- One chart, one message: say out loud what the audience should see in the bars.
-->

---

<!-- _class: fluxo -->

## A day at the conference

1. Talks
2. Coffee break
3. Lightning talks
4. PyBar

<!--
- A flow shows a sequence: the steps of a process, the stages of a pipeline, the schedule of the day.
- Describe the flow from left to right: first, then, finally.
-->

---

<!-- _class: imagem-cheia -->
<!-- _paginate: false -->
<!-- _footer: "" -->

![bg](img/fundo-exemplo-en.png)

Photo caption. Photo: Person's name · CC BY 4.0

<!--
- Replace the file in ![bg](...). The caption is the last paragraph of the slide.
- Credit the photo in the caption, as in the example.
-->

---

<!-- _class: destaque -->

## Your talk is for everyone

- The audience includes children: content for all ages
- Humor that mocks nobody, examples without stereotypes
- Unsure about some content? The organizers can help

<!--
- The Python Brasil code of conduct applies to everyone at the event, including on stage: python.org.br/cdc.
- If you experience or witness harassment, discrimination or humiliation, contact the Response Team.
-->

---

## References

- Python Brasil code of conduct [python.org.br/cdc](https://python.org.br/cdc)
- Marp, slides in Markdown [marp.app](https://marp.app)
- Roboto and Cascadia Mono fonts [fonts.google.com](https://fonts.google.com)
- Contrast checker [webaim.org/resources/contrastchecker](https://webaim.org/resources/contrastchecker/)

<!--
- One resource per line, with its name and a short URL.
- A single page with all the links (a README, a gist or a Linktree) fits in a QR code on the closing slide.
-->

---

<!-- _class: encerramento -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# Questions?

**Your name here**
_@your_username_
_you@example.com_

![QR code for 2026.pythonbrasil.org.br](img/qr.png)

Replace with your QR code: contact, slides or site

<!--
- The QR code can lead to your contact details, your slides or a page with all of them. With a single page of links, you can update the links later and keep the same QR code.
- To generate your QR code: uv run scripts/qr.py https://your-url. The script replaces img/qr.png. Then replace the caption with the link.
- The next slides repeat the layouts in the light version, with more tips.
-->

---

<!-- _class: capa light -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="selo">October<br>14 to 19<br>2026<br>{Floripa/SC}</div>

# Your talk title

Light version, for projectors, TVs and monitors

**Your name here** · @your_username

<!--
- LED screen as big as a wall: use the dark version, which is not too bright for the audience. Projector, TV or monitor: use the light version. Code stays on a light background in both.
-->

---

<!-- _class: secao light -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# _02_ A pause to breathe and drink water

<!--
- Between one part and the next, pause: breathe and take a sip of water.
- A pause feels long to the speaker and short to the audience.
-->

---

<!-- _class: light -->

## Your screen on the big screen

- Notifications off (Do Not Disturb)
- A neutral wallpaper
- Only the tabs and apps for the talk
- Private window: no history suggestions as you type

<!--
- The big screen shows everything on your screen: turn on Do Not Disturb before you go on stage.
- In a private window, the browser does not suggest addresses from your history.
-->

---

<!-- _class: duas-colunas light -->

## Rehearsing out loud helps

### Rehearse

- With a timer
- With someone watching
- On the computer you will present from

### Cut

- What runs over time
- Details that belong in the notes
- Slides you skip in rehearsal

<!--
- Rehearsing out loud shows how long the talk takes and usually makes your delivery more relaxed.
-->

---

<!-- _class: light -->

## Accessible images

![bg right:42%](img/imagem-exemplo-en.png)

- Alt text on every image
- A short caption if the image is not obvious
- Color and emoji help, but not on their own

<!--
- Colors and emoji communicate well, but they cannot be the only difference: some people in the audience are color blind, have low vision or use a screen reader.
- Pair color with a label or an icon: instead of a green dot and a red dot, also write “passed” and “failed”.
- All text in the template has a contrast ratio of 4.5:1 or more against the background. If you use other colors, check them at webaim.org/resources/contrastchecker.
-->

---

<!-- _class: light -->

## Talk to the room

![bg left:42%](img/imagem-exemplo-en.png)

- Look at the audience, if that feels comfortable
- Speaker notes for support
- Point with words, not with the mouse

<!--
- Only you see the speaker notes, in presenter view. Looking at your notes on stage is normal.
- In the exported HTML, press P: presenter view shows the notes, the next slide and the timer.
-->

---

<!-- _class: light -->

## Code in color

```python
@dataclass
class Talk:
    title: str
    duration_min: int = 25

    def fits_in_slot(self, slot_min: int) -> bool:
        # Keep 5 minutes for questions
        return self.duration_min + 5 <= slot_min
```

**Prefer a dark background for code?** Use the Monokai theme and make the font large.

<!--
- For code on a dark background, see the notes on the “Code in color” slide in the dark section.
-->

---

<!-- _class: light -->

> <mark>Pessoas</mark> &gt; Tecnologia

Python Brasil community, 2016

<!--
- On the white background, highlight the main word with the lime green highlighter, <mark>word</mark>, and keep the text black.
- The motto of the Python Brasil community since 2016.
-->

---

<!-- _class: frase light -->

# Less text, larger font.

<!--
- With less text on the slide, a larger font fits, and the audience tends to look at you more.
-->

---

<!-- _class: destaque light -->

## Speak in a welcoming way

- Show the steps instead of saying it is easy
- Explain each acronym the first time
- Ask who has used a tool instead of assuming

<!--
- The lime green panel holds the message the room should not miss, with up to four short bullets beside it.
- For beginners, “it's just” and “everyone knows” sound like “you should know this”.
- For many people, Python Brasil is their first conference; an everyday example helps newcomers.
-->

---

<!-- _class: cartoes light -->

## After the talk

1. **Notes** Write down what worked, for your next talk.
2. **Chat** Stay nearby: many people ask questions in the hallway.
3. **Rest** Enjoy the rest of the event. You earned it.

<!--
- If you write down what worked right after the talk, your next talk benefits.
- Feeling tired after speaking is normal: take a break and enjoy the rest of the event.
-->

---

<!-- _class: palestrante light -->

![Example photo](img/foto-exemplo-en.png)

# Your name here

### Pronouns, role and community

- Where the audience can find you
- Three facts, not a résumé
- A recent photo

<!--
- With your pronouns on the slide, people who mention your talk can refer to you correctly.
-->

---

<!-- _class: fluxo light -->

## From draft to stage

1. Write Markdown
2. Rehearse aloud
3. Export to PDF
4. Present

<!--
- A numbered list becomes boxes with arrows; the last step is lime.
- Three to five steps fit on one line. For a flow with branches, split it into two slides.
-->

---

<!-- _class: light -->

## Which Python version do you use? (%)

![Bar chart with sample data: Python 3.10 8%, 3.11 15%, 3.12 29%, 3.13 33% and 3.14 15%](img/grafico-exemplo-claro.png)

Sample data. To change the data, see the notes on this slide.

<!--
- To change the data, see the notes on the “Which Python version do you use?” slide in the dark section.
- Write the chart numbers in the alt text, for screen readers.
-->

---

<!-- _class: encerramento light -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# Thank you!

**Your name here**
_@your_username_
_you@example.com_

![QR code for 2026.pythonbrasil.org.br](img/qr.png)

Replace with your QR code: contact, slides or site

<!--
- During questions, repeat each question into the microphone, for the room and the recording.
- “I don't know, but I can check and get back to you” is a good answer. A question that breaks the code of conduct does not need an answer.
- From the organizers: we're so happy to have you at Python Brasil 2026. We're here to support you and cheer for you.
-->

---

<!-- _class: figurinhas -->
<!-- _paginate: false -->
<!-- _footer: "" -->

## Stickers

### Dazumbanho! Chegasse ao fim, ixtepô!

![w:290](img/lockup-on-dark.png) ![w:190](img/sticker-witch.png) ![w:220](img/sticker-mago-ola.png) ![w:130](img/sticker-mago.png) ![w:120](img/magia-explosao.png)

![w:280](img/logo-assinatura.png) <span class="circulo">look here</span> <mark>highlighter</mark> ![w:96](img/icone-seta.png) ![w:96](img/icone-codigo.png)

Visual identity by Ana Terhorst, [anaterhorstdesign.com](https://anaterhorstdesign.com). Thanks, Ana!

<!--
- “Dazumbanho! Chegasse ao fim, ixtepô!” is an expression in the Florianópolis (manezinho) dialect, roughly “Wow! You made it to the end, look at that!”.
- Copy the sticker line into your slide; the number in w:190 sets the width in pixels.
- The highlighter sticker is live text: change its word, or use <mark>word</mark> on a word of your own. The pixelated circle is <span class="circulo">word</span>.
- One sticker per slide is usually enough.
-->
