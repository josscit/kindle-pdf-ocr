# 🔧 Installazione OCR per Windows

Per creare PDF searchable servono **DUE programmi**:

## 1️⃣ Tesseract OCR (estrae il testo)

**Download diretto (CONSIGLIATO):**
1. Scarica: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.5.0.20250102.exe
2. Esegui l'installer
3. **⚠️ IMPORTANTE**: Durante installazione, seleziona "Additional language data (download)" e scegli **Italian (ita)**
4. Percorso default: `C:\Program Files\Tesseract-OCR\`

**Via Winget:**
```powershell
winget install UB-Mannheim.TesseractOCR
```
(Poi scarica manualmente `ita.traineddata` e mettilo in `C:\Program Files\Tesseract-OCR\tessdata\`)

## 2️⃣ Ghostscript (manipola i PDF)

**Download diretto:**
1. Scarica: https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10031/gs10031w64.exe
2. Esegui l'installer
3. Percorso default: `C:\Program Files\gs\`

**Via Winget:**
```powershell
winget install Ghostscript.Ghostscript
```

## ✅ Verifica Installazione

Dopo aver installato entrambi, apri un NUOVO terminale PowerShell:

```powershell
tesseract --version
gswin64c --version
```

Se vedi le versioni → tutto ok!

Se vedi errori "comando non trovato" → sono installati ma non nel PATH, **lo script li troverà comunque automaticamente**.

## 🚀 Sei Pronto!

Ora puoi usare:
```powershell
uv run kindle_auto_pdf_ocr.py
```

Lo script trova automaticamente Tesseract e Ghostscript e crea PDF searchable!
