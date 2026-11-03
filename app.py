
import streamlit as st
import requests
from datetime import date

st.set_page_config(
    page_title="Bug Fix Effort Predictor",
    page_icon="🐞",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
:root {
    --bg: #0B1020;
    --panel: #151E33;
    --purple: #9B87F5;
    --lavender: #C4B5FD;
    --blue: #7CB8FF;
    --border: rgba(167, 139, 250, 0.20);
}
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, rgba(105, 78, 190, .17), transparent 34%),
        radial-gradient(ellipse at 95% 5%, rgba(57, 111, 177, .13), transparent 30%),
        var(--bg);
    color: #F4F5FB;
}
[data-testid="stHeader"] { background: rgba(11, 16, 32, .75); }
[data-testid="stSidebar"] { background: #0E1528; border-right: 1px solid var(--border); }
.block-container { max-width: 1380px; padding-top: 2rem; padding-bottom: 3rem; }
h1, h2, h3 { font-family: 'Manrope', sans-serif !important; letter-spacing: -.035em; color: #F7F5FF !important; }
p, label, .stMarkdown { color: #D6DAE7; }
.hero {
    padding: 1.6rem 1.8rem; margin: .3rem 0 1.4rem 0;
    border: 1px solid var(--border); border-radius: 22px;
    background: linear-gradient(115deg, rgba(43, 42, 83, .94), rgba(20, 42, 70, .92));
    box-shadow: 0 18px 50px rgba(0,0,0,.18);
}
.eyebrow { color: #C4B5FD; font-size: .73rem; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }
.hero-title { color: white; font: 800 clamp(1.8rem, 3vw, 2.5rem)/1.15 'Manrope', sans-serif; letter-spacing: -.045em; margin-top: .45rem; }
.hero-copy { color: #C5CDE0; margin-top: .65rem; max-width: 760px; }
div[data-testid="stForm"] {
    background: rgba(19, 28, 48, .82); border: 1px solid var(--border);
    border-radius: 18px; padding: 1.2rem 1.3rem 1rem 1.3rem;
}
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #1B2742, #141D31);
    border: 1px solid var(--border); border-radius: 16px; padding: .9rem 1rem;
}
[data-testid="stMetricLabel"] { color: #AEB9D1 !important; }
[data-testid="stMetricValue"] { color: #E9E3FF !important; font-family: 'Manrope', sans-serif; }
div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
    background: #111B30; border-color: rgba(167,139,250,.24); border-radius: 10px;
}
.stButton > button, div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(110deg, #8065E8, #4D86D8);
    color: white; border: 0; border-radius: 11px; font-weight: 700;
    padding: .62rem 1rem;
}
.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
    color: white; border: 0; filter: brightness(1.1);
    box-shadow: 0 7px 22px rgba(116,91,222,.25);
}
hr { border-color: rgba(167,139,250,.18); }
footer, #MainMenu { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(
        "<div style='display:flex;gap:11px;align-items:center;padding:8px 0 22px 0;'>"
        "<div style='background:linear-gradient(135deg,#7657D8,#397BC5);"
        "border-radius:13px;padding:9px;font-size:21px;'>🐞</div>"
        "<div><div style='font-size:20px;font-weight:800;color:#F8F7FF;'>BugSight</div>"
        "<div style='font-size:10px;letter-spacing:1.5px;color:#929DB8;'>SOFTWARE RISK INTELLIGENCE</div></div></div>",
        unsafe_allow_html=True
    )
    st.caption("Machine learning · Bug effort prediction")
    st.markdown("---")
    st.markdown("**WORKSPACE**")
    st.markdown("Bug prediction  ·  Risk analysis")
    st.markdown("---")
    st.caption("Academic project prototype")

st.markdown("""
<div class="hero">
  <div class="eyebrow">SOFTWARE ENGINEERING · MACHINE LEARNING</div>
  <div class="hero-title">Understand the effort behind every bug.</div>
  <div class="hero-copy">Estimate software bug resolution time, assess potential risk,
  and support better engineering decisions with a trained machine learning model.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("### Create a prediction")
st.caption("Enter the available bug-report details below to generate an estimate.")

with st.form("bug_form"):
    st.subheader("Bug Report Details")

    col1, col2 = st.columns(2)

    with col1:
        project = st.selectbox(
            "Project",
            ["Mozilla", "Novell", "OpenXchange", "W3C"]
        )
        classification = st.text_input("Classification", "Other")
        product = st.text_input("Product", "Other")
        component = st.text_input("Component", "Other")
        version = st.text_input("Version", "Other")
        priority = st.selectbox(
            "Priority", ["P1", "P2", "P3", "P4", "P5"]
        )
        severity = st.selectbox(
            "Bug Severity",
            ["blocker", "critical", "major", "normal", "minor", "trivial", "enhancement"]
        )
        platform = st.text_input("Reported Platform", "Other")
        operating_system = st.text_input("Operating System", "Other")
        reporter = st.text_input("Reporter", "unknown")
        mentor = st.text_input("Mentor", "unknown")

    with col2:
        created = st.date_input("Bug Creation Date", value=date(2024, 6, 15))
        reporter_accessible = st.selectbox("Reporter Accessible", [1, 0])
        cclist_accessible = st.selectbox("CC List Accessible", [1, 0])
        everconfirmed = st.selectbox("Ever Confirmed", [1, 0])
        restrict_comments = st.selectbox("Comments Restricted", [0, 1])
        comment_sort_order = st.text_input(
            "Comment Sort Order", "oldest_to_newest"
        )

    submitted = st.form_submit_button(
        "Predict Fix Effort",
        type="primary",
        use_container_width=True
    )

if submitted:
    payload = {
        "reporter_accessible": reporter_accessible,
        "cclist_accessible": cclist_accessible,
        "everconfirmed": everconfirmed,
        "restrict_comments": restrict_comments,
        "creation_year": created.year,
        "creation_month": created.month,
        "creation_day": created.day,
        "creation_dayofweek": created.weekday(),
        "creation_quarter": (created.month - 1) // 3 + 1,
        "classification": classification,
        "product": product,
        "component": component,
        "version": version,
        "rep_platform": platform,
        "op_sys": operating_system,
        "priority": priority,
        "bug_severity": severity,
        "reporter": reporter,
        "comment_sort_order": comment_sort_order,
        "project": project,
        "mentor": mentor
    }

    try:
        with st.spinner("Analyzing bug report..."):
            response = requests.post(
                "https://bug-fix-effort-predictor-api.onrender.com/predict",
                json=payload,
                timeout=30
            )

        if response.ok:
            result = response.json()
            st.subheader("Prediction Results")

            a, b = st.columns(2)
            a.metric(
                "Estimated Resolution Time",
                f"{result['predicted_resolution_days']} days"
            )
            b.metric("Risk Category", result["risk_category"])

            predicted_days = float(result["predicted_resolution_days"])
            st.progress(
                min(predicted_days / 120, 1.0),
                text="Estimated resolution time · relative scale capped at 120 days"
            )

            st.markdown("### Recommended Action")
            st.write(result["recommended_action"])
            st.caption(result["note"])

            with st.expander("How are risk categories interpreted?"):
                st.markdown(
                    "- **Low:** 0–7 days\n"
                    "- **Moderate:** More than 7–30 days\n"
                    "- **High:** More than 30–90 days\n"
                    "- **Very High:** More than 90 days"
                )
        else:
            st.error(f"API error ({response.status_code}): {response.text}")

    except requests.RequestException as exc:
        st.error(
            "Could not connect to the backend. Make sure the FastAPI "
            "server is running on port 8000."
        )
        st.code(str(exc))

st.divider()
st.caption("Academic project prototype • Random Forest Regression • FastAPI + Streamlit")
