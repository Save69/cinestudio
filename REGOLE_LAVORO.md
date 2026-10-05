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

## Protocollo Controllo Settimanale CineStudio (Ogni Giovedì)

Ogni giovedì, o ogni volta che viene richiesto l'aggiornamento o il controllo dei film, l'agente deve applicare rigorosamente questo protocollo:

**Prompt Operativo Mandatorio:**
> "Esegui il controllo settimanale di CineStudio sui 6 cataloghi (Netflix, Prime, Disney+, RaiPlay, La7, Discovery+). Procedi con calma e verifica live su JustWatch Italia ogni singolo titolo. Se un film non è incluso al 100% in abbonamento flat gratuito, eliminalo o spostalo nel Radar. Preferisco avere 10 film in meno ma la certezza assoluta di zero costi extra."

**Linee guida assolute:**
1. **Precisione (Voto 10) > Velocità (Voto 1)**: Vietata qualsiasi fretta o assunzione da memoria.
2. **Verifica Live Puntuale**: Controllare JustWatch Italia in tempo reale per ciascun titolo sui 6 cataloghi.
3. **Tolleranza Zero Noleggi**: Se un titolo richiede noleggio o acquisto nello Store digitale (€ extra), NON deve mai comparire come disponibile: va rimosso o spostato nel Radar.

