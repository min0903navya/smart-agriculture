import streamlit as st
import pandas as pd
import requests


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI + IoT Precision Agriculture",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# FLOWCHART IMAGES FROM GITHUB
# ============================================================

IMG1 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/1.jpg"
IMG2 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/2.jpg"
IMG3 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/3.jpg"
IMG4 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/4.jpg"
IMG5 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/5.jpg"


# ============================================================
# GOOGLE SHEETS
# IMPORTANT:
# Replace this with YOUR ACTUAL Apps Script Web App URL.
# ============================================================

GOOGLE_SHEET_URL = "PASTE_YOUR_EXISTING_GOOGLE_APPS_SCRIPT_URL_HERE"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- General ---------- */

    .main {
        padding-top: 1rem;
    }

    /* ---------- Hero ---------- */

    .hero-box {
        background: #eaf6ea;
        border: 1px solid #b7d8b7;
        border-radius: 20px;
        padding: 35px 30px;
        text-align: center;
        margin-bottom: 30px;
    }

    .hero-title {
        color: #14532d !important;
        font-size: 42px !important;
        font-weight: 800 !important;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        color: #285943 !important;
        font-size: 20px !important;
        font-weight: 500 !important;
        line-height: 1.5;
    }

    /* ---------- Section headings ---------- */

    .section-subtitle {
        color: #4b5563 !important;
        font-size: 18px;
        margin-top: -10px;
        margin-bottom: 25px;
    }

    /* ---------- Information cards ---------- */

    .info-card {
        background: #ffffff;
        border: 1px solid #d8e5d8;
        border-radius: 16px;
        padding: 22px;
        min-height: 245px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }

    .info-card h3 {
        color: #166534 !important;
        font-size: 22px;
        margin-top: 0;
        margin-bottom: 12px;
    }

    .info-card p {
        color: #374151 !important;
        font-size: 16px;
        line-height: 1.6;
    }

    .info-card li {
        color: #374151 !important;
        margin-bottom: 7px;
    }

    /* ---------- Problem cards ---------- */

    .problem-card {
        background: #ffffff;
        border: 1px solid #e2e8e2;
        border-radius: 14px;
        padding: 20px;
        min-height: 165px;
    }

    .problem-icon {
        font-size: 32px;
        margin-bottom: 8px;
    }

    .problem-title {
        color: #166534 !important;
        font-size: 19px;
        font-weight: 700;
        margin-bottom: 7px;
    }

    .problem-text {
        color: #374151 !important;
        font-size: 15px;
        line-height: 1.5;
    }

    /* ---------- Judge box ---------- */

    .judge-box {
        background: #f0fdf4;
        border-left: 5px solid #22c55e;
        border-radius: 10px;
        padding: 18px 20px;
        color: #1f2937 !important;
        margin: 20px 0;
    }

    .judge-box strong {
        color: #166534 !important;
    }

    /* ---------- Process boxes ---------- */

    .process-box {
        background: #f8faf8;
        border: 1px solid #dce7dc;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 12px;
    }

    .process-number {
        color: #166534 !important;
        font-size: 18px;
        font-weight: 700;
    }

    .process-text {
        color: #374151 !important;
        font-size: 15px;
        line-height: 1.5;
    }

    /* ---------- Future cards ---------- */

    .future-card {
        background: #ffffff;
        border: 1px solid #d9e2d9;
        border-radius: 15px;
        padding: 20px;
        min-height: 190px;
    }

    .future-card h3 {
        color: #166534 !important;
        margin-top: 0;
    }

    .future-card p,
    .future-card li {
        color: #374151 !important;
        line-height: 1.5;
    }

    /* ---------- Footer ---------- */

    .footer {
        text-align: center;
        color: #6b7280 !important;
        padding: 25px 0;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🌱 Project Explorer")

st.sidebar.markdown(
    """
    **AI + IoT Based Precision Agriculture**

    Navigate through the project while explaining it to the judges.
    """
)

page = st.sidebar.radio(
    "Project Sections",
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

st.sidebar.markdown("### Technologies")

st.sidebar.markdown(
    """
    • Arduino Uno  
    • DHT11  
    • LDR  
    • Soil Moisture Sensor  
    • Relay + Pump  
    • Python  
    • Streamlit  
    • Google Sheets  
    • Teachable Machine  
    • TensorFlow.js
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


def get_google_sheet_data(read_type):

    if GOOGLE_SHEET_URL == "PASTE_YOUR_EXISTING_GOOGLE_APPS_SCRIPT_URL_HERE":
        return None

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


def clean_dataframe(df):

    if df is None or df.empty:
        return df

    df = df.copy()

    df.columns = [
        str(column).strip()
        for column in df.columns
    ]

    return df


# ============================================================
# HERO HEADER
# ============================================================

st.markdown(
    """
    <div class="hero-box">

        <div class="hero-title">
            🌱 AI + IoT Based Precision Agriculture
        </div>

        <div class="hero-subtitle">
            Smart Environmental Monitoring&nbsp;&nbsp;•&nbsp;&nbsp;
            Smart Irrigation&nbsp;&nbsp;•&nbsp;&nbsp;
            AI-Powered Plant Disease Detection
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PAGE 1 — THE PROBLEM
# ============================================================

if page == "🌾 The Problem":

    st.title("🌾 The Problem")

    st.markdown(
        '<div class="section-subtitle">'
        'Why does agriculture need better monitoring and decision support?'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        Agriculture is not simply about supplying water to a plant.

        Plant growth depends on several conditions such as
        **temperature, humidity, light, soil moisture and nutrients**.
        At the same time, farmers have to respond to changing field
        conditions, water availability and plant-health problems.

        Our project focuses on three practical challenges:
        **monitoring the growing environment, managing irrigation and
        identifying visible plant-health problems.**
        """
    )

    st.markdown("---")

    st.subheader("🌱 The challenges we are addressing")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="problem-card">

                <div class="problem-icon">💧</div>

                <div class="problem-title">
                    Water Management
                </div>

                <div class="problem-text">
                    Watering a crop without considering the actual soil
                    condition can lead to unnecessary watering or
                    insufficient watering.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class="problem-card">

                <div class="problem-icon">🌡️</div>

                <div class="problem-title">
                    Changing Environmental Conditions
                </div>

                <div class="problem-text">
                    Temperature, humidity and light can change over time,
                    affecting whether the conditions are suitable for
                    a particular plant.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="problem-card">

                <div class="problem-icon">🍃</div>

                <div class="problem-title">
                    Plant Health
                </div>

                <div class="problem-text">
                    A plant may show visible signs of disease or damage
                    on its leaves. Detecting these conditions early can
                    support better plant-health management.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class="problem-card">

                <div class="problem-icon">📊</div>

                <div class="problem-title">
                    Making Sense of Data
                </div>

                <div class="problem-text">
                    Sensors produce raw measurements. Our system converts
                    these measurements into information that is easier
                    to understand and act upon.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("💡 The question behind our project")

    st.markdown(
        """
        **Can affordable electronics, software and AI be combined to
        monitor plant conditions, reduce unnecessary irrigation and
        assist with plant-health identification?**
        """
    )

    show_flowchart(
        IMG1,
        "Overall concept of our precision agriculture system"
    )


# ============================================================
# PAGE 2 — HOW WE SOLVE IT
# ============================================================

elif page == "💡 How We Solve It":

    st.title("💡 How We Solve It")

    st.markdown(
        '<div class="section-subtitle">'
        'Our project combines sensing, automation and AI into one agricultural prototype.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        We divide the system into **three main technological parts**.
        Each part solves a different problem, while the overall system
        demonstrates how these technologies can work together.
        """
    )

    st.markdown("---")

    # --------------------------------------------------------
    # THREE MAIN PARTS
    # --------------------------------------------------------

    st.subheader("1. 🌡️ Environmental Monitoring")

    st.markdown(
        """
        Our sensors continuously collect information about the
        plant's surrounding conditions.

        **We measure:**

        - 🌡️ Temperature
        - 💧 Humidity
        - ☀️ Light intensity
        - 🌱 Soil moisture

        The Arduino receives these measurements and sends the data
        to the computer through USB serial communication.

        The Python and Streamlit application then displays and
        analyses the readings according to the selected plant.
        """
    )

    st.markdown("---")

    st.subheader("2. 🚰 Smart Irrigation")

    st.markdown(
        """
        The soil moisture reading is used to determine whether
        watering is required.

        The system does not continuously operate the pump.

        Instead, when the soil is too dry:

        **Soil dry → Pump ON for 1 second → Pump OFF → Wait 30 seconds → Recheck**

        If the soil is still dry, another short watering cycle can
        take place.

        This creates a feedback-based irrigation process instead of
        simply keeping the pump running.
        """
    )

    st.markdown("---")

    st.subheader("3. 🍃 AI-Powered Plant Disease Detection")

    st.markdown(
        """
        Environmental sensors cannot identify a disease from a leaf.

        Therefore, we use a separate AI image-classification system.

        A leaf image is given to our trained model, which predicts
        the most likely class from the five classes in our prototype.

        The current prototype uses a **70% confidence threshold**.
        """
    )

    st.markdown("---")

    st.subheader("🔄 How the complete idea works")

    show_flowchart(
        IMG1,
        "Overall system flow"
    )

    st.markdown(
        """
        ### The three technologies have different roles

        | Technology | Main role |
        |---|---|
        | IoT sensors | Measure environmental conditions |
        | Automation | Control irrigation based on soil condition |
        | AI | Classify visible leaf conditions |

        **Important:** Environmental suitability analysis in our current
        prototype is **rule-based**, using reference ranges. It is not
        presented as AI.
        """
    )


# ============================================================
# PAGE 3 — ENVIRONMENTAL MONITORING
# ============================================================

elif page == "🌡️ Environmental Monitoring":

    st.title("🌡️ Environmental Monitoring")

    st.markdown(
        '<div class="section-subtitle">'
        'The first step is to know what is happening around the plant.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        A plant's growing environment changes with time.

        Our system measures four important parameters and compares
        them with reference requirements for the selected plant.
        """
    )

    st.markdown("---")

    st.subheader("🔧 Sensors used")

    sensor_table = pd.DataFrame(
        {
            "Sensor": [
                "DHT11",
                "LDR",
                "Soil Moisture Sensor"
            ],
            "Measures": [
                "Temperature and Humidity",
                "Light intensity",
                "Soil moisture"
            ],
            "Arduino Connection": [
                "Digital D2",
                "Analog A0",
                "Analog A1"
            ]
        }
    )

    st.dataframe(
        sensor_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("🔄 Environmental monitoring flow")

    show_flowchart(
        IMG3,
        "Environmental monitoring workflow"
    )

    st.markdown("---")

    st.subheader("🧑‍💻 How our code works")

    st.markdown(
        """
        **Step 1 — Arduino reads the sensors**

        The Arduino program reads temperature, humidity, light and
        soil-moisture values.

        **Step 2 — Serial communication**

        The readings are sent from the Arduino to the computer
        through USB serial communication.

        **Step 3 — Python receives the readings**

        Python reads the serial data.

        **Step 4 — Rule-based analysis**

        The readings are compared with reference ranges for the
        selected plant.

        **Step 5 — Streamlit displays the result**

        Instead of showing only raw numbers, the application gives
        a simple interpretation such as **Suitable**, **Too Low**,
        **Too High**, **Too Dry** or **Too Wet**.
        """
    )

    st.markdown("---")

    st.subheader("🌱 Example reference conditions")

    crop = st.selectbox(
        "Choose a plant:",
        ["Fenugreek", "Money Plant"]
    )

    if crop == "Fenugreek":

        reference_table = pd.DataFrame(
            {
                "Parameter": [
                    "Temperature",
                    "Humidity",
                    "Light",
                    "Soil Moisture"
                ],
                "Reference Range": [
                    "10–24 °C",
                    "40–55 %",
                    "700–1000",
                    "371–649 ADC"
                ]
            }
        )

    else:

        reference_table = pd.DataFrame(
            {
                "Parameter": [
                    "Temperature",
                    "Humidity",
                    "Light",
                    "Soil Moisture"
                ],
                "Reference Range": [
                    "20–29 °C",
                    "50–80 %",
                    "400–700",
                    "651–849 ADC"
                ]
            }
        )

    st.dataframe(
        reference_table,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "The soil-moisture limits shown here are prototype reference "
        "values. Real agricultural deployment would require controlled "
        "calibration for the sensor, soil and crop."
    )

    st.markdown("---")

    st.subheader("📊 Recorded Environmental Data")

    sensor_df = clean_dataframe(
        get_google_sheet_data("sensor")
    )

    if sensor_df is not None and not sensor_df.empty:

        st.dataframe(
            sensor_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "Recorded sensor data will appear here when the Google "
            "Sheets connection is available."
        )


# ============================================================
# PAGE 4 — SMART IRRIGATION
# ============================================================

elif page == "🚰 Smart Irrigation":

    st.title("🚰 Smart Irrigation")

    st.markdown(
        '<div class="section-subtitle">'
        'The system waters the plant only when the soil condition requires it.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        The soil moisture sensor provides the information needed to
        decide whether irrigation is required.

        The pump is operated in short cycles instead of running
        continuously.
        """
    )

    st.markdown("---")

    st.subheader("🔄 Irrigation workflow")

    show_flowchart(
        IMG4,
        "Smart irrigation workflow"
    )

    st.markdown("---")

    st.subheader("⚙️ Actual irrigation sequence")

    steps = [
        (
            "1",
            "Check soil moisture",
            "The system checks the soil condition at the normal five-minute decision interval."
        ),
        (
            "2",
            "Soil is suitable",
            "The pump remains OFF."
        ),
        (
            "3",
            "Soil is too wet",
            "The pump remains OFF and the soil is allowed to dry naturally."
        ),
        (
            "4",
            "Soil is too dry",
            "The relay is activated and the pump runs for approximately one second."
        ),
        (
            "5",
            "Pump OFF",
            "The system stops watering."
        ),
        (
            "6",
            "Soaking period",
            "The system waits approximately 30 seconds so that the water can spread through the soil."
        ),
        (
            "7",
            "Recheck",
            "The soil moisture is measured again."
        ),
        (
            "8",
            "Repeat if necessary",
            "Another short watering cycle can occur only if the soil is still too dry."
        )
    ]

    for number, title, description in steps:

        st.markdown(
            f"""
            <div class="process-box">

                <div class="process-number">
                    {number}. {title}
                </div>

                <div class="process-text">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("🧑‍💻 How our code works")

    st.markdown(
        """
        The control logic can be understood as:

        **Soil reading**
        ↓
        **Determine soil state**
        ↓
        **Decide whether watering is required**
        ↓
        **Arduino controls relay**
        ↓
        **Pump operates briefly**
        ↓
        **Wait**
        ↓
        **Measure again**

        The Arduino also contains a **1-second safety cutoff** for the
        pump. This provides a hardware-level protection against the
        pump staying ON indefinitely.
        """
    )

    st.markdown(
        """
        <div class="judge-box">

        <strong>Why do we wait 30 seconds?</strong>

        The water needs time to spread through the soil. If we measured
        immediately after switching the pump off, the sensor reading
        might not represent the condition of the surrounding soil yet.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader("📊 Recorded Irrigation Data")

    irrigation_df = clean_dataframe(
        get_google_sheet_data("irrigation")
    )

    if irrigation_df is not None and not irrigation_df.empty:

        st.dataframe(
            irrigation_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "Recorded irrigation events will appear here when the "
            "Google Sheets connection is available."
        )


# ============================================================
# PAGE 5 — AI DISEASE DETECTION
# ============================================================

elif page == "🍃 AI Plant Disease Detection":

    st.title("🍃 AI-Powered Plant Disease Detection")

    st.markdown(
        '<div class="section-subtitle">'
        'Using image classification to identify visible leaf conditions.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        Our environmental sensors tell us about the growing conditions
        around a plant.

        But they cannot look at a leaf and identify a visible disease.

        That is why we added a separate **AI-based image-classification
        component**.
        """
    )

    st.markdown("---")

    st.subheader("🔄 AI detection workflow")

    show_flowchart(
        IMG2,
        "Plant disease detection workflow"
    )

    st.markdown("---")

    st.subheader("🧠 How the AI system works")

    ai_steps = [
        (
            "1",
            "Upload a leaf image",
            "The user provides an image of the plant leaf."
        ),
        (
            "2",
            "Send the image to the model",
            "The trained image-classification model receives the image."
        ),
        (
            "3",
            "Generate predictions",
            "The model calculates probabilities for the trained classes."
        ),
        (
            "4",
            "Select the highest probability",
            "The class with the highest predicted probability is selected."
        ),
        (
            "5",
            "Apply the confidence threshold",
            "Our prototype uses a 70% threshold before presenting a confident result."
        )
    ]

    for number, title, description in ai_steps:

        st.markdown(
            f"""
            <div class="process-box">

                <div class="process-number">
                    {number}. {title}
                </div>

                <div class="process-text">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("🍃 Classes in our current model")

    classes = [
        "Rose Healthy",
        "Rose Powdery Mildew",
        "Rose Spider Mite Damage",
        "Brinjal Healthy",
        "Brinjal Leaf Blight"
    ]

    for class_name in classes:

        st.markdown(
            f"- **{class_name}**"
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
        "These are prototype test results from our current trained "
        "model. They are not a claim of validated field accuracy."
    )

    st.markdown("---")

    st.subheader("🧑‍💻 Technology used")

    st.markdown(
        """
        The main application is written in **Python using Streamlit**.

        We use **HTML and CSS** for the embedded interface and
        **JavaScript with TensorFlow.js** to load and run the
        Teachable Machine image-classification model in the browser.

        Therefore:

        **Python / Streamlit → application interface**

        **JavaScript / TensorFlow.js → runs the trained image model**

        **Teachable Machine → trained classification model**
        """
    )


# ============================================================
# PAGE 6 — OUR PROTOTYPE
# ============================================================

elif page == "🏗️ Our Prototype":

    st.title("🏗️ Our Prototype")

    st.markdown(
        '<div class="section-subtitle">'
        'The physical hardware and software components of our system.'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader("🔌 Hardware components")

    hardware_table = pd.DataFrame(
        {
            "Component": [
                "Arduino Uno",
                "DHT11",
                "LDR",
                "Soil Moisture Sensor",
                "Relay Module",
                "Water Pump",
                "10 kΩ Resistors"
            ],
            "Purpose": [
                "Main microcontroller",
                "Measures temperature and humidity",
                "Measures changes in light",
                "Measures soil moisture",
                "Controls the pump electrically",
                "Supplies water to the plant",
                "DHT11 pull-up and LDR voltage-divider circuits"
            ]
        }
    )

    st.dataframe(
        hardware_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("💻 Software components")

    software_table = pd.DataFrame(
        {
            "Technology": [
                "Arduino C++",
                "Python",
                "Streamlit",
                "Google Sheets",
                "Teachable Machine",
                "JavaScript + TensorFlow.js"
            ],
            "Purpose": [
                "Sensor reading and relay control",
                "Data processing",
                "Dashboard and interface",
                "Data logging",
                "Training the image classifier",
                "Running the image classifier in the browser"
            ]
        }
    )

    st.dataframe(
        software_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("🏗️ Complete system architecture")

    show_flowchart(
        IMG5,
        "Complete hardware and software architecture"
    )

    st.markdown("---")

    st.subheader("🔗 How the hardware communicates")

    st.markdown(
        """
        **DHT11 → Arduino D2**

        Temperature and humidity data are sent to the Arduino.

        **LDR → Arduino A0**

        The LDR circuit produces an analogue signal corresponding to
        changes in light.

        **Soil Moisture Sensor → Arduino A1**

        The analogue soil signal is read by the Arduino.

        **Arduino D7 → Relay**

        The Arduino sends the control signal to the relay.

        **Relay → Pump**

        The relay acts as the electrically controlled switch for the pump.

        **Arduino → USB → Computer**

        Sensor readings are sent to the Python/Streamlit application.
        """
    )

    st.markdown(
        """
        <div class="judge-box">

        <strong>Important:</strong>

        Our final prototype does not use an LCD. The computer dashboard
        is used for displaying the monitored data and analysis.

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PAGE 7 — FUTURE VISION
# ============================================================

elif page == "🔮 Future Vision":

    st.title("🔮 Future Vision")

    st.markdown(
        '<div class="section-subtitle">'
        'How could this school prototype develop into a more complete precision-agriculture system?'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        Our current project demonstrates three separate capabilities:

        **Environmental monitoring + Smart irrigation + AI leaf classification**

        Our future aim is to integrate these capabilities more closely
        for a particular crop and field.
        """
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="future-card">

                <h3>🧪 More Soil Information</h3>

                <p>
                Future versions could include sensors for:
                </p>

                <ul>
                    <li>Soil pH</li>
                    <li>Nitrogen</li>
                    <li>Phosphorus</li>
                    <li>Potassium</li>
                </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="future-card">

                <h3>🤖 Integrated AI + IoT</h3>

                <p>
                Environmental data and plant-health information could
                eventually be considered together instead of operating
                as separate demonstrations.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="future-card">

                <h3>🌾 Intelligent Crop Planning</h3>

                <p>
                A future crop-planning system could consider the current
                crop, previous crop, soil condition, water availability,
                environmental conditions and nutrient requirements.
                </p>

                <p>
                It could then suggest suitable candidate crops for the
                next growing cycle.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="future-card">

                <h3>🌱 Crop Rotation</h3>

                <p>
                Crop planning could include suitable leguminous crops
                such as green gram, black gram or cowpea, depending on
                the actual field conditions and crop plan.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="future-card">

                <h3>📱 Farmer-Friendly Application</h3>

                <p>
                Instead of showing complicated raw readings, a future
                mobile or web application could provide simple messages
                such as:
                </p>

                <ul>
                    <li>Water required</li>
                    <li>Temperature too high</li>
                    <li>Environmental conditions suitable</li>
                    <li>Possible leaf condition detected</li>
                </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="future-card">

                <h3>💼 Possible Future Service</h3>

                <p>
                A future version could combine a low-cost sensor unit
                with a web or mobile application.
                </p>

                <p>
                Different versions could be developed for small farms,
                larger farms, greenhouses and different crops.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("🌍 Our larger vision")

    st.markdown(
        """
        The goal is not simply to automate a water pump or classify
        a leaf.

        Our larger idea is to use **AI, IoT and data-driven technology**
        to support agriculture that is more precise, efficient and
        sustainable.

        **Measure → Understand → Decide → Act → Recheck**
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">

        <b>AI + IoT Based Precision Agriculture</b><br>

        Science • Technology • Innovation • Sustainable Agriculture

    </div>
    """,
    unsafe_allow_html=True
)
