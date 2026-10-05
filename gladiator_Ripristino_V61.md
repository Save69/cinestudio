# CineStudio V61: Protocollo Settimanale Giovedì & Ricalibrazione Qualità

## Data: 05 Ottobre 2026
**Agente**: Antigravity  
**Cartella di Lavoro**: `C:\Users\Utente\Documents\Agente studio`

---

## 1. Obiettivo della Sessione
1. **Ricalibrazione Preset di Qualità**: Risolto il disallineamento tra Standard e Scelta Ampia, garantendo scalini qualitativi distinti e differenze numeriche reali nel catalogo.
2. **Implementazione Diretta del Prompt di Controllo Settimanale (Giovedì)**:
   > *"Esegui il controllo settimanale di CineStudio sui 6 cataloghi (Netflix, Prime, Disney+, RaiPlay, La7, Discovery+). Procedi con calma e verifica live su JustWatch Italia ogni singolo titolo. Se un film non è incluso al 100% in abbonamento flat gratuito, eliminalo o spostalo nel Radar. Preferisco avere 10 film in meno ma la certezza assoluta di zero costi extra."*

---

## 2. Modifiche Architetturali e Operative

### A. Ricalibrazione Soglie di Qualità in `CineStudio.html`
- **🌟 Capolavori (7.7+)**: IMDb $\ge$ 7.7 / MYmovies $\ge$ 4.0 $\rightarrow$ **51 film** (26 film serali $\le$ 2h).
- **🎯 Alta Qualità (7.2+) [Default]**: IMDb $\ge$ 7.2 / MYmovies $\ge$ 3.6 $\rightarrow$ **74 film** (39 film serali $\le$ 2h).
- **🌐 Scelta Ampia (6.8+)**: IMDb $\ge$ 6.8 / MYmovies $\ge$ 3.3 $\rightarrow$ **91 film** (+17 film rispetto ad Alta Qualità!).
- **✨ Tutto il Catalogo**: Qualsiasi voto $\rightarrow$ **95 film** (54 film serali $\le$ 2h).
- Migrazione automatica delle impostazioni obsolete (`6.3 / 3.3`) salvate nel `localStorage` dei browser.

### B. Integrazione Permanente del Prompt di Controllo Settimanale
1. **Nel sorgente di `CineStudio.html`**:
   - Inserito come banner di intestazione mandatorio in cima al tag `<script>`, vincolante per qualsiasi assistente o agente.
2. **Nell'Interfaccia Utente (`modal-dna`)**:
   - Creato il riquadro dedicato con il prompt esatto e il pulsante rapido `[📋 Copia Prompt]`.
3. **In `REGOLE_LAVORO.md`**:
   - Aggiunta la sezione ufficiale con la direttiva `Precisione (Voto 10) > Velocità (Voto 1)`.

---

## 3. File Sincronizzati e Pubblicati
- `C:\Users\Utente\Documents\Agente studio\CineStudio.html`
- `C:\Users\Utente\Documents\Agente studio\index.html`
- `C:\Users\Utente\Desktop\CineStudio.html`
- `C:\Users\Utente\Desktop\CineStudio_Web\index.html`
- `REGOLE_LAVORO.md`
- Live su GitHub Pages: `https://save69.github.io/cinestudio/`
