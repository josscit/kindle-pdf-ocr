"""
Kindle to Searchable PDF - Gradio Web UI for Pinokio
"""
import gradio as gr
import os
import sys
from pathlib import Path
import threading
import time

# Import our existing capture script
from kindle_auto_pdf_ocr import capture_kindle_to_searchable_pdf, ensure_programs_in_path, check_tesseract

# Setup paths
ensure_programs_in_path()

def check_dependencies():
    """Check if Tesseract and Ghostscript are installed"""
    tesseract = check_tesseract()
    
    if tesseract:
        return "✅ OCR Ready: Tesseract and Ghostscript found!"
    else:
        return """⚠️ OCR Not Available
        
Please install:
1. Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki
2. Ghostscript: https://ghostscript.com/releases/gsdnld.html

See README.md for detailed instructions."""

def capture_ebook(num_pages, delay, ocr_enabled, ocr_language):
    """Capture ebook and create PDF"""
    
    try:
        # Check dependencies
        if ocr_enabled and not check_tesseract():
            return None, "❌ Error: Tesseract not installed. Install it or disable OCR."
        
        print(f"\n📚 Starting capture of {num_pages} pages...")
        print("⏰ You have 10 seconds to prepare Kindle!")
        
        # Countdown
        for i in range(10, 0, -1):
            print(f"   {i}...")
            time.sleep(1)
        
        print("🚀 Capturing pages...\n")
        
        # Run capture
        result_folder = capture_kindle_to_searchable_pdf(
            num_pages=num_pages,
            delay=delay,
            auto_crop=False,
            use_ocr=ocr_enabled,
            ocr_language=ocr_language
        )
        
        if result_folder:
            # Find the PDF file
            pdf_files = list(Path(result_folder).glob("*_searchable.pdf"))
            if not pdf_files:
                pdf_files = list(Path(result_folder).glob("*_base.pdf"))
            
            if pdf_files:
                pdf_path = str(pdf_files[0])
                success_msg = f"""✅ PDF Created Successfully!

📄 File: {pdf_files[0].name}
📦 Size: {pdf_files[0].stat().st_size / (1024*1024):.2f} MB
📁 Location: {result_folder}

{'🔍 PDF is searchable - AI agents can read the text!' if ocr_enabled else '📸 PDF contains images only'}

Click the Download button to get your PDF!"""
                
                return pdf_path, success_msg
            else:
                return None, "❌ Error: PDF file not found"
        else:
            return None, "❌ Error: Capture failed"
            
    except Exception as e:
        return None, f"❌ Error: {str(e)}"

# Create Gradio interface
with gr.Blocks(title="Kindle to Searchable PDF") as demo:
    
    gr.Markdown("""
    # 📚 Kindle to Searchable PDF
    
    Automatically capture screenshots from Kindle for PC and convert them to searchable PDF with OCR.
    Perfect for creating digital copies with text extraction for AI analysis!
    """)
    
    # Dependency check
    dep_status = gr.Textbox(
        label="System Status",
        value=check_dependencies(),
        interactive=False,
        lines=3
    )
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### ⚙️ Capture Settings")
            
            num_pages = gr.Slider(
                minimum=1,
                maximum=500,
                value=5,
                step=1,
                label="📖 Number of Pages",
                info="How many pages to capture"
            )
            
            delay = gr.Slider(
                minimum=1.0,
                maximum=5.0,
                value=2.0,
                step=0.5,
                label="⏱️ Delay Between Pages (seconds)",
                info="Wait time for page loading"
            )
            
            gr.Markdown("### 🔍 OCR Settings")
            
            ocr_enabled = gr.Checkbox(
                label="Enable OCR (Searchable PDF)",
                value=True,
                info="Add invisible text layer for AI agents"
            )
            
            ocr_language = gr.Dropdown(
                choices=["ita", "eng", "fra", "deu", "spa", "por"],
                value="ita",
                label="OCR Language",
                info="Language for text recognition"
            )
            
            capture_btn = gr.Button("🚀 Start Capture", variant="primary", size="lg")
        
        with gr.Column():
            gr.Markdown("### 📊 Status & Results")
            
            status_text = gr.Textbox(
                label="Status",
                lines=10,
                interactive=False,
                placeholder="Click 'Start Capture' to begin..."
            )
            
            pdf_output = gr.File(
                label="📄 Download PDF",
                interactive=False
            )
    
    gr.Markdown("""
    ---
    ### 📝 Instructions:
    
    1. **Configure** capture settings above
    2. **Click** 'Start Capture' button
    3. **You have 10 seconds** to:
       - Open Kindle for PC in **fullscreen (F11)**
       - Navigate to the **first page** to capture
       - **Hide this window**
       - **Click on Kindle** to activate it
    4. The script will automatically capture pages and create PDF
    5. **Download** your searchable PDF when complete!
    
    ### 💡 Tips:
    - Use **2.0s delay** for standard books
    - Increase delay if pages load slowly
    - Enable **OCR** for AI agent compatibility
    - **Italian (ita)** works best for Italian books
    
    ### ⚠️ Requirements:
    - Kindle for PC installed
    - Tesseract OCR (for searchable PDF)
    - Ghostscript (for OCR processing)
    """)
    
    # Button action
    capture_btn.click(
        fn=capture_ebook,
        inputs=[num_pages, delay, ocr_enabled, ocr_language],
        outputs=[pdf_output, status_text]
    )

# Launch
if __name__ == "__main__":
    print("\n" + "="*60)
    print("  📚 KINDLE TO PDF OCR - WEB INTERFACE")
    print("="*60)
    print("\n🚀 Starting server...")
    print("\n⚠️  If browser doesn't open automatically:")
    print("   👉 Open your browser and go to: http://127.0.0.1:7861")
    print("\n" + "="*60 + "\n")
    
    demo.launch(
        server_name="127.0.0.1",
        server_port=7861,
        share=False,
        show_error=True,
        inbrowser=True,
        quiet=False
    )
