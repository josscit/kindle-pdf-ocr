# 📚 Kindle to Searchable PDF

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

Automate screenshot capture from Kindle for PC and convert to searchable PDF with OCR. Creates AI-ready PDFs with invisible text layer for ChatGPT, Claude, and other AI assistants.

> 📖 **For non-technical users:** See [QUICK_START.md](QUICK_START.md) for beginner-friendly step-by-step guide.

---

## 🎯 Features

- **Automated Screenshot Capture** - PyAutoGUI captures Kindle pages automatically
- **OCR Text Layer** - Tesseract adds invisible searchable text
- **Dual Interface** - Web UI (Gradio) or CLI
- **Multi-language OCR** - Italian, English, French, German, Spanish, Portuguese
- **AI-Ready Output** - Searchable PDFs for AI agents

---

## 🚀 Quick Start for Developers

### One-Time Setup

```bash
# 1. Clone repository
git clone https://github.com/josscit/kindle-pdf-ocr.git
cd kindle-pdf-ocr

# 2. Create virtual environment
python -m venv .venv

# 3. Activate environment
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/Mac

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Install external tools (manual downloads)
# - Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki
# - Ghostscript: https://ghostscript.com/releases/gsdnld.html
```

### Every Time You Use It

**Method 1: Traditional (activate first)**
```bash
.venv\Scripts\activate
python app.py  # Web UI
```

**Method 2: With uv (no activation needed)**
```bash
uv run app.py  # Simpler!
```

---

## 💻 Usage

### Web UI (Recommended)

```bash
.venv\Scripts\activate
python app.py
```

Opens browser at `http://127.0.0.1:7861` with graphical interface.

**Workflow:**
1. Configure: pages, delay, OCR language
2. Click "Start Capture"
3. Prepare Kindle (10 second countdown)
4. Auto-capture runs
5. Download PDF

### CLI

```bash
.venv\Scripts\activate
python kindle_auto_pdf_ocr.py
```

Interactive prompts for all settings.

---

## 🔧 How It Works

### Technical Flow

```
1. PyAutoGUI captures fullscreen screenshot
2. Saves as PNG with 300 DPI metadata
3. Presses right arrow key
4. Waits specified delay
5. Repeats for all pages
6. img2pdf combines PNGs → base PDF (lossless)
7. OCRmyPDF + Tesseract adds text layer
8. Output: Searchable PDF
```

### Dependency Detection

**Tesseract & Ghostscript Auto-Discovery:**

```python
def ensure_programs_in_path() -> None:
    # Searches common paths
    tesseract_paths = [
        r"C:\Program Files\Tesseract-OCR",
        r"C:\Program Files (x86)\Tesseract-OCR"
    ]
    
    # Dynamically finds ALL Ghostscript versions
    gs_base_paths = [r"C:\Program Files\gs", ...]
    gs_versions = sorted(Path(gs_base).glob("gs*/bin"), reverse=True)
    
    # Modifies os.environ["PATH"] at runtime
    # Sets TESSDATA_PREFIX for language data
```

Script modifies `os.environ["PATH"]` only for its own process - not system-wide.

---

## 📁 Output

```
screenshots/
└── 20260101_115732/
    ├── raw/
    │   └── page_0001.png, page_0002.png, ...
    └── ebook_20260101_115732_searchable.pdf
```

**PDF Structure:**
- **Visual layer:** Original Kindle screenshots
- **Text layer:** Invisible OCR text (for search and AI)

---

## 🐛 Troubleshooting

### "ModuleNotFoundError"

**Problem:** Dependencies not installed or wrong Python environment

**Solution:**
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

### "Tesseract not found"

**Problem:** Tesseract not installed or language data missing

**Check:**
```bash
tesseract --version
tesseract --list-langs  # Should show 'ita' or your language
```

**Fix:** Install Tesseract with language packs. Script auto-detects common paths.

### "Ghostscript not found"

**Problem:** Ghostscript not installed

**Check:**
```bash
gswin64c --version  # Windows
gs --version        # Linux/Mac
```

**Fix:** Install Ghostscript. Script finds all versions dynamically.

### "Cannot find empty port"

**Problem:** Port 7861 already in use

**Solutions:**
1. Close previous app.py instance
2. Wait 10 seconds and retry
3. Change port in `app.py`: `server_port=7862`

### Poor Quality PDF

**Expected limitation.** Screenshot-based capture is resolution-limited (typically 1920x1080 → ~160 DPI for full page).

**Acceptable for:** AI analysis, personal reading  
**Not suitable for:** Print, professional publication  

---

## 📘 Technical Details

<details>
<summary><b>Virtual Environments: <code>.venv</code> vs <code>env</code></b></summary>

### What is a Virtual Environment?

Isolated Python installation with its own packages, independent of system Python.

