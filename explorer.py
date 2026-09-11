import streamlit as st

st.set_page_config(
    page_title="Smart Agriculture",
    page_icon="🌱",
    layout="centered"
)

# --------------------------------------------------
# IMAGE PATHS
# --------------------------------------------------

IMG1 = "1.jpg"
IMG2 = "2.jpg"
IMG3 = "3.jpg"
IMG4 = "4.jpg"
IMG5 = "5.jpg"


# --------------------------------------------------
# PAGE CONTROL
# --------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"


def back_button():
    if st.button("⬅️ Back to Menu"):
        st.session_state.page = "home"
        st.rerun()


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if st.session_state.page == "home":

    st.title("🌱 Smart Agriculture")
    st.subheader("AI + IoT Based Precision Agriculture")

    st.write(
        "An intelligent system that combines environmental monitoring, "
        "AI-based disease detection and smart irrigation recommendations "
        "to support healthier and more efficient crop growth."
    )

    st.divider()

    st.subheader("Explore Our Project")

    # First row
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🌾 The Problem", use_container_width=True):
            st.session_state.page = "problem"
            st.rerun()

    with col2:
        if st.button("💡 What We Intend To Do", use_container_width=True):
            st.session_state.page = "idea"
            st.rerun()

    # Second row
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🍃 Disease Detection", use_container_width=True):
            st.session_state.page = "disease"
            st.rerun()

    with col2:
        if st.button("🌡️ Environmental Analysis", use_container_width=True):
            st.session_state.page = "environment"
            st.rerun()

    # Third row
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚰 Smart Irrigation", use_container_width=True):
            st.session_state.page = "irrigation"
            st.rerun()

    with col2:
        if st.button("🏗️ Our Prototype", use_container_width=True):
            st.session_state.page = "prototype"
            st.rerun()


# --------------------------------------------------
# 1. THE PROBLEM
# --------------------------------------------------

elif st.session_state.page == "problem":

    back_button()

    st.title("🌾 The Problem")

    st.write(
        "Agriculture depends on many environmental and biological factors. "
        "Changes in temperature, humidity, soil moisture and light can affect "
        "crop growth. Plant diseases can also reduce crop productivity if they "
        "are not identified early."
    )

    st.subheader("Why is this important?")

    st.write(
        "According to the Indian Council of Agricultural Research (ICAR), "
        "pests and pathogens are associated with around 15–20% yield loss "
        "in major field and horticultural crops."
    )

    st.write(
        "Farmers also need to make decisions about weather, plant protection, "
        "nutrient management, irrigation and other crop-management practices."
    )

    st.subheader("The main challenges")

    st.markdown("""
    - 🌡️ Unfavourable environmental conditions
    - 🍃 Crop diseases
    - 💧 Improper irrigation
    - 🌦️ Changing weather conditions
    - 🔍 Difficulty in identifying problems at an early stage
    """)

    st.info(
        "Our project aims to combine environmental monitoring and AI-based "
        "leaf disease detection to provide useful crop-health recommendations."
    )


# --------------------------------------------------
# 2. WHAT WE INTEND TO DO
# --------------------------------------------------

elif st.session_state.page == "idea":

    back_button()

    st.title("💡 What We Intend To Do")

    st.write(
        "Our project is designed as a smart agriculture system that combines "
        "IoT-based environmental monitoring with AI-based disease detection."
    )

    st.subheader("How the system works")

    st.write(
        "The user first selects the crop. Environmental sensors then collect "
        "important conditions around the plant. A leaf image can also be "
        "provided to the AI model for disease detection."
    )

    st.image(
        IMG1,
        caption="Main System Flow",
        use_container_width=True
    )

    st.subheader("Final Goal")

    st.write(
        "By combining environmental conditions, disease detection and "
        "irrigation information, the system can provide a simple crop-health "
        "advisory."
    )


# --------------------------------------------------
# 3. DISEASE DETECTION
# --------------------------------------------------

