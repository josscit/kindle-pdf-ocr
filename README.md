# 📚 Kindle to Searchable PDF

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

Cattura in automatico le pagine di **Kindle per PC** e le trasforma in un **PDF con testo ricercabile** (OCR). Ideale per creare copie digitali leggibili da ChatGPT, Claude e altri strumenti AI.

> 💡 Non è solo per Kindle: funziona con **molti altri lettori di ebook e PDF** (vedi sotto).

---

## ✨ Cosa fa

- 📸 **Cattura automatica** delle pagine (screenshot uno dopo l'altro)
- 🏁 **Si ferma da sola a fine libro** — non devi sapere quante pagine ha il libro
- 🔍 **Testo OCR invisibile** → il PDF diventa ricercabile e leggibile dall'AI
- 🌍 **Multilingua**: italiano, inglese, francese, tedesco, spagnolo, portoghese

---

## 📚 Funziona anche con altri lettori

Il programma non "conosce" Kindle: fa **screenshot dello schermo** e preme la **freccia destra (→)** per girare pagina. Quindi va con **qualsiasi app su Windows** che:

1. si mette a **schermo intero** (così cattura solo la pagina, senza barre)
2. gira pagina con la **freccia destra →**

Esempi compatibili:
- 📖 **Kindle per PC**
- 📚 Lettori ebook: **Calibre**, **Adobe Digital Editions**, **Thorium**
- 📄 Lettori PDF: **Adobe Acrobat**, **Foxit**, **SumatraPDF**, PDF aperto nel **browser**
- 📊 Presentazioni **PowerPoint/PDF**, **fumetti**, **flipbook** e lettori web

L'OCR lavora sugli screenshot, quindi è **indipendente dal lettore**.

> ⚠️ Eccezione: app con **DRM forte** (o la nuova app Kindle dal Microsoft Store) possono bloccare la cattura schermo → pagine nere.

---

## 📋 Cosa ti serve

| | Dove prenderlo |
|---|---|
| **Windows + Kindle per PC** | già installato |
| **Python 3.10+** | [python.org](https://www.python.org/downloads/) — spunta **"Add Python to PATH"** durante l'installazione |
| **Tesseract OCR** | [download](https://github.com/UB-Mannheim/tesseract/wiki) — spunta la **lingua italiana** |
| **Ghostscript** | [download](https://ghostscript.com/releases/gsdnld.html) |

---

## ⚙️ Installazione (una volta sola)

Apri **PowerShell** nella cartella del progetto e lancia questi due comandi:

```powershell
# 1. crea l'ambiente isolato
python -m venv .venv

# 2. installa le librerie (usando il Python del .venv)
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Poi installa **Tesseract** e **Ghostscript** dai link qui sopra. Fine.

---

## ▶️ Come si usa

**1. Avvia l'app** (sempre con il Python del `.venv`):

```powershell
.\.venv\Scripts\python.exe app.py
```

Si apre il browser su `http://127.0.0.1:7861`.

**2. Imposta le opzioni:**
- Scegli la **lingua OCR**
- Lascia **"Number of Pages"** alto e l'**Auto-stop** attivo → si ferma da solo a fine libro

**3. Clicca "🚀 Start Capture".** Hai **10 secondi** per:
- aprire Kindle a **schermo intero (F11)** sulla **prima pagina** da catturare
- minimizzare il browser e **cliccare sulla finestra di Kindle**

**4.** Le pagine si sfogliano da sole e il programma **si ferma quando il libro finisce**.

**5.** Scarica il PDF. 🎉

---

## 📖 Impostazioni Kindle per un OCR migliore

Nel menu **"Aa"** di Kindle imposta:

- **Modalità colore → Bianco** (testo nero su sfondo bianco). L'OCR è tarato così: il tema scuro o seppia peggiora il riconoscimento.
- **Carattere → più grande**. Lettere più grandi = più dettaglio = OCR più preciso. Con l'auto-stop gli screenshot in più non sono un problema.
- **Larghezza pagina → più stretta** per un'impaginazione più pulita.

> 💡 Con un **font piccolo + pagina larga**, una schermata contiene il testo di 2-3 pagine cartacee (il contatore "Pagina X di Y" scatta di 2 o 3 alla volta). È per questo che far coincidere il numero di pagine non funzionava mai: l'**auto-stop**, che rileva semplicemente la fine del libro, è la soluzione affidabile.

---

## 🆘 Problemi comuni

| Problema | Soluzione |
|---|---|
| `No module named 'gradio'` / `'pyautogui'` | Stai usando il Python sbagliato. Usa **sempre** `.\.venv\Scripts\python.exe ...` |
| `Tesseract not found` | Installa Tesseract con il pacchetto della lingua |
| `Ghostscript not found` | Installa Ghostscript |
| Porta `7861` occupata | L'app prova da sola la `7862`: usa il link mostrato nel terminale |
| Testo un po' sfocato nel PDF | Normale (dipende dalla risoluzione dello schermo): resta leggibile e perfetto per l'AI |
| Screenshot **neri** | La nuova app Kindle dal Microsoft Store (la vecchia "Kindle per PC" chiude il **30/06/2026**) ha un DRM più restrittivo che può bloccare la cattura schermo. Prova prima su poche pagine. |

---

## 📂 Approfondimenti (facoltativi)

<details>
<summary><b>📘 Guida passo-passo per chi parte da zero</b></summary>

<br>

**1. Installa Python**
- Vai su [python.org/downloads](https://www.python.org/downloads/) e scarica Python 3.12
- ⚠️ Durante l'installazione **spunta "Add Python to PATH"**
- Verifica: apri il Prompt dei comandi e scrivi `python --version`

**2. Scarica il programma**
- Su [github.com/josscit/kindle-pdf-ocr](https://github.com/josscit/kindle-pdf-ocr): pulsante verde **"Code" → "Download ZIP"**
- Estrai la cartella (es. sul Desktop)

**3. Apri PowerShell nella cartella**
- Entra nella cartella, clicca sulla **barra dell'indirizzo** in alto, scrivi **powershell** e premi Invio

**4. Installa (una volta sola)**
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```
Poi installa Tesseract e Ghostscript (tendina qui sotto).

**5. Avvia, ogni volta**
```powershell
.\.venv\Scripts\python.exe app.py
```
Si apre il browser: configura, clicca **Start Capture** e prepara Kindle in 10 secondi.

</details>

<details>
<summary><b>🔤 Installare Tesseract e Ghostscript nel dettaglio</b></summary>

<br>

Servono due programmi: **Tesseract** (legge il testo) e **Ghostscript** (costruisce il PDF).

**Tesseract OCR**
- Installer: [release ufficiali](https://github.com/tesseract-ocr/tesseract/releases) — oppure [altre versioni](https://github.com/UB-Mannheim/tesseract/wiki)
- ⚠️ Durante l'installazione seleziona **"Additional language data" → Italian (ita)**
- Oppure con winget: `winget install UB-Mannheim.TesseractOCR`

**Ghostscript**
- Installer: [ghostscript.com/releases](https://ghostscript.com/releases/gsdnld.html)
- Oppure con winget: `winget install Ghostscript.Ghostscript`

**Verifica** (in un nuovo PowerShell):
```powershell
tesseract --version
gswin64c --version
```
Se compaiono le versioni è tutto a posto. Anche se danno "comando non trovato", **lo script li trova comunque da solo** nei percorsi standard.

</details>

<details>
<summary><b>❓ Cos'è il <code>.venv</code> e perché serve</b></summary>

<br>

Il `.venv` è un **ambiente isolato**: una copia di Python con le librerie di *questo* programma, separata dal Python di sistema, così non crea conflitti con altri progetti.

Per questo i comandi usano `.\.venv\Scripts\python.exe`: è il Python "giusto", quello che ha le librerie installate. Se usi il `python` di sistema ottieni l'errore `No module named ...`.

</details>

---

## ⚖️ Note legali

**Usa solo per:** backup personali di ebook **che hai acquistato**, contenuti di pubblico dominio, materiale tuo.

Lo strumento fa **screenshot** — non rimuove e non aggira il DRM. Sei responsabile del rispetto del copyright.

---

## 📝 Licenza

MIT — vedi [LICENSE](LICENSE)

---

**Fatto con ❤️ da Jos di [IeXa Academy](https://www.iexa.it)**
