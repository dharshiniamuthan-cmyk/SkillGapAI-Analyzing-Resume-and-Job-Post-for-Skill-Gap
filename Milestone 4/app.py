import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# -----------------------------
# DATA (From Milestone 3)
# -----------------------------
matched_skills = ["python", "machine learning", "communication", "sql", "statistics", "leadership"]
partial_skills = ["deep learning", "cloud basics"]
missing_skills = ["aws", "project management", "docker", "kubernetes"]

overall_match = 72  # %

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Skill Gap Analysis Dashboard", layout="wide")

st.title("📊 Skill Gap Analysis Dashboard")

# -----------------------------
# METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Overall Match", f"{overall_match}%")
col2.metric("Matched Skills", len(matched_skills))
col3.metric("Missing Skills", len(missing_skills))

# -----------------------------
# PIE CHART
# -----------------------------
st.subheader("Skill Match Overview")

labels = ["Matched Skills", "Partial Matches", "Missing Skills"]
sizes = [len(matched_skills), len(partial_skills), len(missing_skills)]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.0f%%", startangle=140)
ax.axis("equal")
st.pyplot(fig)

# -----------------------------
# SKILL COMPARISON TABLE
# -----------------------------
st.subheader("Skill Comparison")

df = pd.DataFrame({
    "Matched Skills": pd.Series(matched_skills),
    "Partial Skills": pd.Series(partial_skills),
    "Missing Skills": pd.Series(missing_skills)
})

st.dataframe(df)

# -----------------------------
# UPSKILLING RECOMMENDATIONS
# -----------------------------
st.subheader("📘 Upskilling Recommendations")

for skill in missing_skills:
    st.write(f"• Consider learning **{skill.upper()}**")

# -----------------------------
# CSV DOWNLOAD
# -----------------------------
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇ Download CSV Report",
    data=csv,
    file_name="skill_gap_report.csv",
    mime="text/csv"
)

# -----------------------------
# PDF DOWNLOAD
# -----------------------------
def generate_pdf():
    file_name = "skill_gap_report.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)
    text = c.beginText(40, 800)
    text.setFont("Helvetica", 11)

    text.textLine("Skill Gap Analysis Report")
    text.textLine("")
    text.textLine(f"Overall Match: {overall_match}%")
    text.textLine("")
    text.textLine("Matched Skills:")
    for s in matched_skills:
        text.textLine(f"- {s}")

    text.textLine("")
    text.textLine("Missing Skills:")
    for s in missing_skills:
        text.textLine(f"- {s}")

    c.drawText(text)
    c.save()
    return file_name

if st.button("⬇ Download PDF Report"):
    pdf_file = generate_pdf()
    with open(pdf_file, "rb") as f:
        st.download_button(
            label="Click to Download PDF",
            data=f,
            file_name=pdf_file,
            mime="application/pdf"
        )
