# 📚 Kindle to Searchable PDF

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

Automate screenshot capture from Kindle for PC and convert to searchable PDF with OCR. Creates AI-ready PDFs with invisible text layer for ChatGPT, Claude, and other AI assistants.

> 📖 **New user?** See [QUICK_START.md](QUICK_START.md) for beginner-friendly guide.

---

## 🎯 Features

- **Automated Capture** - PyAutoGUI screenshots Kindle pages
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

Browser opens at `http://127.0.0.1:7861`

**Or run CLI:**
```bash
python kindle_auto_pdf_ocr.py
```

---

## 🎨 Web UI Workflow

1. **Configure:** Pages, delay, OCR language
2. **Click "Start Capture"**
3. **10-second countdown:**
   - Open Kindle in fullscreen (F11)
   - Go to first page
   - Minimize browser
   - Click Kindle window
4. **Auto-capture** runs
5. **Download PDF**

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
| Pages | 5 | Number to capture |
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
