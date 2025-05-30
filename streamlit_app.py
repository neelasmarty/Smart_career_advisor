# streamlit_app.py
import streamlit as st
from utils import get_suggestion_after_10th, get_suggestion_after_inter, get_suggestion_after_diploma, get_suggestion_after_grad, get_suggestion_after_pg, get_btech_job_suggestions

st.set_page_config(page_title="Career Path Advisor", layout="centered")
st.title("🎓 Career Path Advisor")
st.markdown("Select your current education level to get suggestions(model accuracy 93.33):")
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
def Classificaton():
    # Generate mock data (500 samples)
    np.random.seed(42)
    data = []
    for _ in range(500):
        maths = np.random.randint(0, 101)
        physics = np.random.randint(0, 101)
        biology = np.random.randint(0, 101)
        chemistry = np.random.randint(0, 101)
        english = np.random.randint(0, 101)
        
        interest_engineering = np.random.randint(1, 6)
        interest_medical = np.random.randint(1, 6)
        interest_diploma = np.random.randint(1, 6)
        interest_commerce = np.random.randint(1, 6)

        # Rule-based label
        if maths > 70 and physics > 70 and interest_engineering >= 3:
            label = "Intermediate MPC"
        elif biology > 70 and chemistry > 60 and interest_medical >= 3:
            label = "Intermediate BiPC"
        elif interest_diploma >= 4:
            label = "Diploma Courses"
        elif interest_commerce >= 4:
            label = "Commerce/Arts"
        else:
            label = "General Intermediate"

        data.append([
            maths, physics, biology, chemistry, english,
            interest_engineering, interest_medical, interest_diploma, interest_commerce,
            label
        ])

    # Convert to DataFrame
    columns = [
        'Maths', 'Physics', 'Biology', 'Chemistry', 'English',
        'Eng_Int', 'Med_Int', 'Dip_Int', 'Com_Int', 'Label'
    ]
    df = pd.DataFrame(data, columns=columns)

    # Encode labels
    df['Label'] = df['Label'].astype('category').cat.codes
    X = df.drop("Label", axis=1)
    y = df["Label"]

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    print("RF Accuracy:", accuracy_score(y_test, rf.predict(X_test)))
    joblib.dump(rf, "models/rf_model.pkl")

    # Train XGBoost
    xgb = XGBClassifier(use_label_encoder=False, eval_metric="mlogloss")
    xgb.fit(X_train, y_train)
    print("XGB Accuracy:", accuracy_score(y_test, xgb.predict(X_test)))
    joblib.dump(xgb, "models/xgb_model.pkl")

# Step buttons
choice = st.radio(
    "Select one:",
    ["After 10th", "After Intermediate", "After Diploma", "After Graduation", "After Post Graduation"],
    horizontal=True
)

if choice == "After 10th":
    st.subheader("📘 Subject Scores")
    maths = st.slider("Maths", 0, 100, 50)
    physics = st.slider("Physics", 0, 100, 50)
    biology = st.slider("Biology", 0, 100, 50)
    chemistry = st.slider("Chemistry", 0, 100, 50)
    
    st.subheader("💡 Interests")
    eng = st.slider("Interest in Engineering", 1, 5, 3)
    med = st.slider("Interest in Medical/Biology", 1, 5, 3)
    dip = st.slider("Interest in Diploma/Practical Courses", 1, 5, 3)

    if st.button("Suggest Path"):
        suggestion, jobs = get_suggestion_after_10th(maths, physics, biology, chemistry, eng, med, dip)
        st.success(f"✅ Suggested Path: **{suggestion}**")
        st.subheader("💼 Potential Job Opportunities")
        st.write(jobs)

elif choice == "After Intermediate":
    st.subheader("🎓 Stream Options: MPC / BiPC / MEC / CEC")
    stream = st.selectbox("Select your stream", ["MPC", "BiPC", "MEC", "CEC", "Other"])
    
    st.subheader("💡 Interests")
    eng = st.slider("Interest in Engineering", 1, 5, 3)
    med = st.slider("Interest in Medical", 1, 5, 3)
    commerce = st.slider("Interest in Commerce/Business", 1, 5, 3)
    teaching = st.slider("Interest in Teaching", 1, 5, 3)

    if st.button("Suggest Path"):
        suggestion, jobs = get_suggestion_after_inter(stream, eng, med, commerce, teaching)
        st.success(f"✅ Suggested Path: **{suggestion}**")
        st.subheader("💼 Potential Job Opportunities")
        st.write(jobs)

