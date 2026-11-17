import streamlit as st
from pathlib import Path
from PIL import Image

# ============================================================
# Tathagata Roy Chowdhury | Academic & Research Portfolio
# Run: streamlit run app.py
# Optional assets:
#   profie2.jpeg (or profile.png / profile.jpg)
#   Tathagata_Roy_Chowdhury_CV.pdf
# ============================================================

st.set_page_config(
    page_title="Tathagata Roy Chowdhury | Academic Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------- Styling -------------------------
st.markdown(
    """
    <style>
    /* ---------- Light AI-inspired visual system ---------- */
    :root {
        --ink: #172554;
        --muted: #64748b;
        --blue: #2563eb;
        --cyan: #06b6d4;
        --violet: #8b5cf6;
        --pink: #ec4899;
        --surface: rgba(255,255,255,.88);
        --line: rgba(148,163,184,.22);
    }

    .stApp {
        background:
            radial-gradient(ellipse at 8% 4%, rgba(6,182,212,.13), transparent 27%),
            radial-gradient(ellipse at 92% 9%, rgba(139,92,246,.13), transparent 28%),
            radial-gradient(ellipse at 80% 75%, rgba(236,72,153,.08), transparent 30%),
            linear-gradient(135deg, #f7fbff 0%, #f4f5ff 48%, #fff8fc 100%);
        color: var(--ink);
    }

    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #eef8ff 0%, #f4f0ff 55%, #fff5fa 100%);
        border-right: 1px solid rgba(148,163,184,.2);
    }
    [data-testid="stSidebar"] > div { background: transparent; }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1440px;
    }

    h1, h2, h3, h4 { color: #172554; letter-spacing: -.025em; }
    p, li, label, .stMarkdown { color: #334155; }
    .small-muted { color: #64748b; font-size: .9rem; }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 2.4rem 2.2rem;
        border-radius: 25px;
        color: #172554;
        background:
            radial-gradient(circle at 88% 18%, rgba(255,255,255,.9) 0 4%, transparent 4.5%),
            radial-gradient(circle at 93% 80%, rgba(6,182,212,.22), transparent 23%),
            radial-gradient(circle at 72% 10%, rgba(236,72,153,.17), transparent 25%),
            linear-gradient(115deg, rgba(255,255,255,.96), rgba(239,246,255,.94) 48%, rgba(250,245,255,.96));
        border: 1px solid rgba(129,140,248,.25);
        box-shadow: 0 18px 55px rgba(59,91,160,.12);
        margin-bottom: 1.5rem;
    }
    .hero:after {
        content: "";
        position: absolute;
        width: 240px; height: 240px;
        right: -65px; top: -95px;
        border-radius: 50%;
        border: 1px solid rgba(99,102,241,.18);
        box-shadow: 0 0 0 22px rgba(99,102,241,.035),
                    0 0 0 48px rgba(6,182,212,.035);
        pointer-events: none;
    }
    .hero h1 {
        color: #172554 !important;
        font-size: clamp(2rem, 4vw, 3.35rem);
        font-weight: 850;
        line-height: 1.08;
        margin: .35rem 0 .65rem;
    }
    .hero h3 { color: #31518b !important; font-weight: 650; }
    .hero p { color: #475569 !important; max-width: 850px; }
    .eyebrow {
        display: inline-block;
        color: #5b4bd8;
        background: rgba(139,92,246,.10);
        border: 1px solid rgba(139,92,246,.16);
        padding: .35rem .75rem;
        border-radius: 999px;
        font-size: .75rem;
        text-transform: uppercase;
        letter-spacing: .14em;
        font-weight: 800;
    }

    .publication-card {
        background: rgba(255,255,255,.88);
        border: 1px solid rgba(148,163,184,.2);
        border-left: 4px solid #6366f1;
        border-radius: 14px;
        padding: 1.1rem 1.25rem;
        margin: .75rem 0;
        box-shadow: 0 7px 22px rgba(51,65,120,.055);
        transition: transform .2s ease, box-shadow .2s ease;
    }
    .publication-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(51,65,120,.10);
    }

    div[data-testid="stMetric"] {
        background: rgba(255,255,255,.88);
        border: 1px solid rgba(129,140,248,.18);
        padding: 15px 16px;
        border-radius: 16px;
        box-shadow: 0 8px 22px rgba(51,65,120,.055);
    }
    div[data-testid="stMetric"] label { color: #64748b !important; }
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #273c83;
        font-weight: 800;
    }

    [data-testid="stTabs"] button {
        border-radius: 10px 10px 0 0;
        font-weight: 650;
    }
    [data-testid="stExpander"] {
        background: rgba(255,255,255,.76);
        border: 1px solid rgba(148,163,184,.2);
        border-radius: 13px;
    }
    div.stButton > button, div.stDownloadButton > button {
        border: 0;
        border-radius: 11px;
        color: white;
        font-weight: 700;
        background: linear-gradient(100deg, #2563eb, #7c3aed);
        box-shadow: 0 7px 18px rgba(79,70,229,.18);
    }
    div.stButton > button:hover, div.stDownloadButton > button:hover {
        color: white;
        border: 0;
        background: linear-gradient(100deg, #1d4ed8, #6d28d9);
        box-shadow: 0 10px 24px rgba(79,70,229,.25);
    }
    [data-testid="stAlert"] { border-radius: 13px; }
    hr { border-color: rgba(148,163,184,.22); }
    a { color: #4f46e5 !important; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------ Reusable data -----------------------
PROFILE = {
    "name": "Tathagata Roy Chowdhury",
    "role": "Assistant Professor, Department of Computer Science & Engineering",
    "institution": "Techno Institute of Engineering and Management, Banipur, Kolkata, India",
    "email": "tathagata.r@tecb.edu.in",
    "alternate_email": "tathagatamtech13@gmail.com",
    "phone": "+91 8902503176",
}

ACADEMIC_LINKS = [
    ("Google Scholar", "https://scholar.google.com/citations?user=jfW7WkEAAAAJ&hl"),
    ("ORCID", "https://orcid.org/0000-0003-1052-4628"),
    ("Web of Science", "https://www.webofscience.com/wos/author/record/QDN-0301-2026"),
    ("Semantic Scholar", "https://www.semanticscholar.org/author/Tathagata-Roy-Chowdhury/2100704574"),
    ("ResearchGate", "https://www.researchgate.net/profile/Tathagata-Roy-Chowdhury"),
    ("Academia.edu", "https://technoindiauniversity.academia.edu/TathagataRoyChowdhury"),
    ("LinkedIn", "https://www.linkedin.com/in/tathagata-roy-chowdhury-877162319/"),
]

JOURNAL_PUBLICATIONS = [
    {
        "year": "2026",
        "title": "An Intelligent Computer Vision Framework for Eye-State Detection and Adaptive Screen Control",
        "citation": "JPHACI, vol. 1, no. 2, pp. 29–48, October 2026.",
        "link": "https://ijpress.com/jphaci/article/view/90",
    },
    {
        "year": "2026",
        "title": "SmartCoughNet: A Deep Learning-Based Mobile Framework for Respiratory Disease Detection Using Cough Audio Analysis",
        "citation": "JPHACI, vol. 1, no. 1, pp. 1–13, September 2026.",
        "link": "https://ijpress.com/jphaci/article/view/6",
    },
    {
        "year": "2026",
        "title": "DeepLungCareNet-FedWeb: A Federated Learning Web Framework for Multiclass Lung Cancer Diagnosis",
        "citation": "S. Chakrabarti, S. Das, T. Roy Chowdhury, A. Nag, and M. A. A. Sheikh, Vishleshikaa – The Analytics Journal, vol. 2, August 2026. DOI: 10.5281/zenodo.22126550.",
        "link": "https://doi.org/10.5281/zenodo.22126550",
    },
    {
        "year": "2026",
        "title": "Evaluating an AI-Assisted Mental Stress Screening Tool for Occupational Health and Nursing Staff",
        "citation": "S. Das and T. R. Chowdhury, Asian Journal of Research in Nursing and Health, vol. 9, no. 1, pp. 1754–1761, August 2026. DOI: 10.9734/ajrnh/2026/v9i1393.",
        "link": "https://doi.org/10.9734/ajrnh/2026/v9i1393",
    },
    {
        "year": "2024",
        "title": "FaceCognizance: Machine Learning-Based Person Recognition System",
        "citation": "IJCRT, 2024.",
        "link": None,
    },
    {
        "year": "2024",
        "title": "Unveiling the Depths: A Pioneering Review of Deep Learning Models",
        "citation": "IJNRD, 2024.",
        "link": None,
    },
    {
        "year": "2023",
        "title": "Precision Colon Cancer Screening: Leveraging Data Analytics",
        "citation": "ICMCRJ, 2023.",
        "link": None,
    },
    {
        "year": "2023",
        "title": "Satellite Mobile Telephone Networks: A Brief Survey",
        "citation": "Acta Scientific, 2023.",
        "link": None,
    },
    {
        "year": "2019",
        "title": "Analysis of 5 Stage Pipelined Operations of ARM",
        "citation": "IJARIIT, 2019.",
        "link": None,
    },
]

BOOK_CHAPTERS = [
    {
        "year": "2026",
        "title": "Feature-rich deep learning architecture for breast cancer detection: From image analysis to real-time app deployment",
        "citation": (
            "Chowdhury, T. R., Roy, P., Singha, B., Mondal, S., & Saha, S. (2026). "
            "In H. Biswas, J. S. Banerjee, S. Bhattacharyya, D. De, P. Sarigiannidis, "
            "J. Platoš, & M. M. Asad (Eds.), Emerging Trends in Smart Computing, "
            "Communication and Automation (1st ed.). CRC Press."
        ),
        "link": "https://doi.org/10.1201/9781042026333",
    },
    {
        "year": "2025",
        "title": "Harnessing the potential of artificial intelligence to promote environmental sustainability",
        "citation": "Roy Chowdhury, T., & Nag, A. (2025). In Harnessing the Potential of Artificial Intelligence to Promote Environmental Sustainability, pp. 185–197. Emerald Publishing. DOI: 10.1108/978-1-83662-996-220251011.",
        "link": "https://doi.org/10.1108/978-1-83662-996-220251011",
    },
]

# ---------------------------- Sidebar -------------------------
with st.sidebar:
    image_candidates = ["profie2.jpeg", "profile.png", "profile.jpg", "assets/profile.png"]
    profile_image = next((Path(p) for p in image_candidates if Path(p).exists()), None)
    if profile_image:
        try:
            st.image(Image.open(profile_image), width=220)
        except Exception:
            st.caption("Profile image could not be loaded.")
    else:
        st.markdown("## 🎓")

    st.title(PROFILE["name"])
    st.caption(PROFILE["role"])
    st.write(PROFILE["institution"])
    st.divider()

    st.subheader("🌐 Academic Profiles")
    for label, url in ACADEMIC_LINKS:
        st.markdown(f"- [{label}]({url})")

    st.divider()
    st.subheader("📩 Professional Contact")
    st.write(f"📧 {PROFILE['email']}")
    st.write(f"📧 {PROFILE['alternate_email']}")
    st.write(f"📞 {PROFILE['phone']}")
    st.caption("For academic, research, collaboration and invited-talk enquiries.")

    cv_candidates = [
        "Tathagata_Roy_Chowdhury_CV.pdf",
        "TathagataRoyChowdhury-UpdatedCV.pdf",
        "CV_Tathagata_Roy_Chowdhury.pdf",
    ]
    cv_path = next((Path(p) for p in cv_candidates if Path(p).exists()), None)
    if cv_path:
        with cv_path.open("rb") as cv_file:
            st.download_button(
                "📄 Download Academic CV",
                data=cv_file,
                file_name="Tathagata_Roy_Chowdhury_CV.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    else:
        st.info("Place the latest CV PDF in the project folder to enable the download button.")

# ----------------------------- Hero ---------------------------
st.markdown(
    f"""
    <div class="hero">
      <div class="eyebrow">Academic • Research • Innovation</div>
      <h1>{PROFILE['name']}</h1>
      <h3>{PROFILE['role']}</h3>
      <p>{PROFILE['institution']}</p>
      <p>Research and teaching at the intersection of Artificial Intelligence,
      Healthcare Informatics, trustworthy machine learning and practical
      software systems.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Research Interests")
research_cols = st.columns(3)
research_areas = [
    ("🧬", "Healthcare Informatics", "Clinical prediction, health data analytics and decision support."),
    ("🖼️", "Medical Image Analysis", "Deep learning for breast, lung and other medical imaging tasks."),
    ("🤖", "Federated Learning", "Privacy-aware collaborative learning and feature alignment."),
    ("🧠", "Explainable AI", "Interpretable models, model evaluation and trustworthy AI."),
    ("✨", "Generative AI", "GANs, diffusion models and synthetic data generation."),
    ("🔐", "Data Security", "Privacy-preserving computation, blockchain and secure health data."),
]
for i, (icon, title, desc) in enumerate(research_areas):
    with research_cols[i % 3]:
        st.markdown(f"**{icon} {title}**")
        st.caption(desc)
        st.markdown("---")

# ---------------------- Overview and expertise ----------------
st.divider()
profile_col, expertise_col = st.columns([1.55, 1])
with profile_col:
    st.header("Professional Profile")
    st.write(
        """
        I am an academician and researcher in Computer Science and Engineering,
        with teaching, mentoring and academic coordination experience. My
        research interests focus on applying machine learning and deep learning
        to healthcare problems, particularly medical image analysis, clinical
        prediction, respiratory disease screening, breast and lung cancer
        analysis, federated learning and explainable AI.

        My work aims to connect methodological research with usable systems,
        including web-based and mobile applications, privacy-aware workflows
        and interpretable decision-support tools.
        """
    )
with expertise_col:
    st.header("Technical Expertise")
    st.markdown(
        """
        **Programming:** Python, Java, C, C++, R, SQL

        **AI / ML:** Machine Learning, Deep Learning, NLP, Computer Vision,
        Explainable AI, Federated Learning

        **Frameworks:** TensorFlow, Keras, PyTorch, Scikit-learn, OpenCV

        **Development:** Django, FastAPI, Streamlit, PHP, HTML, CSS, JavaScript

        **Tools:** Weka, MATLAB, MySQL, Oracle Database, VS Code
        """
    )

# ---------------------- Research snapshot ---------------------
st.divider()
st.header("Research Impact & Academic Contributions")
m1, m2, m3, m4 = st.columns(4)
m1.metric("2026", "Research activity", "Healthcare AI")
m2.metric("12", "Chapters", "Accepted / in press*")
m3.metric("3", "Conference papers", "AMESEOM 2026*")
m4.metric("1", "Student award", "Best Technical Presentation*")
st.caption(
    "*Academic contribution figures and event outcomes are reproduced from the "
    "previous portfolio content; update them if the final publisher or conference records change."
)

# ------------------------------- Tabs ------------------------
tab_research, tab_books, tab_publications, tab_service = st.tabs(
    ["🚀 Research & Patents", "📚 Books & Chapters", "📄 Publications", "🎤 Academic Service"]
)

with tab_research:
    st.subheader("Patents & Intellectual Property")
    st.success(
        "Indian Patent Approved | Application No. 202631052210 | "
        "Bio-Cipher: Privacy-Preserving Federated Learning for Genomic Data Analysis"
    )
    st.info(
        "UK Registered Design | Design No. 6528955 | "
        "Blockchain-Secured Health Data Retrieval Device | Grant date: 04 June 2026"
    )
    st.info(
        "UK Registered Design | Design No. 6544078 | "
        "AI-Powered Medical Device for Early Detection of Oral Cancer | "
        "Grant date: 17 August 2026"
    )

    st.subheader("Featured Research")
    featured = [
        (
            "AURORA",
            "A Self-Supervised Federated Learning Framework with MMD-Based Feature "
            "Alignment for Interpretable Breast Cancer Survival Analysis.",
            "Research manuscript submitted to an international conference; invited resubmission noted for ICIDA 2026.",
        ),
        (
            "DeepLungCareNet / DeepLungCareNet-FedWeb",
            "Deep learning and federated web framework for multiclass lung cancer diagnosis.",
            "Research contribution in lung cancer classification and privacy-aware collaborative learning.",
        ),
        (
            "SmartCoughNet",
            "Mobile deep learning framework for respiratory disease detection using cough audio analysis.",
            "Published in JPHACI, 2026.",
        ),
        (
            "Bio-Cipher",
            "Privacy-preserving federated learning architecture for genomic data analysis.",
            "Indian patent approved; application number 202631052210.",
        ),
        (
            "Intelligent PCOS Prediction Framework",
            "CatBoost-based clinical prediction and automated report generation.",
            "DOI: 10.55041/ijsmt.v2i5.343.",
        ),
        (
            "Strategic Synthetic Oversampling",
            "Synthetic data generation strategies for medical image classification using GANs and diffusion models.",
            "Research monograph proposal and chapter outline activity.",
        ),
    ]
    for title, description, status in featured:
        st.markdown(
            f'<div class="publication-card"><b>{title}</b><br>{description}'
            f'<p class="small-muted">{status}</p></div>',
            unsafe_allow_html=True,
        )

    st.subheader("Research Mentorship")
    st.markdown(
        """
        - Supervision and mentoring of undergraduate projects in AI and healthcare.
        - Student research themes include biomedical waste classification,
          Parkinson’s disease screening using deep learning, and NLP-based
          clinical decision-support systems.
        - Student team recognition: Best Technical Presentation Award at AMESEOM 2026
          (as listed in the previous portfolio).
        """
    )

with tab_books:
    st.subheader("Selected Book Chapters")
    for item in BOOK_CHAPTERS:
        st.markdown(f"**{item['year']} — {item['title']}**")
        st.write(item["citation"])
        if item["link"]:
            st.markdown(f"[View DOI / publication]({item['link']})")
        st.divider()

    st.subheader("Books & Editorial Projects")
    st.markdown(
        """
        - **Next-Generation Healthcare Informatics: Secure, Explainable, and
          Federated Intelligence** — edited-volume coordination and author
          chapter collection activity; final submission date previously set
          for 15 November 2026.
        - **A Pathway to J.E.C.A** — published 21 June 2023.
        - **Unlocking Language: A Beginner’s Guide to NLP** — published book.
        - **Synthetic Over-Sampling for Medical Image Classification: From GANs
          and Diffusion Models to Clinical Deployment** — research monograph
          proposal / development.
        - **MAKAUT BCA curriculum resources** — curriculum-oriented textbook
          development in core computational and application-system areas.
        """
    )
    st.caption(
        "Publisher, ISBN and publication-status details should be added when "
        "the final bibliographic records are available."
    )

with tab_publications:
    st.subheader("Journal Publications")
    selected_year = st.selectbox(
        "Filter by year",
        ["All"] + sorted({p["year"] for p in JOURNAL_PUBLICATIONS}, reverse=True),
    )
    for pub in JOURNAL_PUBLICATIONS:
        if selected_year == "All" or pub["year"] == selected_year:
            st.markdown(
                f'<div class="publication-card"><b>{pub["title"]}</b><br>'
                f'<span class="small-muted">{pub["citation"]}</span></div>',
                unsafe_allow_html=True,
            )
            if pub["link"]:
                st.markdown(f"[Publication / DOI link]({pub['link']})")
    st.caption(
        "The list combines the 2026 publications supplied for this update with "
        "the selected earlier publications listed in the previous portfolio. "
        "Add complete bibliographic metadata for older entries when available."
    )

with tab_service:
    st.subheader("Academic & Professional Engagement")
    st.markdown(
        """
        - **Conference Reviewer:** ICESAIA 2026 (IEEE conference), reviewing
          submissions in AI, IoT, Healthcare Informatics and emerging technologies.
        - **Conference Reviewer:** Analytics Global Conference 2026.
        - **Resource Person:** Parallel Architecture Workshop.
        - **Session Chair:** International conference sessions (as listed in the
          previous portfolio).
        - **Workshop Participant:** Emerging Technologies, MAKAUT, 2026.
        - **Oracle Academy:** Authorized Trainer (as listed in the previous portfolio).
        """
    )
    st.subheader("Awards & Recognition")
    st.markdown(
        """
        - Best Online Teacher Award (2021).
        - Best Technical Presentation recognition for a supervised student team
          at AMESEOM 2026 (as listed in the previous portfolio).
        - Tabla performance recognition / award, Bengal Music College
          (as listed in the previous portfolio).
        - 5-Star Educator status on TeacherOn / UrbanPro (as listed in the
          previous portfolio).
        """
    )

# ----------------------- Professional journey -----------------
st.divider()
st.header("Professional Experience")
experience = [
    {
        "role": "Assistant Professor",
        "institution": "Techno Institute of Engineering and Management, Banipur, Kolkata",
        "period": "March 2024 – Present",
        "details": "Department of Computer Science and Engineering; teaching, mentoring and research activities.",
    },
    {
        "role": "Assistant Professor & In-Charge",
        "institution": "St. Mary's Technical Campus, Kolkata",
        "period": "September 2022 – March 2024",
        "details": "Departmental coordination, academic operations and faculty-development activities.",
    },
    {
        "role": "Assistant Professor",
        "institution": "Brainware University",
        "period": "July 2022 – September 2022",
        "details": "Teaching and academic activities in computing and programming.",
    },
    {
        "role": "Assistant Professor",
        "institution": "Elitte College of Engineering",
        "period": "September 2019 – June 2022",
        "details": "Teaching, academic material development, web expertise and ORKA ERP coordination.",
    },
    {
        "role": "Assistant Professor & Advisor",
        "institution": "Chaibasa Engineering College",
        "period": "February 2015 – September 2019",
        "details": "Academic advising and coordination of technical seminars.",
    },
]
for exp in experience:
    with st.expander(f"{exp['role']} | {exp['institution']} | {exp['period']}", expanded=False):
        st.write(exp["details"])

# ----------------------------- Education -----------------------
st.divider()
edu_col, skill_col = st.columns(2)
with edu_col:
    st.header("Academic Qualifications")
    st.markdown(
        """
        - **Ph.D. (Pursuing):** Health Informatics, National Institute of Technology
          Silchar.
        - **M.Tech:** Computer Science and Engineering, University of Calcutta, 2014.
        - **B.Tech:** Computer Science and Engineering, Saroj Mohan Institute of
          Technology, 2011.
        """
    )
with skill_col:
    st.header("Teaching & Mentoring Areas")
    st.markdown(
        """
        - Programming in C, C++, Java and Python
        - Data Structures and Design & Analysis of Algorithms
        - Database Management Systems and SQL
        - Operating Systems and Computer Networks
        - Artificial Intelligence and Machine Learning
        - Data Mining, NLP and Computer Vision
        - Healthcare Informatics and Explainable AI
        """
    )

# ------------------------------ Footer -------------------------
st.divider()
st.markdown(
    f"""
    <div style="text-align:center; padding: .8rem 0 1.5rem 0;">
      <b>{PROFILE['name']}</b><br>
      <span class="small-muted">{PROFILE['role']} | Techno Institute of Engineering and Management</span><br>
      <span class="small-muted">© 2026 Academic & Research Portfolio</span>
    </div>
    """,
    unsafe_allow_html=True,
)