elif st.session_state.page == "disease":

    back_button()

    st.title("🍃 Disease Detection")

    st.write(
        "Plant diseases can sometimes be difficult to identify at an early "
        "stage. Our project uses an AI image-classification model to analyse "
        "a photograph of a plant leaf."
    )

    st.subheader("AI-based detection")

    st.write(
        "The disease detection model is trained using labelled leaf images. "
        "When a new image is provided, the model analyses visual patterns "
        "and predicts the most likely category."
    )

    st.image(
        IMG2,
        caption="AI Disease Detection Process",
        use_container_width=True
    )

    st.subheader("Why use AI?")

    st.markdown("""
    - ⚡ Fast screening of leaf images
    - 🔍 Detects visual patterns in leaves
    - 📊 Provides a prediction and confidence score
    - 🌱 Can support early identification of possible problems
    """)

    st.subheader("Limitations")

    st.write(
        "The prototype model is trained using a limited dataset. Its accuracy "
        "can be affected by image quality, lighting, background, leaf variety "
        "and diseases that were not included in the training data."
    )

    st.warning(
        "The AI prediction is intended as a screening and assistance tool, "
        "not as a replacement for farmers or agricultural experts."
    )


# --------------------------------------------------
# 4. ENVIRONMENTAL ANALYSIS
# --------------------------------------------------

elif st.session_state.page == "environment":

    back_button()

    st.title("🌡️ Environmental Analysis")

    st.write(
        "Plant growth depends on several environmental conditions. Our "
        "prototype focuses on four important measurable factors."
    )

    st.markdown(
        """
        ### 🌡️ **TEMPERATURE**

        ### 💧 **HUMIDITY**

        ### 🌱 **SOIL MOISTURE**

        ### ☀️ **LIGHT**
        """
    )

    st.divider()

    st.subheader("Sensors used")

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
        "There are also other factors that affect plant growth, such as "
        "soil nutrients, soil pH, water quality, carbon dioxide concentration, "
        "air movement, crop variety and growth stage."
    )

    st.info(
        "Our current prototype does not measure all of these factors. "
        "The environmental analysis in this prototype is rule-based, "
        "not AI-based."
    )


# --------------------------------------------------
# 5. SMART IRRIGATION
# --------------------------------------------------

elif st.session_state.page == "irrigation":

    back_button()

    st.title("🚰 Smart Irrigation")

    st.write(
        "Water is essential for crop growth, but both insufficient and "
        "unnecessary irrigation can cause problems."
    )

    st.subheader("How our system helps")

    st.write(
        "The soil moisture sensor measures the moisture level in the soil. "
        "The reading is then compared with the requirement of the selected "
        "crop to determine whether irrigation may be needed."
    )

    st.image(
        IMG4,
        caption="Smart Irrigation Decision Process",
        use_container_width=True
    )

    st.subheader("Benefits")

    st.markdown("""
    - 💧 Helps avoid unnecessary watering
    - 🌱 Helps identify potentially dry soil
    - 📊 Uses real-time soil moisture readings
    - ♻️ Supports more efficient water use
    """)

    st.info(
        "In the current prototype, the system provides an irrigation "
        "recommendation. Automatic pump control is a possible future extension."
    )


# --------------------------------------------------
# 6. OUR PROTOTYPE
# --------------------------------------------------

elif st.session_state.page == "prototype":

    back_button()

    st.title("🏗️ Our Prototype")

    st.write(
        "Our prototype combines three major components: environmental "
        "monitoring, smart irrigation and AI-based disease detection."
    )

    st.image(
        IMG5,
        caption="Complete Smart Agriculture Prototype Architecture",
        use_container_width=True
    )

    st.subheader("Hardware")

    st.markdown("""
    - 🔵 Arduino Uno
    - 🌡️ DHT11 Temperature and Humidity Sensor
    - 🌱 Soil Moisture Sensor
    - ☀️ LDR Light Sensor
    """)

    st.subheader("Software")

    st.markdown("""
    - 🐍 Python
    - 📊 Streamlit
    - 🤖 Google Teachable Machine
    """)

    st.subheader("Three main components")

    st.markdown("""
    **1. 🌡️ Environmental Monitoring**

    Sensors collect temperature, humidity, soil moisture and light data.

    **2. 🚰 Smart Irrigation**

    Soil moisture is compared with crop requirements to generate an
    irrigation recommendation.

    **3. 🍃 AI Disease Detection**

    A leaf image is analysed by an AI image-classification model to predict
    a possible disease category and confidence score.
    """)

    st.success(
        "The final outputs can be combined to provide a crop-health advisory."
    )
