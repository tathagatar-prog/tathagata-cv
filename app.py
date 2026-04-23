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
        img = Image.open("assets/profile.jpg")
        st.image(img, width=230)
    except:
        st.warning("Profile photo not found in assets/profile.jpg")
    
    st.title("Tathagata Roy Chowdhury")
    st.write("Assistant Professor & PhD Researcher")
    
    st.markdown("---")
    st.subheader("🌐 Academic Profiles")
    st.markdown("[📊 Google Scholar](https://scholar.google.com/citations?user=jfW7WkEAAAAJ&hl)")
    st.markdown("[🆔 ORCID](https://orcid.org/0000-0003-1052-4628)")
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
st.header("🔬 Research & Publications")

tab1, tab2, tab3, tab4 = st.tabs(["🚀 Latest (2025-2026)", "📚 Books Authored", "📄 Journal Archive", "🎤 Conferences & Seminars"])

with tab1:
    st.subheader("Current High-Impact Research")
    st.markdown("""
    * **Advanced DeepLungCareNet:** A Next-Generation Framework for Lung Cancer Prediction. 
        *Published in Springer Nature (LNNS, vol 1691), 2026.*
    * **DeepLungCareNet-FedWeb:** A federated learning web framework for multiclass lung cancer diagnosis. 
        *Accepted at AGC 2026, Kolkata.*
    * **AFWE-CGFS:** A novel adaptive ensemble architecture combining gradient boosting and neural gating for credit approval. 
        *Accepted at AGC 2026.*
    * **Strategic Synthetic Oversampling (SSO):** Benchmark of cGAN versus diffusion models for breast ultrasound classification. 
        *Accepted at HUMAN 2026, Silchar.*
    * **Feature-rich Deep Learning for Breast Cancer Detection:** From image analysis to real-time app deployment. 
        *Accepted at ICSCCA 2025.*
    """)

with tab2:
    st.subheader("Books & Book Chapters")
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        st.write("📖 **A Complete Overview on Web Technology** (2026)")
        st.caption("Taurean Publications | ISBN: 978-93-4731-003-4")
        st.write("📖 **Unveiling the Black Box: Practical Deep Learning and XAI** (2024)")
        st.caption("Lambert Academic Publishing")
    with col_b2:
        st.write("📖 **Anomaly Detection in Log Files** (2024)")
        st.caption("Lambert Academic Publishing | ISBN: 978-620-7-80706-2")
        st.write("📖 **A Pathway to J.E.C.A.** (2023)")
        st.caption("Amazon Kindle Edition | ASIN: B0C8RTG1KJ")
    
    st.markdown("---")
    st.write("**Significant Book Chapters:**")
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
    st.write("✅ **Reviewer:** Analytics Global Conference (2026) and IEEE ICESAIA (2026).")

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
