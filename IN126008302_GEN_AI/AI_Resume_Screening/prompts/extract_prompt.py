from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Extract the following in JSON format:

{{
 "skills": [],
 "experience": "",
 "tools": []
}}

Rules:
- Only JSON
- No explanation

Resume:
{resume}

JSON:
"""
)