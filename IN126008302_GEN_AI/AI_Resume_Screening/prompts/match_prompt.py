from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["resume_data", "job_description"],
    template="""
Compare resume and job description.

Return JSON:

{{
 "matching_skills": [],
 "missing_skills": []
}}

Rules:
- Only JSON
- No explanation

Resume Data:
{resume_data}

Job Description:
{job_description}

JSON:
"""
)