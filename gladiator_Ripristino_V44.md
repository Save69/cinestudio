# GLADIATOR - Ripristino V44

## Sessione

- Data: 30 settembre 2026
- Agente: Antigravity
- Cartella ufficiale: `C:\Users\Utente\Documents\Agente studio`
- File sincronizzato sul Desktop: `C:\Users\Utente\Desktop\CineStudio.html`
- Commit di riferimento: `1517fe9`

## Nuova Web-App Creata: CineStudio (Assistente Cinema Serale)

Creata l'applicazione autonoma **CineStudio** (`CineStudio.html` e script `avvia_cinestudio.bat`) per eliminare la fatica decisionale nella scelta dei film serali su **Netflix, Prime Video, Disney+ e RaiPlay**.

### Caratteristiche Implementate:

1. **Guardrail Quantitativi di Qualità**:
   - Voto IMDb $\ge$ 6.3 (configurabile).
   - Voto MYmovies $\ge$ 3.3 (configurabile).
   - Esclusione categorica di horror, commedie demenziali, film lenti senza trama e musical.

2. **Calibrazione su DNA Cinefilo**:
   - Inclusione dei registi di riferimento: Spielberg, Nolan, Miyazaki, Sorrentino, Leone, Tornatore, Troisi, Benigni.
   - Attori feticcio: Leonardo DiCaprio, Matt Damon, Robin Williams.
   - Punti cardinali: *C'era una volta in America*, *Nuovo Cinema Paradiso*, *Le ali della libertà*, *Il signore degli anelli*, *Il cammino per Santiago*, *Hereafter*, *Hugo Cabret*, *The Wolf of Wall Street*, *Vita di Pi*, *Limitless*.

3. **Motore Decisionale a "3 Scelte Secche"**:
   - Pulsante serale rapido *"3 SCELTE PER STASERA"* per evitare il doomscrolling nei cataloghi.
   - Filtri veloci per mood (Mente, Anima, Cuore, Epica, Meraviglia) e durata massima ($\le$ 1h45m per quando si è stanchi, $\le$ 2h, kolossal).
   - Schede con motivazione esplicita *"Perché è per te"*, voti IMDb/MYmovies, badge piattaforma e link diretto allo streaming.

4. **Tracciamento Personale (LocalStorage)**:
   - Funzione *"Già Visto"* per escludere automaticamente i titoli già visti dalle raccomandazioni future.
   - Watchlist serale integrata.
   - Nessun server o database esterno necessario: funziona sia come file locale sia via web server.

5. **Integrazione Promemoria 1-Click (WhatsApp & Google Calendar)**:
   - Tasto icona campana 🔔 presente su ogni scheda film, nella Watchlist e nel catalogo completo.
   - Apertura modale di pianificazione con orario preimpostato (Stasera 21:00, Stasera 21:30, Domani 21:15 o data/ora personalizzata).
   - **WhatsApp Intent**: genera e apre un messaggio formattato con titolo, piattaforma, durata, voti IMDb/MYmovies, motivazione e link streaming.
   - **Google Calendar Intent**: genera l'evento calendar completo di orario d'inizio e fine calcolato sulla durata esatta del film, alert notifica, link e sinossi.

## Ripristino

Per rimuovere la nuova web-app qualora non desiderata:

```powershell
Remove-Item -Path "C:\Users\Utente\Documents\Agente studio\CineStudio.html" -Force
Remove-Item -Path "C:\Users\Utente\Documents\Agente studio\avvia_cinestudio.bat" -Force
Remove-Item -Path "C:\Users\Utente\Desktop\CineStudio.html" -Force
Remove-Item -Path "C:\Users\Utente\Desktop\avvia_cinestudio.bat" -Force
```
