# CineStudio V66: i film del Radar arrivati in streaming entrano nelle proposte

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `a29e512` (V65, non ancora pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v66-radar`.

## Problema segnalato dall'utente
Nel Radar comparivano film con il badge "Ora incluso su Prime Video" (Il gladiatore, Così parlò Bellavista)
che però restavano solo nel Radar, accanto alla vecchia etichetta "a noleggio Store": la verifica live li
segnalava ma non li portava nelle proposte.

## Modifiche (`CineStudio.html`)
- `defaultRadar`: tutte le 49 voci ora hanno durata, mood, tono emotivo e trama
  (27 recuperate dal catalogo pre-V63, 22 scritte a mano: vedi tabella sotto).
- Le voci Radar già salvate sul dispositivo ricevono i campi mancanti senza perdere i dati dell'utente.
- TMDB: salvati anche durata (`runtime`) e trama (`overview`).
- `getPromotedRadarMovies()`: un film del Radar incluso in un abbonamento entra in `getAllMovies()`
  (proposte, tabella, Top 250 "Disponibili Ora"), con piattaforma, durata e locandina reali.
  Esce di nuovo se la verifica lo trova non più incluso.
- `PUNTI_CARDINALI` + `isPuntoCardinale()`: i film già visti e amati non vengono mai promossi dal Radar.
- Radar diviso in "Arrivati in streaming incluso" e "In attesa"; per gli arrivati sparisce l'etichetta
  di stato vecchia. Il contatore del Radar conta solo i film in attesa.
- `demoteMovieToRadar()` funziona anche sui film arrivati dal Radar.

## Toni assegnati alle 22 voci storiche del Radar
- demanding: Senna, Diego Maradona, Navalny, Robin Williams, Oppenheimer, Piccole cose come queste, Parasite,
  Favolacce, Past Lives, Anatomia di una caduta, Worth, Il miglio verde.
- engaging: I guerrieri, Interstellar, Le ali della libertà, Whiplash, Il gladiatore.
- uplifting: C'eravamo tanto amati, Così parlò Bellavista, Forrest Gump, Amélie, La leggenda del pianista sull'oceano.

## Verifica
Test con dati simulati e Radar "vecchio" salvato: Il gladiatore entra nelle proposte su Prime (2h35m, Teso &
Avvincente, Verificato), Bellavista no (Punto Cardinale), Radar "Arrivati (2)" / "In attesa (47)",
scheda e dettagli funzionanti, nessun errore in console.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Push: in attesa di conferma.

## Come tornare indietro
```
git checkout pre-v66-radar -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.

## Aggiunta successiva: campo "Cerca nel Radar o aggiungi"
- Il campo del Radar ora filtra la lista mentre si scrive e dice se il titolo è già nel Radar o nel catalogo.
- Titoli del Radar in ordine alfabetico in entrambe le sezioni.
- "Monitora" non crea doppioni né aggiunge film già in catalogo.
- I titoli aggiunti a mano non salvano più l'anno "Cercato": la verifica TMDB (subito, se collegata) trova il film,
  completa anno e titolo ufficiale e ne controlla la disponibilità. Prima non venivano mai verificati.
- Verifica JustWatch 08/10/2026: *Storie pazzesche* (2014) è solo a noleggio/acquisto (Amazon Video, TIMvision, CHILI, Rakuten).
