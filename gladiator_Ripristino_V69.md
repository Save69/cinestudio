# CineStudio V69: pulsanti Discovery+ e La7 nascosti

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `38c2011` (V68, pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v69-piattaforme`.

## Motivo (dati JustWatch Italia, 08/10/2026)
- Discovery+: 538 titoli, **0 film** (solo programmi e serie: Matrimonio a prima vista, Bake Off Italia...).
- La7: non tracciata da JustWatch né da TMDB, quindi non verificabile; film quasi solo in replica temporanea.
- Per confronto: Prime Video ~7.800 film, Netflix ~5.500, Disney+ ~2.100, RaiPlay ~1.800.
Decisione dell'utente: nascondere i due pulsanti.

## Modifiche
- Rimossi i pulsanti `btn-plat-discovery` e `btn-plat-la7` dalla barra "Piattaforme della serata".
- `activePlatforms` invariato: se la verifica live trovasse un film incluso su Discovery+, verrebbe proposto comunque.
- Le voci Discovery+/La7 nei menu "Aggiungi film" e "Cambia piattaforma" restano disponibili.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`.

## Come tornare indietro
```
git checkout pre-v69-piattaforme -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop.
