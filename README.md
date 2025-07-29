# 🎭 Multi-Role AI Assistant

<img width="1920" height="920" alt="Screenshot from 2025-07-30 06-17-46" src="https://github.com/user-attachments/assets/381b1208-8027-47c8-976e-79acf77790f4" />

## 📝 Deskripsi

**Multi-Role AI Assistant** adalah aplikasi chat AI yang interaktif dan modern dengan 3 role AI yang berbeda. Aplikasi ini dibangun menggunakan Streamlit dengan antarmuka yang elegan, animasi menarik, dan fitur-fitur canggih untuk pengalaman pengguna yang luar biasa.

## ✨ Fitur Utama

### 🎭 **3 Role AI Profesional**
- **👾 Asisten Umum**: Bantuan untuk berbagai keperluan sehari-hari
- **👨‍🏫 Guru**: Pembelajaran interaktif untuk semua mata pelajaran
- **👩‍💻 Programmer**: Coding, debugging, dan solusi teknologi

### 🎨 **Antarmuka Modern dengan Animasi**
- Animated gradient background yang dinamis
- Typing animation untuk respons AI
- Slide-in animations untuk pesan chat
- Hover effects dan transisi yang smooth
- Loading spinners dan pulse effects
- Success/error animations dengan bounce dan shake effects

### 💬 **Sistem Chatroom Multi-Room**
- Buat dan kelola multiple chatrooms
- Rename dan delete chatrooms
- Switch antar rooms dengan mudah
- Statistik pesan per room

### ⚙️ **Kontrol Parameter AI**
- Temperature control (0.0 - 1.0)
- Max tokens control (100 - 2000)
- Rekomendasi parameter per role
- Reset ke default settings

### 🤖 **Multi-Model Support**
- **Model Gratis**: Mistral 7B, Google Gemma 7B, Llama 3 8B
- **Model Premium**: GPT-4o, Claude 3.5 Sonnet, Gemini Pro
- Auto-switch ke model yang direkomendasikan per role

## 🚀 Instalasi dan Setup

### 1. Clone atau Download File
```bash
gh repo clone HnFaell/Final_project
```

### 2. Install Dependencies
```bash
pip install streamlit requests pillow
```

