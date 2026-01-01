# 📚 Quick Start - Simple Guide for Everyone

**Convert your Kindle ebooks to searchable PDF in 5 easy steps!**

No technical knowledge required! 😊

---

## 🎯 What This Does

Takes your Kindle book → Creates a PDF file → AI tools can read the text!

Perfect for using with ChatGPT, Claude, or any AI assistant.

---

## 📋 What You Need

- Windows 10 or 11
- Kindle for PC (free app from Amazon)
- 20 minutes for first-time setup

---

## 🔧 PART 1: Setup (Do This Once)

Follow these 5 steps **one time only**. After this, using the program is super easy!

---

### **STEP 1: Install Python**

**What's Python?** The "engine" that runs the program.

1. Open browser → Go to **www.python.org/downloads**
2. Click big yellow button **"Download Python 3.12"**
3. Run the downloaded file
4. **⚠️ IMPORTANT:** Check the box **"Add Python to PATH"** ← Don't forget!
5. Click **"Install Now"**
6. Wait 1-2 minutes

**Verify it worked:**
- Press Windows key
- Type **cmd** → Press Enter
- In black window, type: `python --version`
- Should show: `Python 3.12.x` ✅

---

### **STEP 2: Download This Program**

1. Go to **github.com/josscit/kindle-pdf-ocr**
2. Click green button **"<> Code"**
3. Click **"Download ZIP"**
4. File downloads: `kindle-pdf-ocr-main.zip`
5. Go to **Downloads** folder
6. Right-click ZIP → **"Extract All"**
7. Extract to **Desktop** (or anywhere you want)

**You now have a folder:** `kindle-pdf-ocr-main`

---

### **STEP 3: Install Program Components**

1. **Open the folder:** Go to `kindle-pdf-ocr-main` on your Desktop
2. **Open PowerShell here:**
   - Click the address bar at top (where it shows the path)
   - Type: **powershell**
   - Press Enter
   - A blue window opens

3. **Create program space** - Type this and press Enter:
```
python -m venv .venv
```
Wait 10-20 seconds (creates a hidden folder `.venv`)

4. **Activate the space** - Type this and press Enter:
```
.\.venv\Scripts\activate
```
You'll see `(.venv)` appear at start of line ✅

5. **Install components** - Type this and press Enter:
```
pip install -r requirements.txt
```
**Wait 3-5 minutes** - lots of text will scroll. When cursor reappears, it's done! ✅

---

### **STEP 4: Install Tesseract (Text Reader)**

**What is it?** Reads text from screenshot images.

