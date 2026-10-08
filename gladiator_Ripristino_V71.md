# CineStudio V71: 60 film mancanti aggiunti al catalogo (verificati su JustWatch)

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `6ba55cf` (V70, pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v71-catalogo`.

## Verifica "cosa l'app non mi suggerisce" (JustWatch Italia, 08/10/2026)
Controllati 406 film: Top 250 IMDb, filmografie CineScout, Radar e filmografie dei riferimenti del DNA
(Spielberg, Nolan, Miyazaki, Leone, Troisi, Benigni, DiCaprio, Damon, Robin Williams, Chazelle, Eastwood,
cinema francese, Pixar, Italia d'autore).
- 5 film del Radar risultano già inclusi (Il gladiatore, Interstellar, Favolacce, Piccole cose come queste,
  Così parlò Bellavista): li gestisce la promozione automatica V66 (Bellavista escluso: Punto Cardinale).
- 119 film inclusi nei tuoi abbonamenti mancavano dal catalogo (che conteneva solo 62 film scelti a mano).
- L'utente ha approvato tutti i 7 gruppi proposti: 60 film aggiunti.

## Film aggiunti (id `v71-*`)
Francese/europeo: Quasi amici, Le vite degli altri, Grand Budapest Hotel, La famiglia Bélier.
Italia d'autore: I soliti ignoti, Per un pugno di dollari, Perfetti sconosciuti, Le otto montagne, Lazzaro felice,
La chimera, Il traditore, Martin Eden.
Spielberg: I predatori dell'arca perduta, Indiana Jones e l'ultima crociata, Jurassic Park, E.T., The Fabelmans, The Post.
Miyazaki: Princess Mononoke, Totoro, Nausicaä, Il castello nel cielo, Kiki, Si alza il vento, Porco Rosso, Ponyo.
Pixar/animazione: Up, Your Name., Toy Story, Alla ricerca di Nemo, Ratatouille, Monsters & Co., Soul, Gli Incredibili,
Dragon Trainer, Inside Out 2, Luca.
DiCaprio/Damon/Williams: Titanic, Revenant, The Aviator, Il grande Gatsby, Don't Look Up, The Martian, The Bourne Identity,
Ocean's Eleven, Good Morning Vietnam, Mrs. Doubtfire, Aladdin.
Riscatto e storie vere: Rocky, Rush, Dangal, A Beautiful Mind, Apollo 13, First Man, Sully, Million Dollar Baby,
Gran Torino, The Truman Show, La stangata, Ritorno al futuro.

Dati da JustWatch: titolo, anno, durata, IMDb, piattaforma, regia, cast. Tono, mood, "perché" e trama scritti
dall'agente. Toni: 29 uplifting, 19 engaging, 12 demanding.
**MYmovies non disponibile** per questi film: campo `null`, mostrato come "—" (mai inventato).

## Altre modifiche
- `fmtMym()`: formattazione MYmovies sicura in scheda, dettagli, tabella, CineScout, WhatsApp, Calendar.
- Peso delle proposte: senza MYmovies si usa IMDb/2 al suo posto.

## Effetto
Catalogo 62 → 122 film. Preset Alta Qualità, dispositivo nuovo: 71 film con Confort attivo (prima 25), 102 senza.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Push: in attesa di conferma.

## Come tornare indietro
```
git checkout pre-v71-catalogo -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
