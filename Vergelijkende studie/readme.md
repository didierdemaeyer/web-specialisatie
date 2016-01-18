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
- ...

### LESS

- Combineerbaar met CSS
- Variabelen
- Mixins
- Geneste CSS regels
- ...

## 3. Vergelijking

### 3.1 De leercurve (Ruby, Command Line, ...)

De enige leercurve is eigenlijk de nieuwe syntax die je moet leren, omdat je een applicatie zoals CodeKit, LiveReload oof Mixture kan gebruiken om je bestanden in het oog te houden en te converteren wanneer er iets veranderd. Dit betekent dat je eigenlijk niets van Ruby, de Command Line of eender wat anders moet kennen. Het kan natuurlijk alleen maar handig zijn als je deze zaken wel kent.

**Conclusie: Beiden zijn eenvoudig om mee te starten.**

### 3.2 Mogelijkheid om css te prefixen

Je kan met beide talen mixins schrijven die helpen met vendor prefixes. Maar als je in gewone css al geen moeite deed om prefixes up te daten dan zal je dit waarschijnlijk ook niet doen in je mixins. Waardoor je waarschijnlijk een library zal gebruiken die prefixes voor jou update. En deze bestaan zowel voor Sass als LESS.

**Conclusie: Beiden hebben genoeg libraries die al heel wat voor je kunnen doen.**

### 3.3 Caching

Templates en partials die gecompiled zijn naar CSS worden gecached, waardoor ze de volgende keer wanneer je iets aanpast in je SCSS of LESS file waardoor er opnieuw gecompiled moet worden. De compiler zal dan eerst kijken of er templates of partials zijn waar niets aan veranderd is, als deze er zijn zal hun gecompilede versie uit de cache gehaald worden waardoor het compilen veel sneller zal gaan. Het is dus aangeraden om je code op te splitsen in verschillende bestanden zodat caching het beste werkt. Zowel Sass als LESS gebruiken caching.

**Conclusie: Beiden gebruiken caching.**

### 3.4 Variabelen

Variabelen kunnen gebruikt worden in Sass en LESS, ik denk dat dit de feature is waarvoor de meeste mensen kiezen om een preprocessor te gebruiken. Je kan dit gebruiken om kleurcodes op te slaan, een bepaald aantal pixels,...

In beide talen zijn de variabelen enkel te gebruiken binnen hun scope. Het verschil tussen beide is dat Sass gebruikt maakt van een dollar teken (`$`) voor hun variabelen en LESS gebruikt maakt van een ampersant (`@`). Aangezien in beide talen variabelen hetzelfde kunnen, komt het neer op wat jij het beste vindt. `$` of `@`.

Voorbeeld van scope:

```CSS
$color: #000;

header {
  color: $color;
}

.content {
  $color: #555;
  color: $color;
}

footer {
  color: $color;
}
```

Dit wordt gecompiled naar:

```CSS
header { color: #000 }
.content { color: #555 }
footer { color: #000 }
```

**Conclusie: Beiden zijn goed, het hangt af van wat jij het eenvoudigst vindt. `$` of `@`**

### Mogelijkheden: Logica / Loops

### Geneste css regels

### Mixins

### Mixins met argumenten (Dynamische mixins)

### Overerving van selectors

### Aanpassen van kleuren

### Wiskundige berekeningen

### Voorwaardelijke en controle structuren

### Imports

### Output opmaak

### Comments

### Namespaces





## Logboek

- 13/12/2015 - Resources gezocht
- 15/12/2015 - Inleiding geschreven, begonnen met vergelijken

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
