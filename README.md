# AI-Agent-SRL-RAG-Programming-Study (N=80)
### A Study on the Impact of an AI Agent Integrated with SRL Scaffolding and RAG on High School Students’ Programming Learning
### Researcher: [CHIHHSUAN HSU](https://github.com/Aliz1020/HW4)

---

## 📝 Project Overview
This repository contains the dataset structure, analysis scripts, and research materials for a quasi-experimental study investigating the impact of integrating an AI agent with Self-Regulated Learning (SRL) scaffolding and Retrieval-Augmented Generation (RAG) on high school students’ programming learning.

In the context of 21st-century educational reform, fostering students’ interdisciplinary integration and self-regulated learning abilities has become a major educational goal. Taiwan’s 108 Curriculum Guidelines emphasize competency-based learning, especially in STEM and programming education, with the aim of cultivating systems thinking, inquiry, and problem-solving abilities through hands-on activities. However, high school students often experience difficulties in debugging, monitoring their learning process, and understanding abstract programming concepts.

Although Generative Artificial Intelligence (GAI), such as ChatGPT, has gradually been introduced into classrooms, challenges remain regarding the reliability, traceability, and factual accuracy of AI-generated responses. To address these limitations, this study integrates RAG technology with SRL theory and introduces an AI agent as an intelligent teaching assistant. RAG is used to improve the accuracy and grounding of generated responses, while SRL scaffolding is designed to support students in planning, monitoring, and reflecting on their learning process. The AI agent provides adaptive feedback and tiered prompts to help students overcome learning barriers and sustain self-regulation during programming activities.

This study adopts a quasi-experimental design with 80 first-year high school students, divided into an experimental group and a control group by class. During a ten-week hands-on programming activity, the experimental group uses an AI agent integrated with SRL scaffolding and RAG, whereas the control group uses generative AI with SRL scaffolding and RAG but without agent-based adaptive support.

The study examines the effects of this instructional design on students’ basic programming skills, project performance, metacognitive regulation, and programming self-efficacy.

---

## 🎯 Research Purpose
This study aims to explore whether an instructional model integrating AI agents, SRL scaffolding, and RAG can improve high school students’ programming learning outcomes.

Specifically, the study focuses on the following dimensions:

- Programming learning achievement
- Metacognitive regulation
- Programming self-efficacy
- Project performance

---

## 📊 Expected Findings

### 1. Improved Programming Learning Outcomes
- Students in the experimental group are expected to demonstrate better programming performance than those in the control group.
- The AI agent may provide more adaptive and context-aware assistance, helping learners solve programming problems more effectively.

### 2. Enhanced Metacognitive Regulation
- Students using the AI agent with SRL scaffolding are expected to show stronger planning, monitoring, and reflection abilities during programming tasks.
- Continuous prompts and feedback may help students become more aware of their own learning process and strategies.

### 3. Increased Programming Self-Efficacy
- The experimental group is expected to report higher programming self-efficacy after the intervention.
- Timely support and successful task completion may strengthen students’ confidence in dealing with programming challenges.

### 4. Better Project Performance
- Students in the experimental group are expected to perform better in hands-on programming projects and implementation tasks.
- Combining RAG-based knowledge support with adaptive AI guidance may help students translate concepts into actual practice.

---

## 🔬 Methodology & Statistics
- **Participants:** N = 80 first-year high school students
- **Design:** Ten-week quasi-experimental study
- **Grouping:**
  - Experimental Group: AI agent integrated with SRL scaffolding and RAG
  - Control Group: Generative AI integrated with SRL scaffolding and RAG
- **Learning Context:** Hands-on programming activities
- **Analysis Methods:**
  - ANCOVA for post-test differences with pre-test scores as covariates
  - Independent samples t-tests for project performance
  - Effect size analysis

---

## 📁 Main Variables
- **MAI**: Metacognition
- **SELF**: Programming Self-Efficacy
- **Programming Achievement**
- **Project Performance**

---

## 📖 Abstract
In the context of 21st-century educational reform, fostering students’ interdisciplinary integration and self-regulated learning (SRL) abilities has become a central focus. Taiwan’s 108 Curriculum Guidelines emphasize competency-based instruction, placing particular importance on STEM education and programming, with the goal of cultivating students’ systems thinking and problem-solving abilities through inquiry and hands-on activities. However, high school students often encounter difficulties in debugging and understanding abstract programming concepts.

Recently, Generative Artificial Intelligence (GAI), such as ChatGPT, has been introduced into classrooms, yet challenges remain regarding the reliability and factual accuracy of AI-generated content. To address these limitations, this study integrates Retrieval-Augmented Generation (RAG) technology with SRL theory and introduces an AI agent as an intelligent teaching assistant. RAG enhances the accuracy and traceability of generated responses, while SRL scaffolding supports students in planning, monitoring, and reflecting on their learning processes. The AI agent provides adaptive feedback and tiered prompts to help students overcome learning barriers and engage in continuous self-regulation.

This study adopts a quasi-experimental design with 80 first-year high school students, divided by class into experimental and control groups. The experimental group uses an SRL-scaffolded AI agent integrated with RAG, whereas the control group employs an SRL-scaffolded generative AI with RAG during a ten-week hands-on activity. It is expected that this integrated instructional model combining AI agents, RAG, and SRL will effectively improve students’ fundamental programming skills, project performance, and metacognitive regulation.

---

## 📖 中文摘要
在 21 世紀教育改革脈絡下，培養學生的跨領域整合能力與自主學習能力已成為教育的重要目標。臺灣 108 課綱強調素養導向教學，特別重視 STEM 與程式教育，期望透過探究與實作活動培養學生的系統思考與問題解決能力。然而，高中生在程式學習過程中，常面臨除錯困難與抽象概念理解不易等問題。

近年來，生成式人工智慧（GAI）如 ChatGPT 已逐漸被引入課堂，但其回應內容仍存在正確性與事實依據不足的限制。為改善此問題，本研究結合檢索增強生成技術（RAG）與自主學習理論（SRL），並引入 AI Agent 作為智慧教學助理。RAG 可提升生成內容的正確性與可追溯性；SRL 鷹架則協助學生在學習過程中進行規劃、監控與反思；AI Agent 透過適性回饋與分層提示，協助學生克服學習障礙並持續進行自我調節。

本研究採準實驗設計，以 80 位高中一年級學生為研究對象，依班級分為實驗組與對照組，進行為期十週的程式實作活動。實驗組使用結合 SRL 鷹架與 RAG 的 AI Agent，對照組則使用結合 SRL 鷹架與 RAG 的生成式 AI。預期此整合 AI Agent、RAG 與 SRL 的教學模式，將有效提升學生的基礎程式能力、專題實作表現、後設認知調節能力與程式設計自我效能。

---

## 🛠️ Usage

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -r requirements.txt
