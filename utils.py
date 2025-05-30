# utils.py
def get_btech_job_suggestions(branch, skills, job_interests):
    suggestion = ""
    jobs = {"Government": [], "Private": []}
    skill_gaps = {}
    
    # Branch-specific base suggestions
    if "Computer Science" in branch or "Information Technology" in branch:
        suggestion = "Software Engineering and IT Services Path"
        base_govt_jobs = [
            "ISRO Scientist/Engineer (Through ICRB)",
            "DRDO Scientist B (Through GATE score)",
            "BEL, BHEL, BARC Engineer (Through GATE)",
            "Bank IT Officer (IBPS Specialist Officer)"
        ]
        jobs["Government"].extend(base_govt_jobs)
        
    elif "Data Science" in branch or "Artificial Intelligence" in branch:
        suggestion = "Data and AI Specialist Path"
        base_govt_jobs = [
            "Data Scientist at Government Analytics Departments",
            "AI Specialist at DRDO Labs",
            "Research Scientist at CSIR Labs"
        ]
        jobs["Government"].extend(base_govt_jobs)
        
    elif "Electronics" in branch or "Communication" in branch:
        suggestion = "Electronics and Communication Path"
        base_govt_jobs = [
            "ESE (Electronics Engineering Services)",
            "BEL, ECIL Engineer (Through GATE)",
            "Railway JE (Signal & Telecommunication)"
        ]
        jobs["Government"].extend(base_govt_jobs)
        
    # Job interest specific recommendations
    if "Data Scientist" in job_interests:
        required_skills = {'programming': 8, 'dsa': 7, 'ml': 7, 'dbms': 6}
        check_skill_gaps(skills, required_skills, skill_gaps)
        
        jobs["Private"].extend([
            "Data Scientist at Tech Companies (TCS, Infosys, Wipro)",
            "Data Analyst at Analytics Firms",
            "Business Intelligence Engineer at E-commerce"
        ])
        
        if skills['ml'] >= 7:
            jobs["Private"].append("Machine Learning Engineer at AI Startups")
            
    if "Network Engineer" in job_interests:
        required_skills = {'networking': 7, 'problem_solving': 6}
        check_skill_gaps(skills, required_skills, skill_gaps)
        
        jobs["Government"].extend([
            "Network Administrator at NIC",
            "Telecom Engineer at BSNL/MTNL"
        ])
        
        jobs["Private"].extend([
            "Network Engineer at Cisco/Juniper Partners",
            "Cloud Network Specialist at AWS/Azure Partners"
        ])
        
        if skills['cloud'] >= 5:
            jobs["Private"].append("Cloud Network Engineer")
            
    if "Software Developer" in job_interests:
        required_skills = {'programming': 7, 'dsa': 6}
        check_skill_gaps(skills, required_skills, skill_gaps)
        
        jobs["Private"].extend([
            "Software Developer at IT Services Companies",
            "Full Stack Developer at Product Companies",
            "Embedded Software Engineer (for ECE)"
        ])
        
    if "System Administrator" in job_interests:
        required_skills = {'networking': 6, 'problem_solving': 6}
        check_skill_gaps(skills, required_skills, skill_gaps)
        
        jobs["Government"].append("System Admin at Government IT Departments")
        jobs["Private"].extend([
            "Linux Administrator at Hosting Companies",
            "Windows Server Administrator"
        ])
        
    # Format the output
    formatted_jobs = ""
    for sector, job_list in jobs.items():
        if job_list:
            formatted_jobs += f"\n**{sector} Jobs:**\n"
            for job in job_list:
                formatted_jobs += f"- {job}\n"
    
    if not formatted_jobs:
        formatted_jobs = "Consider exploring more career options based on your skills and interests."
    
    return suggestion, formatted_jobs, skill_gaps




def get_suggestion_after_10th(maths, physics, biology, chemistry, eng, med, dip):
    if maths > 70 and physics > 70 and eng >= 3:
        suggestion = "Intermediate MPC or Engineering Diploma"
        jobs = """
        - Government: Railway Technician, SSC, Defense Jobs
        - Private: Technical Assistant, ITI Jobs
        """
    elif biology > 70 and chemistry > 60 and med >= 3:
        suggestion = "Intermediate BiPC or Paramedical Diploma"
        jobs = """
        - Government: ANM, Nursing, Health Inspector
        - Private: Lab Assistant, Pharmacy Assistant
        """
    elif dip >= 4:
        suggestion = "Skill-based Diploma or Polytechnic"
        jobs = """
        - Government: ITI Jobs, Apprenticeships
        - Private: Technician, Electrician, Mechanic
        """
    else:
        suggestion = "General Intermediate (MEC/CEC) or Skill Exploration"
        jobs = """
        - Government: Clerk, Postal Assistant
        - Private: Retail, Customer Service
        """
    return suggestion, jobs

