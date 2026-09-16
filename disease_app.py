

import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(
    page_title="AI Plant Disease Detection",
    page_icon="🌱",
    layout="centered"
)

# ---------- PAGE TITLE ----------

st.title("🌱 AI Plant Disease Detection")

st.markdown(
    """
    <p style="color:#F5E6D3; font-size:18px;">
        Upload a leaf image and the trained AI model will
        predict the most likely plant condition.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------- IMAGE UPLOAD ----------

uploaded_file = st.file_uploader(
    "📷 Upload a leaf image",
    type=["jpg", "jpeg", "png"]
)

# ---------- AI ANALYSIS ----------

if uploaded_file is not None:

    image_bytes = uploaded_file.getvalue()
    image_base64 = base64.b64encode(image_bytes).decode()

    html_code = f"""
<!DOCTYPE html>
<html>

<head>

<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest"></script>

<script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@0.8/dist/teachablemachine-image.min.js"></script>

<style>

body {{
    font-family: Arial, sans-serif;
    text-align: center;
    background: transparent;
    color: #F5E6D3;
}}

img {{
    max-width: 100%;
    max-height: 300px;
    border-radius: 12px;
    margin: 10px;
}}

#result {{
    margin-top: 20px;
    text-align: left;
    color: #F5E6D3;
}}

.prediction {{
    text-align: center;
    font-size: 23px;
    font-weight: bold;
    color: #F5E6D3;
}}

.confidence {{
    text-align: center;
    font-size: 18px;
    color: #F5E6D3;
}}

.confidence b {{
    color: #F5E6D3;
}}

.box {{
    margin-top: 15px;
    padding: 15px;
    border-radius: 12px;
    background: rgba(245, 230, 211, 0.10);
    color: #F5E6D3;
}}

.box p {{
    color: #F5E6D3;
    line-height: 1.5;
}}

.title {{
    font-weight: bold;
    font-size: 18px;
    color: #F5E6D3;
}}

.warning {{
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    color: #F5E6D3;
}}

ul {{
    color: #F5E6D3;
    line-height: 1.7;
}}

li {{
    color: #F5E6D3;
}}

</style>

</head>

<body>

<img
    id="leafImage"
    src="data:image/jpeg;base64,{image_base64}"
>

<div id="result">

    <div class="prediction">
        🤖 Analysing leaf...
    </div>

</div>

<script>

const MODEL_URL =
    "https://teachablemachine.withgoogle.com/models/_uozHQYQX/";