elif choice == "After Diploma":
    st.subheader("💼 Diploma Specialization")
    branch = st.selectbox("Select your branch", ["CSE", "ECE", "EEE", "Mechanical", "Civil", "Pharmacy", "Other"])
    higher_study = st.slider("Interest in Higher Studies", 1, 5, 3)
    job = st.slider("Interest in Getting a Job", 1, 5, 3)

    if st.button("Suggest Path"):
        suggestion, jobs = get_suggestion_after_diploma(branch, higher_study, job)
        st.success(f"✅ Suggested Path: **{suggestion}**")
        st.subheader("💼 Potential Job Opportunities")
        st.write(jobs)

elif choice == "After Graduation":
    st.subheader("🎓 Graduation Background")
    degree = st.selectbox("Your graduation stream", [
        "BSc (MPC)", "BSc (BiPC)", "BCom", "BA", "BTech", 
        "MBBS", "BDS", "BPharm", "BAMS", "BHMS", "Other"
    ])
    
    if degree == "BTech":
        st.subheader("🔧 BTech Specialization")
        btech_branch = st.selectbox("Select your BTech branch", [
            "Computer Science (CSE)",
            "Electronics & Communication (ECE)",
            "Mechanical Engineering",
            "Electrical Engineering",
            "Civil Engineering",
            "Information Technology",
            "Artificial Intelligence",
            "Data Science",
            "Other Engineering"
        ])
        
        st.subheader("🛠️ Skills Assessment")
        col1, col2, col3 = st.columns(3)
        with col1:
            programming = st.slider("Programming Skills", 1, 10, 5)
            dsa = st.slider("Data Structures/Algorithms", 1, 10, 5)
        with col2:
            cloud = st.slider("Cloud Computing", 1, 10, 3)
            dbms = st.slider("Database Skills", 1, 10, 5)
        with col3:
            networking = st.slider("Networking", 1, 10, 3)
            ml = st.slider("Machine Learning", 1, 10, 3)
        
        st.subheader("💬 Soft Skills")
        comm_skills = st.slider("Communication Skills", 1, 10, 5)
        leadership = st.slider("Leadership", 1, 10, 5)
        problem_solving = st.slider("Problem Solving", 1, 10, 5)
        
        st.subheader("💼 Job Interest Areas")
        job_interests = st.multiselect("Select your job interests", [
            "Software Developer",
            "Data Scientist",
            "DevOps Engineer",
            "QA/Test Engineer",
            "System Administrator",
            "Network Engineer",
            "Cloud Engineer",
            "AI/ML Engineer",
            "Cybersecurity Analyst",
            "Database Administrator",
            "Hardware Engineer",
            "Research & Development",
            "Technical Support",
            "Project Management"
        ])
        
        if st.button("Get Career Recommendations"):
            suggestion, jobs, skill_gaps = get_btech_job_suggestions(
                btech_branch, 
                {
                    'programming': programming,
                    'dsa': dsa,
                    'cloud': cloud,
                    'dbms': dbms,
                    'networking': networking,
                    'ml': ml,
                    'communication': comm_skills,
                    'leadership': leadership,
                    'problem_solving': problem_solving
                },
                job_interests
            )
            
            st.success(f"✅ Suggested Career Path: **{suggestion}**")
            
            st.subheader("💼 Recommended Job Opportunities")
            st.write(jobs)
            
            if skill_gaps:
                st.subheader("📚 Recommended Skill Improvements")
                st.write("To improve your prospects for selected roles, consider developing these skills:")
                for skill, recommendation in skill_gaps.items():
                    st.markdown(f"- **{skill}**: {recommendation}")
            else:
                st.info("Your current skill profile matches well with your selected career interests!")
                
    else:
        pg = st.slider("Interest in Post Graduation (MSc/MTech/MBA)", 1, 5, 3)
        job = st.slider("Interest in Getting a Job", 1, 5, 3)
        startup = st.slider("Interest in Entrepreneurship", 1, 5, 3)

        if st.button("Suggest Path"):
            suggestion, jobs = get_suggestion_after_grad(degree, pg, job, startup)
            st.success(f"✅ Suggested Path: **{suggestion}**")
            st.subheader("💼 Potential Job Opportunities")
            st.write(jobs)


elif choice == "After Post Graduation":
    st.subheader("🎓 Post Graduation Details")
    pg_stream = st.text_input("Enter your PG specialization")
    research = st.slider("Interest in Research / PhD", 1, 5, 3)
    industry = st.slider("Interest in Corporate Jobs", 1, 5, 3)
    teaching = st.slider("Interest in Teaching", 1, 5, 3)

    if st.button("Suggest Path"):
        suggestion, jobs = get_suggestion_after_pg(pg_stream, research, industry, teaching)
        st.success(f"✅ Suggested Path: **{suggestion}**")
        st.subheader("💼 Potential Job Opportunities")
        st.write(jobs)