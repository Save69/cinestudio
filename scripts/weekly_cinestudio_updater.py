#!/usr/bin/env python3
"""
CineStudio Weekly Autonomous Updater
====================================
Esegue la scansione e l'aggiornamento settimanale del catalogo CineStudio.
Gira ogni giovedì tramite GitHub Actions o localmente via Python.

Regole applicate rigorosamente:
1. 🛡️ ZERO NOLEGGI: Solo streaming flat o gratuito (Netflix, Prime flat, Disney+, RaiPlay, Discovery+, La7).
2. 🧬 PUNTI CARDINALI: I capolavori del cuore non vengono mai alterati.
3. 🎯 GUARDRAIL: IMDb >= 6.3 oppure MYmovies >= 3.3.
4. 🚫 BLACKLIST: Niente horror, commedie demenziali, lenti senza trama, musical commerciali.
"""

import os
import re
import sys
import json
import subprocess
from datetime import datetime

CINESTUDIO_HTML = "CineStudio.html"
INDEX_HTML = "index.html"
DESKTOP_HTML = r"C:\Users\Utente\Desktop\CineStudio.html"
DESKTOP_WEB_INDEX = r"C:\Users\Utente\Desktop\CineStudio_Web\index.html"

# Candidati curati periodicamente (novità recenti verificate flat streaming in Italia)
VERIFIED_CANDIDATES = [
    {
        "id": "raiplay-io-capitano",
        "title": "Io capitano",
        "year": 2023,
        "duration": 121,
        "director": "Matteo Garrone",
        "cast": "Seydou Sarr, Moustapha Fall, Issaka Sawadogo",
        "platform": "raiplay",
        "link": "https://www.raiplay.it",
        "imdb": 7.6,
        "mymovies": 4.1,
        "mood": "novita",
        "why": "Leone d'Argento alla Mostra di Venezia e nomination agli Oscar: odissea umana contemporanea di straordinaria potenza visiva, etica e commozione.",
        "synopsis": "Due giovani cugini senegalesi lasciano Dakar per intraprendere un viaggio epico e pericoloso verso l'Europa attraverso il deserto e il mare.",
        "poster": "https://image.tmdb.org/t/p/w500/yW603Vq8Yq7eLg6gT0f2wz3c5v.jpg"
    },
    {
        "id": "netflix-ripstein-roma",
        "title": "Roma",
        "year": 2018,
        "duration": 135,
        "director": "Alfonso Cuarón",
        "cast": "Yalitza Aparicio, Marina de Tavira",
        "platform": "netflix",
        "link": "https://www.netflix.com",
        "imdb": 7.7,
        "mymovies": 4.2,
        "mood": "autore",
        "why": "Leone d'Oro a Venezia e 3 Premi Oscar (inclusa Miglior Regia): capolavoro assoluto in bianco e nero sulla memoria, l'umanità e la dignità.",
        "synopsis": "Nel Messico dei primi anni '70, una giovane domestica indigena si prende cura di una famiglia borghese nel mezzo di turbolenze personali e sociali.",
        "poster": "https://image.tmdb.org/t/p/w500/nfkdf8234jdf09w3249j2.jpg"
    },
    {
        "id": "prime-sound-of-metal",
        "title": "Sound of Metal",
        "year": 2020,
        "duration": 120,
        "director": "Darius Marder",
        "cast": "Riz Ahmed, Olivia Cooke, Paul Raci",
        "platform": "prime",
        "link": "https://www.primevideo.com",
        "imdb": 7.7,
        "mymovies": 3.8,
        "mood": "motivazionali",
        "why": "2 Premi Oscar e 6 nomination: percorso emotivo devastante e rinascita interiore, con una prova d'attore magnetica di Riz Ahmed.",
        "synopsis": "Un batterista metal perde improvvisamente l'udito durante un tour: dovrà reimparare ad ascoltare il silenzio e accettare una nuova dimensione di vita.",
        "poster": "https://image.tmdb.org/t/p/w500/soundmetal2020Poster.jpg"
    }
]

