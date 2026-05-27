import streamlit as st
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="Tathagata Roy Chowdhury | Academic Portfolio",
    page_icon="🎓",
    layout="wide"
)

# 2. Custom CSS for Enhanced Professional Look
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stHeader { color: #0e1117; }
    .highlight { color: #1e3a8a; font-weight: bold; }
    .sidebar-text { font-size: 14px; }
    .publication-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Profile, Contact & Academic Links
with st.sidebar:
    try:
        img = Image.open("profie2.jpeg")
        st.image(img, width=230)
    except:
        st.warning("Profile photo not found in assets/profile.jpg")
    
    st.title("Tathagata Roy Chowdhury")
    st.write("Assistant Professor & PhD Researcher | Explainable AI | Bioinformatics | AI Researcher | Tech Strategist")
    
    st.markdown("---")
    st.subheader("🌐 Academic Profiles")
    st.markdown("[📊 Google Scholar](https://scholar.google.com/citations?user=jfW7WkEAAAAJ&hl)")
    st.markdown("[🆔 ORCID](https://orcid.org/0000-0003-1052-4628)")
    st.markdown("[🎓 WebofScience](https://www.webofscience.com/wos/author/record/QDN-0301-2026)")
    st.markdown("[🧬 Semantic Scholar](https://www.semanticscholar.org/author/Tathagata-Roy-Chowdhury/2100704574)")
    st.markdown("[🔬 ResearchGate](https://www.researchgate.net/profile/Tathagata-Roy-Chowdhury)")
    st.markdown("[🎓 Academia.edu](https://technoindiauniversity.academia.edu/TathagataRoyChowdhury)")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/tathagata-roy-chowdhury-877162319/)")
    

    st.markdown("---")
    
    # 1. Personal & Family Section
    st.subheader("👨‍👩‍👦 Personal Details")
    st.write("**Gender:** Male")
    st.write("**Marital Status:** Married")
    st.write("**Father's Name:** Mr. Jayanta Roy Chowdhury")
    st.write("**Mother's Name:** Mrs. Mithu Roy Chowdhury")
    st.write("**Spouse Name:** Mrs. Rhijurekha Roy Chowdhury")
    st.write("**Son:** Trishaan Roy Chowdhury")
    
    st.markdown("---")
    st.subheader("📩 Contact Details")
    st.write("📍 Flat No. 3B, Renuka Palace, Vivekananda Pally , Taki Road, Barasat, Kolkata - 700124")
    st.write("📞 +91 8902503176")
    st.write("📧 tathagatamtech13@gmail.com / tathagata.r@tecb.edu.in ")

    
    
    # Download CV Button
    try:
        with open("CV_Tathagata.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Full CV (PDF)",
                data=pdf_file,
                file_name="CV_Tathagata_Roy_Chowdhury.pdf",
                mime="application/pdf"
            )
    except:
        st.error("CV PDF not found in assets/")

# 4. Hero Section
st.title("Academic & Research Portfolio")
st.markdown("""
### Assistant Professor | PhD Scholar at NIT Silchar | Oracle Academy Trainer
Welcome to my official academic showcase. I am a dedicated researcher and educator with over a decade of experience in 
Computer Science and Engineering, focusing on the intersection of **Artificial Intelligence** and **Healthcare Informatics**.
""")
st.info("🎯 **Primary Research Areas:**")
research_cols = st.columns(3)

with research_cols[0]:
    st.markdown("🧬 **Health Informatics**")
    st.markdown("🖼️ **Medical Image Processing**")

with research_cols[1]:
    st.markdown("🤖 **Federated Learning**")
    st.markdown("🧠 **Explainable AI (XAI)**")

with research_cols[2]:
    st.markdown("🛡️ **Data Security & Steganography**")
    st.markdown("✨ **Generative AI (GANs/Diffusion)**")

# 5. Career & Skills
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📌 Professional Profile")
    st.write("""
    As a PhD researcher at the **National Institute of Technology (NIT), Silchar**, I specialize in developing 
    next-generation diagnostic frameworks using Deep Learning. My work bridges the gap between theoretical 
    Machine Learning and practical healthcare applications, specifically in lung and breast cancer prediction.
    
    Beyond research, I have a strong track record of academic leadership, having served as an In-Charge and 
    Academic Advisor across several prestigious engineering colleges in West Bengal.
    """)

with col2:
    st.header("⚙️ Technical Expertise")
    st.write("**Core Domains:**")
    st.write("Machine Learning, Deep Learning, Medical Imaging, XAI")
    st.write("**Languages:**")
    st.write("Python, Java, C, C++, PHP")
    st.write("**Tools & Frameworks:**")
    st.write("TensorFlow, PyTorch, Oracle Database, ERP Systems")

# 6. Comprehensive Research Section
st.divider()
st.header("🔬 Research & Intellectual Property")

st.info("💡 **Intellectual Property (Patents & Inventions)**")

# Create two clean columns to showcase both patents side-by-side beautifully
patent_col1, patent_col2 = st.columns(2)

with patent_col1:
    st.markdown("""
    <div class="publication-card" style="height: 100%;">

        <span style='color: #1e3a8a; font-weight: bold; font-size: 18px;'>
            🛡️ Indian Provisional Patent Application
        </span><br><br>

        <b>Title:</b> A Privacy-Preserving and Secured Federated Learning Framework for Decentralized Genomic Data Analysis<br><br>

        <b>Application No.:</b> <span class='highlight'>202631052210</span><br>
        <b>Filed On:</b> 24 April 2026<br>
        <b>Status:</b> Provisional Specification Filed<br><br>

        <i>
        This framework, known as <b>Bio-Cipher</b>, integrates 1D-CNN architectures
        with Local Differential Privacy (Noise Injection) techniques to enable secure,
        decentralized medical data collaboration and genomic analysis.
        </i>

    </div>
    """, unsafe_allow_html=True)


with patent_col2:
    st.markdown("""
    <div class="publication-card" style="height: 100%;">

        <span style='color: #0d9488; font-weight: bold; font-size: 18px;'>
            🇬🇧 UK Registered Design Application
        </span><br><br>

        <b>Title:</b> Blockchain-Secured Health Data Retrieval Device<br><br>

        <b>Application No.:</b> 6528955<br>
        <b>Filed With:</b> United Kingdom Intellectual Property Office (UKIPO)<br>
        <b>Filed On:</b> 26 May 2026<br>
        <b>Author Position:</b> 6th Co-Inventor<br>
        <b>Status:</b> Filed / Under Examination<br><br>

        <i>
        An innovative healthcare data retrieval framework integrating blockchain-enabled
        security mechanisms for tamper-resistant, secure, and efficient access to
        critical medical information through a decentralized architecture.
        </i>

    </div>
    """, unsafe_allow_html=True)

# --- Editorial & High-Volume Metrics Status Block ---
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("📊 Editorial & High-Impact Contributions")

metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.metric(label="✅ ICESAIA 2026 Panel", value="Active Reviewer", delta="Reviewer Console")
    st.caption("Evaluating cutting-edge submissions across Deep Learning, Medical Informatics, and IoT architectures.")

with metric_col2:
    st.metric(label="📚 Bentham Science (Scopus)", value="12 Chapters", delta="Accepted / In Press")
    st.caption("Contributed a high volume of specialized research chapters across upcoming scientific volumes.")

with metric_col3:
    st.metric(label="🎤 AMESOM 2026 (Scopus)", value="3 Papers", delta="Accepted")
    st.caption("Presenting upcoming original research frameworks at this premier indexed international conference.")

st.markdown("<br>", unsafe_allow_html=True)

# Tabs update: Adding Patent as its own tab or first in Latest
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Latest & Patents (2025-2026)", "📚 Books Authored", "📄 Journal Archive", "🎤 Conferences & Seminars"])

with tab1:
    st.subheader("Current High-Impact Work")
    st.success("✅ **Patent Pending:** App No. 202631052210 (Genomic Privacy-Preserving FL)")
    
st.markdown("""
### 🔬 Primary Research & Publications

* **Advanced DeepLungCareNet:** A Next-Generation Framework for Lung Cancer Prediction.  
    *Published in Springer Nature (LNNS, Vol. 1691), 2026.*

* **DeepLungCareNet-FedWeb:** A Federated Learning Web Framework for Multiclass Lung Cancer Diagnosis.  
    *Accepted at AGC 2026, Kolkata.*

* **Intelligent PCOS Prediction Framework using CatBoost and AI-Based Clinical Report Generation**  
    *Laha, N., Mazumder, P. & Ghorui, L. (2026).*  
    DOI: https://doi.org/10.55041/ijsmt.v2i5.343

* **Bio-Cipher Analysis:** Verified reduction in distributed loss (**0.56 → 0.51**) and local diagnostic accuracy of **74.17%**.

* **Scopus Conference Track:** 3 research papers accepted for upcoming presentation and publication at **AMESOM 2026**.

### 🎓 Mentorship & External Projects

* **Unity Healthcare Hospitals:** A Role-Based Hospital Management System.
    * **Role:** Project Guide
    * **Student:** Satish Shaw (MCA, Andhra University)
    * **Tech Stack:** Python & Streamlit
    * **Focus:** Developing an authentic, role-based management framework for healthcare environments.
""")

with tab2:
    st.subheader("Books & Book Chapters")
    
    st.info("📖 **Active Curriculum Development (MAKAUT BCA New NEP Syllabus)**")
    bca_col1, bca_col2 = st.columns(2)
    with bca_col1:
        st.write("📘 **Textbook I: Core Computational Track**")
        st.caption("Currently authoring a comprehensive volume tailored specifically to the updated MAKAUT NEP curriculum requirements.")
    with bca_col2:
        st.write("orange **Textbook II: Advanced Application Systems**")
        st.caption("Structuring content to align modern technology implementations with upcoming state university benchmarks.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.success("🔬 **Advanced Research Monograph Proposals**")
    st.markdown("""
    <div class="publication-card" style="border-left: 5px solid #22c55e;">
        <span style='color: #15803d; font-weight: bold; font-size: 17px;'>
            📔 Synthetic Over-Sampling for Medical Image Classification
        </span><br>
        <small style='color: #6b7280;'>Subtitle: From GANs and Diffusion Models to Clinical Deployment</small><br><br>
        <b>Target Publisher:</b> Cambridge Scholars Publishing <i>(In distribution partnership with Taylor & Francis Group)</i><br>
        <b>Key Research Scope:</b> 
        <ul>
            <li>Bridging data scarcity in rare disease diagnostics using Conditional GANs (cGANs) and Latent Diffusion Models (LDMs).</li>
            <li>Introducing structured, benchmarked <b>Strategic Synthetic Oversampling (SSO)</b> frameworks.</li>
            <li>Validation using Explainable AI (XAI) metrics (Grad-CAM, SHAP) to eliminate hallucinations in Breast Ultrasound and Histopathology datasets.</li>
        </ul>
        <b>Status:</b> Official Book Proposal & Chapter Outline Invited
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.write("**Significant Book Chapters:**")
    st.write("- *12 Peer-Reviewed Chapters Accepted & In Press*, **Bentham Science (Scopus Indexed)** (2026).")
    st.write("- *AI-driven Environmental Sustainability*, Wiley + IEEE Press (2026).")
    st.write("- *AI-powered OCR and Healthcare Informatics in Industry 5.0*, Bentham Science (2026).")

with tab3:
    st.subheader("Selected Journal Publications")
    st.write("1. **FaceCognizance:** ML-based person recognition for government surveillance (IJCRT, 2024).")
    st.write("2. **Unveiling the Depths:** A Pioneering Review of Deep Learning Models (IJNRD, 2024).")
    st.write("3. **Precision Colon Cancer Screening:** Leveraging Data Analytics (ICMCRJ, 2023).")
    st.write("4. **Satellite Mobile Telephone Networks:** A Brief Survey (Acta Scientific, 2023).")
    st.write("5. **Analysis of 5 Stage Pipelined Operations of ARM** (IJARIIT, 2019).")

with tab4:
    st.subheader("Professional Engagement")
    st.write("✅ **Resource Person:** Parallel Architecture Workshop.")
    st.write("✅ **Session Chair:** Multiple International Conferences.")
    st.write("✅ **Workshop Participant:** Emerging Technologies (MAKAUT, 2026).")
    st.write("✅ **Reviewer Panel:** ICESAIA 2026 International Conference (Actively reviewing technical tracks across AI, IoT, and Cloud systems).")
    st.write("✅ **Reviewer:** Analytics Global Conference (2026).")
# 7. Professional Journey
st.divider()
st.header("💼 Employment History")

exp_data = [
    {"role": "Assistant Professor", "inst": "Techno Engineering College, Banipur", "period": "Mar 2024 - Present", "details": "Leading core CS courses and mentoring PhD-track research projects."},
    {"role": "Assistant Professor & In-Charge", "inst": "St. Mary's Technical Campus, Kolkata", "period": "Sept 2022 - Mar 2024", "details": "Headed departmental operations and coordinated faculty development programs."},
    {"role": "Assistant Professor", "inst": "Brainware University", "period": "July 2022 - Sept 2022", "details": "Specialized in Machine Learning and Programming pedagogy."},
    {"role": "Assistant Professor", "inst": "Elitte College of Engineering", "period": "Sept 2019 - June 2022", "details": "Web Expert and ERP Manager (ORKA System); Academic material development."},
    {"role": "Assistant Professor & Advisor", "inst": "Chaibasa Engineering College", "period": "Feb 2015 - Sept 2019", "details": "Academic advising and coordination of technical seminars."}
]

for exp in exp_data:
    st.write(f"### {exp['role']}")
    st.write(f"**{exp['inst']}** | *{exp['period']}*")
    st.write(exp['details'])
    st.write("")

# 8. Education & Personal
st.divider()
col_ed, col_aw = st.columns(2)

with col_ed:
    st.header("🎓 Academic Qualifications")
    st.write("🎓 **PhD (Pursuing)** | Health Informatics | NIT Silchar")
    st.write("🎓 **M.Tech in CSE** | University of Calcutta (2014)")
    st.write("🎓 **B.Tech in CSE** | Saroj Mohan Institute of Technology (2011)")

with col_aw:
    st.header("🏆 Awards & Recognition")
    st.write("⭐ **Best Online Teacher Award** (2021)")
    st.write("⭐ **Oracle Academy Authorized Trainer**")
    st.write("⭐ **Award-winning Tabla Player** (Bengal Music College)")
    st.write("⭐ **5-Star Educator Status** on TeacherOn/UrbanPro")

# Footer
st.markdown("---")
st.caption("© 2026 Tathagata Roy Chowdhury. Asst Professor. Dept of CSE. TIEM")
