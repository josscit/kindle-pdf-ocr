# 📚 Quick Start - Simple Guide

**Convert Kindle ebooks to searchable PDF - Easy guide for everyone!**

No technical knowledge needed! 😊

---

## 🎯 What This Does

Kindle book → Automatic screenshots → PDF with searchable text → AI tools can read it!

---

## 👀 What It Looks Like

### The Web Interface

When you run the program, you'll see a clean interface like this:

```
╔═══════════════════════════════════════════════════════╗
║  📚 Kindle to Searchable PDF                         ║
╠═══════════════════════════════════════════════════════╣
║  System Status                                        ║
║  ✅ OCR Ready: Tesseract and Ghostscript found!      ║
╠═══════════════════════════════════════════════════════╣
║  ⚙️ Capture Settings                                 ║
║                                                       ║
║  📖 Number of Pages: [━━━━●━] 5                     ║
║  ⏱️ Delay: [━━●━━] 2.0 seconds                      ║
║                                                       ║
║  🔍 OCR Settings                                     ║
║  ☑️ Enable OCR (Searchable PDF)                     ║
║  Language: [Italian ▼]                               ║
║                                                       ║
║            [ 🚀 Start Capture ]                      ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║  📊 Status & Results                                 ║
║                                                       ║
║  ✅ PDF Created Successfully!                        ║
║  📄 File: ebook_20260101_124609_searchable.pdf       ║
║  📦 Size: 0.95 MB                                    ║
║  🔍 PDF is searchable - AI agents can read it!       ║
║                                                       ║
║            [ 📄 Download PDF ]                       ║
╚═══════════════════════════════════════════════════════╝
```

### The Terminal Shows Progress

```
============================================================
  📚 KINDLE TO PDF OCR - WEB INTERFACE
============================================================

🚀 Starting server on port 7861...

⚠️  If browser doesn't open automatically:
   👉 CLICK THIS LINK: http://127.0.0.1:7861

💡 Keep this window open while using the app!
============================================================

* Running on local URL:  http://127.0.0.1:7861

📸 Pagina 1/5 catturata
📸 Pagina 2/5 catturata
📸 Pagina 3/5 catturata
📸 Pagina 4/5 catturata
📸 Pagina 5/5 catturata

✅ CATTURA COMPLETATA - 5 pagine

📄 Creazione PDF base...
✅ PDF base creato: ebook_20260101_124609_base.pdf

🔍 Aggiunta layer OCR al PDF...

Scanning contents     ████████████████████ 100% 5/5
OCR                   ████████████████████ 100% 5/5
PDF/A conversion      ████████████████████ 100% 5/5

✅ PDF SEARCHABLE CREATO!
📄 File: ebook_20260101_124609_searchable.pdf
📦 Dimensione: 0.95 MB

💡 Ora gli AI agent possono leggere il testo del libro!
```

**That's what you'll see while it works!** Pretty cool, right? 😊

---

## ⏱️ Time Required

- **Setup (first time only):** 20 minutes
- **Each use after:** 2 minutes to start + capture time

---

## 📦 PART 1: Setup (Do Once)

---

### ✅ **STEP 1: Install Python**

**What is it?** The "engine" that runs the program.

1. Go to **www.python.org/downloads**
2. Click yellow **"Download Python 3.12"** button
3. Run downloaded file
4. **⚠️ CRITICAL:** Check box **"Add Python to PATH"** ✓
5. Click **"Install Now"**
6. Wait 1-2 minutes

**Test it worked:**
- Press Windows key → Type **cmd** → Enter
- Type: `python --version`
- See "Python 3.12.x"? ✅ Good!
- See error? Go back and reinstall, check the PATH box!

---

### ✅ **STEP 2: Download Program**

1. Go to **github.com/josscit/kindle-pdf-ocr**
2. Click green **"<> Code"** button
3. Click **"Download ZIP"**
4. Go to **Downloads** folder
5. Right-click `kindle-pdf-ocr-main.zip` → **"Extract All"**
6. Extract to **Desktop**

**Result:** Folder `kindle-pdf-ocr-main` on your Desktop

---

### ✅ **STEP 3: Install Program Parts**

1. **Open the folder** `kindle-pdf-ocr-main`
2. **Open PowerShell:**
   - Click address bar at top
   - Type: **powershell**
   - Press Enter
   - Blue window opens

3. **Type these 3 commands** (press Enter after each):

**Command 1:**
```
python -m venv .venv
```
*Creates program space - wait 10 seconds*

**Command 2:**
```
.\.venv\Scripts\activate
```
*Activates space - you'll see `(.venv)` appear ✅*

**Command 3:**
```
pip install -r requirements.txt
```
*Installs components - wait 3-5 minutes, text scrolls*

**When cursor reappears:** Done! ✅

---

### ✅ **STEP 4: Install Tesseract**

**What is it?** Reads text from images.

