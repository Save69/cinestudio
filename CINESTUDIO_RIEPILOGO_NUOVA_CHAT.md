# CineStudio - Documento di Riepilogo & Handover per Nuova Chat

> **Scopo di questo documento**: Fornire all'utente e a qualsiasi nuovo agente AI (in una nuova chat) il quadro completo, le regole operative, il DNA cinefilo dell'utente e l'architettura tecnica della web-app **CineStudio**.
> **Data ultimo aggiornamento**: 1 ottobre 2026  
> **Cartella ufficiale di lavoro**: `C:\Users\Utente\Documents\Agente studio`  
> **File principale sincronizzato sul Desktop**: `C:\Users\Utente\Desktop\CineStudio.html`  
> **Script rapido di avvio su Desktop**: `C:\Users\Utente\Desktop\avvia_cinestudio.bat`

---

## 1. Cos'è CineStudio & Filosofia del Progetto

**CineStudio** è una web-app autonoma (*single-file* HTML/CSS/JS, zero dipendenze esterne o database lato server) progettata per **eliminare la fatica decisionale serale** (*doomscrolling* tra i cataloghi streaming).

L'utente la sera vuole aprire l'app, indicare il tempo a disposizione e il mood desiderato, e ottenere **3 scelte secche calibrate al millimetro sui suoi gusti**, senza perdere 45 minuti a scorrere trailer o rischiare fregature.

---

## 2. Il DNA Cinefilo dell'Utente (Parametri di Scelta Personali)

### A. I Punti Cardinali del Cuore (Film GIA' VISTI e AMATI)
> ⚠️ **ATTENZIONE CRITICA PER IL PROSSIMO AGENTE**:  
> Questa lista deve contenere **SOLO E SOLTANTO** i film che l'utente ha personalmente indicato come pietre miliari della propria vita. **NON aggiungere MAI a questa lista titoli che l'utente non ha ancora visto** (i film da scoprire vanno nel catalogo proposte o nel radar, non nei punti cardinali).

1. *C'era una volta in America* (Sergio Leone)
2. *Nuovo Cinema Paradiso* (Giuseppe Tornatore)
3. *Le ali della libertà* (Frank Darabont)
4. *Il signore degli anelli* (Peter Jackson)
5. *Il cammino per Santiago* (Emilio Estevez)
6. *Hereafter* (Clint Eastwood)
7. *Hugo Cabret* (Martin Scorsese)
8. *The Wolf of Wall Street* (Martin Scorsese)
9. *Vita di Pi* (Ang Lee)
10. *Limitless* (Neil Burger)
11. *La La Land* (Damien Chazelle)

### B. Maestri e Registi di Riferimento
- Steven Spielberg
- Christopher Nolan
- Hayao Miyazaki (Studio Ghibli)
- Paolo Sorrentino
- Sergio Leone
- Giuseppe Tornatore
- Massimo Troisi
- Roberto Benigni
- Nanni Moretti

### C. Attori Feticcio
- **Leonardo DiCaprio**
- **Matt Damon**
- **Robin Williams**

