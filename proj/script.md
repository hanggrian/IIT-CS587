# Presentation script

## Slide 1

> ![Slide 1](https://github.com/hanggrian/IIT-CS587/raw/assets/proj/slide1_1.png)

- Hi everyone! I am Hendra, and I will be presenting software project planning
  with AutoGen.
- This plan uses waterfall methodology as is the requirement of the first phase.

## Slide 2

> ![Slide 2](https://github.com/hanggrian/IIT-CS587/raw/assets/proj/slide1_2.png)

- First, the project implements pyautogen from previous assignments.
- Then, integrate OpenAI models to produce planning estimates.
- Finally, the experiments are conducted on a Jupyter notebook file.

## Slide 3

> ![Slide 3](https://github.com/hanggrian/IIT-CS587/raw/assets/proj/slide1_3.png)

- Strickland Propane is a traditional company that sells gas-related products.
- In this example, they need a software system to manage customers, inventory
  and sales.

## Slide 4

> ![Slide 4](https://github.com/hanggrian/IIT-CS587/raw/assets/proj/slide1_4.png)

- To generate estimates, I create seven AI agents of different roles.
- One of them represents the customer while the rest are the software team.

## Slide 5

> ![Slide 5](https://github.com/hanggrian/IIT-CS587/raw/assets/proj/slide1_5.png)

- The customer agent lists the requirements to the project manager.
- The project manager collaborates with other engineers to produce the
  estimates.
- The results are then compiled and presented back to the customer.

## Slide 6

> ![Slide 6](https://github.com/hanggrian/IIT-CS587/raw/assets/proj/slide1_6.png)

- This page shows the conversation output between AI agents.
- The customer agent initiates the conversation, triggering nested chats between
  the project manager and the engineers.
- At the end of the conversation, the project manager summarizes the results
  to the customer.

## Slide 7

> ![Slide 7](https://github.com/hanggrian/IIT-CS587/raw/assets/proj/slide1_7.png)

- Here are the generated estimates for each section, in hourly format.
- The results are sometimes too generalized.
- However, I still find the answers impressive given that they were concluded in
  a single round of conversation.

## Slide 8

> ![Slide 8](https://github.com/hanggrian/IIT-CS587/raw/assets/proj/slide1_8.png)

- In this page, the estimates are tabulated in a Work Breakdown Structure.
- The duration calculations assume that multiple engineers are available to
  work on the same task.
- The software is projected to take 9.6 weeks to complete, or more than two
  months.

## Slide 9

> ![Slide 9](https://github.com/hanggrian/IIT-CS587/raw/assets/proj/slide1_9.png)

- In my tests, the reasoning models take longer to respond but produce more
  accurate estimates, especially in consecutive rounds of conversation.
- The second conclusion is that we need to balance cost and performance, better
  results do not always warrant higher cost.
- Finally, to reduce hallucinations, avoid ambiguity when feeding prompts to
  the AI agents.

## Slide 10

> ![Slide 10](https://github.com/hanggrian/IIT-CS587/raw/assets/proj/slide1_10.png)

- That is all for my presentation.
- Thanks everyone for listening and stay safe in this hot summer!
