# 📅 Guida all'integrazione Google Calendar in Agente Studio

Questa guida ti accompagna passo-passo nella configurazione del tuo **Client ID Google** (gratuito e personale) per sincronizzare il tuo Google Calendar con **Agente Studio**, ricevere **alert sonori e notifiche Windows** per i tuoi appuntamenti ed esportare i task della scaletta con 1 click.

---

## 🚀 1. Perché serve un Client ID?
Google Calendar protegge i tuoi dati personali. Con un Client ID OAuth 2.0 personale:
- I tuoi eventi rimangono al 100% privati nel tuo browser (nessun server intermedio).
- Ricevi gli alert sonori (Chime a 3 toni) e notifiche Windows a **-15 min, -5 min e all''orario esatto**.
- Puoi sincronizzare e creare eventi direttamente dalla scaletta settimanale.

---

## 🛠️ 2. Configurazione Rapida (5 minuti)

### Passo 1: Crea un Progetto su Google Cloud Console
1. Vai su [Google Cloud Console](https://console.cloud.google.com/).
2. Accedi con il tuo account Google.
3. In alto a sinistra, clicca sul menu a tendina del progetto e seleziona **"Nuovo Progetto"** (chiamalo ad es. `Agente Studio`).
4. Clicca su **Crea**.

### Passo 2: Abilita l''API Google Calendar
1. Nella barra di ricerca in alto, cerca **"Google Calendar API"**.
2. Clicca sul risultato e poi su **"Abilita"** (Enable).

### Passo 3: Configura la Schermata di Consenso OAuth
1. Dal menu laterale sinistro, vai su **API e servizi** > **Schermata consenso OAuth** (OAuth consent screen).
2. Seleziona **Esterno** (External) e clicca **Crea**.
3. Compila i campi obbligatori:
   - **Nome app**: `Agente Studio`
   - **Email di assistenza utente**: la tua email
   - **Dati di contatto dello sviluppatore**: la tua email
4. Clicca **Salva e continua**.
5. Nella schermata **Utenti di test** (Test users), aggiungi il tuo indirizzo email Gmail personale.
6. Clicca **Salva e continua**.

### Passo 4: Crea le Credenziali (Client ID OAuth)
1. Dal menu laterale, vai su **API e servizi** > **Credenziali** (Credentials).
2. In alto, clicca su **+ Crea credenziali** > **ID client OAuth**.
3. Come *Tipo di applicazione*, seleziona **Applicazione Web** (Web application).
4. Nel campo **Origini JavaScript autorizzate** (Authorized JavaScript origins), clicca **+ Aggiungi URI** e inserisci:
   - `http://localhost:8080`
   - `http://localhost`
   - `http://127.0.0.1:8080`
5. Clicca su **Crea**.
6. Ti verrà mostrato il tuo **ID Client** (avrà una forma tipo `123456789-xxxxxxxx.apps.googleusercontent.com`).
7. Copia questo ID Client.

---

## 💻 3. Come Avviare e Collegare Agente Studio

### Avvio con 1 Click
1. Fai doppio clic sul file **`avvia_agente_studio.bat`** presente nella cartella o sul Desktop.
2. Si aprirà automaticamente il browser su `http://localhost:8080/AgenteStudio.html`.

### Collegamento in Agente Studio
1. Vai nella scheda **Operatività & Agenda**.
2. In alto a destra clicca sul pulsante **`📅 Google Calendar (Disconnesso)`**.
3. Incolla il tuo **Google Client ID** nel campo dedicato.
4. Clicca **💾 Salva Impostazioni** e poi **🔑 Connetti Google Calendar**.
5. Seleziona il tuo account Google e autorizza l''accesso in sola lettura o lettura/scrittura.
6. Clicca su **🔔 Notifiche Desktop** per abilitare i popup su Windows e prova il pulsante **🎵 Test Chime** per verificare l''audio!

---

## 🔔 Funzionalità Incluse
- **Alert Sonoro (Web Audio API)**: Chime melodico a 3 toni senza dipendenze esterne.
- **Notifiche Desktop Windows**: Popup istantaneo con titolo evento, orario e localizzazione.
- **Visualizzazione nella Scaletta**: Gli eventi del giorno appaiono in un box elegante arancione/ambra sotto la data.
- **Esportazione Task su Google Calendar**: Accanto a ciascun compito nella scaletta trovi l''icona 📅 per inviarlo direttamente al tuo calendario.
