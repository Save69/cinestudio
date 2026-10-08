# CineStudio V68: Punti Cardinali esclusi dalle proposte, con "dove rivederli"

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `105d005` (V67, non ancora pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v68-cardinali`.

## Decisione dell'utente
"Per ora escludili": i Punti Cardinali (film già visti e amati) non devono essere proposti per la serata,
ma l'utente vuole poter sapere dove rivederli.

## Modifiche (`CineStudio.html`)
- `getFilteredPool()`: esclusi i Punti Cardinali (Nuovo Cinema Paradiso, Mediterraneo, Inside Out, Vita di Pi
  erano nel catalogo e venivano proposti). La ricerca per nome li trova comunque.
- `PUNTI_CARDINALI` ora con anno e id: la verifica TMDB giornaliera controlla anche i 17 Punti Cardinali.
- Finestra DNA → "I Tuoi Punti Cardinali": generata dinamicamente; ogni film mostra "▶ Netflix" (link alla
  piattaforma), "non incluso ora" o "non ancora verificato".
- Watchlist predefinita: tolti Nuovo Cinema Paradiso e L'attimo fuggente (rimozione una sola volta, poi l'utente
  può rimetterli). Corretto il difetto per cui i film predefiniti tornavano in Watchlist a ogni apertura anche
  se l'utente li aveva tolti (`cinestudio_watchlist_defaults_given`).

## Verifica
Locale con dati simulati: 0 Punti Cardinali nelle proposte, ricerca "Mediterraneo" ok, 17 badge nella finestra DNA
(La La Land ▶ Netflix con link alla ricerca Netflix), WALL-E tolto dalla Watchlist non ricompare dopo il riavvio.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`.

## Come tornare indietro
```
git checkout pre-v68-cardinali -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
