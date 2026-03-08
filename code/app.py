import streamlit as st

# Page config
st.set_page_config(
    page_title="DevOps Portal",
    page_icon="🚀",
    layout="wide"
)

# ---------- Custom UI ----------
st.markdown("""
<style>

.main-title{
font-size:50px;
font-weight:bold;
color:#00f5d4;
text-align:center;
}

.sub{
font-size:20px;
text-align:center;
color:gray;
}

.box{
background-color:#0f172a;
padding:25px;
border-radius:15px;
margin-top:20px;
}

.unlock{
font-size:35px;
color:#00ffcc;
font-weight:bold;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<p class="main-title">🚀 DevOps Engineering Hub</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Register to unlock DevOps Projects</p>', unsafe_allow_html=True)

st.divider()

# ---------- Sidebar ----------
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Page",
    ["Register", "Projects", "Learning"]
)

# ---------- Registration ----------
if menu == "Register":

    st.header("👨‍💻 DevOps Engineer Registration")

    with st.form("devops_form"):

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            role = st.selectbox(
                "Select Role",
                ["DevOps Engineer","Cloud Engineer","SRE","Platform Engineer"]
            )

        with col2:
            experience = st.selectbox(
                "Experience",
                ["Beginner","Intermediate","Advanced"]
            )

            tools = st.multiselect(
                "DevOps Tools",
                ["Docker","Kubernetes","Terraform","Jenkins","GitHub Actions"]
            )

            github = st.text_input("GitHub Profile")

        submit = st.form_submit_button("Register")

    if submit:

        st.balloons()

        st.success(f"Welcome {name} 🎉")

        st.markdown(
            '<p class="unlock">🚀 Congratulations! You have unlocked DevOps Projects!</p>',
            unsafe_allow_html=True
        )

        st.info("Explore real DevOps projects below 👇")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Project", "CI/CD Pipeline")

        with col2:
            st.metric("Project", "Docker + Kubernetes Deployment")

        with col3:
            st.metric("Project", "Terraform AWS Infrastructure")

# ---------- Projects ----------
elif menu == "Projects":

    st.title("🔥 DevOps Projects")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🚀 CI/CD Pipeline")
        st.write("Build automated pipelines using Jenkins and Docker")

    with col2:
        st.subheader("☁️ Cloud Deployment")
        st.write("Deploy microservices on Kubernetes cluster")

    with col3:
        st.subheader("📊 Monitoring Stack")
        st.write("Prometheus + Grafana monitoring system")

# ---------- Learning ----------
elif menu == "Learning":

    st.title("📚 DevOps Learning Videos")

    st.video("https://youtu.be/gLptmcuCx6Q")
    st.video("https://youtu.be/sVlo7W3iDDQ")
    st.video("https://youtu.be/-4e3ewcTupM")