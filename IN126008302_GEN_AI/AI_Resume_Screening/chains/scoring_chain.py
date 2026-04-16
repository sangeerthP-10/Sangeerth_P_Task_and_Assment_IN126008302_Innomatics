from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from prompts.score_prompt import score_prompt

pipe = pipeline(
    "text-generation",
    model="gpt2"
)

llm = HuggingFacePipeline(pipeline=pipe)

scoring_chain = score_prompt | llm