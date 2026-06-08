# 📚 Kindle to Searchable PDF

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

Cattura in automatico le pagine di **Kindle per PC** e le trasforma in un **PDF con testo ricercabile** (OCR). Ideale per creare copie digitali leggibili da ChatGPT, Claude e altri strumenti AI.

> 💡 **Funziona anche con altre app a schermo intero** che si sfogliano con la freccia destra (→): lettori PDF, Calibre, presentazioni PowerPoint, flipbook online.

---

## ✨ Cosa fa

- 📸 **Cattura automatica** delle pagine (screenshot uno dopo l'altro)
- 🏁 **Si ferma da sola a fine libro** — non devi sapere quante pagine ha il libro
- 🔍 **Testo OCR invisibile** → il PDF diventa ricercabile e leggibile dall'AI
- 🌍 **Multilingua**: italiano, inglese, francese, tedesco, spagnolo, portoghese

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

## ⚖️ Note legali

**Usa solo per:** backup personali di ebook **che hai acquistato**, contenuti di pubblico dominio, materiale tuo.

Lo strumento fa **screenshot** — non rimuove e non aggira il DRM. Sei responsabile del rispetto del copyright.

---

## 📝 Licenza

MIT — vedi [LICENSE](LICENSE)

---

**Fatto con ❤️ da Jos di [IeXa Academy](https://www.iexa.it)**
