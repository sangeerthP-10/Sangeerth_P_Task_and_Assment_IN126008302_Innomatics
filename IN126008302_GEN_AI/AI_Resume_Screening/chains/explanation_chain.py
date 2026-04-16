from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from prompts.explain_prompt import explain_prompt

pipe = pipeline(
    "text-generation",
    model="gpt2"
)

llm = HuggingFacePipeline(pipeline=pipe)

explanation_chain = explain_prompt | llm