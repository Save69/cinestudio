# GLADIATOR - Ripristino V12

## Sessione

- Data: 29 luglio 2026
- Agente: Antigravity (Gemini 3.5 Flash)
- Cartella ufficiale: `C:\Users\Utente\Documents\Agente studio`
- Commit iniziale: `f2bee12`
- Tag di ripristino iniziale: `backup-2026-07-29-sesta-sessione` (o stato pulito prima di questa modifica)

## Modifiche

- Aggiornati i temi cromatici delle settimane in `weekThemes` in base alle nuove preferenze:
  - **Settimana Corrente**: Tema **🔴 Rosso** (accento `red-600`, ombre `shadow-red-100`).
  - **Prossima Settimana (+1)**: Tema **🟡 Giallo/Arancio** (accento `amber-500`, ombre `shadow-amber-100`).
  - **Settimana Successiva (+2)**: Tema **🟢 Verde** (accento `emerald-600`, ombre `shadow-emerald-100`).
- Aggiunta la funzionalità di **Archivio Settimane Passate**:
  - Definita la variabile di stato `selectedArchiveWeekKey` e il tema d'archivio `archiveTheme` (Tonalità **Grigio Slate**).
  - Implementate le funzioni JS:
    - `getPastWeeksList()`: individua tutte le settimane salvate antecedenti a quella corrente.
    - `formatWeekRange(weekKey)`: formatta la data in modo amichevole (es. *20 Lug - 26 Lug 2026*).
    - `mostraSettimanaArchivio(weekKey)`: visualizza i compiti della settimana storica selezionata colorandoli a tema grigio slate.
    - `chiudiArchivio()`: esce dalla visualizzazione archivio ritornando alla settimana corrente.
    - `toggleArchiveDropdown()`: mostra un menu a tendina dinamico per selezionare le settimane storiche.
  - Aggiornate `getWeekKey`, `getWeekSchedule`, `isOggi` e `getDataGiornoSettimana` per deviare automaticamente la visualizzazione delle date e il recupero dei dati quando l'archivio è attivo.
  - Aggiornata `rimandaAlBloccoNote` per supportare il nuovo formato dati nidificato.
- Modifiche UI:
  - Inserito il pulsante dropdown **`🗂️ Archivio`** accanto ai pulsanti settimana.
  - Inserito un banner informativo con il pulsante **`Torna all'Agenda Attiva`** visualizzato solo in modalità Archivio.
- Sincronizzato l'aggiornamento nel file `AgenteStudio.html` sul Desktop.

## Ripristino

Per annullare le modifiche e ritornare allo stato iniziale della sessione:

1. Ripristinare il file di lavoro:
```powershell
git checkout -- AgenteStudio.html
```

2. Sincronizzare nuovamente il file del Desktop:
```powershell
Copy-Item -Path "C:\Users\Utente\Documents\Agente studio\AgenteStudio.html" -Destination "C:\Users\Utente\Desktop\AgenteStudio.html" -Force
```
