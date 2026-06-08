# 📚 Kindle to Searchable PDF

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

Automate screenshot capture from Kindle for PC and convert to searchable PDF with OCR. Creates AI-ready PDFs with invisible text layer for ChatGPT, Claude, and other AI assistants.

> 📖 **New user?** See [QUICK_START.md](QUICK_START.md) for beginner-friendly guide.

---

> 💡 **Works with more than just Kindle!**
> 
> This tool captures **any fullscreen application** that navigates with arrow keys:
> - 📱 Kindle for PC, Calibre, other ebook readers
> - 📄 PDF viewers (Adobe, Foxit, browser PDF view)
> - 📊 PowerPoint presentations
> - 🌐 Online book readers, flipbooks, web documents
> 
> **Requirements:** Fullscreen mode (F11) + Right arrow (→) to turn pages

---

## 👀 Preview

### Web Interface

Clean, modern UI with simple controls:

```
┌─────────────────────────────────────────────────────────┐
│ 📚 Kindle to Searchable PDF                            │
├─────────────────────────────────────────────────────────┤
│ System Status                                           │
│ ✅ OCR Ready: Tesseract and Ghostscript found!         │
├─────────────────────────────────────────────────────────┤
│ ⚙️ Capture Settings                                    │
│                                                         │
│ 📖 Number of Pages (max): [━━━━━━●] 1000             │
│ ⏱️ Delay Between Pages: [━━●━━] 2.0s                  │
│ 🏁 Auto-stop at end of book: ☑️                       │
│                                                         │
│ 🔍 OCR Settings                                        │
│ ☑️ Enable OCR (Searchable PDF)                        │
│ Language: [Italian ▼]                                  │
│                                                         │
│         [ 🚀 Start Capture ]                           │
│                                                         │
├─────────────────────────────────────────────────────────┤
│ 📊 Status & Results                                    │
│                                                         │
│ Click 'Start Capture' to begin...                      │
│                                                         │
│         [ 📄 Download PDF ]                            │
└─────────────────────────────────────────────────────────┘
```

### Terminal Output Example

```bash
$ .\.venv\Scripts\activate
$ python app.py

============================================================
  📚 KINDLE TO PDF OCR - WEB INTERFACE
============================================================

🚀 Starting server on port 7861...

⚠️  If browser doesn't open automatically:
   👉 CLICK THIS LINK: http://127.0.0.1:7861

💡 Keep this window open while using the app!
============================================================

* Running on local URL:  http://127.0.0.1:7861

📸 Pagina 1 catturata
📸 Pagina 2 catturata
📸 Pagina 3 catturata
   ... (keeps going until the book ends) ...
📸 Pagina 186 catturata
📸 Pagina 187 catturata
⏸️  Pagina invariata (1/3) — probabile fine libro
⏸️  Pagina invariata (2/3) — probabile fine libro
⏸️  Pagina invariata (3/3) — probabile fine libro

🏁 Fine libro rilevata: la pagina non cambia più → STOP automatico.

✅ CATTURA COMPLETATA - 187 pagine

📄 Creazione PDF base...
✅ PDF base creato: ebook_20260101_124609_base.pdf (0.94 MB)

🔍 Aggiunta layer OCR al PDF...
🔍 Esecuzione OCR (lingua: ita)...

Scanning contents     ████████████████████ 100% 5/5
OCR                   ████████████████████ 100% 5/5
PDF/A conversion      ████████████████████ 100% 5/5
Linearizing           ████████████████████ 100% 100/100

✅ PDF SEARCHABLE CREATO!
📄 File: ebook_20260101_124609_searchable.pdf
📦 Dimensione: 0.95 MB

💡 Ora gli AI agent possono leggere il testo del libro!
```

---

## 🎯 Features

- **Automated Capture** - PyAutoGUI screenshots Kindle pages
- **🏁 Auto-Stop at End of Book** - Detects when pages stop changing and stops on its own — no need to count the book's pages
- **OCR Text Layer** - Invisible searchable text via Tesseract
- **Dual Interface** - Web UI (Gradio) or CLI
- **Multi-language** - Italian, English, French, German, Spanish, Portuguese
- **AI-Ready** - Perfect for ChatGPT, Claude analysis

---

## 🚀 Installation

### Prerequisites