async function predict() {{

    try {{

        const modelURL =
            MODEL_URL + "model.json";

        const metadataURL =
            MODEL_URL + "metadata.json";

        const model = await tmImage.load(
            modelURL,
            metadataURL
        );

        const image =
            document.getElementById("leafImage");

        const predictions =
            await model.predict(image);

        predictions.sort(
            (a, b) =>
            b.probability - a.probability
        );

        const best = predictions[0];

        const confidence =
            (best.probability * 100).toFixed(2);

        // ---------- 70% CONFIDENCE THRESHOLD ----------

        if (best.probability < 0.70) {{

            document.getElementById("result").innerHTML =

                "<div class='warning'>" +
                "⚠️ Unable to confidently identify" +
                "</div>" +

                "<p class='confidence'>" +
                "Model confidence: <b>" +
                confidence +
                "%</b>" +
                "</p>" +

                "<div class='box'>" +

                "<div class='title'>📷 Try Again</div>" +

                "<p>" +
                "Please upload a clear image of a " +
                "<b>rose or brinjal leaf</b>." +
                "</p>" +

                "</div>";

            return;
        }}

        const label =
            best.className.toLowerCase().trim();

        let displayName = best.className;
        let cause = "";
        let action = "";

        // ---------- ROSE HEALTHY ----------

        if (label.includes("rose healthy")) {{

            displayName =
                "Rose — Healthy";

            cause =
                "No disease condition was identified by the trained model.";

            action =
                "Continue normal plant care and monitor the leaves regularly.";

        }}

        // ---------- ROSE MILDEW ----------

        else if (label.includes("mildew")) {{

            displayName =
                "Rose — Powdery Mildew";

            cause =
                "<ul>" +
                "<li>High humidity at night followed by warm, dry days</li>" +
                "<li>Low light or shaded locations</li>" +
                "<li>Poor air circulation or overcrowding</li>" +
                "<li>Leaf moisture remaining overnight</li>" +
                "</ul>";

            action =
                "<ul>" +
                "<li>Prune branches to improve airflow</li>" +
                "<li>Provide adequate sunlight where practical</li>" +
                "<li>Prefer early-morning watering</li>" +
                "<li>Water the roots directly rather than keeping leaves wet</li>" +
                "</ul>";

        }}

        // ---------- ROSE SPIDER MITES ----------

        else if (label.includes("spider")) {{

            displayName =
                "Rose — Spider Mite Damage";

            cause =
                "<ul>" +
                "<li>High temperatures</li>" +
                "<li>Low humidity and very dry air</li>" +
                "<li>Dusty environments</li>" +
                "<li>Drought stress or insufficient watering</li>" +
                "</ul>";

            action =
                "<ul>" +
                "<li>Maintain adequate soil moisture</li>" +
                "<li>Reduce plant stress during hot, dry conditions</li>" +
                "<li>Inspect the undersides of leaves regularly</li>" +
                "<li>Use appropriate plant-safe pest-control methods if needed</li>" +
                "<li>Beneficial predatory insects can also help control mite populations</li>" +
                "</ul>";

        }}

        // ---------- BRINJAL HEALTHY ----------

        else if (label.includes("brinjal healthy")) {{

            displayName =
                "Brinjal — Healthy";

            cause =
                "No disease condition was identified by the trained model.";

            action =
                "Continue normal plant care and monitor the leaves regularly.";

        }}

        // ---------- BRINJAL LEAF BLIGHT ----------

        else if (label.includes("blite")) {{

            displayName =
                "Brinjal — Leaf Blight";

            cause =
                "<ul>" +
                "<li>Warm temperatures combined with heavy rainfall</li>" +
                "<li>High humidity</li>" +
                "<li>Frequent overhead watering</li>" +
                "<li>Water or soil splashing onto lower leaves</li>" +
                "</ul>";

            action =
                "<ul>" +
                "<li>Prefer drip or root-level irrigation</li>" +
                "<li>Use soil mulch to reduce water and mud splashing</li>" +
                "<li>Remove lower leaves that touch the ground</li>" +
                "<li>Clear dead plant debris around the plant</li>" +
                "</ul>";

        }}

        // ---------- FALLBACK ----------

        else {{

            displayName =
                best.className;

            cause =
                "The model identified a condition without a specific advisory in this prototype.";

            action =
                "Monitor the plant and compare symptoms with reliable plant-disease guidance.";

        }}

        document.getElementById("result").innerHTML =

            "<div class='prediction'>" +
            "🤖 AI Prediction" +
            "</div>" +

            "<p class='prediction'>" +
            displayName +
            "</p>" +

            "<p class='confidence'>" +
            "Confidence: <b>" +
            confidence +
            "%</b>" +
            "</p>" +

            "<div class='box'>" +

            "<div class='title'>" +
            "🔍 Possible Environmental Causes" +
            "</div>" +

            cause +

            "</div>" +

            "<div class='box'>" +

            "<div class='title'>" +
            "💡 What To Do" +
            "</div>" +

            action +

            "</div>";

    }}

    catch (error) {{

        document.getElementById("result").innerHTML =

            "<div class='warning'>" +
            "❌ Unable to analyse the image" +
            "</div>" +

            "<p class='confidence'>" +
            "Please check your internet connection and try again." +
            "</p>";

        console.error(error);

    }}

}}

predict();

</script>

</body>
</html>
"""

    components.html(
       html_code,
       height=800,
       scrolling=True
    )

st.divider()

st.markdown(
    """
    <p style="color:#F5E6D3; text-align:center;">
        AI model trained using Google Teachable Machine.
    </p>
    """,
    unsafe_allow_html=True
)

