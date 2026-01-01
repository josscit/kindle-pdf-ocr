# 📚 Kindle to Searchable PDF

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

Automate screenshot capture from Kindle for PC and convert to searchable PDF with OCR. Creates AI-ready PDFs with invisible text layer for ChatGPT, Claude, and other AI tools.

---

## 🎯 Features

- **Automated Screenshot Capture** - Captures pages from Kindle for PC via PyAutoGUI
- **OCR Text Layer** - Adds invisible searchable text with Tesseract OCR
- **Multi-language Support** - Italian, English, French, German, Spanish, Portuguese
- **Dual Interface** - Web UI (Gradio) or CLI
- **AI-Ready Output** - PDF contains both images and searchable text

---

## 🚀 Quick Start

### For End Users (Non-Technical)

📖 **[See QUICK_START.md →](QUICK_START.md)** for step-by-step beginner-friendly guide.

### For Developers

```bash
# Clone repository
git clone https://github.com/josscit/kindle-pdf-ocr
cd kindle-pdf-ocr

# Create virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install external dependencies (manual)
# - Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki
# - Ghostscript: https://ghostscript.com/releases/gsdnld.html

# Run Web UI
python app.py

# Or CLI
python kindle_auto_pdf_ocr.py
```

---

## 📋 Requirements

### Python Packages
```
pyautogui==0.9.54
pillow==10.4.0
numpy==1.26.4
img2pdf==0.5.1
ocrmypdf==16.13.0
gradio>=5.0.0
```

### External Dependencies
- **Tesseract OCR** - Text recognition engine
- **Ghostscript** - PDF processing
- **Kindle for PC** - Source application

---

## 💻 Usage

### Web UI (Recommended)

```bash
python app.py
```

Opens browser interface at `http://127.0.0.1:7861`

Features:
- Slider controls for pages and delay
- OCR toggle and language selection
- Real-time status updates
- Direct PDF download

### CLI

```bash
python kindle_auto_pdf_ocr.py
```

Interactive prompts for:
- Number of pages
- Delay between pages
- OCR enable/disable
- OCR language

---

## 🔧 How It Works

### Architecture

```
Kindle for PC (Fullscreen)
    ↓
PyAutoGUI (Screenshot capture)
    ↓
PIL (Image processing)
    ↓
img2pdf (Base PDF creation)
    ↓
OCRmyPDF + Tesseract (Text recognition)
    ↓
Searchable PDF (Images + invisible text layer)
```

### Script Workflow

1. **Countdown** - 10 seconds to prepare Kindle
2. **Capture Loop** - Screenshot → Press right arrow → Wait delay
3. **PDF Creation** - Combine images into PDF
4. **OCR Processing** - Add searchable text layer
5. **Output** - Save to `screenshots/[timestamp]/ebook_xxx_searchable.pdf`

### Tesseract/Ghostscript Detection

The script automatically finds Tesseract and Ghostscript:

```python
def ensure_programs_in_path():
    """Adds Tesseract and Ghostscript to PATH if found in common locations"""
    
    # Common Tesseract paths
    tesseract_paths = [
        r"C:\Program Files\Tesseract-OCR",
        r"C:\Program Files (x86)\Tesseract-OCR"
    ]
    
    # Common Ghostscript paths  
    gs_paths = [
        r"C:\Program Files\gs\gs10.03.1\bin",
        r"C:\Program Files\gs\gs10.04.0\bin"
    ]
    
    # Add to os.environ["PATH"] if found
    # Set TESSDATA_PREFIX for language data
```

If not in PATH, script searches common install locations and adds them to environment variables at runtime.

---

## 📁 Output Structure

```
screenshots/
└── YYYYMMDD_HHMMSS/
    ├── raw/
    │   ├── page_0001.png
    │   ├── page_0002.png
    │   └── ...
    └── ebook_YYYYMMDD_HHMMSS_searchable.pdf
```

---

## ⚙️ Configuration

### Capture Settings

