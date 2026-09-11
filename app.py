
import streamlit as st

# -----------------------------
# TITLE
# -----------------------------

st.title("🌱 Smart Agriculture System")
st.write("AI + IoT Precision Agriculture")

# -----------------------------
# CROP SELECTION
# -----------------------------

crop = st.selectbox(
    "🌾 Select your crop",
    ["Rice", "Tomato", "Potato", "Maize"]
)

# -----------------------------
# SENSOR INPUTS
# -----------------------------

st.subheader("🌍 Environmental Conditions")

temperature = st.slider(
    "🌡️ Temperature (°C)",
    0,
    50,
    25
)

humidity = st.slider(
    "💦 Humidity (%)",
    0,
    100,
    60
)

soil_moisture = st.slider(
    "💧 Soil Moisture (%)",
    0,
    100,
    50
)

light = st.slider(
    "🌞 Light Intensity (%)",
    0,
    100,
    70
)

# -----------------------------
# CROP REQUIREMENTS
# -----------------------------

if crop == "Rice":
    temp_min, temp_max = 20, 35
    moisture_min, moisture_max = 60, 90
    humidity_min, humidity_max = 60, 90
    light_min = 40

elif crop == "Tomato":
    temp_min, temp_max = 18, 30
    moisture_min, moisture_max = 40, 70
    humidity_min, humidity_max = 40, 70
    light_min = 60

elif crop == "Potato":
    temp_min, temp_max = 15, 25
    moisture_min, moisture_max = 40, 70
    humidity_min, humidity_max = 50, 80
    light_min = 50

else:  # Maize
    temp_min, temp_max = 18, 32
    moisture_min, moisture_max = 45, 70
    humidity_min, humidity_max = 40, 70
    light_min = 50

# -----------------------------
# CHECK CONDITIONS
# -----------------------------

temp_ok = temp_min <= temperature <= temp_max
moisture_ok = moisture_min <= soil_moisture <= moisture_max
humidity_ok = humidity_min <= humidity <= humidity_max
light_ok = light >= light_min

# -----------------------------
# SUITABILITY SCORE
# -----------------------------

suitable_factors = sum([
    temp_ok,
    moisture_ok,
    humidity_ok,
    light_ok
])

total_factors = 4

st.subheader("📊 Environmental Suitability")

st.metric(
    "🌱 Suitable Factors",
    f"{suitable_factors}/{total_factors}"
)

# -----------------------------
# FACTOR ANALYSIS
# -----------------------------

st.write("### 🔍 Factor Analysis")

if temp_ok:
    st.write(f"🌡️ Temperature: ✅ Suitable ({temperature}°C)")
else:
    if temperature < temp_min:
        st.write(
            f"🌡️ Temperature: ❌ Too low "
            f"({temperature}°C) — should be {temp_min}–{temp_max}°C."
        )
    else:
        st.write(
            f"🌡️ Temperature: ❌ Too high "
            f"({temperature}°C) — should be {temp_min}–{temp_max}°C."
        )

if moisture_ok:
    st.write(f"💧 Soil Moisture: ✅ Suitable ({soil_moisture}%)")
else:
    if soil_moisture < moisture_min:
        st.write(
            f"💧 Soil Moisture: ❌ Too low "
            f"({soil_moisture}%) — should be {moisture_min}–{moisture_max}%."
        )
    else:
        st.write(
            f"💧 Soil Moisture: ❌ Too high "
            f"({soil_moisture}%) — should be {moisture_min}–{moisture_max}%."
        )

if humidity_ok:
    st.write(f"💦 Humidity: ✅ Suitable ({humidity}%)")
else:
    if humidity < humidity_min:
        st.write(
            f"💦 Humidity: ❌ Too low "
            f"({humidity}%) — should be {humidity_min}–{humidity_max}%."
        )
    else:
        st.write(
            f"💦 Humidity: ❌ Too high "
            f"({humidity}%) — should be {humidity_min}–{humidity_max}%."
        )

if light_ok:
    st.write(f"🌞 Light: ✅ Suitable ({light}%)")
else:
    st.write(
        f"🌞 Light: ❌ Too low "
        f"({light}%) — should be at least {light_min}%."
    )

# -----------------------------
# ENVIRONMENTAL RECOMMENDATION
# -----------------------------

st.subheader("💡 Environmental Recommendation")

if suitable_factors == 4:

    st.success(
        f"🟢 Environmental conditions are suitable for {crop}."
    )

else:

    st.warning(
        f"🟡 {crop} needs environmental attention."
    )

    if not temp_ok:
        if temperature < temp_min:
            st.write("🌡️ Try to increase the temperature around the crop.")
        else:
            st.write("🌡️ Try to reduce heat around the crop.")

    if not moisture_ok:
        if soil_moisture < moisture_min:
            st.write("💧 Soil moisture is low — irrigation may be required.")
        else:
            st.write("💧 Soil moisture is high — avoid excess watering.")

    if not humidity_ok:
        if humidity < humidity_min:
            st.write("💦 Humidity is low — monitor moisture conditions.")
        else:
            st.write("💦 Humidity is high — improve ventilation if possible.")

    if not light_ok:
        st.write("🌞 Light is low — provide more suitable sunlight.")

# -----------------------------
# IRRIGATION RECOMMENDATION
# -----------------------------

st.subheader("🚰 Irrigation Recommendation")

if soil_moisture < moisture_min:
    st.error(
        f"🚨 Soil moisture is below the preferred range for {crop}. "
        "Irrigation may be required."
    )

elif soil_moisture > moisture_max:
    st.warning(
        f"⚠️ Soil moisture is above the preferred range for {crop}. "
        "Avoid additional watering."
    )

else:
    st.success(
        f"✅ Soil moisture is suitable for {crop}. "
        "No immediate irrigation is indicated."
    )

# -----------------------------
# FINAL STATUS
# -----------------------------

st.subheader("🌱 Overall Environmental Status")

if suitable_factors == 4:
    st.success("🟢 GOOD — Conditions are suitable.")

elif suitable_factors >= 2:
    st.warning("🟡 MODERATE — Some conditions need attention.")

else:
    st.error("🔴 POOR — Several environmental conditions need attention.")

# -----------------------------
# AI DISEASE DETECTION
# -----------------------------

st.subheader("🍃 AI Plant Disease Detection")

uploaded_file = st.file_uploader(
    "📷 Upload a tomato leaf image",
    type=["jpg", "jpeg", "png"]
)
