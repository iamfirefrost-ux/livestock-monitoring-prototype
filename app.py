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
