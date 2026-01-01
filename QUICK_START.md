# 📚 Guida Completa - Kindle to PDF Searchable

**Guida semplicissima per trasformare i tuoi ebook Kindle in PDF con testo leggibile dagli AI!**

Spiegata come se fosse per tua mamma - niente termini tecnici! 😊

---

## 🎯 **Cosa fa questo programma?**

1. Apri un libro su Kindle for PC
2. Il programma fa screenshot automatici delle pagine
3. Crea un PDF con le immagini + testo invisibile sotto (OCR)
4. Gli Agenti AI (ChatGPT, Claude, etc.) possono leggere il testo!

---

## 📋 **Cosa ti serve:**

- Un PC con Windows 10 o 11
- Kindle for PC installato
- 20 minuti per l'installazione (una volta sola)

---

## ⚡ **PARTE 1: Installazione (fai una volta sola)**

### **STEP 1: Installa Python (il "motore" del programma)**

**Cos'è Python?** È come il motore di una macchina - serve per far funzionare il programma.

1. Apri il browser e vai su: **www.python.org/downloads**
2. Vedrai un grosso bottone giallo **"Download Python 3.12"** (o simile)
3. Click sul bottone e scarica il file
4. **SUPER IMPORTANTE**: Quando si apre l'installazione, vedi una casella che dice **"Add Python to PATH"**? 
   - ☑️ **DEVI SPUNTARLA!** (è fondamentale!)
5. Ora click su **"Install Now"**
6. Aspetta che finisca (1-2 minuti)

**Come verifico che funziona?**
1. Premi tasto Windows
2. Scrivi "cmd" e premi Invio (si apre una finestra nera)
3. Scrivi: `python --version` e premi Invio
4. Se vedi "Python 3.12.x" → PERFETTO! ✅
5. Se vedi errore → Hai dimenticato di spuntare "Add to PATH", reinstalla Python

---

### **STEP 2: Scarica il Programma**

**Modo semplice (per tutti):**

1. Vai su: **github.com/josscit/kindle-pdf-ocr**
2. Vedi un pulsante verde con scritto **"<> Code"**? Cliccalo
3. Nel menu che si apre, click su **"Download ZIP"**
4. Il file si scarica (si chiama `kindle-pdf-ocr-main.zip`)
5. Vai nella cartella **Download** del tuo PC
6. Click destro sul file ZIP → **"Estrai tutto"**
7. Scegli dove estrarlo (es: sul Desktop va bene)
8. Si crea una cartella chiamata **"kindle-pdf-ocr-main"**

**Ricordati dove l'hai messa!** Ti servirà dopo.

---

### **STEP 3: Installa le "Librerie" (i componenti del programma)**

