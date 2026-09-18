import streamlit as st
import pandas as pd
import requests


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI + IoT Based Precision Agriculture",
    page_icon="🌱",
    layout="wide"
)


# ============================================================
# FLOWCHART IMAGES
# ============================================================

IMG1 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/1.jpg"
IMG2 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/2.jpg"
IMG3 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/3.jpg"
IMG4 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/4.jpg"
IMG5 = "https://raw.githubusercontent.com/min0903navya/smart-agriculture/main/5.jpg"


# ============================================================
# GOOGLE SHEETS WEB APP
# ============================================================
# PASTE THE SAME GOOGLE APPS SCRIPT WEB APP URL
# THAT YOU ALREADY USED IN YOUR WORKING APP.
# ============================================================

GOOGLE_SHEET_URL = "PASTE_YOUR_EXISTING_GOOGLE_APPS_SCRIPT_URL_HERE"


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🌱 Project Explorer")

st.sidebar.write(
    "AI + IoT Based Precision Agriculture"
)

st.sidebar.write(
    "Use the sections below while explaining the project to the judges."
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

st.sidebar.divider()

st.sidebar.subheader("Technologies")

st.sidebar.markdown(
    """
    - Arduino Uno
    - DHT11
    - LDR
    - Soil Moisture Sensor
    - Relay
    - Water Pump
    - Python
    - Streamlit
    - Google Sheets
    - Teachable Machine
    - TensorFlow.js
    """
)


# ============================================================
# FUNCTIONS
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
# MAIN TITLE
# ============================================================

st.title("🌱 AI + IoT Based Precision Agriculture")

st.markdown(
    "**Smart Environmental Monitoring** • "
    "**Smart Irrigation** • "
    "**AI-Powered Plant Disease Detection**"
)

st.divider()


# ============================================================
# 1. THE PROBLEM
# ============================================================

if page == "🌾 The Problem":

    st.header("🌾 The Problem")

    st.write(
        "Agriculture is not simply about supplying water to a plant. "
        "Plant growth depends on several environmental conditions, "
        "while farmers also have to deal with irrigation, changing "
        "field conditions and plant-health problems."
    )

    st.write(
        "Our project focuses on three connected areas: "
        "understanding the growing environment, managing irrigation "
        "and identifying visible plant-health conditions."
    )

    st.subheader("What problems are we addressing?")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💧 Water Management")

        st.write(
            "Watering without considering the actual soil condition "
            "can lead to unnecessary watering or insufficient watering."
        )

        st.subheader("🌡️ Changing Environmental Conditions")

        st.write(
            "Temperature, humidity and light can change over time. "
            "Different plants also have different environmental requirements."
        )

    with col2:

        st.subheader("🍃 Plant Health")

        st.write(
            "Plants can develop visible symptoms on their leaves. "
            "Image-based analysis can help identify the visible condition "
            "represented by the trained model."
        )

        st.subheader("📊 Understanding Data")

        st.write(
            "Sensors produce raw measurements. Our system converts "
            "these measurements into information that is easier to "
            "understand and use for decisions."
        )

    st.divider()

    st.subheader("💡 The question behind our project")

    st.info(
        "Can affordable electronics, software and AI be combined "
        "to monitor plant conditions, reduce unnecessary irrigation "
        "and assist with plant-health identification?"
    )

    st.subheader("🔄 Overall concept")

    show_flowchart(
        IMG1,
        "Overall concept of our precision agriculture system"
    )


# ============================================================
# 2. HOW WE SOLVE IT
# ============================================================

elif page == "💡 How We Solve It":

    st.header("💡 How We Solve It")

    st.write(
        "Our project combines three main technologies. "
        "Each one has a specific role in the system."
    )

    st.divider()

    st.subheader("1. 🌡️ Environmental Monitoring")

    st.write(
        "We use sensors to monitor the conditions around the plant."
    )

    st.markdown(
        """
        **The system measures:**

        - 🌡️ Temperature
        - 💧 Humidity
        - ☀️ Light intensity
        - 🌱 Soil moisture
        """
    )

    st.write(
        "The Arduino receives the sensor readings and sends them "
        "to the computer through USB serial communication. "
        "Python and Streamlit then display and analyse the readings."
    )

    st.divider()

    st.subheader("2. 🚰 Smart Irrigation")

    st.write(
        "The soil moisture sensor helps determine whether watering "
        "is required."
    )

    st.markdown(
        """
        **Our basic irrigation process is:**

        Soil condition → Decision → Relay → Pump → Wait → Recheck
        """
    )

    st.write(
        "When the soil is too dry, the pump operates for approximately "
        "one second. The pump then turns OFF and the system waits "
        "approximately 30 seconds before checking the soil again."
    )

    st.divider()

    st.subheader("3. 🍃 AI-Powered Plant Disease Detection")

    st.write(
        "Environmental sensors cannot identify a visible leaf condition. "
        "Therefore, we use a separate AI-based image-classification system."
    )

    st.write(
        "A leaf image is given to our trained model, which predicts "
        "the most likely class from the five classes in our prototype."
    )

    st.write(
        "We use a 70% confidence threshold in our current prototype."
    )

    st.divider()

    st.subheader("🔄 How the complete system fits together")

    show_flowchart(
        IMG1,
        "Overall system flow"
    )

    st.info(
        "Important: Environmental suitability analysis in our current "
        "prototype is rule-based using reference ranges. The genuine "
        "AI component is the plant leaf image-classification system."
    )


# ============================================================
# 3. ENVIRONMENTAL MONITORING
# ============================================================

elif page == "🌡️ Environmental Monitoring":

    st.header("🌡️ Environmental Monitoring")

    st.write(
        "The first step is to understand what is happening around "
        "the plant."
    )

    st.write(
        "Our system measures temperature, humidity, light and soil "
        "moisture and compares the readings with reference requirements "
        "for the selected plant."
    )

    st.divider()

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
            "Arduino Pin": [
                "Digital D2",
                "Analog A0",
                "Analog A1"
            ]
        }
    )

    st.table(sensor_table)

    st.divider()

    st.subheader("🔄 Environmental monitoring flow")

    show_flowchart(
        IMG3,
        "Environmental monitoring workflow"
    )

    st.divider()

    st.subheader("🧑‍💻 How our code works")

    st.markdown(
        """
        **Step 1 — Arduino reads the sensors**

        The Arduino program reads temperature, humidity, light and
        soil-moisture values.

        **Step 2 — Serial communication**

        The Arduino sends the readings to the computer through USB.

        **Step 3 — Python receives the readings**

        Python reads the serial data coming from the Arduino.

        **Step 4 — Rule-based analysis**

        The readings are compared with reference ranges for the
        selected plant.

        **Step 5 — Streamlit displays the result**

        The application presents the information as understandable
        conditions such as **Suitable**, **Too Low**, **Too High**,
        **Too Dry** or **Too Wet**.
        """
    )

    st.divider()

    st.subheader("🌱 Reference conditions")

    crop = st.selectbox(
        "Select a plant:",
        [
            "Fenugreek",
            "Money Plant"
        ]
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

    st.table(reference_table)

    st.caption(
        "The soil-moisture limits shown here are prototype reference "
        "values. Real agricultural deployment would require controlled "
        "calibration for the sensor, soil and crop."
    )

    st.divider()

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
# 4. SMART IRRIGATION
# ============================================================

elif page == "🚰 Smart Irrigation":

    st.header("🚰 Smart Irrigation")

    st.write(
        "The system uses soil moisture information to determine "
        "whether irrigation is required."
    )

    st.write(
        "The pump is not allowed to run continuously. "
        "Instead, the system uses short watering cycles followed "
        "by a soaking period and another measurement."
    )

    st.divider()

    st.subheader("🔄 Irrigation workflow")

    show_flowchart(
        IMG4,
        "Smart irrigation workflow"
    )

    st.divider()

    st.subheader("⚙️ Actual irrigation sequence")

    st.markdown(
        """
        **1. Check the soil**

        The normal irrigation decision is made at approximately
        five-minute intervals.

        **2. Soil is suitable**

        The pump remains OFF.

        **3. Soil is too wet**

        The pump remains OFF.

        **4. Soil is too dry**

        The relay is activated and the pump runs for approximately
        one second.

        **5. Pump OFF**

        Watering stops.

        **6. Wait approximately 30 seconds**

        This gives the water time to spread through the soil.

        **7. Recheck the soil**

        The moisture condition is measured again.

        **8. Repeat only if required**

        If the soil is still too dry, another short watering cycle
        can take place.
        """
    )

    st.divider()

    st.subheader("🧑‍💻 How our code works")

    st.markdown(
        """
        **Soil reading**

        ↓

        **Determine soil state**

        ↓

        **Decide whether watering is required**

        ↓

        **Arduino controls the relay**

        ↓

        **Pump operates for a short duration**

        ↓

        **Wait for the water to spread**

        ↓

        **Measure again**
        """
    )

    st.info(
        "The Arduino also contains a one-second safety cutoff for "
        "the pump. This acts as a hardware-level backup against "
        "the pump remaining ON indefinitely."
    )

    st.divider()

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
# 5. AI PLANT DISEASE DETECTION
# ============================================================

elif page == "🍃 AI Plant Disease Detection":

    st.header("🍃 AI-Powered Plant Disease Detection")

    st.write(
        "Environmental sensors tell us about the conditions around "
        "the plant, but they cannot identify a visible condition "
        "on a leaf."
    )

    st.write(
        "For this reason, we added a separate AI-based "
        "image-classification system."
    )

    st.divider()

    st.subheader("🔄 AI detection workflow")

    show_flowchart(
        IMG2,
        "Plant disease detection workflow"
    )

    st.divider()

    st.subheader("🧠 How the AI system works")

    st.markdown(
        """
        **1. Upload a leaf image**

        The user provides an image of a plant leaf.

        **2. Send the image to the model**

        The trained image-classification model receives the image.

        **3. Generate predictions**

        The model calculates probabilities for the trained classes.

        **4. Select the highest probability**

        The class with the highest predicted probability is selected.

        **5. Apply the confidence threshold**

        Our prototype uses a 70% confidence threshold.
        """
    )

    st.divider()

    st.subheader("🍃 Classes in our current model")

    classes_table = pd.DataFrame(
        {
            "Class": [
                "Rose Healthy",
                "Rose Powdery Mildew",
                "Rose Spider Mite Damage",
                "Brinjal Healthy",
                "Brinjal Leaf Blight"
            ]
        }
    )

    st.table(classes_table)

    st.divider()

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

    st.table(test_results)

    st.warning(
        "These are prototype test results from our current trained "
        "model. They are not a claim of validated field accuracy."
    )

    st.divider()

    st.subheader("🧑‍💻 Technology used")

    st.markdown(
        """
        The main application is written in **Python using Streamlit**.

        We use **HTML and CSS** for the embedded interface and
        **JavaScript with TensorFlow.js** to load and run the
        Teachable Machine image-classification model in the browser.

        **Python / Streamlit**
        → application interface

        **JavaScript / TensorFlow.js**
        → runs the image model in the browser

        **Teachable Machine**
        → trained image-classification model
        """
    )


# ============================================================
# 6. OUR PROTOTYPE
# ============================================================

elif page == "🏗️ Our Prototype":

    st.header("🏗️ Our Prototype")

    st.write(
        "Our prototype combines the physical sensing system with "
        "software for monitoring, analysis and AI-based image classification."
    )

    st.divider()

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
                "Temperature and humidity measurement",
                "Light measurement",
                "Soil moisture measurement",
                "Electrical control of the pump",
                "Water supply",
                "DHT11 pull-up and LDR voltage divider"
            ]
        }
    )

    st.dataframe(
        hardware_table,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

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
                "Running the model in the browser"
            ]
        }
    )

    st.dataframe(
        software_table,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("🏗️ Complete system architecture")

    show_flowchart(
        IMG5,
        "Complete hardware and software architecture"
    )

    st.divider()

    st.subheader("🔗 Hardware connections")

    st.markdown(
        """
        **DHT11 → Arduino D2**

        Temperature and humidity data are sent to the Arduino.

        **LDR → Arduino A0**

        The LDR voltage-divider circuit produces an analogue signal
        corresponding to changes in light.

        **Soil Moisture Sensor → Arduino A1**

        The Arduino reads the analogue soil-moisture signal.

        **Arduino D7 → Relay**

        The Arduino sends the pump-control signal to the relay.

        **Relay → Water Pump**

        The relay acts as the electrically controlled switch.

        **Arduino → USB → Computer**

        Sensor readings are sent to the Python/Streamlit application.
        """
    )

    st.info(
        "The final prototype does not use an LCD. The computer dashboard "
        "is used for displaying the monitored data and analysis."
    )


# ============================================================
# 7. FUTURE VISION
# ============================================================

elif page == "🔮 Future Vision":

    st.header("🔮 Future Vision")

    st.write(
        "Our current project demonstrates environmental monitoring, "
        "smart irrigation and AI-based leaf classification."
    )

    st.write(
        "The next step would be to integrate these capabilities more "
        "closely for a particular crop and field."
    )

    st.divider()

    st.subheader("🧪 More complete soil analysis")

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

    st.divider()

    st.subheader("🤖 Integrated AI + IoT")

    st.write(
        "Environmental data and plant-health information could eventually "
        "be considered together instead of being separate demonstrations."
    )

    st.markdown(
        """
        **Environmental data + Soil data + Crop information + Leaf health**
        """
    )

    st.divider()

    st.subheader("🌾 Intelligent Crop Planning")

    st.write(
        "A future crop-planning system could consider the current crop, "
        "previous crop, soil condition, water availability, environmental "
        "conditions and nutrient requirements."
    )

    st.write(
        "It could then suggest suitable candidate crops for the next "
        "growing cycle."
    )

    st.divider()

    st.subheader("🌱 Crop Rotation")

    st.write(
        "Future crop planning could include suitable leguminous crops "
        "such as green gram, black gram or cowpea, depending on the "
        "actual field conditions and crop plan."
    )

    st.divider()

    st.subheader("📱 Farmer-Friendly Application")

    st.write(
        "Instead of showing complicated raw sensor values, a future "
        "mobile or web application could convert the information into "
        "simple messages."
    )

    st.markdown(
        """
        - 💧 Water required
        - 🌡️ Temperature too high
        - ☀️ Light suitable
        - 🌱 Soil condition needs attention
        - 🍃 Possible leaf condition detected
        """
    )

    st.divider()

    st.subheader("💼 Possible Future Service")

    st.write(
        "A future version could combine a low-cost sensor unit with "
        "a mobile or web application."
    )

    st.write(
        "Different versions could potentially be developed for small "
        "farms, larger farms, greenhouses and different crops."
    )

    st.divider()

    st.subheader("🌍 Our larger vision")

    st.info(
        "Our larger idea is to use AI, IoT and data-driven technology "
        "to support agriculture that is more precise, efficient and sustainable."
    )

    st.markdown(
        """
        ### Measure → Understand → Decide → Act → Recheck
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI + IoT Based Precision Agriculture • "
    "Science • Technology • Innovation • Sustainable Agriculture"
)