1. **Download:** [Tesseract Installer](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.5.0.20250102.exe)
2. Run file
3. **⚠️ CRITICAL:** When asked about languages:
   - Check **"Additional language data (download)"** ✓
   - Check **"Italian"** ✓ (or your book's language)
4. Click **"Next"** until done

---

### ✅ **STEP 5: Install Ghostscript**

**What is it?** Builds the final PDF.

1. **Download:** [Ghostscript Installer](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10031/gs10031w64.exe)
2. Run file
3. Click **"Next"** → **"Install"** → **"Finish"**

---

## 🎉 Setup Complete!

**You're ready!** Now let's use it!

---

## 🚀 PART 2: Using the Program

**Choose Method 1 (graphical) or Method 2 (text-based):**

---

## 🎨 METHOD 1: With Interface (Recommended)

### **Every time you want a PDF:**

**Step 1: Start Program**

1. Open `kindle-pdf-ocr-main` folder
2. Click address bar → Type **powershell** → Enter
3. **Type 2 commands:**

```
.\.venv\Scripts\activate
```
*See `(.venv)` appear? Good!*

```
python app.py
```

**What happens:**
- PowerShell shows a link: `http://127.0.0.1:7861`
- Browser should open automatically
- If not, **CTRL+Click the link** or copy-paste it in your browser

> 💡 **Note:** If you see "port 7861 busy", the program automatically tries port 7862. Use the link shown in PowerShell!

---

**Step 2: Configure**

In the web page:
- **Number of Pages:** Slide to your number (e.g., 10)
- **Delay:** Leave at 2.0
- **Enable OCR:** Keep checked ✅
- **Language:** Select your book's language

---

**Step 3: Prepare Kindle**

Before clicking "Start Capture":
- Open **Kindle for PC**
- Open your book
- Press **F11** (fullscreen)
- Go to **first page**

---

**Step 4: Capture**

1. Click **"🚀 Start Capture"** button
2. **10 second countdown starts**
3. **Quick! Do this:**
   - Minimize browser (click on taskbar)
   - Click on Kindle window
4. **Don't touch anything!**
   - Pages turn automatically
   - Wait until done

---

**Step 5: Download**

1. Return to browser
2. See "✅ PDF Created Successfully!"
3. Click **"Download PDF"** button

**Done!** 🎉

---

## ⌨️ METHOD 2: Text-Based

For those who prefer command-line.

1. Open PowerShell in folder
2. Type:
```
.\.venv\Scripts\activate
python kindle_auto_pdf_ocr.py
```
3. Answer questions
4. Same capture process as Method 1
5. Find PDF in `screenshots\[date_time]\` folder

---

## 🆘 Problems?

### Can't activate (.venv not found)

**You skipped STEP 3!** Go back and create `.venv`:
```
python -m venv .venv
```

---

### "No module named 'gradio'"

**You didn't install components!** After activating:
```
pip install -r requirements.txt
```
Wait for it to finish!

---

### "Tesseract not found"

**Fix:** Install Tesseract (STEP 4) with Italian language pack!

---

### "Ghostscript not found"

**Fix:** Install Ghostscript (STEP 5)

---

### Browser doesn't open

**Normal!** Manually open browser and go to:
```
http://127.0.0.1:7861
```

---

### "Port already in use"

Previous program still running.

**Fix:** Close PowerShell, wait 10 seconds, start again.

---

### Blurry text in PDF

**This is normal!** Screenshot quality isn't perfect.
- Text is readable ✅
- AI can read it perfectly ✅
- Good enough for analysis!

---

## 💡 Tips

1. ✅ **Test first** - Try 3 pages before full book
2. ✅ **Fullscreen always** - Press F11 on Kindle
3. ✅ **No distractions** - Close popups/notifications
4. ✅ **Right language** - Match OCR to book language
5. ✅ **Keep PowerShell open** - Don't close while program runs

---

## ⏱️ How Long?

- 10 pages: ~3 minutes
- 50 pages: ~12 minutes
- 200 pages: ~45 minutes

Plan ahead! ☕

---

## ⚖️ Legal

**OK to use for:**
✅ Your purchased ebooks (personal backup)  
✅ Public domain books  
✅ Your own content  

**NOT OK:**
❌ Sharing PDFs  
❌ Selling PDFs  
❌ Copyright violation  

**This tool takes screenshots - doesn't hack DRM. You're responsible for legal use.**

---

## 📘 Technical Box (Optional Reading)

<details>
<summary><b>What is <code>.venv</code> and why activate?</b></summary>

### Simple Explanation

**`.venv`** = A "private box" for this program

When you did `python -m venv .venv`, Python created a hidden folder called `.venv` containing:
- Its own Python
- Its own packages (gradio, etc.)

### Why?

So this program doesn't mess with other Python programs on your PC!

### What Does "Activate" Mean?

When you type `.\.venv\Scripts\activate`:
- Windows temporarily says: "Use Python from THIS box"
- You see `(.venv)` at start of line to remind you
- All commands now use this private Python

### What if I Forget to Activate?

Python uses the "normal" system version, which doesn't have gradio → Error!

**Remember:** Always activate before running!

</details>

---

## ❓ Need Help?

[Open an issue on GitHub](https://github.com/josscit/kindle-pdf-ocr/issues)

---

**Made with ❤️ by Jos from [IeXa Academy](https://www.iexa.it)**
