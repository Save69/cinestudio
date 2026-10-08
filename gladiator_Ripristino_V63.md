# CineStudio V63: verifica reale del catalogo su JustWatch

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `76f5ec6` (V62), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v63-justwatch`.

## Metodo
Tutti gli 89 film del catalogo sono stati interrogati sui dati JustWatch Italia (stessa fonte del sito, offerte web IT),
distinguendo streaming incluso (FLATRATE / FREE / ADS) da noleggio/acquisto.
Piattaforme considerate valide: Netflix, Prime Video (non i canali Amazon a pagamento), Disney+, RaiPlay.
Nota: JustWatch **non traccia La7**, quindi i film "La7" non sono verificabili e sono stati trattati di conseguenza.

## Esito (catalogo da 89 a 62 film)
### 27 film spostati nel Radar (non inclusi nei tuoi abbonamenti)
Il Postino, Non ci resta che piangere, La migliore offerta, Ennio, Il ponte delle spie, L'attimo fuggente,
Le conseguenze dell'amore, Il sol dell'avvenire, Il caso Spotlight, Il giovane favoloso, Il ritorno di Casanova,
Youth, L'uomo in più, Bianca, Habemus Papam, Una pura formalità, Cyrano, Shutter Island,
Mio fratello è figlio unico, La nostra vita, Una giornata particolare, La famiglia, Brutti sporchi e cattivi,
Che ora è?, Tutti gli uomini del presidente, La cena, Il conformista.
Ogni voce Radar riporta dove si trova davvero (es. "solo Sky/NOW", "solo canale Amazon CineAutore").

### 11 film con piattaforma corretta
La vita è bella → Netflix · Ricomincio da tre → Disney+ · La stanza del figlio → Disney+ · Caro diario → Disney+ ·
Io capitano → Netflix · Mediterraneo → Netflix · La stranezza → Prime · Palombella rossa → Disney+ ·
Suburra → RaiPlay · Nessuno mi può giudicare → Netflix · Good Night, and Good Luck → Prime.

### 51 film confermati sulla piattaforma indicata.

## Altre modifiche
- **CineScout**: la disponibilità ora deriva dal catalogo verificato; un film segnato "flat" nella filmografia ma assente
  dal catalogo viene mostrato come non incluso (prima restava "Incluso" con la vecchia piattaforma).
- **GitHub Actions** `weekly_scan.yml`: disattivato l'avvio automatico del giovedì (resta manuale). Prova su copia:
  lo script avrebbe aggiunto 3 duplicati, tra cui *Io capitano* di nuovo su RaiPlay. Lo script non verifica nulla online.
- Il "task-1897" citato in CINESTUDIO_RIEPILOGO_NUOVA_CHAT.md non esiste (nessuna attività pianificata trovata).

## Limiti
- È una fotografia al 08/10/2026: i cataloghi cambiano ogni mese. La soluzione stabile è la verifica live via API TMDB.
- Le piattaforme La7 e Discovery+ ora hanno 0 film in catalogo.
- Eventuali correzioni piattaforma salvate a mano sul dispositivo (`cinestudio_platform_overrides`) hanno la precedenza.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. **Nessun push.**

## Come tornare indietro
```
git checkout pre-v63-justwatch -- CineStudio.html index.html .github/workflows/weekly_scan.yml
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
