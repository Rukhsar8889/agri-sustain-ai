# app.py
import streamlit as st
from google import genai
from PIL import Image

# Page Configuration for High-End Hackathon UI
st.set_page_config(
    page_title="Agri-Sustain AI | Multi-Agent Ecosystem",
    page_icon="🌱",
    layout="wide"
)

# Custom Styling for Dynamic Interface
st.markdown("""
    <style>
    .main {
        background-color: #f1f5f9;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        border: 1px solid #cbd5e1;
    }
    .stTabs [aria-selected="true"] {
        background-color: #15803d !important;
        color: white !important;
    }
    .agent-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #16a34a;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌱 Agri-Sustain AI: Multi-Agent Autonomous Command Center")
st.markdown("### Powered by Google Gemini Free API | Collaborative Multi-Agent Pipeline")
st.markdown("---")

# Initialize Gemini Client using Streamlit Secrets or Sidebar Input
api_key = None
try:
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass

st.sidebar.header("🛠️ Agent Command Center")
if not api_key:
    api_key = st.sidebar.text_input("Enter your Google Gemini API Key", type="password")

if not api_key:
    st.sidebar.warning("⚠️ Please provide a valid Gemini API key to initialize the multi-agent network.")
    st.info("💡 **Judge Preview:** Enter your API key above (or configure it in Streamlit Secrets) to dispatch real-time cooperative AI agents for crop pathology, climate risk assessment, and fair-market negotiation.")
    
    st.markdown("### 🤖 Active Multi-Agent Architecture")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 🔬 Dr. Agro (Vision Agent)")
        st.write("Specialized computer vision diagnostic agent analyzing cellular leaf structures and pathogen vectors.")
    with col2:
        st.markdown("#### 🌤️ ClimaRisk (Weather & Soil Agent)")
        st.write("Predictive meteorological agent forecasting humidity stress, pest lifecycle explosions, and irrigation timing.")
    with col3:
        st.markdown("#### ⚖️ TradeMaster (Negotiation Agent)")
        st.write("Economic strategy agent countering middleman markups and securing wholesale direct contracts.")
    st.stop()

# Initialize official Google GenAI client
client = genai.Client(api_key=api_key)

# Main Multi-Agent Workflow Tabs
tab1, tab2, tab3 = st.tabs([
    "🧬 Autonomous Multi-Agent Diagnosis Hub", 
    "💬 Cooperative Agent War Room", 
    "📊 Hackathon Master Pitch Blueprint"
])

with tab1:
    st.header("Multi-Agent Cooperative Diagnostic Pipeline")
    st.write("Trigger a simultaneous execution of **Dr. Agro (Vision)** and **ClimaRisk (Weather/Soil Intelligence)** on your crop sample using Gemini 2.5 Flash.")
    
    col_img, col_form = st.columns([1, 1])
    
    with col_img:
        uploaded_file = st.file_uploader("Upload Crop Sample (JPG, PNG)", type=["jpg", "jpeg", "png"])
        crop_category = st.selectbox("Select Crop Type", ["Wheat", "Tomato", "Rice", "Cotton", "Sugarcane", "Potato"])
        region_name = st.text_input("Geographic Region / Climate Zone", "Punjab Irrigation Belt")

    with col_form:
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption=f"Active Sample: {crop_category}", use_column_width=True)
        else:
            st.info("Upload a crop image to initialize the multi-agent pipeline.")

    if uploaded_file is not None:
        if st.button("🚀 Dispatch Multi-Agent Network", type="primary"):
            progress_bar = st.progress(0)
            status_text = st.empty()

            try:
                # Step 1: Vision Agent Analysis
                status_text.text("🤖 Agent 1 [Dr. Agro]: Analyzing cellular damage and lesion patterns...")
                progress_bar.progress(33)
                
                vision_prompt = f"You are Dr. Agro, an elite plant pathologist agent. Detail the exact disease name, confidence index, microscopic pathology, and immediate organic/chemical recovery actions for this {crop_category} image from region {region_name}."
                
                vision_response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[image, vision_prompt]
                )
                vision_analysis = vision_response.text

                # Step 2: Climate & Soil Risk Agent
                status_text.text("🤖 Agent 2 [ClimaRisk]: Correlating regional weather patterns and soil stress...")
                progress_bar.progress(66)
                
                climate_prompt = f"You are ClimaRisk, a meteorological and agricultural risk agent. Based on the crop ({crop_category}) in region ({region_name}), evaluate humidity, secondary pest multiplication risk, and prevention protocols given this pathology finding: {vision_analysis[:300]}..."
                
                climate_response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=climate_prompt
                )
                climate_analysis = climate_response.text

                progress_bar.progress(100)
                status_text.text("✅ Multi-Agent Orchestration Complete!")

                # Display Results in Structured Agent Cards
                st.markdown("---")
                col_res1, col_res2 = st.columns(2)
                
                with col_res1:
                    st.markdown("""
                        <div class="agent-card">
                            <h3>🔬 Dr. Agro (Pathology Report)</h3>
                        </div>
                    """, unsafe_allow_html=True)
                    st.markdown(vision_analysis)

                with col_res2:
                    st.markdown("""
                        <div class="agent-card" style="border-left-color: #2563eb;">
                            <h3>🌤️ ClimaRisk (Environmental Copilot)</h3>
                        </div>
                    """, unsafe_allow_html=True)
                    st.markdown(climate_analysis)

            except Exception as e:
                st.error(f"Multi-Agent execution failed: {e}")

with tab2:
    st.header("Cooperative Agent War Room (Interactive Chat)")
    st.write("Directly query the **TradeMaster Agent** regarding supply chain logistics, live commodity estimation, and fair pricing negotiation.")

    if "gemini_chat_messages" not in st.session_state:
        # Initialize chat with system persona using Gemini chat session
        st.session_state.chat = client.chats.create(
            model="gemini-2.5-flash",
            config={
                "system_instruction": "You are TradeMaster, an expert agricultural economist and fair-market negotiation agent. Your goal is to protect smallholder farmers from exploitative intermediaries by providing live commodity pricing strategies, contract templates, and direct wholesale buyer channels."
            }
        )
        st.session_state.gemini_chat_messages = []

    for message in st.session_state.gemini_chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Consult TradeMaster (e.g., 'How do I negotiate a fair price for wheat wholesale this season?')..."):
        st.session_state.gemini_chat_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("TradeMaster Agent formulating strategy..."):
                try:
                    chat_response = st.session_state.chat.send_message(prompt)
                    reply = chat_response.text
                    st.markdown(reply)
                    st.session_state.gemini_chat_messages.append({"role": "assistant", "content": reply})
                except Exception as e:
                    st.error(f"Agent communication error: {e}")

with tab3:
    st.header("Hackathon Pitch & Evaluation Matrix")
    st.markdown("""
    ### Why This Multi-Agent Architecture Wins
    * **Advanced Innovation:** Moves beyond simple single-prompt wrappers by orchestrating collaborative agents (Vision + Meteorological Risk + Economic Negotiation) powered by Gemini 2.5 Flash.
    * **Real-World Problem Solving:** Addresses three compounding crises for rural growers: rapid disease spread, unpredictable climate conditions, and predatory middleman pricing.
    * **Seamless Integration:** Built natively on Google's free-tier AI ecosystem for lightning-fast multimodal inference speeds.
    * **SDG Alignment:** Directly supports **SDG 1 (No Poverty)**, **SDG 2 (Zero Hunger)**, and **SDG 12 (Responsible Consumption)**.
    """)