**Come faccio ad aprire la cartella giusta?**
1. Vai nella cartella **"kindle-pdf-ocr-main"** che hai estratto prima
2. Click sulla barra in alto (dove c'è il percorso tipo "Desktop > kindle-pdf-ocr-main")
3. Scrivi: **powershell** e premi Invio
4. Si apre una finestra blu (PowerShell)

**Ora scrivi questi comandi** (uno alla volta, premi Invio dopo ognuno):

```
python -m venv env
```
*(Crea uno "spazio" per il programma - aspetta 10 secondi)*

```
.\env\Scripts\activate
```
*(Attiva lo "spazio" - vedrai "(env)" all'inizio della riga)*

```
pip install -r requirements.txt
```
*(Installa tutti i componenti - aspetta 3-5 minuti, vedrai tante scritte scorrere)*

**Quando finisce** vedrai di nuovo il cursore lampeggiante. Perfetto! ✅

---

### **STEP 4: Installa Tesseract (il "lettore" che legge il testo dalle immagini)**

**Cos'è?** È il programma che "legge" il testo dagli screenshot e lo trasforma in testo vero.

1. **Click qui per scaricare:** [Tesseract Installer](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.5.0.20250102.exe)
2. Si scarica un file tipo "tesseract-ocr-w64-setup..."
3. **Fai doppio click** sul file per installarlo
4. **⚠️ SUPER IMPORTANTE**: Durante l'installazione, ad un certo punto ti chiede **"Additional language data"**
   - Metti la spunta su **"Additional language data (download)"**
   - Poi cerca e metti la spunta su **"Italian"** (o la lingua dei tuoi libri)
   - Senza questo, non riconosce il testo italiano!
5. Click **"Next"** fino a **"Install"**
6. Aspetta che finisca → **"Finish"**

---

### **STEP 5: Installa Ghostscript (l'"assemblatore" che crea il PDF finale)**

**Cos'è?** È il programma che prende gli screenshot + il testo letto da Tesseract e li mette insieme in un PDF.

1. **Click qui per scaricare:** [Ghostscript Installer](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10031/gs10031w64.exe)
2. Si scarica un file tipo "gs10031w64.exe"
3. **Fai doppio click** per installarlo
4. Click **"Next"** → **"Next"** → **"Install"**
5. Aspetta → **"Finish"**

**Fatto!** ✅

---

## 🎉 **PARTE 2: Come Usarlo (ogni volta che vuoi creare un PDF)**

Hai installato tutto! Ora puoi usarlo in **2 MODI** - scegli quello che preferisci:

---

## 🎨 **MODO 1: Con Interfaccia Grafica (PIÙ FACILE)**

### **Passo 1: Avvia il Programma**

1. Vai nella cartella **"kindle-pdf-ocr-main"**
2. Click sulla barra in alto → scrivi **powershell** → Invio
3. Nella finestra blu che si apre, scrivi:
```
.\env\Scripts\activate
```
*(Apparirà "(env)" all'inizio - è normale)*

4. Poi scrivi:
```
python app.py
```

5. **Si apre automaticamente il browser** con una pagina colorata! 🎨

### **Passo 2: Configura**

Nella pagina vedrai:

- **Number of Pages** → Muovi il cursore per scegliere quante pagine catturare (es: 10)
- **Delay Between Pages** → Lascia 2.0 secondi (va bene così)
- **Enable OCR** → Lascia la spunta ✅ (serve per rendere il PDF leggibile)
- **OCR Language** → Scegli "ita" se è un libro italiano

### **Passo 3: Cattura!**

1. **Prima di clickare "Start Capture"**, prepara Kindle:
   - Apri **Kindle for PC**
   - Apri il libro che vuoi convertire
   - Premi **F11** (mette Kindle a schermo intero)
   - Vai alla **PRIMA PAGINA** che vuoi catturare

2. Ora **torna sul browser** e click sul bottone viola **"🚀 Start Capture"**

3. **HAI 10 SECONDI!** Il programma conta:
   - 10... 9... 8... 
   - In questi 10 secondi devi:
     - **Minimizza il browser** (click sulla X o sulla barra in basso)
     - **Click sulla finestra di Kindle** per attivarla

4. **Ora stai fermo!** 😊
   - Il programma fa tutto da solo
   - Vedrai Kindle sfogliare le pagine automaticamente
   - **Non toccare niente!**

5. Quando finisce (senti che non sfoglia più), **torna sul browser**

6. Vedrai scritto **"✅ PDF Created Successfully!"**

7. Click sul bottone **"📄 Download PDF"** e salva il file!

**FINITO!** Hai il tuo PDF con testo leggibile! 🎉

---

## ⌨️ **MODO 2: Senza Interfaccia (Per Chi Preferisce)**

Questo modo è più "vecchia scuola" - tutto con scritte nella finestra nera.

### **Passo 1: Avvia**

1. Vai nella cartella **"kindle-pdf-ocr-main"**
2. Click barra in alto → **powershell** → Invio
3. Scrivi:
```
.\env\Scripts\activate
```

4. Scrivi:
```
python kindle_auto_pdf_ocr.py
```

### **Passo 2: Rispondi alle Domande**

Il programma ti fa domande (scrivi la risposta e premi Invio):

- **"Quante pagine?"** → Scrivi il numero (es: 10)
- **"Delay?"** → Premi solo Invio (usa il default)
- **"OCR?"** → Premi solo Invio (dice Sì)
- **"Lingua?"** → Scrivi **ita** e premi Invio

### **Passo 3: Prepara Kindle**

Hai 10 secondi per:
- Aprire Kindle in fullscreen (F11)
- Andare alla prima pagina
- Click su Kindle

Poi **non toccare niente!** Il programma lavora da solo.

### **Passo 4: Trova il PDF**

Quando finisce, il PDF è in:
```
kindle-pdf-ocr-main\screenshots\[data_ora]\ebook_xxx_searchable.pdf
```

Apri la cartella **screenshots**, poi l'ultima cartella creata, trovi il PDF! ✅

---

## 📁 **Dove trovo i PDF?**

I PDF vengono salvati in:
```
kindle-pdf-ocr\
  └── screenshots\
      └── YYYYMMDD_HHMMSS\
          └── ebook_YYYYMMDD_HHMMSS_searchable.pdf
```

---

## 🆘 **Aiuto! Qualcosa non Funziona!**

### **Problema: "python non riconosciuto"**

**Cosa vedi:** Scrivi `python --version` e dice "comando non trovato"

**Soluzione:** Hai dimenticato di spuntare "Add Python to PATH" quando hai installato Python!
- Disinstalla Python (Pannello di Controllo → Programmi)
- Reinstalla e **SPUNTA** la casella "Add Python to PATH"

---

### **Problema: "Tesseract non trovato"**

**Cosa vedi:** Il programma dice "Tesseract OCR not found"

**Soluzione:** 
1. Tesseract non è installato → Fai lo Step 4
2. L'hai installato ma **dimenticato** di scaricare la lingua italiana
   - Reinstalla Tesseract
   - Quando chiede "Additional language data" → Spunta "Italian"

---

### **Problema: "Ghostscript non trovato"**

**Cosa vedi:** Dice "Ghostscript not found" o "OCR fallito"

**Soluzione:** Installa Ghostscript (Step 5)

---

### **Problema: Il testo nel PDF è sgranato**

**Cosa vedi:** Il PDF si vede ma il testo non è nitido

**È NORMALE!** 😊
- Stiamo facendo screenshot di un libro a schermo intero
- La qualità dipende dalla risoluzione del tuo schermo
- Il testo è **leggibile** (è l'importante!)
- Non sarà mai qualità stampa, ma gli AI lo leggono benissimo

---

### **Problema: Il programma sfoglia ma non cattura**

**Causa:** Non hai cliccato su Kindle durante i 10 secondi

**Soluzione:** 
- Riprova
- Quando parte il countdown (10...9...8...)
- **CLICK sulla finestra di Kindle** prima che arrivi a zero
- Kindle deve essere "attiva" (la finestra in primo piano)

---

### **Problema: Cattura pagine sbagliate**

**Causa:** Delay troppo corto, Kindle non fa in tempo a caricare

**Soluzione:**
- Usa **3.0 secondi** invece di 2.0 nel delay
- Specie se il libro ha tante immagini

---

### **Problema: L'interfaccia grafica non si apre**

**Cosa fare:**
1. Chiudi tutto
2. Apri PowerShell nella cartella
3. Scrivi: `.\env\Scripts\activate`
4. Scrivi: `pip install gradio`
5. Aspetta che finisce
6. Riprova: `python app.py`

---

## 🔄 **Aggiornare alla Versione Nuova**

```cmd
git pull
pip install -r requirements.txt --upgrade
```

---

## 💡 **Consigli per Usarlo Bene**

1. **Schermo pulito:** Chiudi notifiche, popup, tutto! Altrimenti escono nello screenshot
2. **Fullscreen SEMPRE:** Premi F11 su Kindle - senza la barra in alto/basso
3. **Lingua giusta:** Libro in italiano → OCR ita. Libro in inglese → OCR eng
4. **Test prima:** Fai una prova con 3-5 pagine prima di fare un libro intero!
5. **Non muovere il mouse:** Durante la cattura, mani ferme! 😊
6. **Libri lunghi:** Un libro di 200 pagine prende circa 15-20 minuti

## ⚖️ **Importante - Legalità**

**Puoi usarlo SOLO per:**
- ✅ Libri che hai **comprato** legalmente
- ✅ Materiale di **pubblico dominio**
- ✅ **Backup personale** dei tuoi ebook

**NON usarlo per:**
- ❌ Condividere i PDF con altre persone
- ❌ Vendere i PDF
- ❌ Aggirare protezioni DRM (questo programma fa solo screenshot, non rimuove DRM)

**Rispetta i diritti d'autore!** 📚

---

## ❓ **Serve Aiuto?**

Apri un [Issue su GitHub](https://github.com/josscit/kindle-pdf-ocr/issues)

---

**Made with ❤️ by Jos from [IeXa Academy](https://www.iexa.it)**
