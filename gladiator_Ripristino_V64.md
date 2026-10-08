# CineStudio V64: verifica live della disponibilità con TMDB

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `c879475` (V63), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v64-tmdb`.

## Cosa fa
- Con una chiave TMDB (API v3 o Read Access Token) l'app interroga TMDB per ogni film del catalogo, i film
  aggiunti a mano e le voci del Radar. Fonte: dati JustWatch Italia, offerte flatrate/free/ads.
- Ricontrollo automatico ogni 24 ore all'apertura; esiti più vecchi di 7 giorni non vengono usati.
- Film non incluso in nessuno dei 6 abbonamenti → escluso da terna, tabella e Top 250 "Disponibili Ora".
- Film su una piattaforma diversa → mostrato sulla piattaforma reale (preferendo quelle attive nei filtri).
- Voci del Radar diventate incluse → in cima con badge verde "Ora incluso su …".
- Locandine reali da TMDB (sostituiscono gli URL inventati).
- Schede: badge "Verificato gg/mm" (link alla pagina disponibilità) o "Non verificato" (link JustWatch).
- Riga di stato sotto "Le Tue 3 Opzioni per Stasera": collega chiave, avanzamento, elenco non più inclusi, aggiorna.
- Senza chiave l'app funziona come prima (dati statici) e lo dichiara.

## Modifiche
- `CineStudio.html`: modulo TMDB prima di `getAllMovies()`; `getAllMovies()` applica l'esito live;
  `getFilteredPool()` esclude `liveUnavailable`; `findCatalogMatchForTop250()` idem; badge schede; Radar; init.
- `CINESTUDIO_RIEPILOGO_NUOVA_CHAT.md`: rimossa la descrizione dell'audit del giovedì inesistente, documentata la verifica live.

## Verifica
- Test con risposte TMDB simulate (nessuna chiave reale disponibile all'agente): esclusione dei non inclusi,
  cambio piattaforma, preferenza per piattaforme attive, Radar "Ora incluso", cache 24h (0 chiamate al secondo avvio),
  chiave errata (errore mostrato, ultimi esiti mantenuti). Nessun errore in console.
- Raggiungibilità reale di api.themoviedb.org dal browser confermata (risponde 401 senza chiave).
- **Da fare**: primo test con la chiave reale dell'utente.

## Limiti noti
- La7 non è tracciata da JustWatch/TMDB.
- "Guarda Ora" apre ancora la home della piattaforma (TMDB non fornisce link diretti al film).

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Pubblicato su GitHub Pages il 08/10/2026 (push 5eb57c6..c32aa57, dopo sostituzione del token GitHub).

## Come tornare indietro
```
git checkout pre-v64-tmdb -- CineStudio.html index.html CINESTUDIO_RIEPILOGO_NUOVA_CHAT.md
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.

## Correzione successiva (stessa sessione)
- Primo uso reale con chiave dell'utente: "Verificati live 64/64", 2 non più inclusi.
- Bug: a verifica finita la terna già mostrata restava con i dati vecchi ("Non verificato" sulle schede).
  `generateRecommendations()` ora, quando conserva la terna, la ricostruisce dal pool aggiornato.