### Why Use One?

- **Isolation:** Project dependencies don't conflict with system or other projects
- **Reproducibility:** Same environment on any machine
- **Clean:** Can delete and recreate without affecting system

### Naming Conventions

**`.venv`** (this project uses this)
- Modern Python convention (PEP 518)
- Hidden folder (starts with dot)
- Auto-detected by modern tools (uv, poetry, etc.)

**`env`** or `venv`
- Older convention
- Visible folder
- Still widely used

### Directory Structure

```
.venv/
├── Scripts/              # Windows
│   ├── python.exe        # Isolated interpreter
│   ├── pip.exe           # Package installer
│   └── activate          # Activation script
├── Lib/
│   └── site-packages/    # Installed packages
└── pyvenv.cfg            # Configuration
```

### Activation Explained

**Before activation:**
```bash
which python  # → C:\Python311\python.exe (system)
```

**After activation:**
```bash
.venv\Scripts\activate
which python  # → C:\...\kindle-pdf-ocr\.venv\Scripts\python.exe
```

Activation modifies:
- `PATH` environment variable
- `VIRTUAL_ENV` variable
- Shell prompt (adds `(venv)` prefix)

**All subsequent `python` and `pip` commands use the virtual environment.**

</details>

<details>
<summary><b>What is <code>uv</code> and Why Use It?</b></summary>

### The Problem

Traditional workflow:
```bash
python -m venv .venv          # Create env
.venv\Scripts\activate        # Activate
pip install -r requirements.txt  # Install deps
python app.py                 # Run script
```

**Every. Single. Time.** you open a new terminal session.

### The Solution: uv

[uv](https://github.com/astral-sh/uv) is a fast Python package manager (written in Rust).

**With uv:**
```bash
uv run app.py
```

Done. One command.

### What uv Does Automatically

1. **Finds `.venv`** - Auto-detects virtual environment
2. **Activates it** - No manual activation needed
3. **Installs missing packages** - Reads `requirements.txt`
4. **Runs script** - Executes in correct environment

### Installation

**Windows (PowerShell):**
```powershell
powershell -Command "iwr https://astral.sh/uv/install.ps1 -useb | iex"
```

**Linux/Mac:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Speed Comparison

| Operation | pip | uv |
|-----------|-----|-----|
| Install 50 packages | 45s | 2s |
| Resolve dependencies | 15s | 0.5s |

**uv is 10-100x faster** than pip (written in Rust vs Python).

### Usage Examples

```bash
# Run script (auto-activates .venv)
uv run app.py

# Install package
uv pip install requests

# Create venv
uv venv

# Run with temp dependencies
uv run --with pandas script.py
```

### Why This Project Works With Both

**The code doesn't care** how you run it:
- `python app.py` after activation
- `uv run app.py` without activation

Both execute the same Python interpreter from `.venv`, just different invocation methods.

### Recommendation

**For end users:** Traditional activation (clearer what's happening)  
**For developers:** uv (faster, fewer commands)  

</details>

<details>
<summary><b>Port Management</b></summary>

### What is a Port?

Network "doorway" for applications to communicate. Web servers listen on ports:
- HTTP: port 80
- HTTPS: port 443
- Gradio default: port 7860

### Why Port Conflicts?

Only **one application** can listen on a port at a time.

If you run `python app.py` twice:
1. First instance: Opens port 7861 ✅
2. Second instance: Port 7861 busy ❌

### How This App Handles It

```python
# app.py, line 195
demo.launch(
    server_port=7861,  # Fixed port
    ...
)
```

If port busy, Gradio throws `OSError`.

### Solutions

**1. Kill existing process:**
```bash
# Windows
netstat -ano | findstr :7861
taskkill /PID <number> /F

# Linux/Mac
lsof -ti:7861 | xargs kill -9
```

**2. Change port:**
```python
demo.launch(server_port=7862)  # Or any free port
```

**3. Auto-assign:**
```python
demo.launch(server_port=0)  # Gradio picks free port
```

</details>

---

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- [ ] Add progress bar to CLI
- [ ] Support for Kindle Cloud Reader (browser-based)
- [ ] Batch processing multiple books
- [ ] GUI desktop app (PyQt/Tkinter)

---

## 📝 License

MIT License - See [LICENSE](LICENSE)

---

## 🙏 Credits

Built with:
- [PyAutoGUI](https://pyautogui.readthedocs.io/) - Automation
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - Text recognition
- [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) - PDF processing
- [Gradio](https://gradio.app/) - Web interface
- [img2pdf](https://gitlab.mister-muffin.de/josch/img2pdf) - PDF conversion

---

**Made with ❤️ by Jos from [IeXa Academy](https://www.iexa.it)**

*Built to help the AI community create searchable knowledge bases from their ebook collections.*
