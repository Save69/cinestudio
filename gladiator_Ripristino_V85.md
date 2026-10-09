# CineStudio V85: dal Radar si può guardare o mettere in Watchlist un film arrivato

## Data: 09 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `58b62e4` (V84 pubblicata; ripristinate le copie sul Desktop, che l'utente usa davvero).
- Punto di ripristino: tag `pre-v85-radar`.

## Richiesta dell'utente
"Così parlò Bellavista: l'ho già visto ma stasera mi andrebbe di rivederlo, voglio selezionarlo dal Radar.
Favolacce: è su RaiPlay o no? Perché è nel Radar?"

## Modifiche (`renderRadarItems`)
- Film arrivati: etichetta "Incluso su X · verificato il gg/mm".
- Riga di stato: Punto Cardinale → "già visto e amato, puoi rivederlo quando vuoi"; altrimenti
  "✓ È tra i film che ti propongo" oppure "Non te lo propongo stasera: <motivo>" (es. Filtro Confort).
  Prima diceva sempre "già nelle tue proposte", anche quando il film era escluso dai filtri.
- La nota storica è introdotta da "Era nel Radar perché:".
- Pulsanti: Guarda / Rivedi, + Watchlist / ★ In Watchlist, Scheda. `radarToWatchlist()` usa il film già noto
  oppure, per i Punti Cardinali, lo crea da TMDB (`addLookupToCatalog`).

## Verifica (TMDB simulato)
Così parlò Bellavista → Rivedi su Prime, + Watchlist (creato come film aggiunto, in Watchlist).
Favolacce → "Non te lo propongo stasera: è su RaiPlay, ma il Filtro Confort lo esclude"; + Watchlist ok.

## Come tornare indietro
```
git checkout pre-v85-radar -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
