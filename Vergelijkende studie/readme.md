# Vergelijkende studie: Sass vs LESS

## 1. Inleiding

Dit is een vergelijkende studie tussen 2 bekende css preprocessors: Sass en LESS. In deze studie zullen we beide preprocessors vergelijken op basis van features, snelheid en syntax. Voor we starten is het natuurlijk belangrijk dat je weet wat css preprocessors zijn en wat ze doen en waarom we ze zouden gebruiken.

### Wat zijn CSS preprocessors?

CSS preprocessors nemen code geschreven in de preprocessed taal en converteren dit in gewone css code. 3 populaire css preprocessors zijn Sass, LESS en Stylus, waarvan we Sass en Less met elkaar gaan vergelijken.

### Waarom zouden we CSS preprocessors gebruiken?

CSS is enorm goed, maar het laat ons niet altijd alles doen wat we willen. Het doel van css was om zo simpel te zijn dat iedereen er snel mee kon beginnen zonder enige moeite. Dit zorgt er wel voor dat wat je kan doen met css heel gelimiteerd is en programmeurs hebben liever meer vrijheid. CSS preprocessors bieden ons die vrijheid, door extra functionaliteiten toe te voegen zoals variabelen, geneste css regels, herbruikbare code stukken, enz...

Door al die toegevoegde functionaliteit zal je sneller flexibele en makkelijker onderhoudbare CSS kunnen schrijven, tegenover met pure CSS.


## 2. Voornaamste features

### Sass

- Volledig combineerbaar met CSS
- Uitbreidingen zoals variabelen, geneste regels en mixins
- Handige functies voor het manipuleren van kleuren en andere waarden
- Goed geformateerde en aanpasbare output

### LESS

- Combineerbaar met CSS
- Variabelen
- Mixins
- Geneste CSS regels

## 3. Vergelijking

### 3.1 Installatie

De installatie is een zeer belangrijk onderdeel. Sass maakt gebruik van Ruby om `.scss` en `.sass` bestanden te compilen naar CSS. Bij Mac's is dit al geïnstalleerd, maar bij Windows moet je zelf eerst Ruby installeren omdat dit er niet standaard op staat. LESS daarentegen gebruikt JavaScript om zijn `.less` bestanden te compilen naar CSS, hier moet je alleen less op je computer zetten en het werkt direct.

Beiden hebben wel een aantal programma's waar je gewoon je bestanden kan inslepen of folders kiezen waar je alle bestanden van wilt compilen. Dit is de gemakkelijkste oplossing, maar je kan het niet uitbreiden of kiezen hoe je bepaalde zaken wilt doen.

