# CineStudio V82: nuovi Punti Cardinali, DNA comico (Mel Brooks, Gene Wilder) e soglia DNA

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `2d52ad7` (V81, non ancora pubblicata).
- Punto di ripristino: tag `pre-v82-cardinali-muccino` (su V81).

## Richieste dell'utente
- Punti Cardinali: "Alla ricerca della felicità" (titolo ufficiale: La ricerca della felicità, 2006) e Sette anime (2008),
  poi Che vita da cani! (1991) e Una poltrona per due (1983).
- "Che vita da cani! è bellissimo e Gene Wilder mi piace molto" → "si aggiorna tutto".
  Nota: Che vita da cani! è di e con Mel Brooks (Gene Wilder non c'è); le migliori commedie di Wilder sono di Brooks.

## Dati verificati (JustWatch Italia, 08/10/2026)
- La ricerca della felicità: Muccino, Will Smith, IMDb 8.0 — solo Sky/NOW, canale Amazon a pagamento.
- Sette anime: Muccino, Will Smith, IMDb 7.6 — incluso su Prime Video.
- Che vita da cani!: Mel Brooks, IMDb 5.9 — non disponibile.
- Una poltrona per due: John Landis, Eddie Murphy, Dan Aykroyd, IMDb 7.5 — solo Sky Go, Paramount+.
- Willy Wonka e la fabbrica di cioccolato (1971): incluso su Netflix. La signora in rosso (1984, regia di Wilder): incluso su Prime.
- Frankenstein Junior, Mezzogiorno e mezzo di fuoco, Per favore non toccate le vecchiette!, Wagons-lits con omicidi,
  Nessuno ci può fermare, Non guardarmi non ti sento: solo noleggio/acquisto o non disponibili.

## Modifiche (`CineStudio.html`)
- `PUNTI_CARDINALI`: +4 (ora 21).
- DNA (risonanze): Mel Brooks, Gene Wilder, Gabriele Muccino, Will Smith, John Landis.
- `DNA_SCORE_FLOOR = 6.0`: i film con affinità DNA passano anche sotto la soglia del preset (es. La signora in rosso, 6.0).
- Catalogo: + Willy Wonka (Netflix) e La signora in rosso (Prime) → 124 film.
- Radar: + 6 film di Gene Wilder / Mel Brooks, con tono e mood (promossi da soli quando arrivano sulle piattaforme).
- Ricerca: i Punti Cardinali non in catalogo compaiono come "Punto Cardinale · già visto" con "dove rivederlo" e "Rivedi".
- Documento: lista nera "commedie demenziali" precisata (le commedie di Brooks/Wilder/Landis sono amate).

## Verifica (locale)
La signora in rosso proposta con preset 7.2 (affinità Gene Wilder); Willy Wonka proposto; 6 film nel Radar;
"poltrona per due" → Punto Cardinale; "sette anime" → da rivedere su Prime con link; nessun errore.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`.

## Come tornare indietro
```
git checkout pre-v82-cardinali-muccino -- CineStudio.html index.html CINESTUDIO_RIEPILOGO_NUOVA_CHAT.md
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
