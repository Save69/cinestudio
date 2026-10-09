# CineStudio V84: la barra di ricerca fa agire (pulsanti, saghe, filmografie)

## Data: 09 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `668db46` (V83, pubblicata il 09/10/2026).
- Punto di ripristino: tag `pre-v84-ricerca`.

## Richiesta dell'utente
1. Cercando un film (es. Che vita da cani!) sapere se è disponibile, metterlo in Watchlist o, se non disponibile, nel Radar.
2. Cercando "star wars" poter vedere l'intera saga e metterla nel Radar.
3. Cercando "gene wilder" vedere la filmografia ed eventualmente metterla nel Radar.
Decisione: un film messo in Watchlist ci resta anche se sotto la soglia di voto. Serie TV escluse.

## Modifiche (`CineStudio.html`)
- Righe dei film conosciuti: Scheda, Guarda, + Watchlist / ★ In Watchlist, + Radar (se non più incluso), ✓ Già visto.
- Punti Cardinali: Rivedi + Watchlist se inclusi, altrimenti + Radar. Nel Radar mantengono l'etichetta Punto Cardinale.
- Sezione automatica "Anche su TMDB" (dopo una pausa di scrittura, con cache per ricerca):
  `/search/movie`, `/search/collection`, `/search/person`. Saghe e persone aprono un elenco completo
  (`openSearchView`), con disponibilità di ogni film (4 richieste alla volta) e pulsanti.
- Filmografia (`buildFilmography`): attore/attrice e regia, esclusi documentari (99), film TV (10770),
  "Himself/Herself", film con meno di 3 voti; oltre 40 film tiene i più votati.
- "+ Radar per i N non disponibili": esclude visti, già nel Radar, inclusi e lista nera (horror/splatter); chiede conferma.
- Film aggiunti al Radar dalla ricerca: collegati subito al codice TMDB (`tmdbCache`), con voto, tono e trama.
- Corretto: i pulsanti non passano più titoli nel codice (i titoli con apostrofo rompevano "+ Radar" della V83).
- Placeholder: "Cerca film, saga, attore, regista...". Su telefono i pulsanti vanno a capo sotto il titolo.

## Verifica (TMDB simulato, anteprima locale, desktop e 375 px)
Che vita da cani! → + Radar (collegato a TMDB, etichetta Punto Cardinale). Star Wars → saga di 5 film ordinata
per uscita; + Watchlist, ✓ Già visto e Radar per l'unico non disponibile funzionanti. Gene Wilder → filmografia
di 5 film (esclusi documentario, film TV e "Himself"), Billy Wilder escluso perché il nome non corrisponde.
Senza chiave TMDB: invito a collegarla; chiave non valida: messaggio d'errore, risultati locali intatti.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Push: in attesa di conferma.

## Come tornare indietro
```
git checkout pre-v84-ricerca -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
