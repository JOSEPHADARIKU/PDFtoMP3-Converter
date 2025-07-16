import os
import sys
import fitz  # PyMuPDF
from gtts import gTTS
from datetime import datetime
from tkinter import Tk, filedialog
import platform

def pick_pdf_file():
    Tk().withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if not file_path:
        print("[ERROR] No file selected. Exiting.")
        sys.exit(1)
    return file_path

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    if doc.page_count == 0:
        print("[ERROR] PDF has no pages.")
        sys.exit(1)

    text_list = []
    for page_num in range(doc.page_count):
        try:
            page = doc.load_page(page_num)
            text = page.get_text().strip()
            if text:
                text_list.append(text)
        except Exception as e:
            print(f"[WARN] Failed to read page {page_num}: {e}")

    doc.close()
    if not text_list:
        print("[ERROR] No readable text found in the PDF.")
        sys.exit(1)

    return " ".join(text_list)

def text_to_speech(text, output_name="audio_output"):
    language = 'en'
    tts = gTTS(text=text, lang=language, slow=False)
    filename = f"{output_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    tts.save(filename)
    print(f"[SUCCESS] Audio saved as: {filename}")
    open_audio_file(filename)

def open_audio_file(file_path):
    print(f"[INFO] Opening audio file...")
    if platform.system() == "Windows":
        os.startfile(file_path)
    elif platform.system() == "Darwin":
        os.system(f"open '{file_path}'")
    else:
        os.system(f"xdg-open '{file_path}'")

if __name__ == "__main__":
    print("[INFO] Choose your PDF file...")
    pdf_path = pick_pdf_file()
    print(f"[INFO] Extracting text from: {pdf_path}")
    extracted_text = extract_text_from_pdf(pdf_path)
    print(f"[INFO] Text extracted successfully. Generating audio...")
    text_to_speech(extracted_text)
