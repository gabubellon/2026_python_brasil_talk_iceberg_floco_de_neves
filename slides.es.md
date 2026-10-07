---
marp: true
theme: pybr2026
lang: es
paginate: true
footer: Python Brasil 2026
title: Python Brasil 2026
---

<!-- _class: capa -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="selo">14 al 19<br>de octubre<br>de 2026<br>{Floripa/SC}</div>

# Título de tu charla

Plantilla de diapositivas de Python Brasil 2026

**Tu nombre aquí** · @tu_usuario

<!--
- ¡Qué bueno que vas a dar una charla! Tu manera de hablar vale más que cualquier consejo de esta plantilla.
- Este archivo es una plantilla: cada diapositiva de ejemplo muestra un diseño y trae consejos en las notas. Usa los que te sirvan.
- Para empezar: guarda una copia sin cambios, elige la versión oscura o la clara y copia las diapositivas que quieras usar. El comentario _class al inicio de cada diapositiva elige el diseño.
- Al reutilizar una diapositiva, borra estas notas y escribe las tuyas.
-->

---

<!-- _class: frase -->

# La sala quiere que te vaya bien.

Cada diapositiva de esta plantilla trae consejos en las notas: presiona P para verlos.

<!--
- Una idea por diapositiva, en dos líneas como máximo. ¿Qué frase quieres que se lleve el público?
- Casi todas las personas que dan charlas se ponen nerviosas. Si llegan los nervios, háblale a una cara amiga entre el público.
-->

---

<!-- _class: palestrante -->

![Foto de ejemplo](img/foto-exemplo-es.png)

# Tu nombre aquí

### Lo que haces · dónde

- Quien abre la sesión suele presentarte
- Si hay poco tiempo, puedes quitar esta diapositiva
- Una autodescripción ayuda a quien no ve

<!--
- Para usar tu foto, pon su ruta en lugar de img/foto-exemplo-es.png.
- Quien abre la sesión suele presentarte; si hay poco tiempo, puedes quitar esta diapositiva.
- Una autodescripción ayuda a quien no ve, por ejemplo: “Soy María, mido 1,60 m, tengo el pelo negro suelto, uso lentes de montura verde y llevo una camiseta de PyLadies.”
-->

---

> La legibilidad es importante.

The Zen of Python, PEP 20

Consejos, <mark>no reglas</mark>: usa los que te sirvan.

<!--
- Hasta tres líneas, con quién lo dijo y dónde. Conviene confirmar la autoría en una fuente primaria.
- Las comillas verdes vienen del tema: empieza la línea de la cita con > y escríbela sin comillas.
-->

---

## A la hora de empezar

- Suelta el aire despacio antes de la primera frase
- El público está de tu lado
- Habla con calma y respira entre frases
- La charla es tuya, a tu ritmo

<!--
- De tres a cinco puntos por diapositiva. Si el texto no cabe, divide el contenido en dos diapositivas.
-->

---

## Agenda

1. La agenda muestra el camino de la charla
2. De tres a cinco partes suelen bastar
3. Vuelve a esta diapositiva entre una parte y otra
4. Cada parte puede empezar con una diapositiva de sección
5. Opcional: puedes quitarla si hay poco tiempo

<!--
- La numeración es automática.
- Volver a la agenda entre las partes ayuda al público a saber dónde está.
-->

---

<!-- _class: secao -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# _01_ Una sección para cada parte de la agenda

<!--
- El número entre guiones bajos aparece en el disco verde lima: # _01_ Título. El número sigue el orden de la agenda.
-->

---

<!-- _class: duas-colunas -->

## Texto en la diapositiva

### En lugar de

- Párrafos enteros
- Leer la diapositiva en voz alta
- Reducir la letra para que quepa
- El guion en la diapositiva

### Prueba

- Una idea por diapositiva
- Decir lo que la diapositiva no dice
- Dividir en dos diapositivas
- El guion en las notas de la diapositiva

<!--
- Cada columna tiene su título: antes y después, problema y solución.
- El detalle y el guion van a las notas, que solo tú ves.
-->

---

## Imágenes que explican

![bg right:42%](img/imagem-exemplo-es.png)

- Un diagrama en lugar de un párrafo
- Una imagen por idea
- Descríbela para quien no ve

