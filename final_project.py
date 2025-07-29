import streamlit as st
import requests
import json
import time
from datetime import datetime
from PIL import Image

# ===========================
# PAGE CONFIGURATION
# ===========================
def configure_page():
    """Configure Streamlit page settings"""
    st.set_page_config(
        page_title="Multi-Role AI Assistant",
        page_icon="🎭",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for animations and styling
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Animated gradient background */
    .animated-bg {
        background: linear-gradient(-45deg, #182c7a, #1d2f7e, #233382, #283686, #2d398a, #323d8e, #364092);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Typing animation */
    .typing-animation {
        overflow: hidden;
        border-right: 3px solid #182c7a;
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: 0.1em;
        animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
    }
    
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent; }
        50% { border-color: #182c7a; }
    }
    
    /* Pulse animation for AI response */
    .ai-thinking {
        animation: pulse 2s infinite;
        background: linear-gradient(45deg, #182c7a, #1d2f7e);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    /* Slide in animation for messages */
    .slide-in-left {
        animation: slideInLeft 0.5s ease-out;
    }
    
    .slide-in-right {
        animation: slideInRight 0.5s ease-out;
    }
    
    @keyframes slideInLeft {
        from {
            transform: translateX(-100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    /* Role card animations */
    .role-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.5rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        border: 2px solid transparent;
    }
    
    .role-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        border-color: #182c7a;
    }
    
    .role-card.active {
        background: linear-gradient(135deg, #182c7a, #1d2f7e);
        color: white;
        transform: scale(1.05);
    }
    
    /* Glow effect */
    .glow {
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { box-shadow: 0 0 5px #182c7a, 0 0 10px #182c7a, 0 0 15px #182c7a; }
        to { box-shadow: 0 0 10px #182c7a, 0 0 20px #182c7a, 0 0 30px #182c7a; }
    }
    
    /* Loading spinner */
    .spinner {
        border: 4px solid #f3f3f3;
        border-top: 4px solid #182c7a;
        border-radius: 50%;
        width: 30px;
        height: 30px;
        animation: spin 1s linear infinite;
        margin: 0 auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Text shimmer effect */
    .shimmer {
        background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
        background-size: 200% 100%;
        animation: shimmer 2s infinite;
        color: transparent;
        background-clip: text;
        -webkit-background-clip: text;
    }
    
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    
    /* Sidebar enhancements */
    .sidebar-item {
        background: rgba(24, 44, 122, 0.1);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #182c7a;
        transition: all 0.3s ease;
    }
    
    .sidebar-item:hover {
        background: rgba(24, 44, 122, 0.2);
        transform: translateX(5px);
    }
    
    /* Chat message styling */
    .chat-message {
        animation: fadeInUp 0.5s ease-out;
        margin: 1rem 0;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Success/Error animations */
    .success-bounce {
        animation: bounceIn 0.6s ease-out;
    }
    
    .error-shake {
        animation: shake 0.6s ease-out;
    }
    
    @keyframes bounceIn {
        0% { transform: scale(0.3); opacity: 0; }
        50% { transform: scale(1.05); opacity: 1; }
        70% { transform: scale(0.9); }
        100% { transform: scale(1); }
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-10px); }
        20%, 40%, 60%, 80% { transform: translateX(10px); }
    }
    
    /* Button enhancements */
    .stButton > button {
        background: linear-gradient(45deg, #182c7a, #1d2f7e) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(24, 44, 122, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(24, 44, 122, 0.5) !important;
    }
    
    /* Parameter display enhancements */
    .param-display {
        background: linear-gradient(135deg, #182c7a, #1d2f7e);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        text-align: center;
        font-weight: bold;
        animation: paramGlow 3s ease-in-out infinite;
    }
    
    @keyframes paramGlow {
        0%, 100% { box-shadow: 0 0 5px rgba(24, 44, 122, 0.5); }
        50% { box-shadow: 0 0 20px rgba(24, 44, 122, 0.8); }
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# ===========================
# ROLE CONFIGURATIONS (3 ROLES ONLY) - FIXED
# ===========================
def get_role_configs():
    """Konfigurasi untuk 3 role AI"""
    return {
        "assistant": {
            "name": "👾 Asisten Umum",
            "icon": "👾",
            "color": "#182c7a",
            "gradient": "linear-gradient(135deg, #182c7a, #1d2f7e)",
            "description": "Bantuan umum untuk berbagai keperluan",
            "system_message": """Kamu adalah AI Assistant yang helpful dan efisien. Kamu bertugas memberikan jawaban yang SINGKAT, JELAS, dan LANGSUNG KE INTI.

PENTING - ATURAN RESPONS:
1. JAWAB MAKSIMAL 2-3 KALIMAT untuk pertanyaan sederhana
2. LANGSUNG ke point utama tanpa pembukaan panjang
3. HINDARI penjelasan berlebihan kecuali diminta detail
4. GUNAKAN bullet points hanya jika benar-benar perlu
5. BERIKAN jawaban praktis yang bisa langsung diterapkan

PERSONALITY: Ramah tapi efisien, informatif tapi tidak bertele-tele.

CAPABILITIES: 
- Menjawab pertanyaan umum dengan singkat
- Memberikan saran praktis
- Tips efektif tanpa panjang lebar
- Informasi akurat dan to-the-point

Berikan respons yang helpful namun SINGKAT dan EFISIEN.""",
            "recommended_models": ["mistralai/mistral-7b-instruct:free", "google/gemma-7b-it:free", "meta-llama/llama-3-8b-instruct:free"],
            "default_temperature": 0.3,  # Lebih rendah untuk jawaban lebih konsisten
            "default_max_tokens": 150,   # Lebih rendah untuk jawaban lebih singkat
            "sample_questions": [
                "Bagaimana cara meningkatkan produktivitas kerja?",
                "Apa tips mengatur waktu yang efektif?",
                "Rekomendasi aplikasi untuk belajar bahasa asing"
            ]
        },
        "guru": {
            "name": "👨‍🏫 Guru",
            "icon": "👨‍🏫",
            "color": "#233382",
            "gradient": "linear-gradient(135deg, #233382, #283686)",
            "description": "Pendidikan & pembelajaran interaktif",
            "system_message": """Kamu adalah Prof. AI, guru yang mengajar dengan EFISIEN dan LANGSUNG KE INTI.

PENTING - ATURAN MENGAJAR:
1. JAWAB MAKSIMAL 2-3 KALIMAT untuk konsep sederhana
2. LANGSUNG jelaskan inti materi tanpa pembukaan panjang
3. GUNAKAN analogi sederhana hanya jika benar-benar membantu
4. BERIKAN contoh SINGKAT dan KONKRET
5. HINDARI teori berlebihan, fokus pada pemahaman praktis

TEACHING APPROACH:
- Langsung ke definisi/konsep utama
- Contoh singkat dan mudah dipahami
- Aplikasi praktis dalam 1-2 kalimat
- Motivasi singkat hanya jika relevan

PERSONALITY: Sabar, jelas, tapi tidak bertele-tele.

Berikan penjelasan yang MUDAH DIPAHAMI namun SINGKAT dan EFEKTIF.""",
            "recommended_models": ["mistralai/mistral-7b-instruct:free", "google/gemma-7b-it:free", "meta-llama/llama-3-8b-instruct:free"],
            "default_temperature": 0.4,
            "default_max_tokens": 200,
            "sample_questions": [
                "Jelaskan konsep photosynthesis dengan analogi sederhana",
                "Strategi belajar matematika yang efektif untuk siswa SMA",
                "Bagaimana cara menulis essay yang baik dan benar?"
            ]
        },
        "programmer": {
            "name": "👩‍💻 Programmer",
            "icon": "👩‍💻",
            "color": "#2d398a",
            "gradient": "linear-gradient(135deg, #2d398a, #323d8e)",
            "description": "Coding, debugging & tech solutions",
            "system_message": """Kamu adalah Senior Dev AI yang memberikan solusi coding SINGKAT dan EFEKTIF.

PENTING - ATURAN CODING:
1. JAWAB MAKSIMAL 1-2 KALIMAT penjelasan untuk pertanyaan sederhana
2. LANGSUNG berikan kode/solusi tanpa penjelasan panjang
3. GUNAKAN comment dalam kode untuk penjelasan singkat
4. FOKUS pada solusi yang WORKING dan PRAKTIS
5. HINDARI penjelasan teori panjang kecuali diminta

CODING APPROACH:
- Working code first dengan comment singkat
- Penjelasan teknis minimal tapi jelas
- Best practices dalam comment
- Alternative approach hanya jika diminta

PERSONALITY: Logical, solution-focused, straight to the point.

Berikan solusi coding yang EFEKTIF dan LANGSUNG APPLICABLE.""",
            "recommended_models": ["mistralai/mistral-7b-instruct:free", "google/gemma-7b-it:free", "meta-llama/llama-3-8b-instruct:free"],
            "default_temperature": 0.2,  # Sangat rendah untuk kode yang konsisten
            "default_max_tokens": 250,
            "sample_questions": [
                "Bagaimana cara optimasi performa query database yang lambat?",
                "Jelaskan perbedaan async/await dan Promise di JavaScript",
                "Review dan improve kode Python saya untuk bug dan performance"
            ]
        }
    }

# ===========================
# MODEL CONFIGURATIONS
# ===========================
def get_available_models():
    """Daftar model AI yang tersedia"""
    return {
        # ⭐ GRATIS - Recommended untuk pemula
        "mistralai/mistral-7b-instruct:free": "🆓 Mistral 7B (Free) ⭐",
        "google/gemma-7b-it:free": "🆓 Google Gemma 7B (Free)",
        "meta-llama/llama-3-8b-instruct:free": "🆓 Llama 3 8B (Free)",
        "huggingface/zephyr-7b-beta:free": "🆓 Zephyr 7B (Free)",
        "openchat/openchat-7b:free": "🆓 OpenChat 7B (Free)",
        
        # 💰 PREMIUM - Perlu kredit
        "openai/gpt-4o": "💰 GPT-4o (Premium)",
        "openai/gpt-4o-mini": "💰 GPT-4o Mini (Premium)", 
        "anthropic/claude-3.5-sonnet": "💰 Claude 3.5 Sonnet (Premium)",
        "anthropic/claude-3-haiku": "💰 Claude 3 Haiku (Premium)",
        "google/gemini-pro": "💰 Gemini Pro (Premium)",
        "mistralai/mistral-large": "💰 Mistral Large (Premium)",
        "mistralai/codestral": "💰 Codestral (Premium)"
    }

# ===========================
# SESSION STATE MANAGEMENT
# ===========================
def initialize_session_state():
    """Inisialisasi variabel session state"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False
    if "current_role" not in st.session_state:
        st.session_state.current_role = "assistant"  # Default role
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = "mistralai/mistral-7b-instruct:free"
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.3  # Default lebih rendah
    if "max_tokens" not in st.session_state:
        st.session_state.max_tokens = 150   # Default lebih rendah
    if "typing_speed" not in st.session_state:
        st.session_state.typing_speed = 0.02  # Speed for typing animation
    if "chatrooms" not in st.session_state:
        st.session_state.chatrooms = {"Default": []}
    if "current_chatroom" not in st.session_state:
        st.session_state.current_chatroom = "Default"
    if "chatroom_counter" not in st.session_state:
        st.session_state.chatroom_counter = 1

# ===========================
# SYSTEM MESSAGE
# ===========================
def get_system_message():
    """Return the system message based on current role"""
    user_name = st.session_state.get("user_name", "")
    current_role = st.session_state.get("current_role", "assistant")
    role_configs = get_role_configs()
    
    name_context = f"Nama pengguna adalah {user_name}. " if user_name else ""
    base_message = role_configs[current_role]["system_message"]
    
    return {
        "role": "system",
        "content": f"""{base_message} 

{name_context}

WAJIB DIINGAT:
- Panggil pengguna dengan nama mereka jika ada
- SELALU berikan respons SINGKAT dan EFISIEN
- MAKSIMAL 2-3 kalimat untuk pertanyaan sederhana
- LANGSUNG ke inti tanpa pembukaan panjang
- HINDARI penjelasan berlebihan
- FOKUS pada jawaban praktis dan aplikatif"""
    }

# ===========================
# ANIMATION FUNCTIONS
# ===========================
def show_typing_animation(text, container):
    """Show typing animation for AI responses"""
    typing_placeholder = container.empty()
    displayed_text = ""
    
    for char in text:
        displayed_text += char
        typing_placeholder.markdown(f"{displayed_text}▌")
        time.sleep(st.session_state.typing_speed)
    
    typing_placeholder.markdown(displayed_text)

def show_thinking_animation():
    """Show AI thinking animation"""
    return st.markdown("""
    <div class="ai-thinking">
        <div class="spinner"></div>
        <p style="margin-top: 10px;">🧠 AI sedang berpikir...</p>
    </div>
    """, unsafe_allow_html=True)

def show_success_message(message):
    """Show animated success message"""
    st.markdown(f"""
    <div class="success-bounce" style="background: linear-gradient(45deg, #2ecc71, #27ae60); 
         color: white; padding: 1rem; border-radius: 10px; text-align: center; margin: 1rem 0;">
        ✅ {message}
    </div>
    """, unsafe_allow_html=True)

def show_error_message(message):
    """Show animated error message"""
    st.markdown(f"""
    <div class="error-shake" style="background: linear-gradient(45deg, #e74c3c, #c0392b); 
         color: white; padding: 1rem; border-radius: 10px; text-align: center; margin: 1rem 0;">
        ❌ {message}
    </div>
    """, unsafe_allow_html=True)

# ===========================
# CHATROOM MANAGEMENT - FIXED
# ===========================
def get_current_messages():
    """Get messages for current chatroom"""
    current_room = st.session_state.current_chatroom
    if current_room not in st.session_state.chatrooms:
        st.session_state.chatrooms[current_room] = []
    return st.session_state.chatrooms[current_room]

def save_current_messages(messages):
    """Save messages to current chatroom"""
    current_room = st.session_state.current_chatroom
    st.session_state.chatrooms[current_room] = messages

def switch_chatroom(room_name):
    """Switch to different chatroom"""
    # Save current messages
    if st.session_state.messages:
        save_current_messages(st.session_state.messages)
    
    # Switch room
    st.session_state.current_chatroom = room_name
    
    # Load messages for new room
    st.session_state.messages = get_current_messages()

def create_new_chatroom():
    """Create new chatroom"""
    new_name = f"Room {st.session_state.chatroom_counter}"
    st.session_state.chatrooms[new_name] = []
    st.session_state.chatroom_counter += 1
    switch_chatroom(new_name)
    return new_name

def delete_chatroom(room_name):
    """Delete chatroom - FIXED: Automatic clear messages"""
    if room_name != "Default" and len(st.session_state.chatrooms) > 1:
        # Hapus room dari dictionary
        del st.session_state.chatrooms[room_name]
        
        # Jika room yang dihapus adalah room aktif, pindah ke Default
        if st.session_state.current_chatroom == room_name:
            switch_chatroom("Default")
        
        # Clear messages jika room yang dihapus adalah yang aktif saat ini
        if st.session_state.current_chatroom == room_name:
            st.session_state.messages = []
            
        return True
    return False

# ===========================
# LOGIN SYSTEM
# ===========================
def render_login():
    """Tampilkan form login dengan animasi"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.form("registration_form"):
            st.markdown("### 📝 Registrasi Pengguna")
            
            name = st.text_input(
                "Nama Panggilan *",
                placeholder="Contoh: Ucup atau mawar",
                help="Nama yang akan digunakan AI untuk memanggil Anda"
            )
            
            api_key = st.text_input(
                "OpenRouter API Key *",
                type="password",
                placeholder="sk-or-...",
                help="API Key diperlukan untuk mengakses layanan AI"
            )
            
            st.markdown("---")
            st.markdown("### 🎭 Pilih Role AI Favoritmu")
            
            # Show role preview with animations
            role_configs = get_role_configs()
            cols = st.columns(3)
            
            for idx, (role_key, config) in enumerate(role_configs.items()):
                with cols[idx]:
                    st.markdown(f"""
                    <div class="role-card" style="animation-delay: {idx * 0.2}s;">
                        <div style="font-size: 3rem; text-align: center;">{config['icon']}</div>
                        <h4 style="text-align: center; margin: 0.5rem 0; color: {config['color']};">
                            {config['name'].replace(config['icon'], '').strip()}
                        </h4>
                        <p style="text-align: center; font-size: 0.9rem; color: #666;">
                            {config['description']}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Info section with animations
            with st.expander("ℹ️ Informasi Penting", expanded=False):
                st.markdown("""
                **🔑 Tentang API Key:**
                - Dapatkan **GRATIS** di: [OpenRouter.ai/keys](https://openrouter.ai/keys)
                - API Key diperlukan untuk mengakses berbagai model AI
                - Tersedia model gratis dan premium
                
                **🎭 3 Role AI Profesional:**
                - **👾 Asisten Umum**: Bantuan untuk berbagai keperluan sehari-hari
                - **👨‍🏫 Guru**: Pembelajaran interaktif semua mata pelajaran  
                - **👩‍💻 Programmer**: Coding, debugging, tech solutions
                
                **✨ Fitur Unggulan:**
                - Interface dengan animasi menarik
                - Respons AI dengan typing effect
                - Transisi yang smooth dan modern
                - Parameter yang dapat disesuaikan
                
                **🔒 Keamanan:**
                - API Key Anda aman dan tidak disimpan permanen
                - Hanya digunakan selama session chat berlangsung
                """)
            
            submit = st.form_submit_button("🚀 Daftar & Mulai", type="primary", use_container_width=True)
            
            if submit:
                if name.strip() and api_key.strip():
                    st.session_state.user_name = name.strip()
                    st.session_state.api_key = api_key.strip()
                    st.session_state.is_logged_in = True
                    show_success_message(f"Selamat datang {name}! Registrasi berhasil!")
                    time.sleep(1)
                    st.rerun()
                else:
                    show_error_message("Nama panggilan dan API Key wajib diisi!")
                    if not api_key.strip():
                        st.info("💡 Dapatkan API Key gratis di: https://openrouter.ai/keys")

# ===========================
# API FUNCTIONS
# ===========================
def get_api_key():
    """Mendapatkan API key"""
    if st.session_state.api_key:
        return st.session_state.api_key
    try:
        return st.secrets["openrouter_api_key"]
    except:
        return None

def get_ai_response(user_input):
    """Mendapatkan respons AI dari OpenRouter API"""
    api_key = get_api_key()
    if not api_key:
        show_error_message("API key tidak ditemukan. Silakan masukkan API key di sidebar.")
        return None
    
    # Prepare messages dengan system message
    messages = [get_system_message()]
    for message in st.session_state.messages:
        if message["role"] != "system":
            messages.append(message)
    messages.append({"role": "user", "content": user_input})

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            },
            data=json.dumps({
                "model": st.session_state.selected_model,
                "messages": messages,
                "max_tokens": st.session_state.max_tokens,
                "temperature": st.session_state.temperature,
            })
        )
        
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 402:
            st.markdown("""
            <div class="error-shake" style="background: linear-gradient(45deg, #e74c3c, #c0392b); 
                 color: white; padding: 1.5rem; border-radius: 15px; margin: 1rem 0;">
                <h3 style="margin: 0 0 1rem 0;">💳 Error 402: Payment Required</h3>
                <p><strong>🔧 Solusi:</strong></p>
                <ul>
                    <li><strong>Ganti ke model GRATIS</strong> (yang ada icon 🆓)</li>
                    <li><strong>Top up kredit</strong> di <a href="https://openrouter.ai/credits" style="color: #fff;">OpenRouter.ai</a></li>
                    <li><strong>Cek saldo</strong> di dashboard OpenRouter</li>
                </ul>
                <p><strong>💡 Model gratis yang direkomendasikan:</strong><br>
                🆓 Mistral 7B, Google Gemma 7B, Llama 3 8B</p>
            </div>
            """, unsafe_allow_html=True)
            return None
        else:
            show_error_message(f"HTTP Error {e.response.status_code}: {e}")
            return None
    except Exception as e:
        show_error_message(f"Terjadi kesalahan: {e}")
        return None

# ===========================
# UI COMPONENTS
# ===========================
def render_header():
    """Render animated header with current role"""
    user_name = st.session_state.get("user_name", "")
    current_role = st.session_state.get("current_role", "assistant")
    role_configs = get_role_configs()
    current_config = role_configs[current_role]
    
def render_welcome_message():
    """Tampilkan pesan selamat datang dengan animasi"""
    if not get_current_messages():
        user_name = st.session_state.get("user_name", "")
        current_role = st.session_state.get("current_role", "assistant")
        role_configs = get_role_configs()
        current_config = role_configs[current_role]
        
        with st.chat_message("assistant", avatar=current_config['icon']):
            st.markdown(f"""
            <div class="chat-message">
                <div style="background: {current_config['gradient']}; color: white; 
                           padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
                    <h3 style="margin: 0 0 1rem 0;">{current_config['icon']} Selamat datang {user_name if user_name else ""}!</h3>
                    <p style="margin: 0;">Saya adalah <strong>{current_config['name']}</strong> yang siap membantu Anda dengan {current_config['description'].lower()}.</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Sample questions with animation
            st.markdown("**🌟 Contoh pertanyaan yang bisa Anda ajukan:**")
            for i, question in enumerate(current_config['sample_questions'], 1):
                st.markdown(f"""
                <div class="slide-in-left" style="animation-delay: {i * 0.2}s; 
                           background: rgba(24, 44, 122, 0.1); padding: 0.8rem; 
                           border-radius: 10px; margin: 0.5rem 0; 
                           border-left: 4px solid {current_config['color']};">
                    <strong>{i}.</strong> {question}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="glow" style="background: linear-gradient(45deg, #323d8e, #364092); 
                         color: white; padding: 1rem; border-radius: 15px; margin: 1rem 0; text-align: center;">
                ✨ Mulai percakapan dengan mengetik pertanyaan di bawah!
            </div>
            <div style="text-align: center; margin-top: 1rem; font-size: 0.9rem; color: #666;">
                💡 <em>Multi-Role AI Assistant by <strong>M. Hanif</strong> - AI-Python Bootcamp</em>
            </div>
            """, unsafe_allow_html=True)

def render_chat_history():
    """Tampilkan riwayat chat dengan animasi"""
    current_role = st.session_state.get("current_role", "assistant")
    role_configs = get_role_configs()
    current_icon = role_configs[current_role]['icon']
    
    for i, message in enumerate(get_current_messages()):
        if message["role"] == "user":
            with st.chat_message("user", avatar="👤"):
                st.markdown(f"""
                <div class="slide-in-right chat-message" style="animation-delay: {i * 0.1}s;">
                    {message["content"]}
                </div>
                """, unsafe_allow_html=True)
        else:
            with st.chat_message("assistant", avatar=current_icon):
                st.markdown(f"""
                <div class="slide-in-left chat-message" style="animation-delay: {i * 0.1}s;">
                    {message["content"]}
                </div>
                """, unsafe_allow_html=True)

def update_role_defaults():
    """Update temperature dan max_tokens berdasarkan role yang dipilih"""
    current_role = st.session_state.get("current_role", "assistant")
    role_configs = get_role_configs()
    current_config = role_configs[current_role]
    
    # Update defaults jika belum pernah diubah manual
    if f"manual_temp_{current_role}" not in st.session_state:
        st.session_state.temperature = current_config["default_temperature"]
    if f"manual_tokens_{current_role}" not in st.session_state:
        st.session_state.max_tokens = current_config["default_max_tokens"]

def render_sidebar():
    """Tampilkan sidebar dengan animasi dan styling modern - FIXED: Reorder sections"""
    with st.sidebar:
        # Developer info - ANIMATED
        st.markdown(f"""
        <div class="sidebar-item glow">
            <h3 style="margin: 0 0 0.5rem 0; color: #182c7a;">👨‍💻 Developer</h3>
            <p style="margin: 0;"><strong>Nama:</strong> M. Hanif</p>
            <p style="margin: 0;"><strong>ID:</strong> REAPYTHON3WVTDF</p>
            <p style="margin: 0;"><strong>Class:</strong> AI-Python Bootcamp</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # CHATROOM MANAGEMENT - MOVED HERE (AFTER Developer info)
        st.markdown("### 💬 Chatrooms")
        
        if st.session_state.is_logged_in:
            current_role = st.session_state.get("current_role", "assistant")
            role_configs = get_role_configs()
            current_config = role_configs[current_role]
            
            # Current chatroom display
            current_room = st.session_state.current_chatroom
            total_rooms = len(st.session_state.chatrooms)
            current_msgs = len(get_current_messages())
            
            st.markdown(f"""
            <div style="background: {current_config['gradient']}; color: white; 
                        padding: 1rem; border-radius: 15px; text-align: center; margin-bottom: 1rem;">
                <div style="font-size: 1.5rem;">💬</div>
                <h4 style="margin: 0; color: white;">{current_room}</h4>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;">
                    {current_msgs} pesan | {total_rooms} rooms
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Room selector
            col1, col2 = st.columns([3, 1])
            with col1:
                selected_room = st.selectbox(
                    "Pilih Room:",
                    options=list(st.session_state.chatrooms.keys()),
                    index=list(st.session_state.chatrooms.keys()).index(current_room),
                    key="room_selector"
                )
            with col2:
                if st.button("➕", help="Buat room baru", key="new_room_btn"):
                    new_room = create_new_chatroom()
                    show_success_message(f"Room '{new_room}' dibuat!")
                    time.sleep(0.5)
                    st.rerun()
            
            # Switch room if different
            if selected_room != current_room:
                switch_chatroom(selected_room)
                show_success_message(f"Pindah ke '{selected_room}'!")
                time.sleep(0.5)
                st.rerun()
            
            # Room actions
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔄 Rename Room", key="rename_room", disabled=current_room=="Default"):
                    st.session_state.show_rename_input = True
            with col2:
                if st.button("🗑️ Delete Room", key="delete_room", disabled=current_room=="Default" or total_rooms<=1):
                    if delete_chatroom(current_room):
                        show_success_message(f"Room '{current_room}' dihapus!")
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        show_error_message("Gagal menghapus room!")
            
            # Rename input (conditional)
            if hasattr(st.session_state, 'show_rename_input') and st.session_state.show_rename_input:
                with st.form("rename_form"):
                    new_name = st.text_input("Nama baru:", value=current_room)
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.form_submit_button("✅ Simpan"):
                            if new_name and new_name != current_room and new_name not in st.session_state.chatrooms:
                                # Rename room
                                st.session_state.chatrooms[new_name] = st.session_state.chatrooms.pop(current_room)
                                st.session_state.current_chatroom = new_name
                                st.session_state.show_rename_input = False
                                show_success_message(f"Room diubah ke '{new_name}'!")
                                time.sleep(0.5)
                                st.rerun()
                            else:
                                show_error_message("Nama tidak valid atau sudah ada!")
                    with col2:
                        if st.form_submit_button("❌ Batal"):
                            st.session_state.show_rename_input = False
                            st.rerun()
            
            # All rooms overview
            st.markdown("**📋 Semua Rooms:**")
            for room_name, messages in st.session_state.chatrooms.items():
                is_current = room_name == current_room
                icon = "📍" if is_current else "💬"
                msg_count = len(messages)
                
                st.markdown(f"""
                <div style="{'background: rgba(24, 44, 122, 0.2);' if is_current else 'background: rgba(24, 44, 122, 0.05);'} 
                             padding: 0.5rem; border-radius: 8px; margin: 0.3rem 0;
                             border-left: 4px solid {'#182c7a' if is_current else '#ccc'};">
                    {icon} <strong>{room_name}</strong> ({msg_count} pesan)
                </div>
                """, unsafe_allow_html=True)
            
            # Clear chat with animation
            if st.button("🗑️ Clear Chat", type="secondary"):
                st.session_state.messages = []
                save_current_messages([])
                show_success_message("Chat berhasil dibersihkan!")
                time.sleep(0.5)
                st.rerun()
        
        st.markdown("---")
        
        # User info - ANIMATED
        if st.session_state.is_logged_in:
            available_models = get_available_models()
            
            st.markdown(f"""
            <div class="sidebar-item" style="background: {current_config['gradient']}; color: white;">
                <h3 style="margin: 0 0 0.5rem 0;">👤 User Info</h3>
                <p style="margin: 0;"><strong>Nama:</strong> {st.session_state.user_name}</p>
                <p style="margin: 0;"><strong>Role:</strong> {current_config['name']}</p>
                <p style="margin: 0;"><strong>Model:</strong> {available_models[st.session_state.selected_model][:20]}...</p>
                <div style="display: flex; gap: 1rem; margin-top: 0.5rem;">
                    <div class="param-display" style="flex: 1;">Temp: {st.session_state.temperature}</div>
                    <div class="param-display" style="flex: 1;">Tokens: {st.session_state.max_tokens}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔄 Logout & Ganti User", type="secondary"):
                for key in ["user_name", "is_logged_in", "messages", "api_key"]:
                    if key in st.session_state:
                        del st.session_state[key]
                show_success_message("Logout berhasil!")
                time.sleep(1)
                st.rerun()
        
        st.markdown("---")
        
        # Role Selector with ANIMATED CARDS
        st.markdown("### 🎭 Pilih Role AI")
        role_configs = get_role_configs()
        
        # Create animated role cards
        for role_key, config in role_configs.items():
            is_active = role_key == st.session_state.current_role
            card_class = "role-card active" if is_active else "role-card"
            
            if st.button(f"{config['icon']} {config['name'].replace(config['icon'], '').strip()}", 
                        key=f"role_{role_key}", 
                        help=config['description'],
                        use_container_width=True):
                if role_key != st.session_state.current_role:
                    st.session_state.current_role = role_key
                    # Clear current room when switching roles
                    st.session_state.messages = []
                    save_current_messages([])
                    # Set recommended model for new role
                    recommended_models = config["recommended_models"]
                    available_models = get_available_models()
                    for model in recommended_models:
                        if model in available_models:
                            st.session_state.selected_model = model
                            break
                    # Update role defaults
                    update_role_defaults()
                    show_success_message(f"Beralih ke {config['name']}!")
                    time.sleep(0.5)
                    st.rerun()
        
        # Show current role info with animation
        current_config = role_configs[st.session_state.current_role]
        st.markdown(f"""
        <div style="background: {current_config['gradient']}; color: white; 
                    padding: 1.5rem; border-radius: 15px; margin: 1rem 0; text-align: center;
                    animation: pulse 3s infinite;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">{current_config['icon']}</div>
            <h4 style="margin: 0; color: white;">Role Aktif</h4>
            <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">{current_config['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Model Selection with animations
        st.markdown("### 👾 AI Model")
        available_models = get_available_models()
        recommended_models = current_config["recommended_models"]
        
        # Show recommended models first
        st.markdown("**⭐ Rekomendasi untuk role ini:**")
        for model in recommended_models[:3]:
            if model in available_models:
                if st.button(f"{available_models[model]}", key=f"rec_{model}"):
                    st.session_state.selected_model = model
                    show_success_message("Model berhasil diubah!")
                    time.sleep(0.5)
                    st.rerun()
        
        st.markdown("**📋 Semua Model:**")
        selected_model = st.selectbox(
            "Model:",
            options=list(available_models.keys()),
            format_func=lambda x: available_models[x],
            index=list(available_models.keys()).index(st.session_state.selected_model)
        )
        if selected_model != st.session_state.selected_model:
            st.session_state.selected_model = selected_model
        
        st.markdown("---")
        
        # AI Parameters Section with animations
        st.markdown("### ⚙️ Parameter AI")
        
        # Temperature Control with animated display
        col1, col2 = st.columns([3, 1])
        with col1:
            new_temperature = st.slider(
                "🌡️ Temperature",
                min_value=0.0,
                max_value=1.0,
                value=st.session_state.temperature,
                step=0.1,
                help="Mengontrol kreativitas AI. Rendah = lebih konsisten, Tinggi = lebih kreatif"
            )
        with col2:
            st.markdown(f"""
            <div class="param-display" style="margin-top: 1rem;">
                {new_temperature}
            </div>
            """, unsafe_allow_html=True)
        
        if new_temperature != st.session_state.temperature:
            st.session_state.temperature = new_temperature
            st.session_state[f"manual_temp_{st.session_state.current_role}"] = True
        
        # Max Tokens Control with animated display
        col1, col2 = st.columns([3, 1])
        with col1:
            new_max_tokens = st.slider(
                "📝 Max Tokens",
                min_value=100,
                max_value=2000,
                value=st.session_state.max_tokens,
                step=50,
                help="Mengontrol panjang respons AI. Lebih tinggi = respons lebih panjang"
            )
        with col2:
            st.markdown(f"""
            <div class="param-display" style="margin-top: 1rem;">
                {new_max_tokens}
            </div>
            """, unsafe_allow_html=True)
        
        if new_max_tokens != st.session_state.max_tokens:
            st.session_state.max_tokens = new_max_tokens
            st.session_state[f"manual_tokens_{st.session_state.current_role}"] = True
        
        # Parameter indicators with role recommendations
        st.markdown("**🎯 Rekomendasi untuk role ini:**")
        default_temp = current_config["default_temperature"]
        default_tokens = current_config["default_max_tokens"]
        
        temp_status = "✅" if abs(st.session_state.temperature - default_temp) < 0.05 else "⚠️"
        tokens_status = "✅" if abs(st.session_state.max_tokens - default_tokens) < 50 else "⚠️"
        
        st.markdown(f"""
        <div style="background: rgba(24, 44, 122, 0.1); padding: 1rem; border-radius: 10px;">
            <p style="margin: 0;">{temp_status} Temperature: {default_temp}</p>
            <p style="margin: 0;">{tokens_status} Max Tokens: {default_tokens}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Reset to role defaults button
        if st.button("🔄 Reset ke Default Role", help="Reset parameter sesuai rekomendasi role"):
            st.session_state.temperature = default_temp
            st.session_state.max_tokens = default_tokens
            # Remove manual flags
            current_role = st.session_state.current_role
            if f"manual_temp_{current_role}" in st.session_state:
                del st.session_state[f"manual_temp_{current_role}"]
            if f"manual_tokens_{current_role}" in st.session_state:
                del st.session_state[f"manual_tokens_{current_role}"]
            show_success_message("Parameter direset ke default!")
            time.sleep(0.5)
            st.rerun()
        
        st.markdown("---")
        
        # API Key status with animation
        if not st.session_state.api_key:
            st.markdown("""
            <div class="error-shake" style="background: linear-gradient(45deg, #e74c3c, #c0392b); 
                 color: white; padding: 1rem; border-radius: 10px; text-align: center;">
                🔑 API Key tidak ditemukan!
            </div>
            """, unsafe_allow_html=True)
            st.info("💡 Logout dan daftar ulang dengan API Key yang valid")
        else:
            st.markdown("""
            <div class="success-bounce" style="background: linear-gradient(45deg, #2ecc71, #27ae60); 
                 color: white; padding: 1rem; border-radius: 10px; text-align: center;">
                ✅ API Key aktif!
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Chat stats with animations
        if st.session_state.messages:
            total = len(st.session_state.messages)
            user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
            ai_msgs = len([m for m in st.session_state.messages if m["role"] == "assistant"])
            
            st.markdown("""
            <div class="sidebar-item" style="background: linear-gradient(135deg, #182c7a, #1d2f7e); color: white;">
                <h3 style="margin: 0 0 0.5rem 0;">📊 Chat Statistics</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
                    <div class="param-display">Total: {}</div>
                    <div class="param-display">User: {}</div>
                    <div class="param-display">AI: {}</div>
                    <div class="param-display">Tokens: ~{}</div>
                </div>
            </div>
            """.format(total, user_msgs, ai_msgs, 
                      sum(len(m["content"]) for m in st.session_state.messages) // 4), 
            unsafe_allow_html=True)

# ===========================
# CHAT FUNCTIONALITY
# ===========================
def handle_chat():
    """Handle chat input dan response dengan animasi"""
    current_role = st.session_state.get("current_role", "assistant")
    role_configs = get_role_configs()
    current_icon = role_configs[current_role]['icon']
    
    if prompt := st.chat_input(f"💬 Chat dengan {role_configs[current_role]['name']}...", key="chat_input"):
        # Add user message dengan animasi
        current_messages = get_current_messages()
        current_messages.append({"role": "user", "content": prompt})
        st.session_state.messages = current_messages
        save_current_messages(current_messages)
        
        # Display user message dengan slide animation
        with st.chat_message("user", avatar="👤"):
            st.markdown(f"""
            <div class="slide-in-right chat-message">
                {prompt}
            </div>
            """, unsafe_allow_html=True)
        
        # Get and display AI response dengan animasi
        with st.chat_message("assistant", avatar=current_icon):
            
            # Get AI response
            ai_response = get_ai_response(prompt)
            
            if ai_response:
                # Show typing animation for response
                response_container = st.empty()
                displayed_text = ""
                
                for char in ai_response:
                    displayed_text += char
                    response_container.markdown(f"""
                    <div class="slide-in-left chat-message">
                        {displayed_text}▌
                    </div>
                    """, unsafe_allow_html=True)
                    time.sleep(st.session_state.typing_speed)
                
                # Final response without cursor
                response_container.markdown(f"""
                <div class="slide-in-left chat-message">
                    {ai_response}
                </div>
                """, unsafe_allow_html=True)
                
                current_messages = get_current_messages()
                current_messages.append({"role": "assistant", "content": ai_response})
                st.session_state.messages = current_messages
                save_current_messages(current_messages)
                
                # Show response stats dengan animasi
                response_length = len(ai_response)
                estimated_tokens = response_length // 4
                st.markdown(f"""
                <div class="param-display" style="margin-top: 1rem; font-size: 0.8rem;">
                    📊 {response_length} karakter (~{estimated_tokens} tokens) | 
                    🌡️ {st.session_state.temperature} | 📝 {st.session_state.max_tokens}
                </div>
                """, unsafe_allow_html=True)
            else:
                show_error_message("Gagal mendapat respons. Coba lagi.")

# ===========================
# MAIN APPLICATION
# ===========================
def main():
    """Fungsi aplikasi utama"""
    configure_page()
    initialize_session_state()
    
    # Render sidebar
    render_sidebar()
    
    # Check login status
    if not st.session_state.is_logged_in:
        render_login()
        return
    
    # Main content dengan animasi
    render_header()
    render_welcome_message()
    render_chat_history()
    handle_chat()
    
    # Animated Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <div style="background: linear-gradient(45deg, #182c7a, #1d2f7e); 
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                    font-size: 1.2rem; font-weight: bold; margin-bottom: 0.5rem;">
            🎭 Multi-Role AI Assistant
        </div>
        <p style="margin: 0;">✨ Pengalaman AI yang Interaktif dan Menawan</p>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">
            💻 Dikembangkan oleh <strong>M. Hanif</strong> | 🎓 AI-Python Bootcamp | 🆔 REAPYTHON3WVTDF
        </p>
    </div>
    """, unsafe_allow_html=True)

# ===========================
# RUN APPLICATION
# ===========================
if __name__ == "__main__":
    main()