- Python 3.10+
- Kindle for PC
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) (with language packs)
- [Ghostscript](https://ghostscript.com/releases/gsdnld.html)

### One-Time Setup

```bash
# 1. Clone
git clone https://github.com/josscit/kindle-pdf-ocr.git
cd kindle-pdf-ocr

# 2. Create virtual environment
python -m venv .venv

# 3. Activate
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/Mac

# 4. Install dependencies
pip install -r requirements.txt

# 5. Install Tesseract + Ghostscript manually (see links above)
```

---

## 💻 Usage

### Every Time

```bash
# Activate environment
.venv\Scripts\activate

# Run Web UI
python app.py
```

Browser opens automatically at `http://127.0.0.1:7861`

> 💡 **Note:** If port 7861 is busy, the app automatically tries port 7862. If browser doesn't open, click the link shown in terminal or manually navigate to the displayed URL.

**Or run CLI:**
```bash
python kindle_auto_pdf_ocr.py
```

---

## 🎨 Web UI Workflow

1. **Configure:** Leave **Number of Pages** high (it's just a safety cap) and keep **Auto-stop** enabled, then pick delay and OCR language
2. **Click "Start Capture"**
3. **10-second countdown:**
   - Open Kindle in fullscreen (F11)
   - Go to first page
   - Minimize browser
   - Click Kindle window
4. **Auto-capture** runs
5. **Download PDF**

---

## 📖 Kindle Settings for Best OCR

OCR accuracy depends on how the page looks on screen. Open Kindle's **Aa** menu and set:

| Setting | Recommended | Why |
|---------|-------------|-----|
| **Color mode** | **White** (black text on white) | Tesseract is trained on dark text / light background. Dark and sepia modes lower accuracy. |
| **Font size** | **Larger** | Bigger characters = more pixels per letter = more accurate OCR. With auto-stop the extra screenshots are no problem. |
| **Page width** | **Narrower** | Cleaner layout, less text crammed per screen. |

> 💡 **Why the page counter jumps by 2 or 3:** with a small font + wide page, one screen shows the text of 2–3 print pages at once, so Kindle's "Page X of Y" counter advances by more than 1 per turn. This is exactly why matching the page count never worked reliably — and why **auto-stop** (which just detects the end of the book) is the robust solution.

---

## 🔧 Architecture

```
Kindle (F11) → PyAutoGUI → Screenshots → img2pdf → Base PDF
                                              ↓
                                          OCRmyPDF + Tesseract
                                              ↓
                                      Searchable PDF
```

**PDF Contains:**
- Visual layer: Original screenshots
- Text layer: Invisible OCR text (for AI/search)

---

## 📁 Output

```
screenshots/
└── YYYYMMDD_HHMMSS/
    ├── raw/
    │   └── page_0001.png, page_0002.png, ...
    └── ebook_YYYYMMDD_HHMMSS_searchable.pdf
```

---

## ⚙️ Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| Pages (max) | 1000 | Upper limit — with auto-stop, capture ends earlier at the end of the book |
| Auto-stop | Enabled | Stops automatically when the page stops changing (end of book) |
| Delay | 2.0s | Wait between pages |
| OCR | Enabled | Searchable text |
| Language | ita | OCR language |

**Supported languages:** ita, eng, fra, deu, spa, por

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'gradio'"

Virtual environment not activated or dependencies not installed.

**Fix:**
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

### "Tesseract not found"

Tesseract not installed or language pack missing.

**Fix:** Install Tesseract with your language pack. Script auto-detects common paths.

### "Ghostscript not found"

**Fix:** Install Ghostscript. Script finds all versions automatically.

### "Cannot find empty port: 7861-7861"

Previous instance still running.

**Fix:** Close browser and PowerShell, wait 10 seconds, restart.

### Poor text quality

**Normal behavior.** Screenshot quality limited by screen resolution (~160 DPI). Readable but not print-quality.

> 💡 For noticeably better OCR, set Kindle's **Color mode → White** and a **larger font** (see *Kindle Settings for Best OCR* above).

### Capture stops too early / too late

Auto-stop ends capture when **3 consecutive screens are identical**. If pages load slowly, raise the **Delay** so each page finishes rendering before the next screenshot. To disable end-of-book detection entirely, uncheck **Auto-stop** and set the exact page count.

### Black screenshots / new Kindle app

Amazon is retiring the **legacy "Kindle for PC"** on **June 30, 2026** in favor of a new Microsoft Store app with stricter DRM that **may block screen capture** (screenshots come out black). If your captures turn black after switching apps, that's why — test a few pages first.

---

## 🔐 Legal

**Permitted:**
✅ Personal backups of purchased ebooks  
✅ Public domain content  
✅ Your own content  

**Not permitted:**
❌ DRM circumvention  
❌ Sharing copyrighted material  
❌ Commercial use without rights  

**This tool screenshots - doesn't decrypt or remove DRM. Users responsible for copyright compliance.**

---

## 📘 Technical Notes

<details>
<summary><b>How Dependency Detection Works</b></summary>

### Auto-Finding Tesseract & Ghostscript

Even if not in system PATH, script searches common install locations:

```python
def ensure_programs_in_path() -> None:
    # Tesseract
    tesseract_paths = [
        r"C:\Program Files\Tesseract-OCR",
        r"C:\Program Files (x86)\Tesseract-OCR"
    ]
    
    # Ghostscript (all versions)
    gs_base = r"C:\Program Files\gs"
    gs_versions = sorted(Path(gs_base).glob("gs*/bin"), reverse=True)
    
    # Adds to os.environ["PATH"] at runtime
```

**Key:** Modifies PATH only for this process, not system-wide.

</details>

<details>
<summary><b>Virtual Environment Explained</b></summary>

### What is `.venv`?

Isolated Python installation with its own packages.

**Why?**
- Avoids conflicts with system Python
- Each project has its own dependencies
- Can delete/recreate without breaking other projects

**Structure:**
```
.venv/
├── Scripts/
│   ├── python.exe   # Isolated Python
│   ├── activate     # Activation script
└── Lib/
    └── site-packages/  # Packages (gradio, etc.)
```

**Activation** temporarily modifies PATH to use `.venv/Scripts/python.exe`

</details>

---

## 🤝 Contributing

Pull requests welcome!

---

## 📝 License

MIT - See [LICENSE](LICENSE)

---

**Made with ❤️ by Jos from [IeXa Academy](https://www.iexa.it)**