<!--
- La caja gris marca el lugar de tu imagen: cambia img/imagem-exemplo-es.png por la ruta de la tuya. Con ![bg right:42%](archivo.png), el texto ocupa el resto de la diapositiva.
- Escribe el texto alternativo entre los corchetes de cada imagen que no sea de fondo.
- Al hablar, di lo que muestra la imagen, para quien no ve y para quien escucha la grabación.
-->

---

## Licencia y crédito

![bg left:42%](img/imagem-exemplo-es.png)

- Fotos tuyas o de licencia libre
- ¿La licencia permite este uso?
- El crédito de autoría en la diapositiva
- Al menos 1080 px de altura

<!--
- Una foto vertical llena este espacio; una foto horizontal aparece recortada en los lados. Cambia left por right para que la imagen vaya a la derecha.
- Confirma que la licencia de la foto permite usarla en una charla grabada y da el crédito con el formato “Foto: nombre, licencia, sitio”.
-->

---

<!-- _class: tres-imagens -->

## Capturas de pantalla legibles

- ![Captura de pantalla de ejemplo](img/captura-exemplo-es.png) Solo la parte que importa
- ![Captura de pantalla de ejemplo](img/captura-exemplo-es.png) Letra grande antes de capturar
- ![Captura de pantalla de ejemplo](img/captura-exemplo-es.png) Sin contraseñas, tokens ni correos

<!--
- Para cada captura, pon la ruta del archivo en lugar de img/captura-exemplo-es.png y describe la imagen entre los corchetes.
- Antes de capturar la pantalla, aumenta el zoom del navegador o el tamaño de letra de la terminal.
- Revisa si la captura muestra contraseñas, tokens, correos, pestañas o notificaciones.
-->

---

## Código con colores

```python
@dataclass
class Charla:
    titulo: str
    duracion_min: int = 25

    def cabe_en_bloque(self, bloque_min: int) -> bool:
        # Reserva 5 minutos para preguntas
        return self.duracion_min + 5 <= bloque_min
```

![bg right:22% 70%](img/sticker-mago.png)

<!--
- Si tu charla no tiene código, puedes saltar esta diapositiva.
- Hasta 8 líneas de unos 60 caracteres. Si el fragmento es más largo, divídelo en varias diapositivas o muestra solo lo que importa.
- Marp colorea el código por su cuenta: abre el bloque con ```python, o con el lenguaje del fragmento.
- El código va en una tarjeta blanca también en la diapositiva oscura. Los estudios de legibilidad muestran que el texto oscuro sobre fondo claro se lee mejor, sobre todo en letra pequeña, como la del código (Piepenbrock, Mayr y Buchner, 2014).
- Si prefieres fondo oscuro para el código, cambia los colores del código en pybr2026.css por los del tema Monokai, con el fondo #1A1A1A, y pon la letra bien grande.
-->

---

<!-- _class: duas-colunas miuda -->

## Un ejemplo más corto también enseña

### Muy pequeño para leer 😟

```python
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Charla:
    titulo: str
    inicio: datetime
    duracion_min: int = 25

    @property
    def fin(self) -> datetime:
        return self.inicio + timedelta(minutes=self.duracion_min)

    def choca_con(self, otra: "Charla") -> bool:
        return self.inicio < otra.fin and otra.inicio < self.fin

    def cabe_en_bloque(self, bloque_min: int) -> bool:
        # Reserva 5 minutos para preguntas
        return self.duracion_min + 5 <= bloque_min
```

### Se lee desde el fondo 😊

```python
def cabe(charla, bloque):
    # 5 min para preguntas
    fin = charla.duracion + 5
    return fin <= bloque
