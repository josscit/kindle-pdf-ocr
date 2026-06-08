"""
Script completo per catturare screenshot Kindle e convertirli in PDF Searchable con OCR
"""
import pyautogui
import time
from pathlib import Path
from datetime import datetime
from PIL import Image
import numpy as np
import img2pdf
import subprocess
import sys
import shutil
import os
from typing import Optional, List

def ensure_programs_in_path() -> None:
    """Aggiunge Tesseract e Ghostscript al PATH se necessario"""
    # Tesseract
    tesseract_paths = [
        r"C:\Program Files\Tesseract-OCR",
        r"C:\Program Files (x86)\Tesseract-OCR"
    ]
    
    for tess_path in tesseract_paths:
        if Path(tess_path).exists():
            current_path = os.environ.get("PATH", "")
            if tess_path not in current_path:
                os.environ["PATH"] = tess_path + os.pathsep + current_path
                os.environ["TESSDATA_PREFIX"] = str(Path(tess_path) / "tessdata")
            break
    
    # Ghostscript - Search all versions dynamically
    gs_base_paths = [
        r"C:\Program Files\gs",
        r"C:\Program Files (x86)\gs"
    ]
    
    for gs_base in gs_base_paths:
        if Path(gs_base).exists():
            # Find all gs* subdirectories (gs10.03.1, gs10.04.0, etc.)
            gs_versions = sorted(Path(gs_base).glob("gs*/bin"), reverse=True)
            if gs_versions:
                gs_path = str(gs_versions[0])  # Use latest version
                current_path = os.environ.get("PATH", "")
                if gs_path not in current_path:
                    os.environ["PATH"] = gs_path + os.pathsep + current_path
                break

def check_tesseract() -> Optional[str]:
    """Verifica se Tesseract è installato"""
    return shutil.which("tesseract")

def auto_crop_image(image, threshold=250, margin=10):
    """
    Croppa automaticamente i margini bianchi/neri dell'immagine
    """
    img_array = np.array(image.convert('L'))
    non_empty_columns = np.where(np.mean(img_array, axis=0) < threshold - 20)[0]
    non_empty_rows = np.where(np.mean(img_array, axis=1) < threshold - 20)[0]
    
    if len(non_empty_columns) == 0 or len(non_empty_rows) == 0:
        return image
    
    left = max(0, non_empty_columns[0] - margin)
    right = min(image.width, non_empty_columns[-1] + margin)
    top = max(0, non_empty_rows[0] - margin)
    bottom = min(image.height, non_empty_rows[-1] + margin)
    
    cropped = image.crop((left, top, right, bottom))
    return cropped

def _page_change_fraction(img1, img2, pixel_delta: int = 12, size=(120, 120)) -> float:
    """
    Frazione di pixel che cambiano tra due schermate (0.0 = identiche, 1.0 = tutto diverso).

    Serve per il rilevamento automatico della fine del libro: quando la freccia destra
    non sposta più la pagina, due schermate consecutive diventano identiche e questa
    frazione crolla verso 0. Le immagini vengono ridotte in scala di grigi (veloce) e
    si contano solo i pixel che variano oltre `pixel_delta`, per ignorare il rumore di
    rendering/anti-aliasing.
    """
    a = np.asarray(img1.convert('L').resize(size), dtype=np.int16)
    b = np.asarray(img2.convert('L').resize(size), dtype=np.int16)
    return float(np.mean(np.abs(a - b) > pixel_delta))


def images_to_pdf(image_files: List[Path], output_pdf_path: Path) -> bool:
    """Converte immagini in PDF (lossless)"""
    if not image_files:
        print("❌ Nessuna immagine da convertire")
        return False
    
    try:
        with open(output_pdf_path, "wb") as f:
            f.write(img2pdf.convert([str(img) for img in image_files]))
        return True
    except Exception as e:
        print(f"❌ Errore conversione PDF: {e}")
        return False

def add_ocr_to_pdf(input_pdf: Path, output_pdf: Path, tesseract_path: Optional[str] = None, language: str = 'ita') -> bool:
    """Aggiunge layer OCR al PDF"""
    try:
        import ocrmypdf
        
        # Configura Tesseract se specificato
        env = None
        if tesseract_path:
            env = {'TESSDATA_PREFIX': str(Path(tesseract_path).parent / 'tessdata')}
        
        print(f"🔍 Esecuzione OCR (lingua: {language})...")
        print("   Questo può richiedere alcuni minuti...")
        
        ocrmypdf.ocr(
            input_pdf,
            output_pdf,
            language=language,
            deskew=False,  # Non ruotare
            force_ocr=True,  # Forza OCR anche se sembra già presente
            optimize=1,  # Compressione leggera
            tesseract_timeout=300,  # Timeout 5 minuti per pagina
            progress_bar=True
        )
        
        return True
    except Exception as e:
        print(f"❌ Errore OCR: {e}")
        return False

