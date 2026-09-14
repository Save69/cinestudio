# GLADIATOR - Ripristino V31

## Sessione

- Data: 14 settembre 2026
- Agente: Antigravity
- Cartella ufficiale: `C:\Users\Utente\Documents\Agente studio`
- File sincronizzato sul Desktop: `C:\Users\Utente\Desktop\AgenteStudio.html`
- Commit precedente: `914cbc9`

## Modifiche

1. **Blocchi con Subtask / Checklist Espandibile**:
   - Ogni compito della scaletta può ora contenere una checklist di sotto-attività (`subtasks`).
   - Visualizzazione con pulsante toggle `📋` e chevron per espandere/comprimere le sotto-attività senza intasare la vista.
   - Checkbox indipendenti per spuntare i singoli micro-passaggi (es. "Invia email", "Scouting bandi", "Rivedi bozze") con indicatore numerico di avanzamento (es. `2/3`).
   - Inserimento rapido di nuove sotto-voci con input dedicato sia in visualizzazione rapida che in modalità Modifica.
   - Conservazione totale delle sotto-attività durante lo spostamento tra giorni e nei Promemoria.

2. **Calcolo Carico Cognitivo Ponderato per Quadranti Eisenhower (`calcolaCaricoGiorno`)**:
   - **Q1 (Fai Subito) & Q2 (Pianifica / Focus profondo)**: Peso **1.0** (Focus pieno).
   - **Q3 (Delega / Routine rapida <15min)**: Peso **0.25** (4 task di routine equivalgono a 1 compito focus).
   - **Q4 (Parcheggia / Bassa priorità)**: Peso **0.1**.
   - Nessuna priorità: Peso **0.75**.
   - **Badge intelligenti parlanti**:
     - 🟢 **Ottimale / Libero** (punteggio ≤ 3.0, es. `🟢 2 Focus · 4 Rapidi`)
     - 🟡 **Medio / Bilanciato** (punteggio 3.1 - 4.5, es. `🟡 3 Focus · 3 Rapidi`)
     - 🔴 **Sovraccarico ⚠️** (punteggio > 4.5)
   - Eliminazione completa dei falsi positivi di sovraccarico a inizio settimana dovuti alla routine quotidiana (come Irpinia Bandi).

3. **Integrazione nel Pianificatore Futuro con Controllo Carico**:
   - Il modale del calendario ora mostra per ogni giorno il badge con calcolo ponderato e indica i compiti che contengono checklist (`📋 x/y`).
   - I blocchi possono essere trascinati tra i giorni preservando intatta la loro checklist.

4. **Sincronizzazione**:
   - File aggiornato in `C:\Users\Utente\Documents\Agente studio\AgenteStudio.html` e sincronizzato su `C:\Users\Utente\Desktop\AgenteStudio.html` con verifica hash SHA256.

## Ripristino

Per annullare questa modifica e tornare allo stato del commit `914cbc9`:

```powershell
git checkout 914cbc9 -- AgenteStudio.html
Copy-Item -Path "C:\Users\Utente\Documents\Agente studio\AgenteStudio.html" -Destination "C:\Users\Utente\Desktop\AgenteStudio.html" -Force
```