```

<!--
- Antes y después de una refactorización, o dos formas de resolver el mismo problema.
- Cada bloque de código admite líneas de hasta 30 caracteres. Con la clase miuda en la diapositiva, el código de la izquierda queda pequeño a propósito, para mostrar cómo se ve la letra diminuta en la pantalla grande.
- El emoji también es un recurso: una cara triste o feliz muestra al instante qué lado es el ejemplo a evitar. El título dice lo mismo con palabras, para quien no ve el emoji.
-->

---

<!-- _class: numeros -->

## Tres números que ayudan

- **18** puntos de letra: se puede leer desde el fondo de la sala
- **1** ensayo en voz alta muestra cuánto dura la charla
- **5** minutos para preguntas al final

<!--
- Hasta tres números, cada uno con una etiqueta de lo que mide.
- El número va en negrita al inicio del punto: - **18** etiqueta.
-->

---

<!-- _class: cartoes -->

## Antes de subir al escenario

1. **Live coding** Plan B: capturas de pantalla o un video de la demo.
2. **Internet** Con los videos y las páginas descargados, no dependes de la red.
3. **PDF** Lleva las diapositivas en PDF en una memoria USB.

<!--
- Elige el plan B que vaya con tu charla y ensaya el cambio a ese plan en tu computadora.
- Con charlas seguidas, no siempre hay tiempo de probar el sonido; un video subtitulado funciona sin audio.
-->

---

## El día de tu charla

| Cuándo | Sugerencia |
|---|---|
| Antes del evento | Preguntar en el grupo de Telegram de quienes presentan |
| La víspera | Con calma en el karaoke :P Cuida la voz y descansa |
| El día | Llegar temprano y conocer la sala |
| 15 min antes | Saludar al equipo de voluntariado de la sala |
| En la charla | Micrófono cerca de la boca, incluso cuando mires la pantalla |
| Después | Subir las diapositivas al enlace de tu código QR |

<!--
- Las tablas en Markdown ya salen con el encabezado verde lima.
- Probar en casa el adaptador de video y la opción de duplicar pantalla suele hacer el día más tranquilo.
- Cada sala tiene una persona voluntaria. Proyector, micrófono, ánimo: si te falta algo, te ayudamos.
-->

---

## La versión de Python que usas (%)

![Gráfico de barras con datos de ejemplo: Python 3.10 8%, 3.11 15%, 3.12 29%, 3.13 33% y 3.14 15%](img/grafico-exemplo.png)

Datos de ejemplo. Para cambiar los datos, mira las notas de esta diapositiva.

<!--
- Marp no tiene gráficos nativos: el gráfico es una imagen hecha con matplotlib. Cambia las etiquetas y los valores en scripts/grafico.py y ejecuta uv run scripts/grafico.py.
- Escribe los números del gráfico en el texto alternativo, para los lectores de pantalla.
- Un gráfico, un mensaje: di en voz alta lo que el público debe ver en las barras.
-->

---

<!-- _class: fluxo -->

## Un día de evento

1. Charlas
2. Coffee break
3. Lightning talks
4. PyBar

<!--
- Un flujo muestra una secuencia: los pasos de un proceso, las etapas de un pipeline, el programa del día.
- Recorre el flujo de izquierda a derecha: primero, después, al final.
-->

---

<!-- _class: imagem-cheia -->
<!-- _paginate: false -->
<!-- _footer: "" -->

![bg](img/fundo-exemplo-es.png)

Leyenda de la foto. Foto: Nombre de la persona · CC BY 4.0

<!--
- Cambia el archivo en ![bg](...). La leyenda es el último párrafo de la diapositiva.
- Da el crédito de la foto en la leyenda, como en el ejemplo.
-->

---

<!-- _class: destaque -->

## Tu charla es para todo el público

- Hay público infantil: contenido para todas las edades
- Humor que no ridiculiza a nadie, ejemplos sin estereotipos
- Si tienes dudas sobre algún contenido, la organización te ayuda

<!--
- El código de conducta de Python Brasil se aplica a todas las personas del evento, también en el escenario: python.org.br/cdc.
- Si sufres o presencias acoso, discriminación o humillación, busca al Equipo de Respuesta.
-->

---

## Referencias

- Código de conducta de Python Brasil [python.org.br/cdc](https://python.org.br/cdc)
- Marp, diapositivas en Markdown [marp.app](https://marp.app)
- Fuentes Roboto y Cascadia Mono [fonts.google.com](https://fonts.google.com)
- Verificador de contraste [webaim.org/resources/contrastchecker](https://webaim.org/resources/contrastchecker/)

<!--
- Una referencia por línea, con el nombre y la URL corta.
- Una sola página con todos los enlaces (un README, un gist o un Linktree) cabe en un código QR en el cierre.
-->

---

<!-- _class: encerramento -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# ¿Preguntas?

**Tu nombre aquí**
_@tu_usuario_
_tu@ejemplo.com_

![Código QR para 2026.pythonbrasil.org.br](img/qr.png)

Reemplázalo por tu código QR: contacto, diapositivas o web

<!--
- El código QR puede llevar a tu contacto, a tus diapositivas o a una página con todo. Con una sola página, puedes actualizar los enlaces después sin generar otro código QR.
- Para generar tu código QR: uv run scripts/qr.py https://tu-direccion. El script reemplaza el archivo img/qr.png. Después, cambia la leyenda por el enlace.
- Las siguientes diapositivas repiten los diseños en la versión clara, con más consejos.
-->

---

<!-- _class: capa light -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="selo">14 al 19<br>de octubre<br>de 2026<br>{Floripa/SC}</div>

# Título de tu charla

Versión clara, para proyector, TV o monitor

**Tu nombre aquí** · @tu_usuario

<!--
- Pantalla LED del tamaño de una pared: usa la versión oscura, que no deslumbra al público. Proyector, TV o monitor: usa la versión clara. El código va sobre fondo claro en las dos.
-->

---

<!-- _class: secao light -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# _02_ Una pausa para respirar y tomar agua

<!--
- Entre una parte y otra, haz una pausa: respira y toma un sorbo de agua.
- La pausa parece larga para quien habla y corta para quien escucha.
-->

---

<!-- _class: light -->

## Tu computadora en la pantalla grande

- Notificaciones apagadas (modo No molestar)
- Fondo de pantalla neutro
- Solo las pestañas y los programas de la charla
- Ventana privada: el historial no aparece al escribir direcciones

<!--
- La pantalla grande muestra todo lo que aparece en tu computadora: activa el modo No molestar antes de subir al escenario.
- En una ventana privada, el navegador no sugiere direcciones del historial.
-->

---

<!-- _class: duas-colunas light -->

## Un ensayo en voz alta ayuda

### Ensayar

- Con cronómetro
- Con alguien mirando
- En la computadora con la que vas a presentar

### Recortar

- Lo que se pase del tiempo
- Detalles que caben en las notas
- Diapositivas que saltas al ensayar

<!--
- Ensayar en voz alta muestra cuánto dura la charla y suele darte más soltura al hablar.
-->

---

<!-- _class: light -->

## Imágenes accesibles

![bg right:42%](img/imagem-exemplo-es.png)

- Texto alternativo en cada imagen
- Leyenda corta si la imagen no es obvia
- El color y el emoji ayudan, pero no por sí solos

<!--
- Los colores y los emojis comunican bien, pero no pueden ser la única diferencia: parte del público tiene daltonismo, baja visión o usa lector de pantalla.
- Acompaña el color con una etiqueta o un ícono: en lugar de un punto verde y uno rojo, escribe también “pasó” y “falló”.
- Todo el texto de la plantilla tiene un contraste de 4,5:1 o más con el fondo. Si usas otros colores, revísalos en webaim.org/resources/contrastchecker.
-->

---

<!-- _class: light -->

## Hablar con la sala

![bg left:42%](img/imagem-exemplo-es.png)

- Mirar al público, si te resulta cómodo
- Las notas de la diapositiva como apoyo
- Señalar con palabras, no con el puntero

<!--
- Las notas aparecen solo para ti en la vista de presentación. Mirar las notas en el escenario es normal.
- En el HTML exportado, presiona P: la vista de presentación muestra las notas, la siguiente diapositiva y el cronómetro.
-->

---

<!-- _class: light -->

## Código con colores

```python
@dataclass
class Charla:
    titulo: str
    duracion_min: int = 25

    def cabe_en_bloque(self, bloque_min: int) -> bool:
        # Reserva 5 minutos para preguntas
        return self.duracion_min + 5 <= bloque_min
