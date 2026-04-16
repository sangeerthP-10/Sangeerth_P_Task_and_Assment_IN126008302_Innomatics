
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline  # updated import

pipe = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct",  # or "google/flan-t5-base"
    max_new_tokens=512,
    do_sample=False,
)
llm = HuggingFacePipeline(pipeline=pipe)