# CineStudio V76: una sola ricerca (barra in alto) che trova, spiega e dice dove si vede

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `3d93f38` (V75, pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v76-ricerca-unica`.

## Problema ("non ci siamo")
L'utente ha cercato "Mr ove" nella barra in alto (naturale): risultato "Nessun film trovato" e un vecchio blocco
"Esploratore" poco utile. Cause: la V75 aveva aggiunto una SECONDA ricerca dentro "Sfoglia tutti i film" (confusione);
la barra in alto confrontava il testo esatto ("mr ove" ≠ "mr. ove") e senza risultati non dava informazioni.

## Modifiche (`CineStudio.html`)
- Barra in alto: confronto senza punteggiatura né accenti (`movieMatchesQuery` + `normalizeForMatch`) su titolo,
  titolo originale, regista, cast e piattaforma.
- Barra in alto senza risultati: nel riquadro "Le Tue 3 Opzioni" compare la spiegazione della V75
  (film escluso e perché / nel Radar e stato / sconosciuto → "Cerca dove si vede" su TMDB → "Guarda" o "+ Radar").
- Rimossa la ricerca doppia dentro "Sfoglia tutti i film"; lì, senza risultati, un rimando al riquadro sopra.

## Verifica (locale, TMDB simulato)
"Mr ove" sconosciuto → spiegazione + "Cerca dove si vede" → "✓ Incluso su Prime Video"; "Mr ove" scoperto →
scheda Prime Video con TMDB 7.6; "hannes holm" → Mr. Ove; "il postino" → Radar con stato.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Push: in attesa di conferma.

## Come tornare indietro
```
git checkout pre-v76-ricerca-unica -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
