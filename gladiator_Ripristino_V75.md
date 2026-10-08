# CineStudio V75: ricerca dentro "Sfoglia tutti i film" (c'è? dove si vede? perché no?)

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `0d6d7a1` (V74, non ancora pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v75-cerca`.

## Richiesta dell'utente
"A volte leggo un titolo, non ricordo dove è disponibile e perdo molto tempo a ritrovarlo": cercare un film
nella sezione "Sfoglia tutti i film disponibili" per capire se è nella lista.
(Il trasferimento dati della V74 è stato giudicato troppo complicato: resta nella finestra DNA, non serve usarlo.)

## Modifiche (`CineStudio.html`)
- Campo di ricerca dentro la sezione "Sfoglia tutti i film": filtra mentre si scrive per titolo, titolo originale,
  regista o attore e indica quanti film corrispondono.
- Se il film non è nella lista, `renderListSearchMiss()` spiega cosa sa:
  - film conosciuto → piattaforma e motivo (`whyNotInList`, stesse regole e stesso ordine di `getFilteredPool`):
    non più incluso, Punto Cardinale, piattaforma spenta, già visto, bocciato, Filtro Confort, voto sotto soglia,
    durata/mood; pulsanti "Scheda" e "Guarda su …";
  - film nel Radar → stato attuale (o "ora incluso su …");
  - film sconosciuto → "Cerca dove si vede" (TMDB: primi 3 risultati con "Incluso su …", "Non nei tuoi abbonamenti:
    su …", "Solo noleggio o acquisto", "Non disponibile") con "Guarda" o "+ Radar"; sempre il link a JustWatch.
- Lista: badge MYmovies mostrato solo dove il voto esiste.

## Verifica (locale)
Totoro → trovato; "spielberg" → 6 film; Le vite degli altri → "su RaiPlay, ma il Filtro Confort lo esclude";
Il Postino → Radar con stato; Nuovo Cinema Paradiso → "Punto Cardinale"; Mr. Ove (TMDB simulato) →
"Incluso su Prime Video" con link alla ricerca Prime; film a noleggio → "+ Radar" funzionante. Nessun errore nuovo.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Push: in attesa di conferma.

## Come tornare indietro
```
git checkout pre-v75-cerca -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
