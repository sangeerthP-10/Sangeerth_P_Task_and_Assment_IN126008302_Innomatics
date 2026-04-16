# 🤖 Resume Analyzer using LLMs

An AI-powered tool that scores resumes against job descriptions using LangChain pipelines, HuggingFace text-to-text generation, and LangSmith for tracing and observability. It extracts key resume data, compares it with job requirements, and produces a structured evaluation with a score and explanation.

---

## ✨ Features

- **Resume parsing** — extracts skills, tools, and experience from raw text
- **JD matching** — compares resume data against job description requirements
- **Skill gap analysis** — identifies matching and missing skills
- **Scoring** — generates a 0–100 match score
- **Explanation** — produces a concise rationale for the score
- **LangSmith tracing** — full pipeline observability and chain debugging
- **Modular pipeline** — each step is a separate LangChain chain

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| LLM Framework | LangChain |
| LLM Backend | HuggingFace Transformers |
| Task | Text-to-Text Generation |
| Model | google/flan-t5-base |
| Tracing & Observability | LangSmith |
| Data | Plain text (.txt) resume and JD files |

---

## 📁 Project Structure

```
resume-analyzer/
├── chains/
│   ├── extraction_chain.py   # Extracts skills/experience from resume
│   ├── matching_chain.py     # Matches resume vs job description
│   └── scoring_chain.py      # Generates score and explanation
├── data/
│   ├── resume_strong.txt
│   ├── resume_weak.txt
│   └── job_description.txt
├── .env                      # API keys (never commit this)
├── main.py                   # Entry point — runs full pipeline
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

**1. Clone the repo**
```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory:
```env
# HuggingFace
HF_TOKEN=your_huggingface_token_here

# LangSmith
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=resume-analyzer
```

> Get your HuggingFace token at https://huggingface.co/settings/tokens
> Get your LangSmith API key at https://smith.langchain.com

---

## ▶️ Usage

```bash
python main.py
```

The script reads resume and JD files from `data/` and runs the full pipeline:
**extraction → matching → scoring → explanation**

All chain runs are automatically traced in your LangSmith dashboard.

---

## 🔍 LangSmith Tracing

This project is integrated with **LangSmith** for full pipeline visibility:

- Trace every LangChain call in real time
- Inspect inputs/outputs of each chain step
- Debug prompt formatting and model responses
- Monitor token usage and latency

Once running, view your traces at:
👉 https://smith.langchain.com → your project → **resume-analyzer**

---

## 📊 Example Output

### Strong Resume
```
Resume: data/resume_strong.txt
Score: 85

Explanation:
Strong alignment with the job description across most required skills.
Minor gaps in a few specialized tools listed in the JD.
```

### Weak Resume
```
Resume: data/resume_weak.txt
Score: 30

Explanation:
Resume lacks most technical skills and tools required by the job.
Very limited overlap with the job description requirements.
```

---

## 📦 Requirements

```
transformers
torch
langchain
langchain-huggingface
huggingface-hub
langsmith
python-dotenv
```

Install with:
```bash
pip install transformers torch langchain langchain-huggingface huggingface-hub langsmith python-dotenv
```

---

## ⚠️ Notes

- Model runs **locally** via HuggingFace Transformers — no inference API needed
- First run downloads model weights from HuggingFace Hub (~250MB for flan-t5-base)
- Never commit your `.env` file — add it to `.gitignore`
- Avoid using `max_length` and `max_new_tokens` together — use only `max_new_tokens`

---

## 📄 License

MIT License © 2025
