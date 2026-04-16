from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_data"],
    template="""
Give a score from 0 to 100.

Return ONLY a number.
Do NOT explain.

Answer:
"""
)