def get_suggestion_after_inter(stream, eng, med, commerce, teaching):
    if stream == "MPC" and eng >= 3:
        suggestion = "BTech / BSc (Maths/Physics)"
        jobs = """
        - Government: Engineering Services, DRDO, ISRO
        - Private: Software Engineer, Data Analyst
        """
    elif stream == "BiPC" and med >= 3:
        suggestion = "MBBS / BDS / BSc (Life Sciences)"
        jobs = """
        - Government: AIIMS, JIPMER, State Medical Colleges
        - Private: Nursing, Physiotherapy, Medical Lab Tech
        """
    elif stream in ["MEC", "CEC"] and commerce >= 3:
        suggestion = "BCom / BBA / CA"
        jobs = """
        - Government: Bank PO, SSC CGL
        - Private: Accountant, Financial Analyst
        """
    elif teaching >= 4:
        suggestion = "BA / BSc + B.Ed (Teaching Career)"
        jobs = """
        - Government: Teacher Eligibility Test (TET)
        - Private: Private School Teacher
        """
    else:
        suggestion = "General Degree or Skill Development Courses"
        jobs = """
        - Government: SSC, State Govt Jobs
        - Private: Various entry-level positions
        """
    return suggestion, jobs

def get_suggestion_after_diploma(branch, higher_study, job):
    if higher_study >= 4:
        suggestion = f"Pursue BTech in {branch}"
        jobs = f"""
        - Government: PSUs like BHEL, SAIL (after BTech)
        - Private: Junior Engineer in {branch} field
        """
    elif job >= 4:
        suggestion = "Apply for Govt/Private Jobs or Apprenticeships"
        jobs = f"""
        - Government: {branch} Technician in PWD, Railways
        - Private: {branch} Technician in MNCs
        """
    else:
        suggestion = "Skill Certification or Lateral Entry BTech"
        jobs = """
        - Government: Skill India certified jobs
        - Private: Industry-specific certifications
        """
    return suggestion, jobs

def get_suggestion_after_grad(degree, pg, job, startup):
    jobs = ""
    if "MBBS" in degree or "BDS" in degree or "BAMS" in degree:
        suggestion = "Complete Internship and PG Preparation"
        jobs = """
        - Government: NEET PG for MD/MS, Civil Surgeon
        - Private: Junior Doctor, Clinic Setup
        """
    elif "BPharm" in degree:
        suggestion = "Pharma Industry or Higher Studies"
        jobs = """
        - Government: Drug Inspector, Pharmacist
        - Private: Pharmaceutical Companies
        """
    elif pg >= 4:
        suggestion = "MSc / MTech / MBA"
        jobs = """
        - Government: GATE for PSUs, UGC NET
        - Private: Corporate roles after MBA
        """
    elif job >= 4:
        suggestion = "Prepare for Jobs (Govt/Private/IT)"
        jobs = """
        - Government: UPSC, SSC, Banking
        - Private: IT, Marketing, HR
        """
    elif startup >= 4:
        suggestion = "Start your own Business / Startup"
        jobs = """
        - Government: Startup India schemes
        - Private: Entrepreneurship
        """
    else:
        suggestion = "Skill Certification + Job Prep"
        jobs = """
        - Government: Skill Development Programs
        - Private: Industry certifications
        """
    return suggestion, jobs

def get_suggestion_after_pg(pg_stream, research, industry, teaching):
    if "MD" in pg_stream or "MS" in pg_stream:
        suggestion = "Specialization or Super Specialization"
        jobs = """
        - Government: Senior Doctor in Hospitals
        - Private: Specialist in Corporate Hospitals
        """
    elif research >= 4:
        suggestion = "Pursue PhD / Research Fellowships"
        jobs = """
        - Government: CSIR, DST, ICMR Fellowships
        - Private: Industrial R&D
        """
    elif teaching >= 4:
        suggestion = "Apply for Lecturer / Asst Professor via NET/SET"
        jobs = """
        - Government: College Professor
        - Private: University Lecturer
        """
    elif industry >= 4:
        suggestion = "Join Industry Jobs or MNCs"
        jobs = """
        - Government: PSUs (if qualified)
        - Private: Corporate Leadership Roles
        """
    else:
        suggestion = "Skill-based Short-term Certifications"
        jobs = """
        - Government: Skill Development Instructor
        - Private: Industry-specific roles
        """
    return suggestion, jobs


def check_skill_gaps(current_skills, required_skills, skill_gaps):
    for skill, required_level in required_skills.items():
        if current_skills[skill] < required_level:
            gap = required_level - current_skills[skill]
            skill_gaps[skill] = (
                f"Current level {current_skills[skill]}/10, "
                f"recommended {required_level}/10. "
                f"Consider online courses or projects to improve."
            )