# [Bonus homework](https://github.com/hanggrian/IIT-CS587/blob/assets/assignments/hw4_1.pdf): Analysis

> **Overview:**
>
> In this assignment, you will create estimates for the different tasks needed
  for the project plan for the software product requested in the Requirements
  Specification document for Chicago WideCast Smart-Home Services.
>
> **Instructions:**
>
> 1.  Create venv that has Python 3.10
> 1.  Execute every experiment requested for every model on every platform using
      the frameworks listed in the provided table below:
>
> Experiment number | Platform | Model | Framework
> ---: | --- | --- | ---
> 1 | Replicate (Cloud) | <ul><li>meta/meta-llama-3-70b-instruct</li><li>HuggingFaceEmbedding</li><li>BAAI/bge-small-en-v1.6</li></ul> | LangChain/LangGraph
> 2 | OpenAI (Cloud) | <ul><li>gpt-4o-mini</li><li>text-embedding-3-small</li></ul> | LangChain/LangGraph
> 3 | Replicate (Cloud) | <ul><li>deepseek-ai/deepseek-r1</li><li>HuggingFaceEmbedding</li><li>BAAI/bge-small-en-v1.6</li></ul> | LangChain/LangGraph

The scripts are created for each experiments:

- `experiment1.ipynb`: Replicate with Llama
- `experiment2.ipynb`: OpenAI with GPT
- `experiment3.ipynb`: Replicate with DeepSeek

## [Deliverables](https://github.com/hanggrian/IIT-CS587/blob/assets/assignments/hw4_2.pdf)

> You are required to submit on Canvas a SINGLE Zip file that has the following
  deliverables are:
>
> 1.  Your IPYNB scripts
> 1.  All of your source code and output
> 1.  Analysis and Output report that has your assignment run, output, and
      analysis saved in Analysis.pdf
> 1.  Video recording of 15-20 minutes as a demo for the run of your assignment
      using Panopto.

The project directory is zipped as `HW4_Wijaya.zip`.

- `data`: Contains PDF files of project description and requirements.
- `doc`: Analysis report (this file in PDF format) and video recording.
- `src`: Experiments in Jupyter Notebook files.

## Output

### Loading documents

**Replicate with Llama**

<img
  width="320"
  alt="Screenshot 1.2.1"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot1_2_1.png">
<img
  width="320"
  alt="Screenshot 1.2.2"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot1_2_2.png">

**OpenAI with GPT**

<img
  width="320"
  alt="Screenshot 2.2.1"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_2_1.png">
<img
  width="320"
  alt="Screenshot 2.2.2"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_2_2.png">
<img
  width="320"
  alt="Screenshot 2.2.2"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_2_3.png">

**Replicate with DeepSeek**

<img
  width="320"
  alt="Screenshot 3.2.1"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_2_1.png">
<img
  width="320"
  alt="Screenshot 3.2.2"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_2_2.png">
<img
  width="320"
  alt="Screenshot 3.2.3"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_2_3.png">

### Conversation summary

**Replicate with Llama**

<img
  width="640"
  alt="Screenshot 1.3"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot1_3.png">

**OpenAI with GPT**

<img
  width="320"
  alt="Screenshot 2.3.1"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_1.png">
<img
  width="320"
  alt="Screenshot 2.3.2"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_2.png">
<img
  width="320"
  alt="Screenshot 2.3.3"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_3.png">
<img
  width="320"
  alt="Screenshot 2.3.4"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_4.png">
<img
  width="320"
  alt="Screenshot 2.3.5"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_5.png">
<img
  width="320"
  alt="Screenshot 2.3.6"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_6.png">
<img
  width="320"
  alt="Screenshot 2.3.7"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_7.png">
<img
  width="320"
  alt="Screenshot 2.3.8"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_8.png">

**Replicate with DeepSeek**

<img
  width="320"
  alt="Screenshot 3.3.1"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_3_1.png">
<img
  width="320"
  alt="Screenshot 3.3.2"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_3_2.png">
<img
  width="320"
  alt="Screenshot 3.3.3"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_3_3.png">
<img
  width="320"
  alt="Screenshot 3.3.4"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_3_4.png">

## Analysis

Judging from the results, the Llama model from Replicate performed the worst
in terms of understanding the context of input documents and generating the
estimate summary. Several points during the execution, the conversation stopped
without finishing the summary. And although this issue can sometimes be resolved
in consecutive runs, other models never had this issue.

The reasoning model from OpenAI performed better than expected, considering that
it is a cost-effective option. In this experiment, a nested chat was used for
the development team to discuss internally before the project manager summarizes
the plan to the customer. The agents successfully tagged the tasks with
`REQ-XXX` identifiers and efforts for each task.

Finally, the DeepSeek model from Replicate performed the best in terms of the
completeness of the summary. In this example, it included a productivity rate
calculation in the work breakdown structure. However, it is considerably
slower than the other two models, especially when the input query is longer.
