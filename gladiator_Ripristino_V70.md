# CineStudio V70: testi e regole allineati alla verifica live

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `151e3fa` (V69, non ancora pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v70-testi`.

## Modifiche (approvate dall'utente)
- `CineStudio.html`, finestra DNA: il riquadro "Aggiornamento Settimanale Autonomo Attivo / Task Programmato"
  (mai esistito) è sostituito da "Zero Noleggi: verifica automatica ogni 24 ore", che spiega la verifica TMDB.
- `CineStudio.html`, intestazione dello script: il "protocollo del giovedì" per gli agenti è sostituito da regole
  coerenti (disponibilità decisa dalla verifica live, mai piattaforme a memoria, non ricreare script del giovedì).
- `REGOLE_LAVORO.md`: il protocollo settimanale obbligatorio diventa un controllo a campione facoltativo
  (5 film su JustWatch); restano le linee guida Precisione > Velocità e Tolleranza Zero Noleggi.
- `CINESTUDIO_RIEPILOGO_NUOVA_CHAT.md`: prompt di avvio rapido con le 4 piattaforme e la regola sulla verifica live.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`.

## Come tornare indietro
```
git checkout pre-v70-testi -- CineStudio.html index.html REGOLE_LAVORO.md CINESTUDIO_RIEPILOGO_NUOVA_CHAT.md
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