1. **Download:** [Click here for Tesseract](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.5.0.20250102.exe)
2. Run the downloaded file
3. **⚠️ CRITICAL:** During installation, when it asks about languages:
   - Check **"Additional language data (download)"**
   - Find and check **"Italian"** (or your book's language)
   - If you skip this, OCR won't work!
4. Click **"Next"** until **"Install"**
5. Wait → **"Finish"**

---

### **STEP 5: Install Ghostscript (PDF Builder)**

**What is it?** Combines screenshots and text into final PDF.

1. **Download:** [Click here for Ghostscript](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10031/gs10031w64.exe)
2. Run the downloaded file
3. Click **"Next"** → **"Next"** → **"Install"**
4. Wait → **"Finish"**

---

## ✅ Setup Complete!

**You did it!** 🎉 Now you can use the program anytime!

---

## 🚀 PART 2: Using the Program (Every Time)

Choose **Method 1** (with interface) or **Method 2** (without interface):

---

## 🎨 METHOD 1: With Graphical Interface (Easier)

### **Every time you want to create a PDF:**

1. **Open PowerShell in program folder:**
   - Go to `kindle-pdf-ocr-main` folder
   - Click address bar → Type **powershell** → Enter

2. **Start the program** - Type these 2 commands:
```
.\.venv\Scripts\activate
python app.py
```

3. **Browser opens automatically** with colorful interface!

4. **Configure what you want:**
   - **Number of Pages:** Move slider (e.g., 10 pages)
   - **Delay:** Leave at 2.0 seconds
   - **Enable OCR:** Keep checked ✅
   - **Language:** Choose your book's language (ita/eng/fra/deu)

5. **Before clicking "Start Capture":**
   - Open **Kindle for PC**
   - Open your book
   - Press **F11** (fullscreen)
   - Go to **first page** you want

6. **Click "🚀 Start Capture"** button

7. **Countdown starts - YOU HAVE 10 SECONDS:**
   - Minimize browser
   - Click on Kindle window
   - Don't touch anything!

8. **Program works automatically** - Kindle pages turn by themselves

9. **When done, return to browser** - Click **"Download PDF"** ✅

**DONE!** You have your searchable PDF! 🎉

---

## ⌨️ METHOD 2: Without Interface (Text-Based)

For those who prefer the classic way.

### **Every time you want to create a PDF:**

1. **Open PowerShell** in `kindle-pdf-ocr-main` folder

2. **Type these 2 commands:**
```
.\.venv\Scripts\activate
python kindle_auto_pdf_ocr.py
```

3. **Answer questions** (type and press Enter):
   - How many pages? → Type number (e.g., **10**)
   - Delay? → Press Enter (uses default)
   - OCR? → Press Enter (says Yes)
   - Language? → Type **ita** (or **eng** for English)

4. **Countdown starts (10 seconds)** - Prepare Kindle same as Method 1

5. **Program captures automatically**

6. **Find your PDF:**
   - Go to `screenshots` folder
   - Open newest folder
   - PDF is there! ✅

---

## 🆘 Common Problems

### "python not recognized"

**You forgot** to check "Add Python to PATH" during install!

**Fix:** Uninstall Python → Reinstall → Check the box!

---

### "ModuleNotFoundError: No module named 'gradio'"

**You skipped** the install step!

**Fix:**
```
.\.venv\Scripts\activate
pip install -r requirements.txt
```
Wait for it to finish, then try again.

---

### "Tesseract not found"

**Fix:** Install Tesseract (STEP 4) - don't forget to select Italian language!

---

### "Ghostscript not found" or "OCR failed"

**Fix:** Install Ghostscript (STEP 5)

---

### Text is blurry in PDF

**This is normal!** Screenshot quality isn't perfect, but:
- Text is **readable** ✅
- AI tools can **read it perfectly** ✅
- Good enough for analysis!

---

### Program turns pages but doesn't capture

**You didn't click on Kindle!**

**Remember:** During 10-second countdown, you MUST click on Kindle window to activate it!

---

### Captures wrong pages

**Delay too short** - pages don't load in time.

**Fix:** Change delay to 3.0 seconds instead of 2.0

---

## 💡 Pro Tips

1. ✅ **Clean screen** - Close all popups before capturing
2. ✅ **Always fullscreen** - Press F11 on Kindle
3. ✅ **Test first** - Try 3 pages before doing whole book
4. ✅ **Right language** - Italian book? Use "ita" for OCR
5. ✅ **Hands off** - Don't touch mouse during capture!

---

## ⏱️ How Long Does It Take?

- 10-page book: ~2-3 minutes
- 100-page book: ~15-20 minutes
- 300-page book: ~45-60 minutes

**Plan accordingly!** ☕

---

## ⚖️ Legal - Important!

**You can ONLY use this for:**
- ✅ Books you purchased legally
- ✅ Public domain content
- ✅ Personal backup

**Do NOT:**
- ❌ Share PDFs with others
- ❌ Sell the PDFs
- ❌ Violate copyright

**Respect authors' rights!** 📚

---

## 📘 Technical Box: Understanding Virtual Environments

<details>
<summary><b>Click here if you want to understand what <code>.venv</code> means</b></summary>

### What's a Virtual Environment?

Think of it like a **separate kitchen** for this program:
- Has its own ingredients (packages)
- Doesn't mess with your main kitchen (system Python)
- Can be cleaned up without breaking anything else

### Why `.venv`?

When you installed components (STEP 3), they went into a folder called `.venv` (the dot makes it hidden).

This folder contains:
- Python (just for this program)
- All packages (gradio, pyautogui, etc.)

### Why Activate?

When you type `.\.venv\Scripts\activate`:
- Windows temporarily uses **this folder's Python**
- All commands now use this isolated version
- You see `(.venv)` at start of line to remind you

### What if I Don't Activate?

Python uses the system version, which doesn't have gradio installed → Error!

### The `.venv` vs `env` Confusion

- `.venv` = Modern standard (what we actually use)
- `env` = Old name (some guides use this)

**They're the same thing, just different names!**

Our project uses `.venv` (starts with dot = hidden folder on Windows).

</details>

<details>
<summary><b>Click here to learn about <code>uv</code> (the shortcut tool)</b></summary>

### What is uv?

A **faster way** to run Python programs without typing multiple commands.

### Normal Way (4 commands):
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### With uv (1 command):
```
uv run app.py
```

**That's it!** uv automatically:
1. Finds `.venv` folder
2. Activates it
3. Installs missing packages
4. Runs your program

### Should You Install uv?

**Optional!** The program works fine without it.

**Install if:** You want fewer commands and faster speed

**Skip if:** You're comfortable with traditional method

### How to Install uv

**Windows (PowerShell):**
```powershell
powershell -Command "iwr https://astral.sh/uv/install.ps1 -useb | iex"
```

Then you can use `uv run app.py` instead of activating each time!

</details>

---

## ❓ Still Need Help?

Open an [Issue on GitHub](https://github.com/josscit/kindle-pdf-ocr/issues) - we're happy to help!

---

**Made with ❤️ by Jos from [IeXa Academy](https://www.iexa.it)**
