# CineStudio V83: dai risultati di "Cerca dove si vede" si può aggiungere un film o segnarlo come visto

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `d952470` (V82, pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v83-aggiungi`.

## Problema
Cercando "il falsario" l'app trovava Il falsario (2025) incluso su Netflix, ma offriva solo "Guarda":
non c'era modo di aggiungerlo alle proposte o alla Watchlist.

## Modifiche (`CineStudio.html`)
- `lookupWhereToWatch()` conserva i dati TMDB di ogni risultato (`window.__lookupFilms`).
- Pulsanti: incluso → "Guarda", "+ Aggiungi", "✓ Già visto"; non incluso → "+ Radar", "✓ Già visto".
- `addLookupToCatalog()`: crea un film "aggiunto da te" (`cinestudio_user_movies`, id `user-tmdb-<id>`) con durata,
  regia, cast, voto TMDB, mood stimato e tono da `classifyContent`; lo mette in Watchlist; lo registra come già
  verificato oggi (la verifica giornaliera lo segue da lì). Nessun doppione se il film è già noto.
- `markLookupSeen()`: registra il film come già visto (codice `tmdb-<id>` + titolo), escluso da tutte le proposte.

## Verifica (TMDB simulato)
Il falsario (2025) → "+ Aggiungi": nelle proposte su Netflix, 110 min, TMDB 6.9, tono Cupo (crimine/dramma), in Watchlist,
verificato. Il falsario – Operazione Bernhard (2007) → "✓ Già visto": nella lista Già visti ed escluso.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Push: in attesa di conferma.

## Come tornare indietro
```
git checkout pre-v83-aggiungi -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
