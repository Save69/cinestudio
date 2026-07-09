# GLADIATOR - Ripristino V1

## Scopo

Questo file documenta il punto di ripristino della sessione e deve essere
aggiornato o duplicato a fine lavoro quando Codex, Antigravity o un altro agente
modificano il progetto.

## Regola di fine sessione

A fine sessione creare un file markdown di ripristino con nome progressivo:

`gladiator_Ripristino_V2.md`

`gladiator_Ripristino_V3.md`

e cosi' via.

Ogni file deve indicare:

1. data e ora della sessione;
2. agente usato;
3. cartella ufficiale;
4. commit o tag di partenza;
5. commit o tag finale;
6. file modificati;
7. cosa e' stato cambiato;
8. come tornare indietro.

## Stato iniziale noto

Cartella ufficiale:

`C:\Users\Utente\Documents\Agente studio`

Baseline:

`0bbfe72 Baseline Agente Studio recuperato`

Tag disponibili:

- `baseline-agente-studio`
- `backup-2026-07-09-prima-sessione`
- `backup-2026-07-09-prima-regola-ripristino`

## Comandi di controllo

```powershell
cd "C:\Users\Utente\Documents\Agente studio"
git status
git log --oneline --decorate -n 5
git tag --list
```

## Comando da dare all'agente a fine sessione

```text
Prima di chiudere la sessione, crea o aggiorna un file markdown di ripristino
con nome progressivo tipo gladiator_Ripristino_V2.md.

Il file deve contenere:
- data e ora;
- agente usato;
- cartella di lavoro;
- stato Git iniziale;
- stato Git finale;
- commit/tag di backup creati;
- file modificati;
- riepilogo delle modifiche;
- istruzioni concrete per tornare indietro.

Dopo aver creato il file, esegui git status e proponi un commit finale.
```

## Procedura di ripristino base

Per vedere i punti disponibili:

```powershell
git log --oneline --decorate --all
git tag --list
```

Per tornare a un file specifico dal baseline:

```powershell
git restore --source baseline-agente-studio -- AgenteStudio.html
```

Per annullare modifiche non ancora committate:

```powershell
git restore .
```

Usare comandi distruttivi come `git reset --hard` solo dopo conferma esplicita.