def capture_kindle_to_searchable_pdf(num_pages, output_folder="screenshots", delay=1.5,
                                      auto_crop=False, use_ocr=True, ocr_language='ita',
                                      auto_stop=True, stop_after=3, change_threshold=0.003):
    """
    Cattura screenshot Kindle e crea PDF Searchable con OCR
    """
    # Fix PATH per Tesseract e Ghostscript
    ensure_programs_in_path()
    
    # Verifica Tesseract se OCR richiesto
    tesseract_path = None
    if use_ocr:
        tesseract_path = check_tesseract()
        if not tesseract_path:
            print("\n⚠️  ATTENZIONE: Tesseract OCR non trovato!")
            print("   Il PDF sarà creato SENZA testo ricercabile.")
            print("   Per installare Tesseract, vedi la sezione 'Installare Tesseract' nel README.md")
            response = input("\n   Continuo senza OCR? [S/n]: ").strip().lower()
            if response == 'n':
                print("Operazione annullata.")
                return None
            use_ocr = False
        else:
            print(f"✅ Tesseract trovato: {tesseract_path}")
    
    # Crea cartelle
    output_path = Path(output_folder)
    output_path.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_folder = output_path / timestamp
    session_folder.mkdir(exist_ok=True)
    
    raw_folder = session_folder / "raw"
    raw_folder.mkdir(exist_ok=True)
    
    if auto_crop:
        cropped_folder = session_folder / "cropped"
        cropped_folder.mkdir(exist_ok=True)
    
    print("="*70)
    print("  📚 KINDLE TO SEARCHABLE PDF - AUTOMAZIONE COMPLETA")
    print("="*70)
    print(f"\n📊 Configurazione:")
    print(f"   • Pagine da catturare: {num_pages}" + (" (MAX — stop automatico a fine libro)" if auto_stop else ""))
    print(f"   • Delay tra pagine: {delay}s")
    print(f"   • Auto-stop fine libro: " + (f"✅ Sì (dopo {stop_after} schermate identiche)" if auto_stop else "❌ No"))
    print(f"   • Auto-crop margini: {'✅ Sì' if auto_crop else '❌ No'}")
    print(f"   • OCR (testo searchable): {'✅ Sì (' + ocr_language + ')' if use_ocr else '❌ No'}")
    print(f"   • Cartella output: {session_folder}")
    
    print("\n⚠️  PREPARAZIONE:")
    print("   1. Apri Kindle for PC e premi F11 per FULLSCREEN")
    print("   2. Apri il libro alla PRIMA PAGINA da catturare")
    print("   3. NASCONDI questa finestra del terminale")
    print("   4. CLICCA sulla finestra di Kindle per attivarla")
    print("\n⏰ Hai 10 secondi per prepararti...")
    
    for i in range(10, 0, -1):
        print(f"   {i}...")
        time.sleep(1)
    
    print("\n🚀 INIZIO CATTURA!\n")
    
    captured_pages = []
    prev_img = None          # ultima pagina UNICA catturata (per il confronto)
    consecutive_dup = 0      # schermate identiche di fila viste finora
    page_num = 0             # pagine effettivamente salvate
    stopped_at_end = False

    # Cattura pagine — con rilevamento automatico della fine del libro.
    # `num_pages` qui è il LIMITE MASSIMO: se auto_stop è attivo, ci si ferma prima,
    # quando la freccia destra non cambia più la pagina (= fine libro).
    while page_num < num_pages:
        try:
            screenshot = pyautogui.screenshot()

            # --- AUTO-STOP: la pagina non cambia più? ---
            if auto_stop and prev_img is not None:
                frac = _page_change_fraction(prev_img, screenshot)

                if frac < change_threshold:
                    # Sembra identica. Distinguo "fine libro" da "pagina ancora in
                    # caricamento": aspetto ancora un po' e riscatto prima di decidere.
                    time.sleep(delay)
                    screenshot = pyautogui.screenshot()
                    frac = _page_change_fraction(prev_img, screenshot)

                if frac < change_threshold:
                    consecutive_dup += 1
                    print(f"⏸️  Pagina invariata ({consecutive_dup}/{stop_after}) — probabile fine libro")
                    if consecutive_dup >= stop_after:
                        print("\n🏁 Fine libro rilevata: la pagina non cambia più → STOP automatico.")
                        stopped_at_end = True
                        break
                    # Non ancora certi: provo ad avanzare e ricontrollo al giro dopo.
                    pyautogui.press('right')
                    time.sleep(delay)
                    continue

                consecutive_dup = 0  # pagina diversa → ripartiamo da zero

            # --- Pagina nuova: salvala ---
            page_num += 1
            raw_filename = raw_folder / f"page_{page_num:04d}.png"
            screenshot.save(raw_filename, dpi=(300, 300))

            cap_info = f"📸 Pagina {page_num} catturata"
            if not auto_stop:
                cap_info = f"📸 Pagina {page_num}/{num_pages} catturata"
            print(cap_info)

            if auto_crop:
                cropped = auto_crop_image(screenshot)
                cropped_filename = cropped_folder / f"page_{page_num:04d}.png"
                cropped.save(cropped_filename, dpi=(300, 300))
                print(f"✂️  Croppata: {screenshot.size} → {cropped.size}")
                captured_pages.append(cropped_filename)
            else:
                captured_pages.append(raw_filename)

            prev_img = screenshot

            # Avanza alla pagina successiva (salto solo dopo l'ultima consentita)
            if page_num < num_pages:
                pyautogui.press('right')
                time.sleep(delay)
                print()

        except KeyboardInterrupt:
            print(f"\n\n⚠️  Interrotto dall'utente alla pagina {page_num}")
            break
        except Exception as e:
            print(f"\n❌ Errore alla pagina {page_num}: {e}")
            break

    if auto_stop and not stopped_at_end and page_num >= num_pages:
        print(f"\n⚠️  Raggiunto il limite massimo di {num_pages} scatti senza rilevare la fine.")
        print("    Se il libro è più lungo, rilancia con un limite più alto.")
    
    print("\n" + "="*70)
    print(f"✅ CATTURA COMPLETATA - {len(captured_pages)} pagine")
    print("="*70)
    
    # Crea PDF base
    if captured_pages:
        print("\n📄 Creazione PDF base...")
        pdf_base = session_folder / f"ebook_{timestamp}_base.pdf"
        
        if images_to_pdf(captured_pages, pdf_base):
            pdf_size_mb = pdf_base.stat().st_size / (1024 * 1024)
            print(f"✅ PDF base creato: {pdf_base.name} ({pdf_size_mb:.2f} MB)")
            
            # Aggiungi OCR se richiesto
            if use_ocr and tesseract_path:
                pdf_final = session_folder / f"ebook_{timestamp}_searchable.pdf"
                print(f"\n🔍 Aggiunta layer OCR al PDF...")
                
                if add_ocr_to_pdf(pdf_base, pdf_final, tesseract_path, ocr_language):
                    final_size_mb = pdf_final.stat().st_size / (1024 * 1024)
                    print(f"\n✅ PDF SEARCHABLE CREATO!")
                    print(f"📄 File: {pdf_final.name}")
                    print(f"📦 Dimensione: {final_size_mb:.2f} MB")
                    print(f"\n💡 Ora gli AI agent possono leggere il testo del libro!")
                    
                    # Rimuovi PDF base se OCR ha avuto successo
                    pdf_base.unlink()
                else:
                    print(f"\n⚠️  OCR fallito, mantengo PDF base senza OCR")
                    pdf_final = pdf_base
            else:
                pdf_final = pdf_base
                print(f"\n📄 PDF finale (senza OCR): {pdf_base.name}")
        else:
            print("❌ Errore nella creazione del PDF")
            return None
    
    print(f"\n📁 Tutti i file salvati in:")
    print(f"   {session_folder}")
    print("\n" + "="*70)
    
    return session_folder