[Sass installeren](http://sass-lang.com/install)

[LESS installeren](http://lesscss.org/)

**Conclusie: LESS is wat eenvoudiger te installeren, aangezien Sass Ruby nodig heeft.**

### 3.2 De leercurve (Ruby, Command Line, ...)

De enige leercurve is eigenlijk de nieuwe syntax die je moet leren, aangezien je een applicatie zoals CodeKit, LiveReload of Mixture kan gebruiken om je bestanden in het oog te houden en te converteren wanneer er iets veranderd. Dit betekent dat je eigenlijk niets van Ruby, de Command Line of eender wat anders moet kennen. Het kan natuurlijk alleen maar handig zijn als je deze zaken wel kent.

**Conclusie: Beiden zijn eenvoudig om mee te starten.**

### 3.3 Extensies

Zowel Sass als LESS hebben verschillende extensies zodat je sneller en eenvoudiger code kan schrijven.

De populairste Sass extensie is volgens mij [Compass](http://compass-style.org/), dit heeft een aantal mixins om sneller CSS te schrijven. Compass heeft ook nog enkele andere zaken, zoals [Helper functies](http://compass-style.org/reference/compass/helpers/), [Layout](http://compass-style.org/reference/compass/layout/), [Typografie stijlen](http://compass-style.org/reference/compass/typography/), [Manier om met sprite images te werken](http://compass-style.org/reference/compass/utilities/sprites/). Compass bevat zowat alles wat je kan nodig hebben in je project.

LESS heeft ook een aantal extensies, maar er is geen volledig pakket zoals Compass. Hier zal je dus meer moeten zoeken naar de juiste extensies voor je project, wat het wat moeilijker maakt voor mensen die nog maar juist met een preprocessor beginnen werken.

Enkele LESS extensies zijn:

- Mixins: [LESS](http://lesselements.com/), [Preboot](http://markdotto.com/bootstrap/), [LESS-Mixins](https://github.com/tophermade/LESS-Mixins)
- Grids: [Fluidable](http://fluidable.com/), [Frameless](https://github.com/jonikorpi/Frameless)
- Layout: [even.less](https://github.com/bisrael/even.less)
- Algemeen: [Bootstrap](http://getbootstrap.com/)

**Conclusie: Beiden hebben genoeg extensies om je leven gemakkelijker te maken. Bij LESS zal je zelf een pakket van extensies moeten samenstellen, terwijl bij Sass Compass zowat alles bevat.**

### 3.4 Caching

Templates en partials die gecompiled zijn naar CSS worden gecached, waardoor ze de volgende keer wanneer je iets aanpast in je SCSS of LESS file waardoor er opnieuw gecompiled moet worden. De compiler zal dan eerst kijken of er templates of partials zijn waar niets aan veranderd is, als deze er zijn zal hun gecompilede versie uit de cache gehaald worden waardoor het compilen veel sneller zal gaan. Het is dus aangeraden om je code op te splitsen in verschillende bestanden zodat caching het beste werkt. Zowel Sass als LESS kunnen gebruik maken van caching.

**Conclusie: Beiden kunnen gebruik maken van caching.**

### 3.5 Variabelen

Variabelen kunnen gebruikt worden in Sass en LESS, ik denk dat dit de feature is waarvoor de meeste mensen kiezen om een preprocessor te gebruiken. Je kan dit gebruiken om kleurcodes op te slaan, een bepaald aantal pixels,...

In beide talen zijn de variabelen enkel te gebruiken binnen hun scope. Het verschil tussen beide is dat Sass gebruikt maakt van een dollar teken (`$`) voor hun variabelen en LESS gebruikt maakt van een ampersant (`@`). Aangezien in beide talen variabelen hetzelfde kunnen, komt het neer op wat jij het beste vindt. `$` of `@`.

Voorbeeld van scope:

```CSS
Sass                    | LESS
------------------------+---------------------
$color: #000;           | @color: #000            /* Global scope*/
                        |
header {                | header {
  color: $color;        |   color: @color;      
}                       | }
                        |
.content {              | .content {
  $color: #555;         |   @color: #555;         /* Selector scope */
  color: $color;        |   color: @color;
}                       | }
                        |
footer {                | footer {
  color: $color;        |   color: @color;
}                       | }
```

Beiden worden gecompiled naar:

```CSS
Output
------
header {
  color: #000
}
.content {
  color: #555
}
footer {
  color: #000
}
```

**Conclusie: Beiden zijn goed, het hangt af van wat jij het eenvoudigst vindt. `$` of `@`**

### 3.6 Geneste CSS regels

Zowel in Sass als LESS heb je de mogelijkheid om nesting te gebruiken bij selectors.

```CSS
Sass & LESS
-----------
nav {
  width: 100%;
  height: 50px;

  ul {
    padding: 0;
    margin: 0;

    li {
      margin-left: 10px;
    }
  }
}

Output
------
nav {
  width: 100%;
  height: 50px;
}
nav ul {
  padding: 0;
  margin: 0;
}
nav ul li {
  margin-left: 10px;
}
```

Maar in Sass kan je ook CSS properties nesten. Voorbeeld:

```CSS
Sass
----
nav {
  width: 100%;
  height: 50px;

  ul {
    padding: 0;
    margin: 0;

    li {
      margin-left: 10px;

      border: {
        style: solid;
        color: #000;
        left: {
          width: 4px;
          color: #222;
        }
      }
    }
  }
}

Output
------
nav {
  width: 100%;
  height: 50px;
}
nav ul {
  padding: 0;
  margin: 0;
}
nav ul li {
  margin-left: 10px;
  border-style: solid;
  border-color: #000;
  border-left-width: 4px;
  border-left-color: #222;
}
```

**Conclusie: Beiden kunnen selectors nesten, maar Sass gaat hier juist nog wat verder in door ook CSS regels te kunnen nesten.**

### 3.7 Mixins

Mixins kunnen zowel geschreven worden in Sass als LESS, maar de manier waarop je ze schrijft en aanroept is verschillend. In Sass gebruik je `@mixin` om een mixin te definiëren en in LESS gebruik je een class selector `.` . Om de mixin dan te gebruiken in een selector gebruik je in Sass `@include` en in LESS de naam die je aan de mixin klasse hebt gegeven.

```CSS
Sass                              | LESS
----------------------------------+-------------------------------
@mixin bordered {                 | .bordered {
  border: 2px solid #222;         |   border: 2px solid #222;
  border-top: 1px solid #000;     |   border-top: 1px solid #000;
}                                 | }
                                  |
button {                          | button {
  color: #fff;                    |   color: #fff;
  @include bordered;              |   .bordered
}                                 | }
                                  |
Output                            | Output
----------------------------------+-------------------------------                          
button {                          | .bordered {
  color: #fff;                    |   border: 2px solid #222;
  border: 2px solid #222;         |   border-top: 1px solid #000;
  border-top: 1px solid #222;     | }
}                                 | button {
                                  |   color: #fff;
                                  |   border: 2px solid #222;
                                  |   border-top: 1px solid #222;
                                  | }
```

Zoals je kan zien wordt de mixin in LESS ook mee gecompiled en in de output gezet, waardoor bestanden iets groter zullen zijn al is dit verschil miniem indien je weinig mixins gebruikt.

**Conclusie: Je kan mixins gebruiken in beide. De syntax is wat anders, in Sass wordt `@mixin` en `@include` gebruikt en in LESS gebruik je: `.naam-van-je-mixin`. In LESS blijft de mixin mee in de output staan.**

### 3.8 Mixins met argumenten (Dynamische mixins)

Dynamische mixins zijn mixins waar je argumenten met kan meegeven.

```CSS
Sass                              | LESS
----------------------------------+------------------------------
@mixin bordered($width: 1px) {    | .bordered(@width: 1px) {
  border: $width solid #222;      |   border: @width solid #222;
}                                 | }
                                  |
button {                          | button {
  @include bordered(3px);         |   .bordered(3px)
}                                 | }
                                  |
Sass                              | Output
----------------------------------+------------------------------
button {                          | button {
  border: 3px solid #222;         |   border: 3px solid #222;
}                                 | }
```

**Conclusie: Beiden hebben dezelfde output.**

### 3.9 Overerving van selectors

In Sass kan je door middel van `@extend` stijlen overerven van andere selectors, zo hoef je niet telkens verschillende klassen aan een HTML element geven.

```CSS
Sass
----
.error {
  border: 1px solid #f00;
  background-color: #fdd;
}

.seriousError {
  @extend .error;
  border-width: 5px;
}

Output
------
.error, .seriousError {
  border: 1px #f00;
  background-color: #fdd;
}
.seriousError {
  border-width: 5px;
}
```

In LESS is dit niet mogelijk. Je kan een soortgelijk resultaat behalen door middel van mixins, maar hierbij worden alle stijlen gekopieerd in plaats van dat de selector wordt toegevoegd. Dit zorgt er dus voor dat je gecompiled bestand groter zal zijn bij LESS dan bij Sass.

```CSS
LESS
----
.error {
  border: 1px solid #f00;
  background-color: #fdd;
}

.seriousError {
  .error();
  border-width: 5px;
}

Output
------
.error {
  border: 1px solid #f00;
  background-color: #fdd;
}
.seriousError {
  border: 1px solid #f00;
  background-color: #fdd;
  border-width: 5px;
}
```

**Conclusie: In Sass kan je d.m.v. `@extend` een selector toevoegen bij een stuk code, bij LESS gaat dit niet en zal je met mixins moeten werken. Hierdoor zal je gecompiled bestand groter zijn bij LESS.**

### 3.10 Kleurmanipulatie



### 3.11 Wiskundige berekeningen

### 3.12 Logica en Loops

### 3.13 Media queries

### 3.14 Impoteren van andere bestanden

### 3.15 Opmaak van de Output

### 3.16 Namespaces





## Logboek

- 13/12/2015 - Resources gezocht
- 15/12/2015 - Inleiding geschreven, begonnen met vergelijken
- 16/01/2016 - Sass en LESS documentatie doorgenomen en verschillen opgeschreven
- 17/01/2016 - Verschillen met code voorbeelden uitwerken
- 18/01/2016 - Verschillen met code voorbeelden uitwerken

## Resources

- Sass: http://sass-lang.com/
- Less: http://lesscss.org/
- Sass And LESS: An Introduction To CSS Preprocessors: http://vanseodesign.com/css/css-preprocessors/
- CSS Preprocessors Compared: Sass vs. LESS: http://www.hongkiat.com/blog/sass-vs-less/
- Sass vs. LESS: https://css-tricks.com/sass-vs-less/
- Sass/Less Comparison: https://gist.github.com/chriseppstein/674726
- Less vs Sass? It’s time to switch to Sass: http://www.zingdesign.com/less-vs-sass-its-time-to-switch-to-sass/
- CSS Preprocessor Benchmarks: https://www.solitr.com/blog/2014/01/css-preprocessor-benchmark/
- Increasing Sass Compiling Performance or "When Every Second Counts”: https://www.devbridge.com/articles/increasing-sass-compiling-performance-or-when-every-second-counts/
