# GLADIATOR - Ripristino V38

## Sessione

- Data: 22 settembre 2026
- Agente: Antigravity
- Cartella ufficiale: `C:\Users\Utente\Documents\Agente studio`
- File sincronizzato sul Desktop: `C:\Users\Utente\Desktop\AgenteStudio.html`
- Commit precedente: `9db3fe8`

## Modifiche

1. **Rimozione Automatica della Scritta "In sospeso" con Nuova Scadenza / Ripianificazione**:
   - Quando viene impostata una nuova data o scadenza per un compito (tramite menu a tendina nella Matrice, calendario di pianificazione o selettore data libera), la dicitura `⏳ In sospeso` viene **immediatamente rimossa**.
   - Mostrato badge pulito con la data di scadenza attiva: `📅 GG/MM/AAAA`.

2. **Calcolo e Assegnazione Automatica Scadenza (`calcolaDataISO`)**:
   - Aggiunta la funzione `calcolaDataISO(indiceGiorno, offset)` per determinare con precisione la data di calendario assegnata quando un compito viene spostato in un giorno della settimana corrente o futura.
   - `spostaAttivitaTraGiorni`: ora assegna automaticamente la nuova data (`itemData.data = nuovaData || dataCalcolata`) ed elimina il blocco per compiti con stesso nome giorno ma settimana differente (`srcWeekKey !== destMondayKey`).

3. **Selettore Scadenza Libera nel Modal Calendario**:
   - Nel modal di pianificazione, il campo data libera permette ora di impostare direttamente la nuova scadenza per l'attività (`pianificaDataLiberaModal`), salvando la data e trasferendo il compito.

4. **Integrità & Sincronizzazione**:
   - File aggiornato in workspace e sincronizzato 1:1 su Desktop con verifica hash SHA256.

## Ripristino

Per annullare questa modifica e tornare allo stato del commit `9db3fe8`:

```powershell
git checkout 9db3fe8 -- AgenteStudio.html
Copy-Item -Path "C:\Users\Utente\Documents\Agente studio\AgenteStudio.html" -Destination "C:\Users\Utente\Desktop\AgenteStudio.html" -Force
```
