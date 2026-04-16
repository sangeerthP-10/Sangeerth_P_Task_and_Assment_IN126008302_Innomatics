from dotenv import load_dotenv
load_dotenv()

from chains.extraction_chain import extraction_chain
from chains.matching_chain import matching_chain
from chains.scoring_chain import scoring_chain
from chains.explanation_chain import explanation_chain


def run_pipeline(resume, job_description):

    extracted = extraction_chain.invoke({"resume": resume})

    matched = matching_chain.invoke({
        "resume_data": extracted,
        "job_description": job_description
    })

    score = scoring_chain.invoke({"match_data": matched})

    explanation = explanation_chain.invoke({
        "score": score,
        "match_data": matched
    })

    return score, explanation


resume_files = [
    "data/resume_strong.txt",
    "data/resume_avg.txt",
    "data/resume_weak.txt"
]

with open("data/job_description.txt") as f:
    jd = f.read()

for file in resume_files:
    with open(file) as f:
        resume = f.read()

    score, explanation = run_pipeline(resume, jd)
print("\n====================")
print("Resume:", file)
print("Score:", str(score).strip())
print("Explanation:", str(explanation).strip())