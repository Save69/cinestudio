# CineStudio V80: "Cerca dove si vede" mostra regia, attori, locandina e avviso horror

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `7a4495c` (V79, non ancora pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v80-dettagli-ricerca`.

## Problema
Cercando "the others" comparivano tre film con lo stesso titolo (2001, 1970, 1997) e l'utente non poteva
capire quale fosse quello con Nicole Kidman.

## Modifiche (`CineStudio.html`, `lookupWhereToWatch`)
- Per ogni risultato una sola chiamata `/movie/{id}?append_to_response=credits,watch/providers`
  (prima solo `/watch/providers`): stesso numero di richieste.
- Ogni riga mostra locandina piccola, "Regia di … · con …" (2 attori) e la disponibilità.
- Avviso "⚠️ Horror: nella tua lista nera" se il genere TMDB è horror.

## Verifica (TMDB simulato)
The Others (2001) → Horror, Amenábar, Nicole Kidman, solo noleggio/acquisto, locandina; 1970 con regista;
1997 senza dati. 4 chiamate TMDB come prima.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Push: in attesa di conferma.

## Come tornare indietro
```
git checkout pre-v80-dettagli-ricerca -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