```

**¿Prefieres fondo oscuro para el código?** Usa el tema Monokai y pon la letra bien grande.

<!--
- Para código sobre fondo oscuro, mira las notas de la diapositiva “Código con colores”, en la parte oscura.
-->

---

<!-- _class: light -->

> <mark>Pessoas</mark> &gt; Tecnologia

Comunidad Python Brasil, 2016

<!--
- En el fondo blanco, destaca la palabra principal con el resaltador verde lima, <mark>palabra</mark>, y mantén el texto negro.
- El lema de la comunidad Python Brasil desde 2016: «Personas > Tecnología».
-->

---

<!-- _class: frase light -->

# Menos texto, letra más grande.

<!--
- Con menos texto en la diapositiva, cabe una letra más grande, y el público tiende a mirarte más a ti.
-->

---

<!-- _class: destaque light -->

## Habla de forma acogedora

- Muestra el paso a paso en vez de decir que es fácil
- Explica cada sigla la primera vez que aparece
- Pregunta quién ya lo usó en vez de suponer

<!--
- El panel verde lima lleva el mensaje que la sala no puede perderse, con hasta cuatro puntos cortos al lado.
- Para quien está empezando, “solo tienes que” y “todo el mundo sabe” suenan a “deberías saberlo”.
- Para muchas personas, Python Brasil es su primera conferencia; un ejemplo cotidiano ayuda a quien acaba de llegar.
-->

---

<!-- _class: cartoes light -->

## Después de la charla

1. **Notas** Anota lo que funcionó, para la próxima charla.
2. **Conversación** Quédate cerca: muchas preguntas surgen en el pasillo.
3. **Descanso** Disfruta el resto del evento. Te lo mereces.

<!--
- Anotar justo después lo que funcionó ayuda en la próxima charla.
- El cansancio después de presentar es normal: descansa y disfruta el resto del evento.
-->

---

<!-- _class: palestrante light -->

![Foto de ejemplo](img/foto-exemplo-es.png)

# Tu nombre aquí

### Pronombres, cargo y comunidad

- Dónde puede encontrarte el público
- Tres datos, no un currículum
- Una foto reciente

<!--
- Con los pronombres en la diapositiva, quien mencione tu charla sabrá cómo referirse a ti.
-->

---

<!-- _class: fluxo light -->

## Del borrador al escenario

1. Escribir en Markdown
2. Ensayar en voz alta
3. Exportar a PDF
4. Presentar

<!--
- Una lista numerada se convierte en cajas con flechas; el último paso va en verde lima.
- De tres a cinco pasos caben en una línea. Para un flujo con ramificaciones, divídelo en dos diapositivas.
-->

---

<!-- _class: light -->

## La versión de Python que usas (%)

![Gráfico de barras con datos de ejemplo: Python 3.10 8%, 3.11 15%, 3.12 29%, 3.13 33% y 3.14 15%](img/grafico-exemplo-claro.png)

Datos de ejemplo. Para cambiar los datos, mira las notas de esta diapositiva.

<!--
- Para cambiar los datos, mira las notas de la diapositiva “La versión de Python que usas”, en la parte oscura.
- Escribe los números del gráfico en el texto alternativo, para los lectores de pantalla.
-->

---

<!-- _class: encerramento light -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# ¡Gracias!

**Tu nombre aquí**
_@tu_usuario_
_tu@ejemplo.com_

![Código QR para 2026.pythonbrasil.org.br](img/qr.png)

Reemplázalo por tu código QR: contacto, diapositivas o web

<!--
- Durante las preguntas, repite cada una al micrófono, para la sala y la grabación.
- “No lo sé, puedo revisarlo y te respondo después” es una buena respuesta. Una pregunta que no respeta el código de conducta no necesita respuesta.
- De la organización: nos alegra mucho tenerte en Python Brasil 2026. Cuenta con el equipo: estamos aquí para apoyarte y estamos de tu lado.
-->

---

<!-- _class: figurinhas -->
<!-- _paginate: false -->
<!-- _footer: "" -->

## Stickers

### Dazumbanho! Chegasse ao fim, ixtepô!

![w:290](img/lockup-on-dark.png) ![w:190](img/sticker-witch.png) ![w:220](img/sticker-mago-ola.png) ![w:130](img/sticker-mago.png) ![w:120](img/magia-explosao.png)

![w:280](img/logo-assinatura.png) <span class="circulo">mira aquí</span> <mark>resaltador</mark> ![w:96](img/icone-seta.png) ![w:96](img/icone-codigo.png)

Identidad visual de Ana Terhorst, [anaterhorstdesign.com](https://anaterhorstdesign.com). ¡Gracias, Ana!

<!--
- “Dazumbanho! Chegasse ao fim, ixtepô!” es un saludo en el dialecto de Florianópolis, algo como “¡Caramba! Llegaste al final, ¡mira nada más!”.
- Copia la línea del sticker a tu diapositiva; el número en w:190 define el ancho en píxeles.
- El sticker resaltador es texto editable: cambia su palabra, o usa <mark>palabra</mark> en una palabra tuya. El círculo pixelado es <span class="circulo">palabra</span>.
- Un sticker por diapositiva suele bastar.
-->
