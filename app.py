# app.py
import streamlit as st
from google import genai
from PIL import Image

# Page Configuration for High-End Hackathon UI
st.set_page_config(
    page_title="Agri-Sustain AI | Autonomous Agricultural Intelligence",
    page_icon="🌱",
    layout="wide"
)

# Custom Styling for Professional Interface
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        border: 1px solid #e2e8f0;
    }
    .stTabs [aria-selected="true"] {
        background-color: #16a34a !important;
        color: white !important;
    }
    .agent-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #16a34a;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌱 Agri-Sustain AI: Autonomous Agricultural Intelligence Ecosystem")
st.markdown("### Bridging smallholder farmers with crop pathology, climate risk mitigation, and fair-market optimization[cite: 2].")
st.markdown("---")

# Initialize Gemini Client using Streamlit Secrets or Sidebar Input
api_key = None
try:
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass

st.sidebar.header("🛠️ System Configuration")
if not api_key:
    api_key = st.sidebar.text_input("Enter Google Gemini API Key", type="password")

if not api_key:
    st.sidebar.warning("⚠️ Please provide a Gemini API key to activate the ecosystem.")
    st.info("💡 **Judge Preview:** Enter your free Google AI Studio API key in the sidebar to run multimodal crop diagnostics, weather forecasting, and fair-pricing negotiations.")
    
    st.markdown("### 🤖 Integrated Ecosystem Architecture")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 🔬 Vision-Based Crop Doctor")
        st.write("Instant AI-powered diagnoses and localized treatment plans from leaf photos[cite: 2].")
    with c2:
        st.markdown("#### 🌤️ Weather Risk Copilot")
        st.write("Proactive analysis of frost, flood, or pest risks based on regional weather shifts[cite: 2].")
    with c3:
        st.markdown("#### ⚖️ Fair-Market Price Optimizer")
        st.write("Connects smallholders directly with verified wholesale buyers, eliminating middlemen[cite: 2].")
    st.stop()

# Initialize official Google GenAI client
client = genai.Client(api_key=api_key)

# Main Application Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🧬 Vision Crop Doctor", 
    "🌤️ Weather Risk Copilot", 
    "⚖️ Fair-Market Optimizer", 
    "📊 Pitch & SDG Blueprint"
])

# --- TAB 1: VISION CROP DOCTOR ---
with tab1:
    st.header("Vision-Based Crop Doctor")
    st.write("Upload a photo of your crop to run instant computer vision pathology and receive customized treatment actions[cite: 2].")
    
    col_img, col_form = st.columns([1, 1])
    
    with col_img:
        uploaded_file = st.file_uploader("Upload Leaf / Plant Image", type=["jpg", "jpeg", "png"])
        crop_name = st.selectbox("Select Crop Type", ["Wheat", "Tomato", "Rice", "Cotton", "Sugarcane", "Potato", "Corn"])
        growth_stage = st.selectbox("Growth Stage", ["Seedling", "Vegetative", "Flowering", "Fruiting/Maturity"])

    with col_form:
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption=f"Sample: {crop_name} ({growth_stage})", use_column_width=True)
        else:
            st.info("Awaiting image upload for diagnostic analysis...")

    if uploaded_file is not None:
        if st.button("🚀 Run Diagnostic Scan", type="primary"):
            with st.spinner("Dr. Agro analyzing cellular damage and disease vectors..."):
                try:
                    prompt = f"You are Dr. Agro, an expert plant pathologist. Analyze this {crop_name} image at the {growth_stage} stage. Provide: 1) Disease Name / Health Status, 2) Confidence Index, 3) Root Cause / Pathology, and 4) Immediate Organic & Chemical Treatment Plan."
                    
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    
                    st.markdown("### 📋 Pathology & Treatment Report")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Diagnosis failed: {e}")

