import os
import json
import tempfile

import streamlit as st
from analyzer import analyze_handwriting

st.set_page_config(
    page_title="AI Handwriting Analyzer",
    page_icon="✍️",
    layout="wide"
)

st.title("✍️ AI Handwriting Analyzer")

st.markdown(
    "Upload a handwritten **image** or **PDF** and receive OCR + handwriting analysis."
)

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["png", "jpg", "jpeg", "pdf"]
)

if uploaded_file is not None:
    suffix = os.path.splitext(uploaded_file.name)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    st.divider()

    if suffix.lower() == ".pdf":

        st.success("PDF uploaded successfully.")

    else:
        st.image(
            file_path,
            caption="Uploaded Image",
            use_container_width=True
        )

    if st.button("🚀 Analyze Handwriting", type="primary"):

        with st.spinner("Analyzing..."):

            result = analyze_handwriting(file_path)

        st.success("Analysis Complete!")

        st.divider()

        c1, c2, c3 = st.columns(3)

        c1.metric("Overall Score", result["overall_score"])
        c2.metric("Legibility", result["legibility"])
        c3.metric("Letter Consistency", result["letter_consistency"])

        c4, c5, c6 = st.columns(3)

        c4.metric("Word Spacing", result["word_spacing"])
        c5.metric("Line Spacing", result["line_spacing"])
        c6.metric("Baseline Alignment", result["baseline_alignment"])

        st.divider()

        st.subheader("Writing Style")

        st.write(f"**Estimated Level:** {result['estimated_level']}")
        st.write(f"**Slant:** {result['slant']}")
        st.write(f"**Writing Style:** {result['writing_style']}")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Strengths")

            if result["strengths"]:
                for item in result["strengths"]:
                    st.success(item)
            else:
                st.info("None")

        with col2:

            st.subheader("Areas to Improve")

            if result["weaknesses"]:
                for item in result["weaknesses"]:
                    st.error(item)
            else:
                st.info("None")

        st.divider()

        st.subheader("Improvement Suggestions")

        if result["improvements"]:
            for tip in result["improvements"]:
                st.info(tip)

        st.divider()

        st.subheader("Difficult Words")

        if result["difficult_words"]:
            st.write(result["difficult_words"])
        else:
            st.success("No difficult words detected.")

        st.divider()

        with st.expander("Extracted Text", expanded=True):
            st.text_area(
                "",
                result["extracted_text"],
                height=350
            )

        st.divider()

        st.download_button(
            label="⬇ Download JSON Report",
            data=json.dumps(result, indent=4),
            file_name="handwriting_analysis.json",
            mime="application/json"
        )

        os.remove(file_path)