from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from prompts.match_prompt import match_prompt

pipe = pipeline(
    "text-generation",
    model="gpt2"
)

llm = HuggingFacePipeline(pipeline=pipe)

matching_chain = match_prompt | llm