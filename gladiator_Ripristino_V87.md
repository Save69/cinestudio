# CineStudio V87: "Prima la Watchlist" (acceso di partenza)

## Data: 13 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `79b2f8c` (V86, pubblicata).
- Punto di ripristino: tag `pre-v87-watchlist`.

## Richiesta dell'utente
"Prevedere la possibilità che mi venissero proposti prima i film della Watchlist e poi gli altri." Interruttore acceso di partenza.

## Modifiche (`CineStudio.html`)
- Pulsante "Prima la Watchlist: sì/no" accanto al titolo della terna (`cinestudio_watchlist_first`, acceso se assente).
- `getFilteredPool({ ignoreScore: true })`: per i film della Watchlist valgono piattaforme, durata, mood, Filtro Confort,
  già visti e disponibilità, ma non la soglia di voto.
- Terna: prima i film della Watchlist adatti a stasera, a rotazione; finito il giro un lancio va agli altri film,
  poi si ricomincia. Se non ci sono altri film adatti, resta la Watchlist.
- Etichetta "Dalla tua Watchlist" sulle schede; riga sotto la terna: quanti film della Watchlist sono adatti stasera,
  quanti no (piattaforma, durata, mood o tono) e quanti non più inclusi, con link alla Watchlist.

## Verifica (anteprima locale, dati del catalogo)
Watchlist con 3 film adatti: terna 3/3 dalla Watchlist, lancio successivo 0/3, poi di nuovo 3/3.
Con 4 film: 3, 1+2 altri, 0, 3. Soglia di voto 9.5: i film della Watchlist restano proposti. Interruttore spento: 0.
Telefono 375 px: pulsante e riga leggibili.

## Come tornare indietro
```
git checkout pre-v87-watchlist -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