### D. Interessi d'Autore & Festival Internazionali
- Vincitori della **Mostra Internazionale d'Arte Cinematografica di Venezia** (Leone d'Oro, Orizzonti, Settimana della Critica)
- Vincitori del **Festival Internazionale del Cinema di Berlino** (Orso d'Oro / Argento)
- Vincitori e candidati ai **Premi Oscar**
- Produzioni **Fandango** (Domenico Procacci)

### E. I Blacklistati (Cosa ESCLUDERE CATEGORICAMENTE)
- ❌ **Horror & Splatter**
- ❌ **Commedie demenziali / trash**
- ❌ **Dialetti regionali stretti privi di sottotitoli chiari** *(es. Margini: lo sforzo d'ascolto continuo infastidisce la visione serale)*
- ❌ **Film incentrati su sottoculture punk/hardcore o musica sguaiata/aggressiva** *(l'utente ama le partiture liriche ed emotive di Morricone, Piovani, il pianoforte, non il punk rumoroso)*
- ❌ **Musical canzonettistici commerciali**  
  *(Con eccezione esplicita per capolavori cinematografici acclamati come La La Land)*

> 💡 **NOTA CRUCIALE SUL RITMO & CINEMA FRANCESE**:  
> L'utente **NON richiede** che ci sia un "gancio hollywoodiano" o un'azione frenetica nei primi 20 minuti. Ama profondamente il **cinema francese ed europeo d'autore** (*Amélie*, *Quasi amici*, Truffaut, Jeunet), con i suoi tempi distesi, le sfumature psicologiche e le atmosfere poetiche. Il problema con *Margini* era unicamente linguistico (dialetto incomprensibile senza sottotitoli) e musicale (punk sgradito).


---

## 3. I Guardrail Quantitativi & la Regola "Zero Noleggi"

### Guardrail Quantitativi di Qualità
- **Soglia Minima IMDb**: $\ge 6.3$ (configurabile dall'interfaccia)
- **Soglia Minima MYmovies**: $\ge 3.3$ (configurabile dall'interfaccia)
- Un film viene ammesso se supera **almeno uno dei due guardrail** e rispetta il DNA.

### 🛡️ REGOLA FERREA "ZERO NOLEGGI A PAGAMENTO"
- **L'utente NON è interessato a noleggiare film a pagamento** (niente titoli a 2.99€ o 3.99€ su Prime Video Store, Apple TV o Chili).
- Devono essere suggeriti **esclusivamente film inclusi negli abbonamenti** o **completamente gratuiti**:
  - ✅ **Netflix** (Incluso in abbonamento)
  - ✅ **Prime Video** (Solo catalogo standard flat, NO Store/Noleggio)
  - ✅ **Disney+** (Incluso in abbonamento)
  - ✅ **RaiPlay** (100% Gratuito on-demand)
  - ✅ **Discovery+** (100% Gratuito)
  - ✅ **La7** (100% Gratuito)
- **Cosa fare se un film cercato è solo a noleggio** (es. *I guerrieri* del 1970 con Clint Eastwood):
  - Il film viene escluso dalla selezione per stasera (`rentalOnly: true`).
  - Viene archiviato nel **Radar Film Cercati**, in attesa che approdi gratis su RaiPlay o incluso in abbonamento.

---

## 4. Architettura Tecnica & Funzionalità di CineStudio (`CineStudio.html`)

### 1. Selezione Serale Istantanea ("3 Scelte per Stasera")
- Pulsante centrale che estrae casualmente una **terna mirata** dal pool filtrato.
- Ogni scheda mostra: badge piattaforma, durata, voti IMDb & MYmovies, box *"Perché è per te"*, sinossi, pulsante *"Guarda Ora"*, campana promemoria, tasto Watchlist e tasto *"Già Visto"*.

### 2. Modale Dettagli & Trama Completa a 1-Click
- Cliccando su **qualsiasi titolo o scheda** nell'app (sia nelle 3 scelte, sia nella tabella di tutti i film, sia nella Watchlist), si apre la modale `#modal-movie-details`.
- Mostra la **trama completa estesa (Di cosa parla)**, il cast dettagliato, i voti, la motivazione del consiglio e i comandi rapidi.

### 3. Filtro Novità: *"🆕 Novità & Gemme Recenti (2022-2026)"*
- Categoria specifica nel selettore del Mood per escludere i classici già visti e proporre solo novità d'autore recenti vincitrici a festival (es. *Piccole cose come queste* su RaiPlay con Cillian Murphy, *E i figli dopo di loro* da Venezia su RaiPlay, *La società della neve* su Netflix, *Past Lives* su Prime, *Anatomia di una caduta*).

### 4. 📡 Radar Film Cercati & Desiderati (`#modal-radar`)
- Accessibile dal pulsante con la parabola nell'header.
- Permette di tenere traccia dei film che l'utente cerca ma che attualmente sono solo a noleggio o non disponibili in streaming, con monitoraggio dello stato.

### 5. Integrazione Promemoria 1-Click (WhatsApp & Google Calendar)
- **WhatsApp**: genera messaggio formattato con titolo, piattaforma, durata, voti, motivazione e link streaming diretto.
- **Google Calendar**: genera evento con data/ora preimpostata (Stasera 21:00, 21:30, Domani 21:15 o personalizzata), calcolando automaticamente la durata esatta del film e impostando alert notifica.

### 6. Gestione Persistenza Locale (LocalStorage)
Nessun database remoto necessario:
- `cinestudio_seen`: Array JSON degli ID film segnati come già visti (esclusi per sempre dai suggerimenti).
- `cinestudio_watchlist`: Array JSON dei film salvati per le prossime sere.
- `cinestudio_custom_dna`: Array dei tag/registi aggiunti manualmente dall'utente.
- `cinestudio_user_movies`: Film personalizzati aggiunti tramite la modale `+ Aggiungi Film`.
- `cinestudio_radar_movies`: Film in monitoraggio nel Radar personale.
- `cinestudio_disliked_movies`: Array JSON dei film bocciati / esperienze negative con motivi (es. dialetti senza sottotitoli, punk/metal) e note personali.
- `cinestudio_top250_seen`: Array JSON dei rank (1-250) dei capolavori IMDb già visti (sincronizzati bidirezionalmente con `cinestudio_seen`).
- `cinestudio_min_imdb` e `cinestudio_min_mymovies`: Soglie guardrail salvate.

---

## 4.1. Sfida IMDb Top 250 & Audit Autonomo del Giovedì

1. **Dataset Completo IMDb Top 250 Integrato**:
   - Tutti i 250 capolavori della classifica IMDb (dal #1 *Le ali della libertà* al #250) sono integrati in `IMDB_TOP_250` con titolo italiano, titolo originale, anno, regista, cast, rating IMDb e genere.
   - Accessibile direttamente dal pulsante `🏆 Top 250` nell'header e dal tab dedicato nella finestra Radar.
   - **Tracciatore di Progresso**: barra di avanzamento e contatore dinamico `[ X / 250 Visti ] (Y%)`.
   - **Filtri Rapidi**: `Tutti (250)`, `🟢 Disponibili Ora` (nel catalogo flat 6 piattaforme), `📡 In Attesa / Radar` (solo a noleggio), `✅ Già Visti`, `Da Vedere`.
   - **Sincronizzazione Automatica**: contrassegnare un film come visto lo esclude anche dalla rotazione delle terne serali.

2. **Verifica live della disponibilità (TMDB, dati JustWatch) — dalla V64**:
   - ⚠️ L'"audit autonomo del giovedì" (`task-1897`) descritto in precedenza **non è mai esistito**, e lo script
     `scripts/weekly_cinestudio_updater.py` non verificava nulla online (aggiungeva film scritti a mano).
     Script e workflow GitHub Actions `weekly_scan.yml` sono stati **eliminati nella V67**: non ricrearli.
     Il controllo manuale del giovedì descritto in `REGOLE_LAVORO.md` resta valido come verifica a campione.
   - Film del Radar diventati inclusi entrano da soli nelle proposte (V66), esclusi i Punti Cardinali.
   - "Guarda Ora" apre la ricerca del titolo su Netflix, Prime Video e RaiPlay; per Disney+ la pagina TMDB "dove guardarlo" (V67).
   - Catalogo curato: 122 film (V71: +60 film verificati su JustWatch; MYmovies assente mostrato come "—", mai inventato).
   - **Scoperta automatica (V72)**: ogni 24 ore TMDB "discover" trova i film inclusi oggi sulle 4 piattaforme
     (qualità alta, cinema europeo per lingua originale, novità dal 2022; horror escluso). Fino a 320 film,
     badge "✨ Scoperto per te", voto **TMDB** (non IMDb), tono e mood **stimati dai generi** (nel dubbio "demanding"),
     peso ridotto del 30% senza affinità DNA. Si attiva/disattiva dalla riga di stato. Dati in `cinestudio_tmdb_discovery`.
   - Ora è l'app stessa a verificare: con la chiave TMDB impostata (link "Collega TMDB" sotto "Le Tue 3 Opzioni"),
     ogni 24 ore interroga TMDB per catalogo e Radar, salvando l'esito in `cinestudio_tmdb_cache`.
   - Film non incluso in nessun abbonamento → escluso dalle proposte (elenco cliccabile "N non più inclusi").
     Film su un'altra piattaforma → mostrato su quella reale. Film del Radar diventato incluso → "Ora incluso su …".
   - Le schede mostrano "Verificato gg/mm" oppure "Non verificato". I canali Amazon a pagamento NON contano come Prime.
   - JustWatch/TMDB non tracciano La7: i film La7 risultano sempre non verificabili.
   - Chiave salvata in `cinestudio_tmdb_key`, solo sul dispositivo (mai nel codice).

---

## 5. Capacità dell'Agente AI a Supporto di CineStudio

1. **Scansione Web di Pagine Streaming**:
   - L'agente è in grado di leggere direttamente URL (es. raccolte RaiPlay, elenchi Prime, cataloghi festival), filtrare in pochi secondi i titoli mediocri e isolare solo le perle conformi al DNA dell'utente.
2. **Verifica Streaming in Tempo Reale**:
   - Quando l'utente chiede: *"Cercami questo film"*, l'agente verifica tramite ricerca live se è disponibile **gratis o incluso** (senza costi di noleggio).
3. **Aggiornamento del Codice**:
   - Qualsiasi modifica a `CineStudio.html` deve mantenere la validità JavaScript pura, preservare le chiavi di LocalStorage, sincronizzare la copia sul Desktop ed essere committata su Git secondo `REGOLE_LAVORO.md`.

---

## 6. Prompt di Avvio Rapido Consigliato per Nuova Chat

Quando apri una nuova chat, puoi incollare questo messaggio:

```text
Ciao! Continuiamo a lavorare su CineStudio (assistente film serale per Netflix, Prime Video, Disney+ e RaiPlay).
Fai riferimento al file di documentazione ufficiale "CINESTUDIO_RIEPILOGO_NUOVA_CHAT.md" e alle "REGOLE_LAVORO.md" nella cartella C:\Users\Utente\Documents\Agente studio.
Ricorda la regola Zero Noleggi (solo streaming incluso o gratuito) e il rispetto rigoroso dei miei Punti Cardinali del DNA. La disponibilità la verifica l'app con TMDB: non inserire piattaforme a memoria e non ricreare script del giovedì.
```
