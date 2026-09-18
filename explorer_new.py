import streamlit as st
import pandas as pd
import requests


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Agriculture",
    page_icon="🌱",
    layout="centered"
)


# ============================================================
# IMAGE PATHS
# ============================================================

IMG1 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/1.jpg"
IMG2 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/2.jpg"
IMG3 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/3.jpg"
IMG4 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/4.jpg"
IMG5 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/5.jpg"


# ============================================================
# GOOGLE APPS SCRIPT URL
# ============================================================

GOOGLE_SCRIPT_URL = (
    "https://script.google.com/macros/s/"
    "AKfycbxahGoaxdj2J_3M2lyy_UPOdfJTaBNXsF0NW8FReMvuOR-mQg23flpPiMXKwgqIAjWiJw"
    "/exec"
)


# ============================================================
# PAGE CONTROL
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


def back_button():
    if st.button("⬅️ Back to Menu"):
        st.session_state.page = "home"
        st.rerun()


# ============================================================
# GOOGLE SHEET DATA FUNCTIONS
# ============================================================

def get_sensor_data():

    try:
        response = requests.get(
            GOOGLE_SCRIPT_URL + "?read=sensor",
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            st.error("Google Sheet returned an unexpected response.")
            return pd.DataFrame()

        df = pd.DataFrame(data)

        if df.empty:
            return df

        # Remove completely empty rows
        df = df.dropna(how="all")

        return df

    except Exception as e:
        st.error(f"Could not load Sensor Data: {e}")
        return pd.DataFrame()


def get_irrigation_data():

    try:
        response = requests.get(
            GOOGLE_SCRIPT_URL + "?read=irrigation",
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            st.error("Google Sheet returned an unexpected response.")
            return pd.DataFrame()

        df = pd.DataFrame(data)

        if df.empty:
            return df

        # Remove completely empty rows
        df = df.dropna(how="all")

        return df

    except Exception as e:
        st.error(f"Could not load Irrigation Log: {e}")
        return pd.DataFrame()


# ============================================================
# HOME PAGE
# ============================================================

if st.session_state.page == "home":

    st.title("🌱 Smart Agriculture")
    st.subheader("AI + IoT Based Precision Agriculture")

    st.write(
        "A prototype that combines environmental monitoring, "
        "smart irrigation and AI-based plant disease detection."
    )

    st.divider()

    st.subheader("Explore Our Project")

    # --------------------------------------------------------
    # ROW 1
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🌾 The Problem", use_container_width=True):
            st.session_state.page = "problem"
            st.rerun()

    with col2:
        if st.button("💡 What We Intend To Do", use_container_width=True):
            st.session_state.page = "idea"
            st.rerun()

    # --------------------------------------------------------
    # ROW 2
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🍃 Disease Detection", use_container_width=True):
            st.session_state.page = "disease"
            st.rerun()

    with col2:
        if st.button("🌡️ Environmental Analysis", use_container_width=True):
            st.session_state.page = "environment"
            st.rerun()

    # --------------------------------------------------------
    # ROW 3
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚰 Smart Irrigation", use_container_width=True):
            st.session_state.page = "irrigation"
            st.rerun()

    with col2:
        if st.button("🧑‍💻 Our Code", use_container_width=True):
            st.session_state.page = "code"
            st.rerun()

    # --------------------------------------------------------
    # ROW 4
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📊 Recorded Data", use_container_width=True):
            st.session_state.page = "data"
            st.rerun()

    with col2:
        if st.button("🏗️ Our Prototype", use_container_width=True):
            st.session_state.page = "prototype"
            st.rerun()


# ============================================================
# 1. THE PROBLEM
# ============================================================

elif st.session_state.page == "problem":

    back_button()

    st.title("🌾 The Problem")

    st.write(
        "Agriculture depends on many environmental and biological factors. "
        "Changes in temperature, humidity, soil moisture and light can affect "
        "crop growth. Plant diseases can also reduce crop productivity."
    )

    st.subheader("The main challenges")

    st.markdown("""
    - 🌡️ Unfavourable environmental conditions
    - 🍃 Plant diseases
    - 💧 Improper irrigation
    - 🌦️ Changing weather conditions
    - 🔍 Difficulty in identifying problems early
    """)

    st.subheader("Why this matters")

    st.write(
        "Farmers need to make decisions about irrigation, plant health, "
        "weather conditions, nutrients and plant protection."
    )

    st.info(
        "Our project explores how sensors, automation and AI can support "
        "better-informed crop-management decisions."
    )


# ============================================================
# 2. WHAT WE INTEND TO DO
# ============================================================

elif st.session_state.page == "idea":

    back_button()

    st.title("💡 What We Intend To Do")

    st.write(
        "We intend to build a precision agriculture system that can monitor "
        "plant conditions, automate irrigation and analyse leaf images."
    )

    st.image(
        IMG1,
        caption="Main System Flow",
        use_container_width=True
    )

    st.subheader("Our approach")

    st.markdown("""
    **🌡️ Monitor**

    Measure temperature, humidity, soil moisture and light.

    **🚰 Manage Water**

    Use soil moisture information to control irrigation.

    **🍃 Analyse Leaves**

    Use AI to classify visible conditions in leaf images.
    """)

    st.subheader("Goal")

    st.write(
        "The aim is to use available information about the plant and its "
        "environment to support better crop management."
    )


# ============================================================
# 3. DISEASE DETECTION
# ============================================================

elif st.session_state.page == "disease":

    back_button()

    st.title("🍃 AI Disease Detection")

    st.write(
        "Our AI model analyses a photograph of a plant leaf and predicts "
        "the category that most closely matches the visual patterns it "
        "has learned."
    )

    st.image(
        IMG2,
        caption="AI Disease Detection Process",
        use_container_width=True
    )

    st.subheader("🤖 AI Classification")

    st.write(
        "The model was trained using Google Teachable Machine with five "
        "leaf-image classes."
    )

    st.markdown("""
    ### 🌹 Rose

    • Rose Healthy  
    • Rose Powdery Mildew  
    • Rose Spider Mite Damage

    ### 🍆 Brinjal

    • Brinjal Healthy  
    • Brinjal Leaf Blight
    """)

    st.divider()

    st.subheader("🧪 Our Testing")

    st.write(
        "We tested one demonstration image for each of the five classes "
        "and recorded the confidence shown by the model."
    )

    testing_data = pd.DataFrame({
        "Plant": [
            "Rose",
            "Rose",
            "Rose",
            "Brinjal",
            "Brinjal"
        ],
        "Tested Condition": [
            "Healthy",
            "Powdery Mildew",
            "Spider Mite Damage",
            "Healthy",
            "Leaf Blight"
        ],
        "Confidence": [
            "93%",
            "93%",
            "95%",
            "98%",
            "97%"
        ]
    })

    st.dataframe(
        testing_data,
        use_container_width=True,
        hide_index=True
    )

    st.write(
        "The model's confidence was above 90% for each of these "
        "demonstration tests."
    )

    st.subheader("70% Confidence Threshold")

    st.write(
        "For our application, predictions at or above 70% are displayed "
        "with the corresponding possible causes and suggested actions. "
        "Below 70%, the system asks for a clearer leaf image."
    )


# ============================================================
# 4. ENVIRONMENTAL ANALYSIS
# ============================================================

elif st.session_state.page == "environment":

    back_button()

    st.title("🌡️ Environmental Analysis")

    st.write(
        "Our prototype focuses on four measurable environmental factors "
        "that influence plant growth."
    )

    st.markdown("""
    ### 🌡️ Temperature

    Affects plant growth and suitability for different crops.

    ### 💧 Humidity

    Indicates the moisture present in the surrounding air.

    ### 🌱 Soil Moisture

    Indicates whether the soil is sufficiently wet or becoming dry.

    ### ☀️ Light

    Indicates the amount of light available to the plant.
    """)

    st.divider()

    st.subheader("Sensors Used")

    st.markdown("""
    **DHT11 → Temperature + Humidity**

    **Soil Moisture Sensor → Soil Moisture**

    **LDR → Light**

    **Arduino Uno → Collects sensor readings**

    **Python + Streamlit → Displays and analyses the readings**
    """)

    st.image(
        IMG3,
        caption="Environmental Monitoring and Analysis",
        use_container_width=True
    )

    st.subheader("Other factors")

    st.write(
        "Plant growth is also affected by soil pH, nutrients such as NPK, "
        "water quality, pests, diseases, crop variety and growth stage."
    )

    st.write(
        "NPK measurement was considered for the prototype but was not "
        "included because of the additional equipment required."
    )


# ============================================================
# 5. SMART IRRIGATION
# ============================================================

elif st.session_state.page == "irrigation":

    back_button()

    st.title("🚰 Smart Irrigation")

    st.write(
        "The smart irrigation system uses soil moisture information to "
        "determine whether the selected crop may need water."
    )

    st.image(
        IMG4,
        caption="Smart Irrigation Decision Process",
        use_container_width=True
    )

    st.subheader("How it works")

    st.markdown("""
    **Soil Moisture Sensor**

    ↓

    **Arduino Uno**

    ↓

    **Compare with Crop Requirement**

    ↓

    **Relay**

    ↓

    **DC Water Pump**
    """)

    st.subheader("🌱 Crop-specific soil conditions")

    st.markdown("""
    **Fenugreek**

    Target moisture: approximately 50–85%

    **Money Plant**

    Target moisture: approximately 25–50%
    """)

    st.subheader("⚙️ Automatic irrigation")

    st.write(
        "When the soil is detected as too dry, the Arduino activates "
        "the relay and the small DC pump runs for a short watering period. "
        "The system then checks the soil condition again."
    )

    st.subheader("📟 LCD Display")

    st.write(
        "The 16×2 I²C LCD displays the pump status and soil sensor value "
        "during operation."
    )

    st.success(
        "The system is designed to water according to the crop's soil "
        "condition instead of relying only on a fixed watering schedule."
    )


# ============================================================
# 6. OUR CODE
# ============================================================

elif st.session_state.page == "code":

    back_button()

    st.title("🧑‍💻 Our Code")

    st.write(
        "Three main coding parts were used in our prototype."
    )

    # --------------------------------------------------------
    # ARDUINO
    # --------------------------------------------------------

    st.subheader("🔌 1. Arduino Code")

    st.markdown("""
    The Arduino program handles:

    - DHT11 temperature and humidity
    - LDR light readings
    - Soil moisture readings
    - Relay control
    - DC water pump control
    - LCD display
    - Serial communication with Python
    """)

    st.code("""
Sensors
   ↓
Arduino Uno
   ↓
Read values
   ↓
Send data through USB Serial

Arduino
   ↓
Relay
   ↓
DC Water Pump
""", language="text")

    # --------------------------------------------------------
    # PYTHON
    # --------------------------------------------------------

    st.subheader("🐍 2. Python + Streamlit")

    st.markdown("""
    Python is used to:

    - Receive Arduino sensor data
    - Display sensor readings
    - Analyse crop conditions
    - Make irrigation decisions
    - Communicate with the Google Sheets data system
    """)

    # --------------------------------------------------------
    # AI
    # --------------------------------------------------------

    st.subheader("🤖 3. AI Disease Detection")

    st.markdown("""
    The AI application handles:

    - Leaf image upload
    - Loading the trained model
    - Image prediction
    - Confidence calculation
    - 70% confidence threshold
    - Displaying possible causes and suggested actions
    """)

    st.info(
        "The disease model was trained using Google Teachable Machine."
    )


# ============================================================
# 7. RECORDED DATA
# ============================================================

elif st.session_state.page == "data":

    back_button()

    st.title("📊 Recorded Data")

    st.write(
        "The sensor readings from our prototype are recorded in our "
        "Google Sheet and can be viewed here."
    )

    # --------------------------------------------------------
    # SENSOR DATA
    # --------------------------------------------------------

    st.subheader("📡 Sensor Data")

    sensor_df = get_sensor_data()

    if not sensor_df.empty:

        st.dataframe(
            sensor_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.warning(
            "No sensor data could be loaded from the Google Sheet."
        )

    st.divider()

    # --------------------------------------------------------
    # IRRIGATION LOG
    # --------------------------------------------------------

    st.subheader("🚰 Irrigation Log")

    irrigation_df = get_irrigation_data()

    if not irrigation_df.empty:

        st.dataframe(
            irrigation_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.warning(
            "No irrigation data could be loaded from the Google Sheet."
        )

    st.caption(
        "Data shown here comes from the Smart Agriculture data logging system."
    )


# ============================================================
# 8. OUR PROTOTYPE
# ============================================================

elif st.session_state.page == "prototype":

    back_button()

    st.title("🏗️ Our Prototype")

    st.write(
        "Our prototype combines environmental sensing, smart irrigation "
        "and AI-based leaf analysis."
    )

    st.image(
        IMG5,
        caption="Complete Smart Agriculture Prototype Architecture",
        use_container_width=True
    )

    st.subheader("🔧 Hardware")

    st.markdown("""
    - Arduino Uno
    - DHT11 Temperature and Humidity Sensor
    - Soil Moisture Sensor
    - LDR Light Sensor
    - Relay Module
    - Small DC Water Pump
    - 16×2 I²C LCD
    - Breadboard and jumper wires
    """)

    st.subheader("💻 Software")

    st.markdown("""
    - Python
    - Streamlit
    - Arduino IDE
    - Google Teachable Machine
    """)

    st.subheader("🌱 What our prototype demonstrates")

    st.markdown("""
    **Environmental Monitoring**

    Measures temperature, humidity, soil moisture and light.

    **Smart Irrigation**

    Uses soil moisture and crop requirements to control watering.

    **AI Disease Detection**

    Analyses leaf images and classifies them into the five trained categories.
    """)

    st.divider()

    st.write(
        "In the future, these environmental measurements and AI leaf analysis "
        "can be integrated for the same crop and field, with additional "
        "measurements such as NPK and soil pH."
    )