# --- TAB 2: WEATHER RISK COPILOT ---
with tab2:
    st.header("Hyper-Local Weather Risk Copilot")
    st.write("Evaluate regional climate stress, humidity factors, and secondary pest multiplication risks[cite: 2].")

    region = st.text_input("Enter Region / District", "Punjab Agrarian Belt")
    current_season = st.selectbox("Current Season", ["Monsoon / Kharif", "Winter / Rabi", "Spring Transition", "Dry Summer"])
    recent_weather = st.text_area("Recent Weather Observations (e.g., unexpected heavy rainfall, high humidity, dry spell)", "High humidity with intermittent rainfall over the last 5 days.")

    if st.button("🌤️ Run Climate Risk Assessment", type="primary"):
        with st.spinner("ClimaRisk evaluating meteorological pressure points..."):
            try:
                weather_prompt = f"You are ClimaRisk, an agricultural meteorology agent. For the region '{region}' during '{current_season}' with recent conditions: '{recent_weather}', evaluate: 1) Frost, Flood, or Drought Risk, 2) Secondary Pest / Fungal Explosion Triggers, and 3) Proactive Mitigation Protocols for local farmers."
                
                weather_response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=weather_prompt
                )
                
                st.markdown("### 📊 Regional Climate & Risk Report")
                st.markdown(weather_response.text)
            except Exception as e:
                st.error(f"Weather analysis failed: {e}")

# --- TAB 3: FAIR-MARKET PRICE OPTIMIZER ---
with tab3:
    st.header("Fair-Market Price Optimizer & Trade Agent")
    st.write("Consult the negotiation agent to analyze live commodity pricing benchmarks and structure direct wholesale buyer contracts[cite: 2].")

    commodity = st.selectbox("Select Commodity", ["Wheat (Grade A)", "Raw Cotton", "Paddy Rice", "Tomatoes (Wholesale)", "Sugarcane"])
    yield_amount = st.number_input("Estimated Yield Volume (Metric Tons / Maunds)", min_value=1.0, value=10.0)
    farmer_location = st.text_input("Farmer Location / Mandi Hub", "Multan Regional Market")

    if "trade_chat_messages" not in st.session_state:
        st.session_state.trade_chat = client.chats.create(
            model="gemini-2.5-flash",
            config={
                "system_instruction": "You are TradeMaster, an elite agricultural supply chain economist and fair-market negotiation agent. Your mission is to protect smallholder farmers from exploitative intermediaries by offering benchmark pricing guidance, direct wholesale buyer strategies, and contract templates[cite: 2]."
            }
        )
        st.session_state.trade_chat_messages = []

    for msg in st.session_state.trade_chat_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if user_prompt := st.chat_input("Ask TradeMaster (e.g., 'What is the fair market value for this yield and how do I pitch to bulk buyers?')..."):
        st.session_state.trade_chat_messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)

        with st.chat_message("assistant"):
            with st.spinner("TradeMaster formulating market strategy..."):
                try:
                    context_query = f"Commodity: {commodity}, Yield: {yield_amount} units, Location: {farmer_location}. User Question: {user_prompt}"
                    chat_res = st.session_state.trade_chat.send_message(context_query)
                    reply = chat_res.text
                    st.markdown(reply)
                    st.session_state.trade_chat_messages.append({"role": "assistant", "content": reply})
                except Exception as e:
                    st.error(f"Negotiation agent error: {e}")

# --- TAB 4: HACKATHON PITCH & SDG BLUEPRINT ---
with tab4:
    st.header("Hackathon Master Pitch Blueprint")
    st.markdown("""
    ### 🏆 Value Proposition & Impact
    * **Problem Solved:** Overcomes crop loss from delayed identification, volatile weather, and predatory middleman pricing[cite: 2].
    * **Technology Foundation:** Built using Streamlit, Python, and multimodal Google Gemini 2.5 Flash for lightning-fast image and text processing.
    * **Scalability:** Highly scalable architecture designed to support rural farming communities across regional agricultural sectors[cite: 2].
    * **SDG Alignment:** 
        * **SDG 1:** No Poverty (Securing fair incomes for smallholders).
        * **SDG 2:** Zero Hunger (Protecting crop yields and food security).
        * **SDG 12:** Responsible Consumption (Optimizing resource use and sustainable farming practices).
    """)