# CineStudio V86: "Non fa per me" con filoni evitati (rari, non esclusi) e DNA completo

## Data: 13 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `9860bc6` (V85, non ancora pubblicata).
- Punto di ripristino: tag `pre-v86-filoni`.

## Richiesta dell'utente
"Nei film proposti ci sono molti Avengers, genere che non mi piace. Non voglio escluderlo completamente."
Scelta dell'utente: filoni evitati "rari" (non "solo su richiesta").

## Modifiche (`CineStudio.html`)
- Finestra 👎 "Non fa per te": prima "Vedine meno, senza escluderli" con i filoni del film
  (tematici da parole chiave TMDB: supereroi, catastrofici, spionaggio, mostri giganti, videogiochi; la saga; i generi),
  poi l'esclusione del singolo film come prima.
- Filone evitato (`cinestudio_avoided_filoni`): peso × 0.2 nella terna, mai due nella stessa terna, in fondo a
  Sfoglia tutti con etichetta, verdetto "te lo propongo, ma di rado" nella ricerca. Non vale per i film del DNA.
  Elenco con ✕ nella finestra DNA. Incluso nel trasferimento dati.
- Sfoglia tutti: aggiunto il pulsante 👎 su ogni film.
- Dati TMDB: verifica live e scoperta leggono anche parole chiave, generi e saga (una rilettura una tantum).
- DNA: Spielberg, Nolan, Miyazaki, Sergio Leone, Tornatore, Troisi, Benigni, Nanni Moretti, DiCaprio e Matt Damon
  erano mostrati nella finestra DNA ma non usati nel calcolo: ora contano.
- Corretto: dopo il 👎 su un film della terna veniva chiamata `renderRecommendations()`, inesistente:
  la funzione si interrompeva (niente conferma, elenco non aggiornato).

## Verifica (dati simulati)
Avengers: Infinity War → filoni: Supereroi e cinecomic, Saga: The Avengers, Avventura, Azione, Fantascienza.
Evitato "Supereroi": su 250 terne i cinecomic passano da 15 a 3 (mai due insieme); Il cavaliere oscuro resta
normale (DNA Nolan). In Sfoglia i 3 cinecomic sono in fondo. 👎 classico su Aladdin: sostituito, conferma mostrata.

## Come tornare indietro
```
git checkout pre-v86-filoni -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
