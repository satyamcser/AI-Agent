# 🧠 Research-Driven AI Agent: LangChain + Gemini + Tool Calling

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![LangChain](https://img.shields.io/badge/langchain-0.1.0%2B-yellowgreen)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Model](https://img.shields.io/badge/model-gemini--1.5--flash-blue)

This project demonstrates a **fully functional, research-grade AI Agent system** that integrates:

- 🧠 [LangChain](https://www.langchain.com/)
- ⚡ Google Gemini (`gemini-1.5-flash`) via `langchain-google-genai`
- 🔧 Real-time web tools (e.g., DuckDuckGo search)
- 📦 Structured outputs via Pydantic
- 🧪 Support for future research integrations (Koopman operators, SpectralONNs, Causal Models)

Unlike typical chatbot wrappers, this system is designed for **autonomous reasoning**, **tool augmentation**, and **structured research output**.

---

## ✨ Features

- ✅ Google Gemini integration via API key (MakerSuite)
- ✅ Modular Tool Calling with LangChain's agent framework
- ✅ Real-time web search via DuckDuckGo
- ✅ Pydantic schema parsing for research-ready output
- ✅ Markdown-safe JSON formatting and robust response parsing
- ✅ Research scaffold: extendable to Spectral, Koopman, or NeuroAI models

---

## 📐 Architecture Overview

```text
User Query
   ↓
Prompt Template (system + query + scratchpad)
   ↓
LangChain Agent with Tool Routing
   ↓
Google Gemini LLM (gemini-1.5-flash)
   ↓
Optional Tool Use (DuckDuckGo search)
   ↓
Markdown-safe JSON Output
   ↓
Pydantic Model Parsing
   ↓
Structured Answer (topic, summary, sources, tools_used)
```

## 🛠️ Installation

```bash
git clone https://github.com/satyamcser/AI-Agent.git
cd AI-Agent
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🔐 Setup

Create a `.env` file in the root directory and paste:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
Obtain your Gemini API key here: https://makersuite.google.com/app/apikey
```
## 🚀 Usage

```bash
python main.py
```
### You'll be prompted with:
```bash
What can I help you research?
```
### Enter a query like:
```bash
Latest use of AI agents in space robotics
```
## Ouput
```bash
{
  "topic": "AI Agents in Space Robotics",
  "summary": "AI agents have been deployed in spacecraft for navigation, autonomous decision-making, anomaly detection, and multi-agent coordination.",
  "sources": ["https://example.com/nasa-ai"],
  "tools_used": ["search"]
}
```