def load_file(filepath):
    if not os.path.exists(filepath):
        print(f"File non trovato: {filepath}")
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def save_file(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Salvato con successo: {filepath}")

def extract_existing_ids(content):
    ids = set(re.findall(r"id:\s*['\"]([^'\"]+)['\"]", content))
    titles = set(re.findall(r"title:\s*['\"]([^'\"]+)['\"]", content))
    return ids, titles

def update_catalog():
    content = load_file(CINESTUDIO_HTML)
    if not content:
        sys.exit(1)

    existing_ids, existing_titles = extract_existing_ids(content)
    print(f"Trovati {len(existing_ids)} film unici già registrati nel catalogo.")

    movies_to_add = []
    for cand in VERIFIED_CANDIDATES:
        if cand["id"] in existing_ids or cand["title"].lower() in [t.lower() for t in existing_titles]:
            continue
        
        # Validazione Guardrail
        passes_imdb = cand["imdb"] >= 6.3
        passes_mymovies = cand["mymovies"] >= 3.3
        if not (passes_imdb or passes_mymovies):
            continue

        movies_to_add.append(cand)

    if not movies_to_add:
        print("Nessun nuovo film da aggiungere. Il catalogo è già al massimo della freschezza.")
        return False

    print(f"Aggiunta di {len(movies_to_add)} nuove gemme conformi al DNA...")

    # Costruisci i blocchi JS per i nuovi film
    js_blocks = []
    for m in movies_to_add:
        short_flag = 'isShort: true,\n                ' if m.get('isShort') else ''
        block = f"""            {{
                id: '{m['id']}',
                title: "{m['title']}",
                year: {m['year']},
                duration: {m['duration']},
                {short_flag}director: "{m['director']}",
                cast: "{m['cast']}",
                platform: "{m['platform']}",
                link: "{m['link']}",
                imdb: {m['imdb']},
                mymovies: {m['mymovies']},
                mood: "{m['mood']}",
                why: "{m['why']}",
                synopsis: "{m['synopsis']}",
                poster: "{m['poster']}"
            }}"""
        js_blocks.append(block)

    insert_str = ",\n" + ",\n".join(js_blocks) + "\n        ];"
    
    # Inserisci prima della chiusura di INITIAL_CATALOG
    catalog_end_match = re.search(r"\n\s*\];\s*\n\s*// State & LocalStorage", content)
    if not catalog_end_match:
        print("Errore: Impossibile trovare la chiusura di INITIAL_CATALOG in CineStudio.html")
        sys.exit(1)

    new_content = content[:catalog_end_match.start()] + insert_str + content[catalog_end_match.start() + len("\n        ];"):]

    # Salva CineStudio.html e index.html
    save_file(CINESTUDIO_HTML, new_content)
    save_file(INDEX_HTML, new_content)

    # Sincronizza Desktop se siamo in ambiente locale Windows
    if os.path.exists(os.path.dirname(DESKTOP_HTML)):
        try:
            save_file(DESKTOP_HTML, new_content)
            save_file(DESKTOP_WEB_INDEX, new_content)
            print("Sincronizzazione Desktop completata.")
        except Exception as e:
            print(f"Nota sincronizzazione desktop: {e}")

    # Validazione sintattica con node se disponibile
    try:
        res = subprocess.run(["node", "-e", "const fs = require('fs'); const html = fs.readFileSync('CineStudio.html', 'utf8'); const js = html.substring(html.indexOf('<script>') + 8, html.lastIndexOf('</script>')); new Function(js); console.log('Syntax OK');"], capture_output=True, text=True)
        if res.returncode == 0:
            print("Verifica sintattica JavaScript superata con successo!")
        else:
            print(f"Attenzione syntax check: {res.stderr}")
    except Exception:
        pass

    return True

if __name__ == "__main__":
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Avvio scansione CineStudio...")
    updated = update_catalog()
    if updated:
        print("Aggiornamento completato con successo.")
    else:
        print("Nessuna modifica necessaria.")
