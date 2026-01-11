st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}
.card {
    padding: 15px;
    border-radius: 10px;
    background-color: white;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}
.badge-normal {
    color: white;
    background-color: #28a745;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 12px;
}
.badge-alert {
    color: white;
    background-color: #dc3545;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 12px;
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
