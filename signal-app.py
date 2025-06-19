import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from logic import generate_multiplier, analyze_signal

st.set_page_config(page_title="Aviator Dashboard", layout="centered")
st.title("✈️ অ্যাভিয়েটর সিগন্যাল বট (Dashboard সহ)")

if "results" not in st.session_state:
    st.session_state.results = []

# Auto simulation
rounds = st.slider("🔁 কত রাউন্ড চলবে?", 1, 50, 1)
if st.button("🚀 রাউন্ড চালাও"):
    for _ in range(rounds):
        st.session_state.results.append(generate_multiplier())
    st.success(f"{rounds} রাউন্ড সফলভাবে সিমুলেটেড!")

# Result display
if st.session_state.results:
    recent = st.session_state.results[-10:]
    st.markdown(f"**🕒 শেষ ১০টি রেজাল্ট:** `{recent}`")
    signal = analyze_signal(st.session_state.results)
    st.info(f"📡 সিগন্যাল: {signal}")

    # Chart
    st.subheader("📊 ট্রেন্ড চার্ট")
    fig, ax = plt.subplots()
    ax.plot(range(len(st.session_state.results)), st.session_state.results, marker='o', color="blue")
    ax.set_xlabel("রাউন্ড")
    ax.set_ylabel("মাল্টিপ্লায়ার")
    ax.set_title("মাল্টিপ্লায়ার ট্রেন্ড")
    st.pyplot(fig)

# Reset
if st.button("🔄 রিসেট করো"):
    st.session_state.results = []
