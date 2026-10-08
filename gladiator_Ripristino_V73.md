# CineStudio V73: un solo voto (TMDB) per tutti i film, MYmovies non è più un filtro

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `ae0fcc0` (V72, pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v73-voto`.

## Motivo
MYmovies era stato introdotto dall'utente come criterio per i film senza voto su Prime. Problemi emersi:
non è aggiornabile in automatico (nessun servizio dati), i voti del catalogo non erano mai stati verificati,
e copriva meno di un quarto dei film (assente per i 60 della V71 e per i ~300 scoperti dalla V72).
Decisione dell'utente: opzione A, voto TMDB unico (l'opzione B, IMDb reale + Metacritic via OMDb, resta possibile in futuro).

## Modifiche (`CineStudio.html`)
- `tmdbCheck()` salva anche `voteAverage`/`voteCount`; i film verificati prima della V73 vengono ricontrollati
  automaticamente una volta per leggere il voto.
- `getAllMovies()`: per ogni film verificato, voto = TMDB (etichetta "TMDB") se basato su almeno 50 voti;
  altrimenti resta il voto IMDb del catalogo (etichetta "IMDb").
- `getFilteredPool()`: guardrail solo "voto ≥ soglia" (prima: IMDb ≥ soglia OPPURE MYmovies ≥ soglia).
- Peso delle estrazioni: `voto × 10` (stessa scala di prima, bonus DNA invariato).
- Interfaccia: selettore "Voto ≥" (ex "IMDb ≥"); selettore MYmovies nascosto nella barra e nelle impostazioni;
  badge MYmovies sulle schede solo dove il voto esiste (informativo); preset con descrizioni aggiornate;
  sottotitolo in testata aggiornato.

## Attenzione
La scala TMDB è simile a IMDb ma spesso qualche decimo più bassa, soprattutto per i film italiani con pochi voti
internazionali (es. una commedia classica può scendere sotto 7.2). Se il preset "Alta Qualità" risulta troppo
stretto, usare "Scelta Ampia" (6.8) o ricalibrare le soglie dopo aver visto la distribuzione reale.

## Verifica (TMDB simulato)
Cache vecchia senza voti → ricontrollo automatico; Coco TMDB 8.2 con MYmovies 4.0 informativo; Quasi amici TMDB 7.5
senza badge MYmovies; Hustle con 20 voti TMDB → resta IMDb del catalogo; selettore MYmovies nascosto; nessun errore.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Push: in attesa di conferma.

## Come tornare indietro
```
git checkout pre-v73-voto -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
