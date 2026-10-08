# CineStudio V67: "Guarda Ora" mirato ed eliminazione dello script del giovedì

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `a99ffc6` (V66, non ancora pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v67-guarda`.

## Modifiche
### "Guarda Ora" (`getWatchUrl()` in `CineStudio.html`)
Usato da scheda, dettagli, Watchlist e messaggio WhatsApp. Indirizzi provati l'08/10/2026:
- Netflix: `netflix.com/search?q=…` (senza login chiede l'accesso e poi apre la ricerca).
- Prime Video: `primevideo.com/search/…&phrase=…` (risultati corretti anche senza login).
- RaiPlay: `raiplay.it/ricerca.html?q=…` (risultati corretti).
- Disney+: nessun indirizzo di ricerca pubblico (le varianti provate rispondono "pagina non trovata"):
  si apre la pagina TMDB "dove guardarlo" del film se verificato, altrimenti la home di Disney+.
- La7 / Discovery+: home della piattaforma.

### Script del giovedì eliminato
- Rimossi `scripts/weekly_cinestudio_updater.py` e `.github/workflows/weekly_scan.yml`.
  Non verificavano nulla online e, se riattivati, avrebbero reinserito film duplicati con piattaforme errate.
  La verifica della disponibilità la fa l'app con TMDB (V64).
- `CINESTUDIO_RIEPILOGO_NUOVA_CHAT.md` aggiornato (script eliminato, Radar V66, Guarda Ora V67).
- `REGOLE_LAVORO.md` non toccato: il controllo manuale del giovedì resta una regola dell'utente.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Push: in attesa di conferma.

## Come tornare indietro
```
git checkout pre-v67-guarda -- CineStudio.html index.html CINESTUDIO_RIEPILOGO_NUOVA_CHAT.md scripts .github
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
