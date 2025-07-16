# 📚 PDF to Audiobook Converter

Turn any PDF into an audiobook with a click. Choose between a cloud-free offline voice or Google TTS.

---

## 🚀 Features

- 🔍 Pick any `.pdf` file using a file dialog
- 📖 Automatically extracts clean text from all pages
- 🔊 Converts text into a spoken `.mp3` file
- 🧠 Fully offline mode available using `pyttsx3`
- ✅ Runs instantly with no setup beyond Python

---

## 💡 How to Use

### 1. Install dependencies:

#### 🔁 For Google TTS (requires internet):
```bash
pip install gTTS PyMuPDF
```

#### 🔒 For fully offline voice:
```bash
pip install pyttsx3 PyMuPDF
```

### 2. Run the script:

```bash
python Audio-book.py
```

### 3. Pick your PDF file when the window opens.

### 4. Audio is saved in the same folder as `audio_output_*.mp3`.

---

## 🔧 Optional Switch: Offline Mode

Replace `gTTS` with `pyttsx3` if you want **fully offline** speech synthesis.

> Already included in `Audio-book.py`, just uncomment the mode you want to use.

---

## 📁 Output Sample

```
audio_output_20250716_101203.mp3
```

---

## 🛡️ No Tokens. No APIs. No Signups.

This project runs entirely **locally**, nothing is stored or sent anywhere. It’s just you, your PDF, and your audiobook.

---

## 👤 Author

Made by [ Joseph Adariku ].
PRs and stars welcome 🌟
