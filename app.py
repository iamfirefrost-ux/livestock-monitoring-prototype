import streamlit as st
st.set_page_config(
    page_title="Livestock Monitoring System",
    layout="wide"
)
st.markdown("""
<style>
/* Remove top padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* App background */
.stApp {
    background-color: #f4f6f9;
}

/* Card style */
.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* Status badges */
.badge-normal {
    background-color: #2ecc71;
    color: white;
    padding: 4px 12px;
    border-radius: 15px;
    font-size: 12px;
}

.badge-alert {
    background-color: #e74c3c;
    color: white;
    padding: 4px 12px;
    border-radius: 15px;
    font-size: 12px;
}

/* Section titles */
.section-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h4>Animal Analysis</h4>
<p><b>Animal ID:</b> Cow-01</p>
<p><b>Status:</b> <span class="badge-normal">Normal</span></p>
<p><b>Attendance:</b> Present</p>
</div>
""", unsafe_allow_html=True)

import streamlit as st

# App title
st.title("AI-Based Livestock Monitoring System")

st.write(
    "This prototype demonstrates image-based animal identification, "
    "visual abnormality alerts, and attendance tracking."
)

# Offline mode toggle
offline_mode = st.toggle("Offline Mode")

st.subheader("Upload Animal Image")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

# Pre-registered animals (demo data)
animals = {
    "Cow-01": "Present",
    "Cow-02": "Present",
    "Cow-03": "Present",
    "Cow-04": "Absent"
}

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Animal Image", use_column_width=True)

    st.subheader("Analysis Result")

    # Simulated AI result
    st.write("**Animal ID:** Cow-01")
    st.write("**Visual Status:** Normal")
    st.write("**Attendance:** Marked Present")

    if offline_mode:
        st.info("Data saved locally (Offline Mode)")
    else:
        st.success("Data synced to cloud")

st.subheader("Daily Attendance Dashboard")

for animal, status in animals.items():
    if status == "Present":
        st.write(f"✅ {animal} : Present")
    else:
        st.write(f"❌ {animal} : Missing")

st.subheader("Vet Alerts")
st.warning("Cow-04 missing today. Requires attention.")
