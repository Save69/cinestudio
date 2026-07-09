# Checklist sessione Agente Studio

## Avvio sessione

```powershell
cd "C:\Users\Utente\Documents\Agente studio"
git status
git tag backup-YYYY-MM-DD-prima-sessione
```

Se `git status` mostra modifiche non salvate, creare prima un commit di backup:

```powershell
git add .
git commit -m "Backup prima sessione YYYY-MM-DD"
git tag backup-YYYY-MM-DD-prima-sessione
```

## Modifiche sperimentali

```powershell
git checkout -b codex/nome-modifica
```

## Fine sessione

```powershell
git status
git add .
git commit -m "Descrizione breve della modifica"
```

## Ripristino di emergenza

Per tornare al punto iniziale salvato:

```powershell
git switch master
git restore .
```

Per ispezionare i punti salvati:

```powershell
git log --oneline --decorate --all
git tag
```
