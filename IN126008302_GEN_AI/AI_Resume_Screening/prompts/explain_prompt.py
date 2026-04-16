from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["score", "match_data"],
    template="""
Explain the score in 2 lines only.

Do NOT repeat input.

Explanation:
"""
)