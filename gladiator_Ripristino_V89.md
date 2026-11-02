# CineStudio V89: Esclusione automatica Animazione e nuovi Mood Serali

## Data: 2 Novembre 2026
**Agente**: Antigravity
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `fe72233` (dopo V88).
- Punto di ripristino: tag `pre-v89-mood-animazione`.

## Richiesta dell'utente
1. Escludere in automatico i film d'animazione (con possibilità di riattivarli se desiderato).
2. Sostituire i vecchi mood con: Fantascienza, Avventura, Anima e Spiritualità, Motivazionale + Commedia & Leggerezza, Thriller & Mistero (Opzione B) e farli funzionare realmente sia sul catalogo curato sia sui film scoperti da TMDB.

## Modifiche (`CineStudio.html` e `index.html`)
- **Escludi Animazione (`#check-exclude-animation`)**:
  - Interruttore nella barra filtri accanto a *Filtro Confort Serale*, **attivo di default** (`localStorage: cinestudio_exclude_animation`).
  - Integrato in `getFilteredPool()` e spiegato in `whyNotInList()` nella ricerca.
  - Ampliato `isAnimated(movie)` / `ANIMATION_HINTS` (includendo anche `movie.cast` e i registi d'animazione mancanti) così da riconoscere 32/32 film animati del catalogo anche prima della verifica TMDB.
- **Nuovi Mood multi-dimensionali (`MOOD_RULES`, `getMovieMoods`, `movieMatchesMood`, `estimateMood`)**:
  - Menu `#select-mood` e `#add-movie-mood` aggiornati alle 6 categorie scelte (`fantascienza`, `avventura`, `anima`, `motivazionali`, `commedia`, `thriller`) più `top250` e `novita`.
  - Ogni film può appartenere a più mood contemporaneamente (es. *Sopravvissuto - The Martian* risponde a *Fantascienza*, *Avventura* e *Motivazionale*) combinando generi TMDB, parole chiave TMDB (`keywords`), mood e testo della scheda.
  - Aggiornato `onchange` di `#select-mood` e `#select-duration` per rinfrescare subito anche la lista *"Sfoglia tutti"*.

## Come tornare indietro
```powershell
git checkout pre-v89-mood-animazione -- CineStudio.html index.html
```
