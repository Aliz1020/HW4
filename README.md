
# AI-Agent-SRL-RAG-Programming-Study (N=80)
### A Study on the Impact of AI Agents with Self-Regulated Learning Processes and Retrieval-Augmented Generation on High School Students’ Learning Performance and Attitudes in Hands-on Activity
### Instructor: [Chih-Hsuan Hsu](https://github.com/Aliz1020)

## 📝 Project Overview
This repository contains the dataset and analysis for a quasi-experimental study investigating how an AI agent integrated with Self-Regulated Learning (SRL) processes and Retrieval-Augmented Generation (RAG) functions as an intelligent pedagogical scaffold for high school students in programming education.

Situated in Taiwan—within the context of competency-based learning under the 108 Curriculum Guidelines—this study addresses the dual challenge of abstract programming concepts and students’ difficulties in debugging and self-monitoring during hands-on programming activities. A ten-week study was conducted with 80 first-year high school students, divided into experimental and control groups.

The study evaluates the intervention’s impact on multiple dimensions, including metacognitive regulation and programming self-efficacy. By integrating RAG technology with SRL theory, the AI agent is designed to provide more accurate, traceable, and adaptive support than conventional generative AI. Data were collected through pre- and post-tests and analyzed using ANCOVA, independent samples t-tests, and effect size analysis.

## 📊 Key Findings (Combined N=80)

### 1. Enhanced Metacognitive Regulation ($p < .001$)
* Cognitive Scaffolding: Students in the AI-agent group demonstrated significantly higher metacognitive regulation (MAI) than those in the control group after controlling for pre-test scores ($F = 45.53,\ p < .001,\ \eta^2 = .37$).
* So What? The integration of SRL scaffolding and adaptive AI support helped students better plan, monitor, and reflect on their programming learning process.

### 2. Increased Programming Self-Efficacy ($p < .001$)
* Affective Impact: The experimental group showed significantly higher programming self-efficacy (SELF) than the control group after controlling for baseline differences ($F = 89.97,\ p < .001,\ \eta^2 = .54$).
* So What? Timely feedback, structured prompts, and grounded responses may strengthen students’ confidence in solving programming problems.

### 3. Stronger Post-Test Metacognitive Performance ($p < .001$)
* Skill Development: Students receiving AI-agent support scored significantly higher on the post-test of metacognitive regulation than the control group ($t = 4.14,\ p < .001,\ d = 0.93$).
* So What? The AI agent may support students in developing stronger learning awareness and strategic control during programming activities.

### 4. Improved Post-Test Programming Self-Efficacy ($p < .001$)
* Behavioral Outcome: Learners in the experimental group demonstrated significantly higher post-test programming self-efficacy than the control group ($t = 4.24,\ p < .001,\ d = 0.95$).
* So What? AI-supported scaffolding appears to reduce uncertainty and encourage more active engagement in hands-on programming tasks.

---

## 🔬 Methodology & Statistics
* Participants: N = 80 ($n_{exp}=40, n_{ctrl}=40$)
* Design: Ten-week quasi-experimental study comparing an SRL-scaffolded AI agent with an SRL-scaffolded generative AI with RAG
* Analysis: ANCOVA and independent samples t-tests
* Results: Significant differences were found in metacognitive regulation and programming self-efficacy ($p < .001$)
* Pretest Equivalence: No significant pretest differences were found between groups in MAI ($p = .770$) or SELF ($p = .631$)

## 📖 中文摘要
本研究採準實驗設計（N=80），探討結合自主學習歷程（Self-Regulated Learning, SRL）與檢索增強生成（Retrieval-Augmented Generation, RAG）之 AI Agent，對高中生程式學習表現與學習態度之影響。核心發現如下：
1.  **後設認知提升**：AI Agent 結合 SRL 鷹架後，學生在後設認知調節表現上顯著優於對照組，顯示其有助於學生進行規劃、監控與反思。
2.  **程式自我效能提升**：實驗組在程式設計自我效能後測顯著高於對照組，表示適性回饋與結構化提示能增強學生的信心。
3.  **學習支持更具適性**：AI Agent 結合 RAG 可提供較具依據性與可追溯性的回應，降低學生在程式學習中的不確定感。
4.  **促進程式學習歷程**：透過 SRL 鷹架、分層提示與即時支援，學生較能有效處理抽象概念與除錯問題。
5.  **教學模式價值**：研究結果支持 AI Agent、SRL 與 RAG 整合應用於高中程式教育，作為提升學習成效與學習態度的可行模式。
 
 -AI agents integrated with SRL processes and RAG significantly enhance high school students’ metacognitive regulation and programming self-efficacy in hands-on programming activities.
---

## 🛠️ Usage
Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -r requirements.txt

```

Optional (export Plotly figures to PNG in addition to HTML):

```bash
pip install -U kaleido
```

## Run

Place your Excel file in the repo root (default: `data_all.xlsx`) and run:

```bash
python analysis.py
```

## 📜 Reference
[Analysis Code](https://github.com/peculab/genai-psafety)# -
