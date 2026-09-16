import streamlit as st
import streamlit.components.v1 as components
import base64

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="AI Plant Disease Detection",
    page_icon="🌿",
    layout="centered"
)

# ============================================================
# TITLE
# ============================================================

st.title("🌿 AI Plant Disease Detection")

st.write(
    "Upload a clear image of a rose or brinjal leaf. "
    "Our AI model will analyse the image and identify the most likely condition."
)

# ============================================================
# SUPPORTED PLANTS
# ============================================================

st.markdown("### 🌱 Supported Plant Categories")

st.write("🌹 Rose")
st.write("🍆 Brinjal")

st.markdown("### 🤖 AI Model Classes")

st.write("• Rose Healthy")
st.write("• Rose Powdery Mildew")
st.write("• Rose Spider Mite Damage")
st.write("• Brinjal Healthy")
st.write("• Brinjal Leaf Blight")

# ============================================================
# IMAGE UPLOAD
# ============================================================

uploaded_file = st.file_uploader(
    "📷 Upload a leaf image",
    type=["jpg", "jpeg", "png"]
)

# ============================================================
# AI PREDICTION
# ============================================================

if uploaded_file is not None:

    # Display uploaded image
    st.image(
        uploaded_file,
        caption="Uploaded Leaf Image",
        use_container_width=True
    )

    # Convert image to Base64
    image_bytes = uploaded_file.getvalue()
    image_base64 = base64.b64encode(image_bytes).decode()

    # ========================================================
    # JAVASCRIPT AI COMPONENT
    # ========================================================

    html_code = f"""
    <!DOCTYPE html>
    <html>

    <head>

        <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>

        <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest/dist/teachablemachine-image.min.js"></script>

        <style>

            body {{
                background: transparent;
                color: #F5E6D3;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 10px;
            }}

            .result {{
                margin-top: 20px;
                padding: 20px;
                border-radius: 12px;
                background: rgba(255,255,255,0.08);
            }}

            .prediction {{
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 10px;
            }}

            .confidence {{
                font-size: 20px;
                margin-bottom: 20px;
            }}

            .section {{
                margin-top: 20px;
            }}

            .section-title {{
                font-size: 21px;
                font-weight: bold;
                margin-bottom: 8px;
            }}

            .text {{
                font-size: 17px;
                line-height: 1.5;
            }}

            .loading {{
                font-size: 20px;
            }}

        </style>

    </head>

    <body>

        <div id="status" class="loading">
            🔄 Loading AI model...
        </div>

        <div id="result"></div>

        <script>

            const MODEL_URL =
                "https://teachablemachine.withgoogle.com/models/_uozHQYQX/";

            const imageBase64 = "{image_base64}";

            async function runPrediction() {{

                try {{

                    // ------------------------------------------------
                    // LOAD MODEL
                    // ------------------------------------------------

                    const modelURL = MODEL_URL + "model.json";
                    const metadataURL = MODEL_URL + "metadata.json";

                    const model = await tmImage.load(
                        modelURL,
                        metadataURL
                    );

                    document.getElementById("status").innerHTML =
                        "🔍 Analysing leaf image...";

                    // ------------------------------------------------
                    // CREATE IMAGE
                    // ------------------------------------------------

                    const image = new Image();

                    image.onload = async function() {{

                        // ------------------------------------------------
                        // PREDICT
                        // ------------------------------------------------

                        const prediction =
                            await model.predict(image);

                        // ------------------------------------------------
                        // FIND HIGHEST CONFIDENCE
                        // ------------------------------------------------

                        let highestPrediction = prediction[0];

                        for (
                            let i = 1;
                            i < prediction.length;
                            i++
                        ) {{

                            if (
                                prediction[i].probability >
                                highestPrediction.probability
                            ) {{

                                highestPrediction =
                                    prediction[i];

                            }}

                        }}

                        const label =
                            highestPrediction.className;

                        const confidence =
                            highestPrediction.probability * 100;

                        // ------------------------------------------------
                        // 70% CONFIDENCE THRESHOLD
                        // ------------------------------------------------

                        const threshold = 70;

                        let resultHTML = "";

                        document.getElementById("status").innerHTML = "";

                        if (confidence >= threshold) {{

                            // ==================================================
                            // ROSE HEALTHY
                            // ==================================================

                            if (label.toLowerCase().includes("rose healthy")) {{

                                resultHTML = `
                                    <div class="result">

                                        <div class="prediction">
                                            🌹 Rose — Healthy
                                        </div>

                                        <div class="confidence">
                                            Confidence: ${{confidence.toFixed(2)}}%
                                        </div>

                                        <div class="section">

                                            <div class="section-title">
                                                🌱 Possible Condition
                                            </div>

                                            <div class="text">
                                                The leaf appears healthy based on
                                                the visual patterns learned by
                                                the AI model.
                                            </div>

                                        </div>

                                        <div class="section">

                                            <div class="section-title">
                                                💡 What to do
                                            </div>

                                            <div class="text">
                                                Continue providing suitable
                                                sunlight, water, air circulation
                                                and regular plant care.
                                            </div>

                                        </div>

                                    </div>
                                `;

                            }}

                            // ==================================================
                            // ROSE POWDERY MILDEW
                            // ==================================================

                            else if (
                                label.toLowerCase().includes("mildew")
                            ) {{

                                resultHTML = `
                                    <div class="result">

                                        <div class="prediction">
                                            🌹 Rose — Powdery Mildew
                                        </div>

                                        <div class="confidence">
                                            Confidence: ${{confidence.toFixed(2)}}%
                                        </div>

                                        <div class="section">

                                            <div class="section-title">
                                                ⚠️ Possible Environmental Causes
                                            </div>

                                            <div class="text">
                                                • High humidity at night followed
                                                by warm, dry days.<br>

                                                • Low light or shaded locations.<br>

                                                • Poor air circulation or
                                                overcrowding.<br>

                                                • Leaf moisture remaining
                                                overnight.
                                            </div>

                                        </div>

                                        <div class="section">

                                            <div class="section-title">
                                                🛠️ What to do
                                            </div>

                                            <div class="text">
                                                • Prune branches to improve
                                                airflow.<br>

                                                • Move the plant to an area with
                                                around 6 or more hours of direct
                                                sunlight where practical.<br>

                                                • Prefer early-morning watering.<br>

                                                • Water the roots directly and
                                                try to keep the leaves dry.
                                            </div>

                                        </div>

                                    </div>
                                `;

                            }}

                            // ==================================================
                            // ROSE SPIDER MITE
                            // ==================================================

                            else if (
                                label.toLowerCase().includes("spider")
                            ) {{

                                resultHTML = `
                                    <div class="result">

                                        <div class="prediction">
                                            🌹 Rose — Spider Mite Damage
                                        </div>

                                        <div class="confidence">
                                            Confidence: ${{confidence.toFixed(2)}}%
                                        </div>

                                        <div class="section">

                                            <div class="section-title">
                                                ⚠️ Possible Environmental Causes
                                            </div>

                                            <div class="text">
                                                • High temperatures.<br>

                                                • Low humidity and very dry air.<br>

                                                • Dusty environments.<br>

                                                • Drought-stressed or
                                                underwatered plants.
                                            </div>

                                        </div>

                                        <div class="section">

                                            <div class="section-title">
                                                🛠️ What to do
                                            </div>

                                            <div class="text">
                                                • Overhead water misting can
                                                increase humidity and help wash
                                                away mites.<br>

                                                • Frequent misting of leaf
                                                undersides can also help.<br>

                                                • Regular soil watering helps
                                                prevent plant stress.<br>

                                                • Predatory insects such as
                                                ladybugs can help control mites.
                                            </div>

                                        </div>

                                    </div>
                                `;

                            }}

                            // ==================================================
                            // BRINJAL HEALTHY
                            // ==================================================

                            else if (
                                label.toLowerCase().includes("brinjal healthy")
                            ) {{

                                resultHTML = `
                                    <div class="result">

                                        <div class="prediction">
                                            🍆 Brinjal — Healthy
                                        </div>

                                        <div class="confidence">
                                            Confidence: ${{confidence.toFixed(2)}}%
                                        </div>

                                        <div class="section">

                                            <div class="section-title">
                                                🌱 Possible Condition
                                            </div>

                                            <div class="text">
                                                The leaf appears healthy based
                                                on the visual patterns learned
                                                by the AI model.
                                            </div>

                                        </div>

                                        <div class="section">

                                            <div class="section-title">
                                                💡 What to do
                                            </div>

                                            <div class="text">
                                                Continue regular watering,
                                                suitable sunlight, good airflow
                                                and normal plant care.
                                            </div>

                                        </div>

                                    </div>
                                `;

                            }}

                            // ==================================================
                            // BRINJAL LEAF BLIGHT
                            // ==================================================

                            else if (
                                label.toLowerCase().includes("brinjal") &&
                                (
                                    label.toLowerCase().includes("blite") ||
                                    label.toLowerCase().includes("blight")
                                )
                            ) {{

                                resultHTML = `
                                    <div class="result">

                                        <div class="prediction">
                                            🍆 Brinjal — Leaf Blight
                                        </div>

                                        <div class="confidence">
                                            Confidence: ${{confidence.toFixed(2)}}%
                                        </div>

                                        <div class="section">

                                            <div class="section-title">
                                                ⚠️ Possible Environmental Causes
                                            </div>

                                            <div class="text">
                                                • Warm temperatures combined
                                                with heavy rainfall.<br>

                                                • High humidity.<br>

                                                • Frequent overhead watering.<br>

                                                • Water or soil splashing onto
                                                lower leaves.
                                            </div>

                                        </div>

                                        <div class="section">

                                            <div class="section-title">
                                                🛠️ What to do
                                            </div>

                                            <div class="text">
                                                • Use drip irrigation instead
                                                of overhead sprinklers.<br>

                                                • Apply soil mulch to reduce
                                                soil splashing.<br>

                                                • Prune lower leaves touching
                                                the ground.<br>

                                                • Clear dead plant debris from
                                                around the plant.
                                            </div>

                                        </div>

                                    </div>
                                `;

                            }}

                            // ==================================================
                            // UNKNOWN CLASS
                            // ==================================================

                            else {{

                                resultHTML = `
                                    <div class="result">

                                        <div class="prediction">
                                            🌿 ${{label}}
                                        </div>

                                        <div class="confidence">
                                            Confidence: ${{confidence.toFixed(2)}}%
                                        </div>

                                    </div>
                                `;

                            }}

                        }}

                        // ======================================================
                        // BELOW 70%
                        // ======================================================

                        else {{

                            resultHTML = `
                                <div class="result">

                                    <div class="prediction">
                                        ⚠️ Unable to confidently identify
                                    </div>

                                    <div class="confidence">
                                        Highest confidence:
                                        ${{confidence.toFixed(2)}}%
                                    </div>

                                    <div class="section">

                                        <div class="section-title">
                                            📷 Please try again
                                        </div>

                                        <div class="text">
                                            Upload a clear image of a rose or
                                            brinjal leaf with good lighting and
                                            the leaf clearly visible.
                                        </div>

                                    </div>

                                </div>
                            `;

                        }}

                        document.getElementById("result").innerHTML =
                            resultHTML;

                    }};

                    image.src =
                        "data:image/jpeg;base64," + imageBase64;

                }}

                catch (error) {{

                    document.getElementById("status").innerHTML =
                        "❌ Error loading or running the AI model.";

                    document.getElementById("result").innerHTML = `
                        <div class="result">

                            <div class="text">
                                Please check your internet connection
                                and try again.
                            </div>

                        </div>
                    `;

                    console.error(error);

                }}

            }}

            runPrediction();

        </script>

    </body>

    </html>
    """

    # ========================================================
    # DISPLAY AI COMPONENT
    # ========================================================

    components.html(
        html_code,
        height=900,
        scrolling=True
    )
