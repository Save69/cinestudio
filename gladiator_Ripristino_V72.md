# CineStudio V72: scoperta automatica dei film sulle piattaforme (TMDB discover)

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `372b9d5` (V71, non ancora pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v72-scoperta`.

## Problema
L'utente ha notato *Mr. Ove* su Prime Video (visto e amato) e ha chiesto perché l'app non lo proponesse.
Causa: l'app proponeva solo i film di un elenco fisso scritto nel codice (122 dopo la V71) e non esplorava mai
i cataloghi delle piattaforme. Decisione dell'utente: scoperta automatica ("procedi con la 2, con calma").

## Come funziona (`CineStudio.html`, modulo "SCOPERTA AUTOMATICA")
1. Con la chiave TMDB, dopo la verifica giornaliera del catalogo, `runDiscovery()` interroga
   `/discover/movie` (regione IT, piattaforme Netflix/Prime Video/Disney+/RaiPlay e varianti con pubblicità,
   solo streaming incluso/gratuito, horror e film TV esclusi) con 3 ricerche:
   - qualità: TMDB ≥ 7.3, ≥ 3000 voti (8 pagine);
   - cinema europeo per lingua originale (it, fr, es, de, sv, da, no, mk...): TMDB ≥ 6.8, ≥ 80 voti (8 pagine);
   - novità dal 2022: TMDB ≥ 7.0, ≥ 300 voti (3 pagine).
2. Esclude ciò che l'app conosce già (catalogo, film aggiunti, Radar, Punti Cardinali, bocciati), max 320 film.
3. Per i film nuovi legge durata, regia, cast, piattaforma, locandina e trama (riletti ogni 7 giorni).
4. La ricerca si ripete ogni 24 ore: un film non più incluso sparisce da solo.
- Tono stimato dai generi in modo prudente (`estimateTone`): guerra e crimine drammatico → Cupo; animazione,
  famiglia e commedia → Caldo; thriller, avventura, fantascienza → Teso; tutto il resto → Cupo.
- Mood stimato (`estimateMood`). Voto mostrato come **TMDB** (`scoreLabel`), non IMDb. MYmovies "—".
- Badge "✨ Scoperto per te"; peso ridotto del 30% nelle estrazioni se non c'è affinità con il DNA.
- Riga di stato: "✨ N scoperti per te (disattiva)" / "attiva la scoperta automatica" (`cinestudio_discovery_off`).
- Corretto anche il promemoria Calendar: "Guarda ora" usava ancora il link alla home.

## Verifica (TMDB simulato, nessuna chiave reale disponibile all'agente)
- Mr. Ove (sv, Commedia/Dramma, Prime): scoperto, tono Caldo, entra nelle proposte.
- Petrunya (mk, TMDB 6.9): scoperto ma fuori con il preset Alta Qualità (≥ 7.2); entra con "Scelta Ampia".
- 1917 (guerra): scoperto, tono Cupo, escluso dal Filtro Confort. Coco (già in catalogo): non duplicato.
- Film solo su canale Amazon a pagamento: scartato. Parametri inviati a TMDB controllati.
- Interruttore on/off, nessuna nuova ricerca entro 24 ore, film sparito dalla ricerca → sparito dall'app.
- **Da fare**: primo test reale con la chiave dell'utente (la prima ricerca fa circa 340 chiamate TMDB).

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Push: in attesa di conferma.

## Come tornare indietro
```
git checkout pre-v72-scoperta -- CineStudio.html index.html CINESTUDIO_RIEPILOGO_NUOVA_CHAT.md
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop. In alternativa basta "disattiva" nella riga di stato.
