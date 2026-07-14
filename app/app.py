import sys
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Add project root to Python path
sys.path.insert(0, str(BASE_DIR))

import streamlit as st
from PIL import Image

from src.predict import predict_image
from src.leaf_detector import predict_leaf
from src.disease_info import (
    CONFIDENCE_THRESHOLD,
    SUPPORTED_CROPS,
    disease_information,
    get_crop_display,
    get_result,
)


# ---------------------------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="SeeIt - Crop Disease Classification",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Global Dark Theme Styling
# Every text color is set explicitly so nothing renders dark-on-dark.
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    :root {
        --bg-main: #0b1410;
        --bg-card: #142019;
        --bg-card-alt: #182a1f;
        --border-soft: #24352b;
        --text-primary: #eaf5ec;
        --text-secondary: #a9bdae;
        --accent-green: #3ecf72;
        --accent-green-dark: #1b6b3c;
        --accent-orange: #f0965a;
        --accent-red: #ef6a6a;
    }

    .stApp {
        background: radial-gradient(circle at top left, #12241a 0%, #0b1410 55%);
        color: var(--text-primary);
    }

    /* Make sure every generic text element is readable on the dark bg */
    .stApp, .stApp p, .stApp span, .stApp li, .stApp label,
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    .stMarkdown, .stMarkdown p, .stMarkdown li,
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] li {
        color: var(--text-primary) !important;
    }

    .stCaption, .stApp small, [data-testid="stCaptionContainer"] {
        color: var(--text-secondary) !important;
    }

    .seeit-hero {
        background: linear-gradient(120deg, #14532e 0%, #1f8f4d 60%, #3ecf72 100%);
        padding: 2.2rem 2rem;
        border-radius: 18px;
        color: #ffffff;
        margin-bottom: 1.6rem;
        box-shadow: 0 8px 28px rgba(0, 0, 0, 0.45);
    }
    .seeit-hero h1 { margin: 0 0 0.4rem 0; font-size: 2.1rem; color: #ffffff !important; }
    .seeit-hero p { margin: 0; opacity: 0.95; font-size: 1.02rem; color: #eafff0 !important; }

    .seeit-card {
        background: var(--bg-card);
        border-radius: 16px;
        padding: 1.4rem 1.6rem;
        box-shadow: 0 4px 18px rgba(0,0,0,0.35);
        border: 1px solid var(--border-soft);
        margin-bottom: 1rem;
        color: var(--text-primary);
    }
    .seeit-card p, .seeit-card h4, .seeit-card li, .seeit-card b {
        color: var(--text-primary) !important;
    }

    .result-good { border-left: 6px solid var(--accent-green); }
    .result-bad { border-left: 6px solid var(--accent-orange); }
    .result-reject { border-left: 6px solid var(--accent-red); }

    .crop-pill {
        display: inline-block;
        background: var(--bg-card-alt);
        color: var(--accent-green) !important;
        border-radius: 999px;
        padding: 0.35rem 0.9rem;
        margin: 0.2rem;
        font-size: 0.92rem;
        font-weight: 600;
        border: 1px solid var(--border-soft);
    }

    .metric-chip {
        background: var(--bg-card-alt);
        border-radius: 12px;
        padding: 0.7rem 1rem;
        text-align: center;
        border: 1px solid var(--border-soft);
        color: var(--text-primary) !important;
    }
    .metric-chip b, .metric-chip span {
        color: var(--text-primary) !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #0a1a10;
        border-right: 1px solid var(--border-soft);
    }
    section[data-testid="stSidebar"] * {
        color: var(--text-primary) !important;
    }
    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.12) !important;
    }

    /* Tabs */
    button[data-baseweb="tab"] {
        color: var(--text-secondary) !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: var(--accent-green) !important;
    }
    div[data-baseweb="tab-highlight"] {
        background-color: var(--accent-green) !important;
    }
    div[data-baseweb="tab-border"] {
        background-color: var(--border-soft) !important;
    }

    /* Expanders */
    div[data-testid="stExpander"] {
        background: var(--bg-card);
        border: 1px solid var(--border-soft);
        border-radius: 12px;
    }
    div[data-testid="stExpander"] summary {
        color: var(--text-primary) !important;
    }

    /* Inputs: text input, selectbox, file uploader */
    div[data-baseweb="select"] > div,
    input[type="text"],
    .stTextInput input {
        background-color: var(--bg-card-alt) !important;
        color: var(--text-primary) !important;
        border-color: var(--border-soft) !important;
    }
    div[data-testid="stFileUploaderDropzone"] {
        background-color: var(--bg-card-alt) !important;
        border: 1px dashed var(--border-soft) !important;
    }
    div[data-testid="stFileUploaderDropzone"] * {
        color: var(--text-primary) !important;
    }

    /* Buttons */
    .stButton button {
        background-color: var(--accent-green-dark) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
    }
    .stButton button:hover {
        background-color: var(--accent-green) !important;
        color: #05130a !important;
    }

    /* Alerts (info / warning / error / success) */
    div[data-testid="stAlert"] {
        background-color: var(--bg-card-alt) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-soft) !important;
    }
    div[data-testid="stAlert"] p {
        color: var(--text-primary) !important;
    }

    /* Progress bar track */
    div[data-testid="stProgress"] > div > div {
        background-color: var(--accent-green) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Hero Header
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="seeit-hero">
        <h1>🌿 SeeIt — Crop Disease Classification</h1>
        <p>AI-powered leaf diagnosis using MobileNetV2 · Upload a photo and get an instant health check.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

tab_predict, tab_library, tab_about = st.tabs(
    ["🔍 Predict", "📚 Disease Library", "ℹ️ About"]
)

# =====================================================================
# TAB 1 — PREDICT
# =====================================================================
with tab_predict:
    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown("#### 📷 Upload a Leaf Image")
        uploaded_file = st.file_uploader(
            "Choose a clear photo of a single leaf",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed",
        )

        if uploaded_file is not None:
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, caption="Uploaded Leaf Image", use_container_width=True)
            predict_clicked = st.button(
                "🔍 Predict Disease", use_container_width=True, type="primary"
            )
        else:
            image = None
            predict_clicked = False
            st.info("👆 Upload a leaf image (JPG or PNG) to get started.")

    with right:
        st.markdown("#### 🌿 Result")

        if uploaded_file is None:
            st.markdown(
                """
                <div class="seeit-card">
                    <p style="margin:0;">
                    Your prediction will appear here once you upload an image and click
                    <b>Predict Disease</b>.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif not predict_clicked:
            st.markdown(
                """
                <div class="seeit-card">
                    <p style="margin:0;">
                    Image ready ✅ — click <b>Predict Disease</b> to analyze it.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            try:
                with st.spinner("🧠 AI is analyzing the image..."):

                    temp_path = BASE_DIR / "temp_leaf.jpg"
                    image.save(temp_path)

                    # -------- Leaf Detector --------
                    leaf_result, leaf_confidence = predict_leaf(temp_path)

                    if leaf_result == "non_leaf":

                        st.error("❌ Please upload a valid leaf image.")

                        

                        st.stop()

                    # -------- Disease Detector --------
                    raw_label, confidence, top_predictions = predict_image(temp_path)
            except FileNotFoundError as e:
                st.error(
                    f"⚠️ Could not load the model or dataset folder.\n\n"
                    f"Make sure these exist relative to your project root:\n"
                    f"- `models/mobilenet_plant_disease_new.pth`\n"
                    f"- `data/color/` (class folders used to read class names)\n\n"
                    f"Details: {e}"
                )
                st.stop()

           
            result = get_result(raw_label, confidence)

            if not result["accepted"]:
                # -----------------------------------------------
                # Low confidence / unknown class -> not a supported leaf
                # -----------------------------------------------
                info = result["info"]
                st.markdown(
                    f"""
                    <div class="seeit-card result-reject">
                        <h4 style="margin-top:0;">❌ {info['display_name']}</h4>
                        <p>
The model is not confident enough to make a reliable prediction.

Current confidence:
<b>{confidence:.2f}%</b>

Please upload a clearer image of a single crop leaf.

The top possible predictions are shown below.
</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                for tip in info["suggestion"]:
                    st.markdown(f"- {tip}")

                st.markdown("**🌱 Supported Crops**")
                pills = "".join(
                    f'<span class="crop-pill">{emoji} {name}</span>'
                    for name, emoji in (get_crop_display(c) for c in SUPPORTED_CROPS)
                )
                st.markdown(pills, unsafe_allow_html=True)

            else:
                info = result["info"]
                crop_name, crop_emoji = result["crop_display"]
                is_healthy = info["status"] == "Healthy"
                card_class = "result-good" if is_healthy else "result-bad"
                icon = "✅" if is_healthy else "🍃"

                st.markdown(
                    f"""
                    <div class="seeit-card {card_class}">
                        <h4 style="margin-top:0;">{icon} {crop_emoji} {crop_name} — {info['display_name']}</h4>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown(
                        f"""<div class="metric-chip"><b>🎯 Confidence</b><br>
                        <span style="font-size:1.4rem;">{confidence:.2f}%</span></div>""",
                        unsafe_allow_html=True,
                    )
                with c2:
                    st.markdown(
                        f"""<div class="metric-chip"><b>🩺 Status</b><br>
                        <span style="font-size:1.4rem;">{info['status']}</span></div>""",
                        unsafe_allow_html=True,
                    )

                st.progress(min(int(confidence), 100))

                st.markdown("### 🔍 Top 3 Predictions")

                for i, pred in enumerate(top_predictions, start=1):

                    crop = pred["class"].split("___")[0]

                    disease = pred["class"].split("___")[1].replace("_", " ")

                    st.write(
                    f"**{i}. {crop} — {disease}** : {pred['confidence']:.2f}%"
                    )

                st.markdown("<br>", unsafe_allow_html=True)

                d_tab, s_tab, t_tab, p_tab = st.tabs(
                    ["📝 Description", "🔬 Symptoms", "💊 Treatment", "🛡️ Prevention"]
                )
                with d_tab:
                    st.write(info["description"])
                with s_tab:
                    for item in info["symptoms"]:
                        st.markdown(f"- {item}")
                with t_tab:
                    for item in info["treatment"]:
                        st.markdown(f"- {item}")
                with p_tab:
                    for item in info["prevention"]:
                        st.markdown(f"- {item}")

# =====================================================================
# TAB 2 — DISEASE LIBRARY
# =====================================================================
with tab_library:
    st.markdown("#### 📚 Browse All 38 Classes")
    st.caption("Reference information for every disease (and healthy state) the model recognizes.")

    crop_options = ["All Crops"] + [get_crop_display(c)[0] for c in SUPPORTED_CROPS]
    crop_filter = st.selectbox("Filter by crop", crop_options)

    search = st.text_input("🔎 Search by keyword (e.g. 'blight', 'rust', 'mildew')", "")

    for raw_label, info in disease_information.items():
        crop_name, crop_emoji = get_crop_display(info["crop"])

        if crop_filter != "All Crops" and crop_name != crop_filter:
            continue
        if search and search.lower() not in info["display_name"].lower() and search.lower() not in info["description"].lower():
            continue

        status_icon = "✅" if info["status"] == "Healthy" else "⚠️"

        with st.expander(f"{crop_emoji} {status_icon} {crop_name} — {info['display_name']}"):
            st.markdown(f"**Description:** {info['description']}")
            st.markdown("**Symptoms:**")
            for item in info["symptoms"]:
                st.markdown(f"- {item}")
            st.markdown("**Treatment:**")
            for item in info["treatment"]:
                st.markdown(f"- {item}")
            st.markdown("**Prevention:**")
            for item in info["prevention"]:
                st.markdown(f"- {item}")

# =====================================================================
# TAB 3 — ABOUT
# =====================================================================
with tab_about:
    st.markdown("#### ℹ️ About SeeIt")
    st.markdown(
        f"""
        <div class="seeit-card">
        <p>
        <b>SeeIt</b> is an AI-powered crop disease classifier built with a
        <b>MobileNetV2</b> convolutional neural network trained on the PlantVillage
        dataset (38 classes across 14 crops).
        </p>
        <p>
        Predictions below <b>{CONFIDENCE_THRESHOLD:.0f}% confidence</b> are treated as
        "not a supported crop leaf" rather than forcing a guess, to reduce false
        positives on unrelated images (phones, faces, random objects, etc.).
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """<div class="metric-chip"><b>Model</b><br>MobileNetV2</div>""",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """<div class="metric-chip"><b>Validation Accuracy</b><br>94.40%</div>""",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """<div class="metric-chip"><b>Classes</b><br>38</div>""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**🌱 Supported Crops**")
    pills = "".join(
        f'<span class="crop-pill">{emoji} {name}</span>'
        for name, emoji in (get_crop_display(c) for c in SUPPORTED_CROPS)
    )
    st.markdown(pills, unsafe_allow_html=True)

# =====================================================================
# Sidebar
# =====================================================================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/plant-under-rain.png", width=90)
    st.title("🌿 SeeIt AI")
    st.markdown("---")

    st.subheader("📊 Model Information")
    st.write("**Model:** MobileNetV2")
    st.write("**Validation Accuracy:** 94.40%")
    st.write("**Classes:** 38")
    st.write(f"**Confidence Threshold:** {CONFIDENCE_THRESHOLD:.0f}%")

    st.markdown("---")
    st.subheader("🌱 Supported Crops")
    for raw_crop in SUPPORTED_CROPS:
        name, emoji = get_crop_display(raw_crop)
        st.write(f"{emoji} {name}")

    st.markdown("---")
    st.info("Upload a clear image of a single crop leaf for the best prediction.")

    st.markdown("---")
    st.caption("Developed using ❤️ Streamlit + PyTorch")