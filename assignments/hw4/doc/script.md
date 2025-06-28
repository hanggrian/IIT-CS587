# [Homework 4](https://github.com/hanggrian/IIT-CS587/blob/assets/assignments/hw4_1.pdf): Script

## Introduction

- Hello everyone, I am Hendra.
- I will be presenting a demonstration of this bonus assignment.

## Experiment 1

### Screenshot 1

> <img
    width="640"
    alt="Screenshot 1.1"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot1_1.png">

- In the first experiment, we are using Replicate platform to run Llama
  3.70B instruct model.
- It uses HuggingFace embedding to query and summarize the documents.
- Then, several chat interactions are conducted to generate a project plan
  with estimated effort.

### Screenshot 2

> <img
    width="320"
    alt="Screenshot 1.2.1"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot1_2_1.png">
> <img
    width="320"
    alt="Screenshot 1.2.2"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot1_2_2.png">

- In this snippet, the script extracts information from the documents.
- The information is then used as a context for the chat agents.

### Screenshot 3

> <img
    width="640"
    alt="Screenshot 1.3"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot1_3.png">

- I consider the output from Llama model to be the worst among the three
  experiments.
- It does not generate additional comments unless explicitly asked.
- It does not even complete the estimates, it stopped at Design phase.
- Consecutive runs can sometime fix the issue.

## Experiment 2

### Screenshot 1

> <img
    width="640"
    alt="Screenshot 2.1"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_1.png">

- The second experiment uses OpenAI platform with GPT-4o-mini model.
- It uses OpenAI's text embedding to query and summarize the documents.
- Unlike Replicate, I am using nested chat agents to discuss the project plan
  internally.

### Screenshot 2

> <img
    width="320"
    alt="Screenshot 2.2.1"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_2_1.png">
> <img
    width="320"
    alt="Screenshot 2.2.2"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_2_2.png">
> <img
    width="320"
    alt="Screenshot 2.2.2"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_2_3.png">

- First, the customer agent explain the requirements to the project manager
  agent.
- At this point, the customer has already reviewed the overview statement and
  task description documents.

### Screenshot 3

> <img
    width="320"
    alt="Screenshot 2.3.1"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_1.png">
> <img
    width="320"
    alt="Screenshot 2.3.2"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_2.png">
> <img
    width="320"
    alt="Screenshot 2.3.3"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_3.png">
> <img
    width="320"
    alt="Screenshot 2.3.4"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_4.png">
> <img
    width="320"
    alt="Screenshot 2.3.5"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_5.png">
> <img
    width="320"
    alt="Screenshot 2.3.6"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_6.png">
> <img
    width="320"
    alt="Screenshot 2.3.7"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_7.png">
> <img
    width="320"
    alt="Screenshot 2.3.8"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot2_3_8.png">

- The project manager then ask each engineer to estimate their tasks.
- The engineers may only comment on the tasks they are assigned to.
- At the end of the conversation, the project manager summarizes the project
  plan and estimated effort.
- OpenAI models generate acceptable output, it is also the most straightforward
  to use.

## Experiment 3

### Screenshot 1

> <img
    width="640"
    alt="Screenshot 3.1"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_1.png">

- We are now in the last experiment.
- Like the first experiment, it uses Replicate platform, but this time with
  DeepSeek R1 model.

### Screenshot 2

> <img
    width="320"
    alt="Screenshot 3.2.1"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_2_1.png">
> <img
    width="320"
    alt="Screenshot 3.2.2"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_2_2.png">
> <img
    width="320"
    alt="Screenshot 3.2.3"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_2_3.png">

- There is no change in the text embedding process.
- But as we can see, DeepSeek R1 model the context better than Llama.

### Screenshot 3

> <img
    width="320"
    alt="Screenshot 3.3.1"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_3_1.png">
> <img
    width="320"
    alt="Screenshot 3.3.2"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_3_2.png">
> <img
    width="320"
    alt="Screenshot 3.3.3"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_3_3.png">
> <img
    width="320"
    alt="Screenshot 3.3.4"
    src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw4/screenshot3_3_4.png">

- DeepSeek generates more comments and suggestions for each task.
- In this example, it even includes a productivity rate column in the work
  breakdown table.
- However, it is considerably slower and gets worse when the input query is
  longer.

## Conclusion

- That is all for my experiments.
- Thank you for listening!