### 3. Dapatkan API Key OpenRouter (Gratis)
1. Kunjungi [OpenRouter.ai](https://openrouter.ai/keys)
2. Daftar akun gratis
3. Generate API Key baru
4. Copy API Key untuk digunakan di aplikasi

### 4. Jalankan Aplikasi
```bash
streamlit run final_project.py
```

## 📋 Cara Penggunaan

### 1. **Registrasi**
- Masukkan nama panggilan Anda
- Input API Key OpenRouter
- Pilih role AI yang diinginkan
- Klik "🚀 Daftar & Mulai"

### 2. **Chat dengan AI**
- Pilih role AI di sidebar (👾 Asisten, 👨‍🏫 Guru, 👩‍💻 Programmer)
- Ketik pertanyaan di chat input
- Nikmati respons AI dengan typing animation
- Switch role kapan saja tanpa kehilangan chat

### 3. **Kelola Chatrooms**
- Buat room baru dengan tombol ➕
- Rename room dengan tombol 🔄
- Delete room dengan tombol 🗑️
- Switch antar rooms di dropdown

### 4. **Sesuaikan Parameter**
- Atur Temperature untuk kreativitas AI
- Atur Max Tokens untuk panjang respons
- Gunakan reset button untuk default per role

## 🎯 Contoh Penggunaan per Role

### 👾 **Asisten Umum**
```
User: "Bagaimana cara meningkatkan produktivitas kerja?"
AI: "Gunakan teknik Pomodoro (25 menit fokus, 5 menit istirahat), buat to-do list harian yang realistis, dan eliminasi distraksi seperti notifikasi sosmed selama jam kerja."
```

### 👨‍🏫 **Guru**
```
User: "Jelaskan photosynthesis dengan analogi sederhana"
AI: "Photosynthesis seperti 'dapur' tumbuhan. Daun adalah chef yang menggunakan sinar matahari sebagai 'api kompor', CO2 sebagai 'bahan utama', dan air sebagai 'bumbu' untuk memasak glukosa (makanan) sambil menghasilkan oksigen sebagai 'bonus'."
```

### 👩‍💻 **Programmer**
```
User: "Bagaimana optimasi query database yang lambat?"
AI: "Tambahkan index pada kolom yang sering di-query, gunakan EXPLAIN untuk analisis, batch queries untuk multiple operations, dan implementasikan connection pooling untuk mengurangi overhead koneksi."
```

## 🛠️ Teknologi yang Digunakan

- **Frontend**: Streamlit
- **Backend**: Python 3.7+
- **API**: OpenRouter.ai (akses ke multiple AI models)
- **Styling**: Custom CSS dengan animations
- **Libraries**: 
  - `streamlit` - Web framework
  - `requests` - HTTP client untuk API calls
  - `pillow` - Image processing
  - `json` - Data handling
  - `datetime` - Time management

## 📊 Struktur File

```
final_project.py
├── Page Configuration      # Setup halaman dan CSS animations
├── Role Configurations     # 3 role AI dengan settings
├── Model Configurations    # Daftar model gratis dan premium
├── Session State          # Management state aplikasi
├── Animation Functions    # Typing, thinking, success/error animations
├── Chatroom Management    # Multi-room chat system
├── Login System          # User registration
├── API Functions         # OpenRouter API integration
├── UI Components         # Header, sidebar, chat components
├── Chat Functionality    # Chat handling dengan animations
└── Main Application      # App entry point
```

## 🎨 Fitur Visual

### **Animasi CSS**
- **Gradient Background**: Animated 7-color gradient
- **Typing Effect**: Realistic typing animation untuk AI responses
- **Slide Animations**: Messages slide in dari kiri/kanan
- **Pulse Effects**: Parameter displays dengan glow effect
- **Hover Transitions**: Smooth transform pada interactive elements
- **Loading States**: Spinning loaders dan shimmer effects

### **Color Scheme**
- **Primary**: `#182c7a` (Deep Blue)
- **Secondary**: `#1d2f7e` hingga `#364092` (Blue Gradient)
- **Success**: `#2ecc71` (Green)
- **Error**: `#e74c3c` (Red)
- **White/Gray**: Clean contrast colors

## 🚨 Troubleshooting

### **Error 402 - Payment Required**
- Ganti ke model gratis (🆓)
- Top up credit di OpenRouter.ai
- Cek saldo di dashboard OpenRouter

### **API Key Tidak Valid**
- Pastikan API Key dimulai dengan `sk-or-`
- Generate API Key baru di OpenRouter
- Cek koneksi internet

### **Aplikasi Lambat**
- Turunkan typing speed di session state
- Kurangi max_tokens untuk respons lebih cepat
- Gunakan model yang lebih ringan

### **Animasi Tidak Muncul**
- Refresh browser (Ctrl+F5)
- Cek browser support untuk CSS animations
- Disable browser extensions yang memblokir CSS

### **Masalah lainnya**
- Jawaban AI kadang kemana mana
- Ketika mau menghapus room, riwayat chat harus di hapus terlebih dahulu

## 📈 Statistik dan Monitoring

Aplikasi menampilkan statistik real-time:
- **Total pesan** per chatroom
- **Jumlah pesan user** vs **AI**
- **Estimasi tokens** yang digunakan
- **Parameter aktif** (temperature, max_tokens)
- **Model aktif** dan role yang dipilih

## 🎓 Informasi Developer

- **Nama**: M. Hanif
- **Student ID**: REAPYTHON3WVTDF
- **Program**: AI-Python Bootcamp
- **Teknologi**: Python, Streamlit, OpenRouter API
- **Fokus**: Multi-role conversational AI dengan modern UX

---

⭐ **Selamat menggunakan Multi-Role AI Assistant!** ⭐

*Nikmati pengalaman chat AI yang interaktif dengan 3 role profesional, animasi menawan, dan fitur-fitur canggih untuk produktivitas maksimal.*