if __name__ == "__main__":
    print("\n" + "="*70)
    print("  KINDLE TO SEARCHABLE PDF - AUTOMATION TOOL")
    print("="*70)
    
    # Fix PATH prima di verificare
    ensure_programs_in_path()
    
    # Verifica subito Tesseract
    tesseract_path = check_tesseract()
    if tesseract_path:
        print(f"\n✅ Tesseract OCR trovato: {tesseract_path}")
    else:
        print(f"\n⚠️  Tesseract OCR NON trovato")
        print("   Per installarlo, vedi la sezione 'Installare Tesseract' nel README.md")
        print("   Puoi comunque creare PDF senza OCR\n")
    
    try:
        num_pages = int(input("\n🔢 Quante pagine vuoi catturare? [default: 5]: ") or "5")
        delay = float(input("⏱️  Secondi di attesa tra le pagine? [default: 2.0]: ") or "2.0")
        crop_input = input("✂️  Vuoi croppare automaticamente i margini? [s/N]: ").strip().lower()
        auto_crop = crop_input == 's'
        
        use_ocr = False
        ocr_lang = 'ita'
        if tesseract_path:
            ocr_input = input("🔍 Vuoi aggiungere OCR (testo searchable)? [S/n]: ").strip().lower()
            use_ocr = ocr_input != 'n'
            if use_ocr:
                lang_input = input("🌍 Lingua OCR? [ita/eng/deu/fra...] [default: ita]: ").strip() or "ita"
                ocr_lang = lang_input
    except ValueError:
        print("\n⚠️  Input non valido, uso valori di default")
        num_pages = 5
        delay = 2.0
        auto_crop = False
        use_ocr = tesseract_path is not None
        ocr_lang = 'ita'
    
    # Esegui
    capture_kindle_to_searchable_pdf(
        num_pages=num_pages,
        delay=delay,
        auto_crop=auto_crop,
        use_ocr=use_ocr,
        ocr_language=ocr_lang
    )
