import streamlit as st
import pandas as pd
import requests
from datetime import datetime


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI + IoT Precision Agriculture",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# GITHUB FLOWCHART IMAGES
# ============================================================

IMG1 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/1.jpg"
IMG2 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/2.jpg"
IMG3 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/3.jpg"
IMG4 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/4.jpg"
IMG5 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/5.jpg"


# ============================================================
# GOOGLE SHEETS WEB APP
# ============================================================

GOOGLE_SHEET_URL = (
    "https://script.google.com/macros/s/"
    "AKfycbwxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/"
    "exec"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .hero {
        padding: 35px 25px;
        border-radius: 20px;
        background: linear-gradient(135deg, #e8f5e9, #f1f8e9);
        text-align: center;
        margin-bottom: 30px;
        border: 1px solid #c8e6c9;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        color: #1b5e20;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 21px;
        color: #33691e;
    }

    .section-card {
        padding: 22px;
        border-radius: 15px;
        border: 1px solid #d7e8d5;
        background-color: #fafdf9;
        margin: 12px 0;
    }

    .metric-card {
        padding: 18px;
        border-radius: 14px;
        background-color: #f5f9f4;
        border: 1px solid #dce8da;
        text-align: center;
        min-height: 120px;
    }

    .metric-number {
        font-size: 30px;
        font-weight: 800;
        color: #2e7d32;
    }

    .metric-label {
        font-size: 15px;
        color: #555555;
    }

    .flow-step {
        padding: 15px;
        border-radius: 12px;
        background-color: #f6faf5;
        border-left: 5px solid #66bb6a;
        margin-bottom: 10px;
    }

    .judge-box {
        padding: 20px;
        border-radius: 15px;
        background-color: #f1f8e9;
        border: 1px solid #c5e1a5;
        margin: 15px 0;
    }

    .future-box {
        padding: 20px;
        border-radius: 15px;
        background-color: #f7f7f7;
        border: 1px solid #dddddd;
        margin: 10px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("🌱 Project Explorer")

st.sidebar.markdown(
    """
    **AI + IoT Based Precision Agriculture**

    Use this menu while explaining the project to the judges.
    """
)

page = st.sidebar.radio(
    "Navigate to:",
    [
        "🌾 The Problem",
        "💡 How We Solve It",
        "🌡️ Environmental Monitoring",
        "🚰 Smart Irrigation",
        "🍃 AI Plant Disease Detection",
        "🏗️ Our Prototype",
        "🔮 Future Vision"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Main technologies**

    • Arduino Uno  
    • DHT11  
    • LDR  
    • Soil Moisture Sensor  
    • Relay + Pump  
    • Python  
    • Streamlit  
    • Teachable Machine  
    • TensorFlow.js  
    • Google Sheets
    """
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def show_flowchart(image_url, caption):
    st.image(
        image_url,
        caption=caption,
        use_container_width=True
    )


def section_title(title, subtitle=None):
    st.title(title)

    if subtitle:
        st.markdown(
            f"<p style='font-size:18px;color:#555;'>{subtitle}</p>",
            unsafe_allow_html=True
        )


def get_google_sheet_data(read_type):
    """
    Reads data from the Google Apps Script Web App.

    The function is deliberately defensive so that the
    exhibition website does not crash if the sheet is
    temporarily unavailable.
    """

    try:
        response = requests.get(
            GOOGLE_SHEET_URL,
            params={"read": read_type},
            timeout=10
        )

        if response.status_code != 200:
            return None

        data = response.json()

        if isinstance(data, list):
            return pd.DataFrame(data)

        return None

    except Exception:
        return None


def normalise_columns(df):
    """
    Makes Google Sheet column names easier to use.
    """

    if df is None or df.empty:
        return df

    df = df.copy()

    df.columns = [
        str(column).strip()
        for column in df.columns
    ]

    return df


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">
            🌱 AI + IoT Based Precision Agriculture
        </div>

        <div class="hero-subtitle">
            Smart Environmental Monitoring • Smart Irrigation • AI Plant Disease Detection
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 1. THE PROBLEM
# ============================================================

if page == "🌾 The Problem":

    section_title(
        "🌾 The Problem",
        "Why do we need technology in agriculture?"
    )

    st.markdown(
        """
        Agriculture depends on many factors working together.

        A plant does not need only water. Its growth is affected by
        **temperature, humidity, light, soil moisture and soil nutrients**.

        At the same time, farmers have to deal with problems such as:

        - 💧 Inefficient or excessive irrigation
        - 🌡️ Changing environmental conditions
        - 🍃 Plant diseases and visible leaf damage
        - 🌱 Maintaining suitable conditions for different crops
        - 📊 Making decisions from changing field conditions
        """
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-number">💧</div>
                <div class="metric-label">
                    Water management
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-number">🌡️</div>
                <div class="metric-label">
                    Environmental changes
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-number">🍃</div>
                <div class="metric-label">
                    Plant health
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-number">📊</div>
                <div class="metric-label">
                    Data-based decisions
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("Our basic question")

    st.markdown(
        """
        **Can we use affordable electronics, software and AI to continuously
        monitor plant conditions and support better agricultural decisions?**
        """
    )

    st.markdown(
        """
        Our project is a prototype that combines **IoT-based environmental
        monitoring, automated irrigation and AI-based leaf image analysis**
        into one system.
        """
    )

    show_flowchart(
        IMG1,
        "Overall concept of our precision agriculture system"
    )


# ============================================================
# 2. HOW WE SOLVE IT
# ============================================================

elif page == "💡 How We Solve It":

    section_title(
        "💡 How We Solve It",
        "Our system has three major technological parts."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="section-card">
                <h3>🌡️ Environmental Monitoring</h3>

                <p>
                Sensors continuously measure important environmental
                conditions around the plant.
                </p>

                <b>Measures:</b>

                <ul>
                    <li>Temperature</li>
                    <li>Humidity</li>
                    <li>Light intensity</li>
                    <li>Soil moisture</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="section-card">
                <h3>🚰 Smart Irrigation</h3>

                <p>
                The system checks the soil condition and operates the
                pump only when watering is required.
                </p>

                <b>Technology:</b>

                <ul>
                    <li>Arduino</li>
                    <li>Relay</li>
                    <li>Water pump</li>
                    <li>Soil moisture sensor</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="section-card">
                <h3>🍃 AI Disease Detection</h3>

                <p>
                A trained image-classification model analyses a leaf
                image and predicts the visible class.
                </p>

                <b>Technology:</b>

                <ul>
                    <li>Teachable Machine</li>
                    <li>TensorFlow.js</li>
                    <li>JavaScript</li>
                    <li>Streamlit interface</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("🔄 Overall system flow")

    show_flowchart(
        IMG1,
        "Overall project workflow"
    )

    st.markdown(
        """
        ### The basic idea

        **Sensors → Arduino → Computer → Data analysis → Decision → Action**

        At the same time:

        **Leaf image → AI model → Predicted visible condition**
        """
    )

    st.markdown(
        """
        <div class="judge-box">
        <b>Important:</b> Our environmental analysis is
        <b>rule-based</b>. The genuine AI component of our current
        prototype is the plant leaf image-classification system.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# 3. ENVIRONMENTAL MONITORING
# ============================================================

elif page == "🌡️ Environmental Monitoring":

    section_title(
        "🌡️ Environmental Monitoring",
        "Measuring the conditions that affect plant growth."
    )

    st.markdown(
        """
        Our Arduino receives readings from four environmental measurements:

        | Sensor | Measurement | Arduino connection |
        |---|---|---|
        | DHT11 | Temperature + Humidity | Digital D2 |
        | LDR | Light intensity | Analog A0 |
        | Soil moisture sensor | Soil moisture | Analog A1 |

        The Arduino converts the analogue sensor signals into digital
        values and sends the readings to the computer through USB serial
        communication.
        """
    )

    st.markdown("---")

    st.subheader("🔧 Environmental monitoring flow")

    show_flowchart(
        IMG3,
        "Environmental monitoring workflow"
    )

    st.markdown("---")

    st.subheader("🧑‍💻 How our code works")

    st.markdown(
        """
        **1. Arduino reads the sensors**

        The Arduino program reads temperature, humidity, light and
        soil-moisture values.

        **2. Serial communication**

        The Arduino sends the readings to the computer through USB.

        **3. Python receives the data**

        Python reads the serial data coming from the Arduino.

        **4. The application analyses the readings**

        The readings are compared with reference requirements for
        the selected plant.

        **5. Streamlit displays the result**

        Instead of showing only raw numbers, the application gives
        understandable information about the current condition.
        """
    )

    st.markdown("---")

    st.subheader("🌱 Crop suitability analysis")

    crop = st.selectbox(
        "Select a crop to understand the analysis:",
        ["Fenugreek", "Money Plant"]
    )

    if crop == "Fenugreek":

        st.markdown(
            """
            **Reference environmental range used in our prototype**

            - Temperature: **10–24 °C**
            - Humidity: **40–55 %**
            - Light: **700–1000**
            - Soil moisture: **371–649 ADC = reference suitable range**

            The soil thresholds are prototype reference values and would
            require field calibration for real agricultural deployment.
            """
        )

    else:

        st.markdown(
            """
            **Reference environmental range used in our prototype**

            - Temperature: **20–29 °C**
            - Humidity: **50–80 %**
            - Light: **400–700**
            - Soil moisture: **651–849 ADC = reference suitable range**

            The soil thresholds are prototype reference values and would
            require field calibration for real agricultural deployment.
            """
        )

    st.markdown("---")

    st.subheader("📊 Recorded Environmental Data")

    sensor_df = get_google_sheet_data("sensor")
    sensor_df = normalise_columns(sensor_df)

    if sensor_df is not None and not sensor_df.empty:

        st.dataframe(
            sensor_df,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "These readings are retrieved from our Google Sheets data log."
        )

    else:

        st.info(
            "The recorded sensor data could not be loaded at the moment. "
            "The physical monitoring system can still be demonstrated directly."
        )


# ============================================================
# 4. SMART IRRIGATION
# ============================================================

elif page == "🚰 Smart Irrigation":

    section_title(
        "🚰 Smart Irrigation",
        "Water is supplied only when the soil condition requires it."
    )

    st.markdown(
        """
        The soil moisture sensor tells us whether the soil is too dry,
        suitable or too wet.

        The system does **not** keep the pump running continuously.

        Instead, it uses short irrigation cycles followed by a soaking
        period and another measurement.
        """
    )

    st.markdown("---")

    st.subheader("🔄 Irrigation sequence")

    show_flowchart(
        IMG4,
        "Smart irrigation workflow"
    )

    st.markdown(
        """
        ### Our actual irrigation logic

        **1️⃣ Check the soil condition**

        The normal irrigation decision is made at approximately
        **5-minute intervals**.

        **2️⃣ If the soil is suitable**

        The pump remains OFF.

        **3️⃣ If the soil is too wet**

        The pump also remains OFF.

        **4️⃣ If the soil is too dry**

        The relay is activated and the pump runs for approximately
        **1 second**.

        **5️⃣ Pump OFF**

        The system waits approximately **30 seconds**.

        **6️⃣ Recheck**

        The soil moisture is measured again.

        **7️⃣ Repeat only if required**

        If the soil is still too dry, another short watering cycle
        can occur.
        """
    )

    st.markdown("---")

    st.subheader("🧑‍💻 How our code works")

    st.markdown(
        """
        The basic decision chain is:

        **Soil reading → Soil state → Irrigation decision → Relay → Pump → Wait → Recheck**

        The Arduino also has a **1-second safety cutoff**.

        This provides a hardware-level backup so that the pump cannot
        remain ON indefinitely if something goes wrong with the control
        process.
        """
    )

    st.markdown(
        """
        <div class="judge-box">
        <b>Why 1 second?</b><br><br>
        For our prototype, the watering duration was chosen according to
        the small pot size and the water flow of our pump and pipe.
        The 30-second waiting period allows the water to spread through
        the soil before the next measurement.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader("📊 Recorded Irrigation Data")

    irrigation_df = get_google_sheet_data("irrigation")
    irrigation_df = normalise_columns(irrigation_df)

    if irrigation_df is not None and not irrigation_df.empty:

        st.dataframe(
            irrigation_df,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "These events are retrieved from our irrigation log."
        )

    else:

        st.info(
            "The irrigation log could not be loaded at the moment."
        )


# ============================================================
# 5. AI PLANT DISEASE DETECTION
# ============================================================

elif page == "🍃 AI Plant Disease Detection":

    section_title(
        "🍃 AI Plant Disease Detection",
        "Using image classification to identify visible leaf conditions."
    )

    st.markdown(
        """
        Environmental sensors can tell us about the surroundings of a
        plant, but they cannot directly identify a visible disease on a leaf.

        Therefore, we added a separate **AI-based image classification
        system**.
        """
    )

    st.markdown("---")

    st.subheader("🔄 AI workflow")

    show_flowchart(
        IMG2,
        "Plant disease detection workflow"
    )

    st.markdown("---")

    st.subheader("🧠 How our AI system works")

    st.markdown(
        """
        **1. Leaf image**

        A leaf image is uploaded to the application.

        **2. Image classification model**

        Our trained Teachable Machine model receives the image.

        **3. Prediction**

        The model calculates probabilities for the trained classes.

        **4. Highest probability**

        The class with the highest probability is selected.

        **5. Confidence threshold**

        We use a **70% confidence threshold** for our prototype.

        If the confidence is below this threshold, the result is treated
        cautiously instead of being presented as a confident prediction.
        """
    )

    st.markdown("---")

    st.subheader("🍃 Classes in our current prototype")

    classes = [
        "Rose Healthy",
        "Rose Powdery Mildew",
        "Rose Spider Mite Damage",
        "Brinjal Healthy",
        "Brinjal Leaf Blight"
    ]

    cols = st.columns(5)

    for index, class_name in enumerate(classes):

        with cols[index]:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div style="font-size:30px;">🍃</div>
                    <div class="metric-label">
                        <b>{class_name}</b>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("---")

    st.subheader("🧪 Prototype test results")

    test_results = pd.DataFrame(
        {
            "Class": [
                "Brinjal Healthy",
                "Brinjal Leaf Blight",
                "Rose Healthy",
                "Rose Powdery Mildew",
                "Rose Spider Mite Damage"
            ],
            "Prototype Test Confidence": [
                "98%",
                "97%",
                "93%",
                "93%",
                "95%"
            ]
        }
    )

    st.dataframe(
        test_results,
        use_container_width=True,
        hide_index=True
    )

    st.warning(
        "These are prototype test results from our current trained model. "
        "They should not be interpreted as validated field accuracy."
    )

    st.markdown("---")

    st.subheader("🧑‍💻 Technology used")

    st.markdown(
        """
        The main application is written in **Python using Streamlit**.

        Inside the Streamlit application, we embedded **HTML and CSS**
        for the interface and **JavaScript** to load and run the
        Teachable Machine image-classification model using TensorFlow.js.

        So, the Python application provides the main interface, while
        the trained image model is executed in the browser.
        """
    )


# ============================================================
# 6. OUR PROTOTYPE
# ============================================================

elif page == "🏗️ Our Prototype":

    section_title(
        "🏗️ Our Prototype",
        "The hardware and software working together."
    )

    st.subheader("🔌 Hardware")

    hardware = [
        ("Arduino Uno", "Main microcontroller"),
        ("DHT11", "Temperature and humidity"),
        ("LDR", "Light sensing"),
        ("Soil Moisture Sensor", "Soil moisture measurement"),
        ("Relay Module", "Controls the pump electrically"),
        ("Water Pump", "Supplies water"),
        ("10 kΩ Resistors", "DHT11 pull-up and LDR voltage divider")
    ]

    hardware_df = pd.DataFrame(
        hardware,
        columns=["Component", "Purpose"]
    )

    st.dataframe(
        hardware_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("💻 Software")

    software = [
        ("Arduino C++", "Reads sensors and controls relay"),
        ("Python", "Receives and processes data"),
        ("Streamlit", "Interactive dashboard"),
        ("Google Sheets", "Data logging"),
        ("Teachable Machine", "Image classification model"),
        ("JavaScript + TensorFlow.js", "Runs the AI model in the browser")
    ]

    software_df = pd.DataFrame(
        software,
        columns=["Technology", "Role"]
    )

    st.dataframe(
        software_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("🏗️ Complete prototype architecture")

    show_flowchart(
        IMG5,
        "Complete hardware and software architecture"
    )

    st.markdown("---")

    st.subheader("🔗 How everything connects")

    st.markdown(
        """
        ### Physical side

        **DHT11 + LDR + Soil Sensor**

        ↓

        **Arduino Uno**

        ↓

        **Relay**

        ↓

        **Water Pump**

        ### Computer side

        **Arduino**

        ↓ USB Serial

        **Python / Streamlit**

        ↓

        **Dashboard + Data Logging**

        ### AI side

        **Leaf Image**

        ↓

        **AI Image Classifier**

        ↓

        **Predicted Visible Condition**
        """
    )

    st.markdown(
        """
        <div class="judge-box">
        <b>Important design point:</b><br><br>
        The Arduino handles the physical sensing and pump control.
        The computer handles data display, analysis and logging.
        The AI disease classifier is a separate image-based component.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# 7. FUTURE VISION
# ============================================================

elif page == "🔮 Future Vision":

    section_title(
        "🔮 Future Vision",
        "Moving from a school prototype towards an integrated precision-agriculture system."
    )

    st.markdown(
        """
        Our current project demonstrates separate technologies working
        towards the same agricultural goal.

        The next step would be to integrate them more closely for a
        particular crop and field.
        """
    )

    st.markdown("---")

    st.subheader("🌱 1. More complete soil analysis")

    st.markdown(
        """
        Future versions could include:

        - Soil pH
        - Nitrogen
        - Phosphorus
        - Potassium
        - Better soil-moisture calibration
        """
    )

    st.markdown("---")

    st.subheader("🤖 2. Integrated AI + IoT")

    st.markdown(
        """
        Instead of treating environmental monitoring and disease
        detection as separate systems, a future version could combine:

        **Environmental data + Soil data + Crop information + Leaf health**

        to provide a more complete picture of crop condition.
        """
    )

    st.markdown("---")

    st.subheader("🌾 3. Intelligent crop planning")

    st.markdown(
        """
        A future AI crop-planning system could consider:

        - Current crop
        - Previous crop
        - Soil condition
        - Water availability
        - Environmental conditions
        - Nutrient requirements
        - Disease considerations

        It could then suggest suitable candidate crops for the next
        growing cycle.

        Crop rotation could include suitable leguminous crops such as
        green gram, black gram or cowpea, depending on the actual
        agricultural conditions and crop plan.
        """
    )

    st.markdown("---")

    st.subheader("📱 4. Farmer-friendly interface")

    st.markdown(
        """
        The technology should not require farmers to understand raw
        sensor values.

        A future mobile or web application could convert complex data
        into simple information such as:

        **💧 Water required**

        **🌡️ Temperature too high**

        **☀️ Light suitable**

        **🍃 Possible leaf condition detected**

        **🌱 Crop suitability needs attention**
        """
    )

    st.markdown("---")

    st.subheader("💼 5. Possible future service model")

    st.markdown(
        """
        A future version could be developed as a hardware-and-software
        service.

        A farmer could use a low-cost sensor unit connected to a mobile
        or web application.

        Different versions could potentially be developed for:

        - Small farms
        - Larger farms
        - Greenhouses
        - Different crops
        - Different levels of monitoring

        The goal would be to make precision-agriculture tools more
        accessible and easier to use.
        """
    )

    st.markdown("---")

    st.markdown(
        """
        <div class="future-box">

        <h3>🌍 Our long-term idea</h3>

        The aim is not simply to automate a pump or classify a leaf.

        Our larger vision is to use <b>AI, IoT and data-driven
        technology</b> to support agriculture that is more precise,
        efficient and sustainable.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.success(
        "🌱 From measuring the field → understanding the data → "
        "taking action → learning from the results."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;color:#777;padding:15px;">

    <b>AI + IoT Based Precision Agriculture</b><br>

    Science • Technology • Innovation • Sustainable Agriculture

    </div>
    """,
    unsafe_allow_html=True
)
