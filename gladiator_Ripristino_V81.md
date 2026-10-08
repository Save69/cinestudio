# CineStudio V81: crudezza stimata da parole chiave e divieti (The Others sì, splatter no, Tarantino "Cupo")

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `9d83695` (V80, non ancora pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v81-crudezza`.

## Decisioni dell'utente
- "Considero The Others e Il sesto senso alla stessa stregua: suspense, non horror" → The Others non va escluso.
- "Tarantino mi piace molto" → aggiunto al DNA.
- Il divieto "Horror & Splatter" riguarda sangue, splatter, mostri; non la suspense d'atmosfera.

## Analisi (dati reali TMDB, 08/10/2026)
I generi TMDB non misurano la crudezza: The Others è "Horror, Mistero, Thriller", Il sesto senso "Mistero, Thriller,
Dramma"; nessun film di Tarantino è "Horror" ma Kill Bill, Django, The Hateful Eight sono molto violenti, e
"C'era una volta a Hollywood" risultava "Caldo & Confortante" per l'etichetta Commedia.

## Modifiche (`CineStudio.html`)
- `classifyContent()` su generi + parole chiave TMDB + divieto (IT VM18 / US NC-17) + voto:
  - horror d'atmosfera (Mistero/Thriller/Dramma, voto ≥ 7.3, niente gore, niente demoni, niente VM18) → ammesso, "Teso"
    con nota "Suspense soprannaturale, senza splatter";
  - horror con gore/splatter/slasher/zombie/tortura, demoni/possessioni/esorcismi, o VM18 → escluso sempre;
  - non horror con violenza esplicita (o VM18) → "Cupo", nota "Violenza esplicita";
  - non horror con temi molto duri (schiavitù, KKK, genocidio, Olocausto, stupro) → "Cupo", nota "Temi molto duri".
- `estimateTone()`: commedia con crimine o thriller → "Teso" (prima solo con entrambi).
- Scoperta automatica: horror non più escluso dalla ricerca TMDB (valutato film per film); i dettagli includono
  parole chiave e divieti (i film letti prima della V81 vengono riletti; senza parole chiave l'horror resta fuori).
- "Cerca dove si vede": stessa classificazione (avviso rosso solo per l'escluso, nota per violenza/suspense).
- DNA: risonanza "Quentin Tarantino".
- Corretto un difetto di scrittura dei file su Windows: `\b` passato da riga di comando diventava un carattere invisibile
  (regole inattive); ora gli script vengono scritti come file.

## Verifica (dati reali TMDB, logica dell'app)
The Others e Il sesto senso → Teso (proposti anche col Filtro Confort); Kill Bill, Le iene, Pulp Fiction, Il padrino →
Cupo/violenza; Django → Cupo/temi duri; C'era una volta a Hollywood → Teso; Saw, L'alba dei morti viventi, The Conjuring,
Hereditary → esclusi. Scoperta simulata: The Others e Il sesto senso proposti, Kill Bill con affinità DNA Tarantino,
Hereditary scartato.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Push: in attesa di conferma.

## Come tornare indietro
```
git checkout pre-v81-crudezza -- CineStudio.html index.html CINESTUDIO_RIEPILOGO_NUOVA_CHAT.md
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
