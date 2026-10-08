# CineStudio V74: i "già visti" non si perdono più + trasferimento dati tra copie dell'app

## Data: 08 Ottobre 2026
**Agente**: Claude Code (Opus 5.5)
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

## Stato Git
- Iniziale: `main` a `9baa1ca` (V73, pubblicata), nessuna modifica ai file tracciati.
- Punto di ripristino: tag `pre-v74-visti`.

## Problema segnalato: "si sono persi i film già visti"
Due cause:
1. **Difetto introdotto in V63** (dall'agente): la lista "Già visti" mostrava solo i film presenti nel catalogo;
   i 27 film spostati nel Radar (e quelli usciti dal catalogo) sparivano dalla vista. I dati NON erano cancellati
   (`cinestudio_seen` intatto). Inoltre un film visto poteva essere riproposto se tornava con un altro codice
   (promosso dal Radar in V66, scoperto da TMDB in V72) o se segnato come visto solo nella sfida Top 250.
2. **Memorie separate**: copia sul Desktop (`file:///`), versione online (`save69.github.io`) e telefono hanno
   ciascuno i propri dati. Visti/Watchlist/Radar salvati in una copia non compaiono nelle altre.

## Modifiche (`CineStudio.html`)
- `cinestudio_seen_titles`: ogni "già visto" ricorda titolo, titolo originale, anno, regista (`rememberSeen`);
  i visti precedenti vengono completati all'avvio (`backfillSeenTitles`, cerca in catalogo, Radar, film scoperti,
  codici storici).
- `getFilteredPool()`: esclude i film visti anche **per titolo** (`getSeenTitleSet`), compresi quelli segnati
  nella sfida Top 250.
- Lista "Già visti" e contatore basati su `getSeenEntries()`: mostrano tutti i film segnati, ordinati per titolo.
- Finestra DNA → **"Trasferisci i tuoi dati"**: "Copia i miei dati" (testo negli appunti) e "Incolla dati"
  (unione: visti, Watchlist, Top 250, DNA, Radar personale, bocciati, film aggiunti, correzioni piattaforma).
  Nulla viene cancellato; la chiave TMDB non viene copiata.

## Verifica (locale, dati simulati)
Dispositivo "vecchio" con visti in catalogo, spostati nel Radar, codice storico e Top 250: lista completa
(Hustle, L'attimo fuggente, La migliore offerta, Parasite + un codice sconosciuto); La migliore offerta promossa
dal Radar NON riproposta; Il padrino (visto in Top 250, scoperto da TMDB) NON riproposto; film nuovo proposto.
Trasferimento: dati di due copie uniti correttamente, chiave TMDB assente dal testo esportato.

## Come recuperare i visti salvati nella copia del Desktop
Desktop (`file:///C:/Users/Utente/Desktop/CineStudio.html`) → DNA → "Copia i miei dati" →
versione online → DNA → "Incolla dati". Stesso procedimento per il telefono.

## File sincronizzati
`CineStudio.html`, `index.html`, `Desktop\CineStudio.html`, `Desktop\CineStudio_Web\index.html`. Push: in attesa di conferma.

## Come tornare indietro
```
git checkout pre-v74-visti -- CineStudio.html index.html
```
poi ricopiare `CineStudio.html` nelle due copie sul Desktop. I dati salvati nei browser non vengono toccati.