| Parameter | Default | Description |
|-----------|---------|-------------|
| `num_pages` | 5 | Number of pages to capture |
| `delay` | 2.0s | Wait time between page turns |
| `auto_crop` | False | Auto-detect and remove margins |
| `use_ocr` | True | Enable OCR text layer |
| `ocr_language` | 'ita' | Tesseract language code |

### Supported OCR Languages

Tesseract must have the language data installed:
- `ita` - Italian
- `eng` - English  
- `fra` - French
- `deu` - German
- `spa` - Spanish
- `por` - Portuguese

Install additional languages: [tessdata repository](https://github.com/tesseract-ocr/tessdata)

---

## 🐛 Troubleshooting

### "Tesseract not found"

**Cause:** Tesseract not installed or not in PATH

**Solution:**
```bash
# Check if installed
tesseract --version

# If not found, install from:
# https://github.com/UB-Mannheim/tesseract/wiki

# Script will auto-detect common install paths
```

### "Ghostscript not found"

**Cause:** Ghostscript not installed

**Solution:**
```bash
# Check if installed
gswin64c --version  # Windows
gs --version        # Linux/Mac

# Install from:
# https://ghostscript.com/releases/gsdnld.html
```

### Poor text quality in PDF

**Expected behavior.** Screenshot quality depends on screen resolution (typically 1920x1080).

**Workarounds:**
- Use higher resolution display
- Accept quality trade-off (text is readable, not print-quality)
- This is inherent limitation of screenshot-based approach

### OCR fails or hangs

**Check:**
1. Both Tesseract AND Ghostscript installed?
2. Correct language data installed in Tesseract?
3. Sufficient disk space in output folder?

---

## 🔐 Legal & Ethics

### Appropriate Use

✅ **Permitted:**
- Personal backups of legally purchased ebooks
- Public domain content
- Content you have rights to

❌ **Not Permitted:**
- Circumventing DRM (this tool doesn't - it only screenshots)
- Distribution/sharing of copyrighted material
- Commercial use of captured content without rights

**This tool creates screenshots. It does not remove DRM or decrypt ebooks. Users are responsible for compliance with copyright laws and Terms of Service.**

---

## 🛠️ Development

### Project Structure

```
kindle-pdf-ocr/
├── app.py                      # Gradio web interface
├── kindle_auto_pdf_ocr.py      # CLI script and core logic
├── requirements.txt            # Python dependencies
├── README.md                   # Technical documentation (you are here)
├── QUICK_START.md             # Beginner-friendly guide
├── INSTALL_TESSERACT.md       # OCR setup instructions
└── LICENSE                     # MIT License
```

### Key Functions

**`capture_kindle_to_searchable_pdf()`**
- Main capture logic
- Parameters: pages, delay, OCR settings
- Returns: path to output folder

**`ensure_programs_in_path()`**
- Auto-detects Tesseract/Ghostscript
- Adds to PATH if found in common locations

**`images_to_pdf()`**
- Lossless PNG to PDF conversion via img2pdf

**`add_ocr_to_pdf()`**
- Adds searchable text layer via OCRmyPDF

---

## 📊 Performance

### Typical Metrics

- **Capture speed:** ~2-3 seconds per page (including OCR)
- **PDF size:** ~150-200 KB per page (1920x1080 screenshots)
- **OCR accuracy:** 95%+ for clear text
- **Memory usage:** ~500MB during OCR processing

### Optimization

For faster processing:
- Disable OCR (`use_ocr=False`) - creates image-only PDF
- Reduce screenshot delay (`delay=1.5`)
- Use SSD for output directory

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Test your changes
4. Submit a pull request

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

- **PyAutoGUI** - Screenshot and keyboard automation
- **Tesseract OCR** - Text recognition
- **OCRmyPDF** - PDF processing
- **Gradio** - Web interface
- **img2pdf** - Lossless PDF conversion

---

**Made with ❤️ by Jos from [IeXa Academy](https://www.iexa.it)**

*Built to help the AI community create searchable knowledge bases from their ebook collections.*
