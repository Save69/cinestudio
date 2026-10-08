# Regole operative Agente Studio

## Cartella ufficiale

La cartella ufficiale di lavoro e':

`C:\Users\Utente\Documents\Agente studio`

Codex, Antigravity o qualunque altro agente devono lavorare su questa cartella.
Le cartelle `_Irpinia Bandi`, `scratch`, backup, download o copie temporanee sono solo archivi o sorgenti storiche, non luoghi di lavoro.

## Prima di ogni modifica

Prima di modificare qualsiasi file:

1. verificare la cartella corrente;
2. eseguire `git status`;
3. segnalare eventuali modifiche non salvate;
4. non sovrascrivere modifiche esistenti senza conferma;
5. creare un punto di ripristino con commit o tag;
6. spiegare quali file saranno modificati.

## Durante il lavoro

- Fare modifiche piccole e verificabili.
- Non copiare dentro il progetto file sensibili come `.env`, token, credenziali, installer o archivi non necessari.
- Per esperimenti rischiosi usare un branch dedicato.
- Se qualcosa non funziona, fermarsi e confrontare lo stato con Git prima di procedere.

## Dopo ogni modifica

Alla fine della sessione:

1. verificare che l'app sia ancora apribile;
2. eseguire `git status`;
3. riepilogare i file modificati;
4. creare o aggiornare un file di ripristino markdown progressivo;
5. creare un commit se la modifica e' valida;
6. lasciare istruzioni chiare per il prossimo agente.

## File di ripristino obbligatorio

A fine sessione ogni agente deve creare un file markdown di ripristino con nome
progressivo, per esempio:

`gladiator_Ripristino_V2.md`

Il modello iniziale e':

`gladiator_Ripristino_V1.md`

Il file di ripristino deve contenere data, agente usato, cartella di lavoro,
stato Git iniziale e finale, tag o commit creati, file modificati, riepilogo
delle modifiche e istruzioni concrete per tornare indietro.

## Prompt operativo da usare con ogni agente

Prima di lavorare su Agente Studio, verifica che la cartella sia
`C:\Users\Utente\Documents\Agente studio`, controlla `git status`, non
sovrascrivere modifiche non committate, crea un punto di ripristino prima di
editare e riepiloga i file che intendi modificare.

## Disponibilità dei film CineStudio (Zero Noleggi)

Dalla V64 (ottobre 2026) la disponibilità la verifica **l'app stessa**, ogni 24 ore, tramite TMDB (dati JustWatch Italia):
i film non più inclusi escono da soli dalle proposte, quelli del Radar che diventano inclusi entrano da soli.
Il vecchio "controllo settimanale autonomo" e lo script del giovedì non verificavano nulla e sono stati eliminati (V67):
**non ricrearli**.

**Controllo a campione (facoltativo, ad esempio il giovedì o quando richiesto):**
> "Apri CineStudio, controlla che la riga sotto «Le Tue 3 Opzioni per Stasera» dica «Verificati live» con la data di oggi,
> poi verifica su JustWatch Italia 5 film a caso tra quelli proposti. Se qualcosa non torna, segnalalo con il titolo e la piattaforma."

**Linee guida assolute:**
1. **Precisione (Voto 10) > Velocità (Voto 1)**: vietata qualsiasi fretta o assunzione da memoria.
2. **Mai piattaforme a memoria**: ogni film aggiunto al catalogo va verificato prima su JustWatch Italia
   (streaming incluso, non noleggio/acquisto, non canali Amazon a pagamento come CineAutore o MGM+).
3. **Tolleranza Zero Noleggi**: un titolo a noleggio o acquisto (€ extra) non deve mai comparire come disponibile:
   va nel Radar, dove la verifica live lo terrà d'occhio.
4. **Piattaforme**: Netflix, Prime Video, Disney+, RaiPlay. Discovery+ (0 film) e La7 (non verificabile) sono nascoste dalla V69.

