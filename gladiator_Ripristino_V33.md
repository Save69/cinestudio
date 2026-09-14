# GLADIATOR - Ripristino V33

## Sessione

- Data: 14 settembre 2026
- Agente: Antigravity
- Cartella ufficiale: `C:\Users\Utente\Documents\Agente studio`
- File sincronizzato sul Desktop: `C:\Users\Utente\Desktop\AgenteStudio.html`
- File di avvio Desktop: `C:\Users\Utente\Desktop\Avvia_AgenteStudio.bat`
- Commit precedente: `8c6c514`

## Modifiche

1. **Integrazione Google Calendar Ufficiale (OAuth 2.0)**:
   - Integrazione delle librerie Google Identity Services (`gsi/client`) e Google API Client (`gapi.js`).
   - Modulo JS completo con supporto autenticazione OAuth 2.0 (token client), salvataggio configurazione nel `localStorage`, recupero eventi del calendario e gestione stato connessione.
   - Pulsante dinamico `📅 Google Calendar` aggiunto nell'intestazione di **Operatività & Agenda** per aprire la configurazione o mostrare lo stato di connessione / sincronizzazione in tempo reale.

2. **Sistema di Alert Multi-Livello (Sonoro + Notifiche Desktop Windows + Toast)**:
   - **Chime Sonoro a 3 Toni**: generato nativamente tramite Web Audio API (`AudioContext`) senza dipendenze o file audio esterni.
   - **Notifiche Desktop Windows**: integrate con la Web Notification API per avvisare a **-15 minuti**, **-5 minuti** e **all'orario esatto (0 min)** dell'evento.
   - Loop di monitoraggio automatico in background con memoria degli alert già inviati per evitare notifiche duplicate.

3. **Visualizzazione nella Scaletta Settimanale ed Esportazione Task**:
   - Inserimento box arancione ambra "Eventi Google Calendar" all'inizio di ciascun giorno della scaletta con orario, titolo, link a Google Meet e luogo.
   - Aggiunta icona calendario 📅 accanto a ciascun task della scaletta per esportarlo direttamente come nuovo evento su Google Calendar con data, orari e promemoria preimpostati.

4. **Strumenti di Supporto**:
   - Creato launcher con 1 click `avvia_agente_studio.bat` (e duplicato sul Desktop) per avviare il server HTTP locale autorizzato (`http://localhost:8080`) e aprire il browser.
   - Creata documentazione dettagliata `GUIDA_GOOGLE_CALENDAR.md` con i 4 passaggi per creare il Client ID gratuito su Google Cloud Console.

## Ripristino

Per annullare questa modifica e tornare allo stato del commit `8c6c514`:

```powershell
git checkout 8c6c514 -- AgenteStudio.html
Copy-Item -Path "C:\Users\Utente\Documents\Agente studio\AgenteStudio.html" -Destination "C:\Users\Utente\Desktop\AgenteStudio.html" -Force
```
