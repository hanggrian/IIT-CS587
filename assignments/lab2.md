# [Lab 2](https://github.com/hanggrian/IIT-CS587/blob/assets/assignments/lab2.pdf)

> After you complete the tasks listed in the instructions document
  (`Lab_2 - Instructions-2.pdf`), submit (a link in this class discussion where
  anyone of your classmates will be able to watch) the Panopto Video Recording
  of a successful run on your computer.
>
> And provide you answers to the following prompts (your answer for every prompt
  shall not exceed 100 words):

[Screen recording](https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab2/screenrecord.mov)

## Question 1

> Did you encounter any issue part of the setup process?

Yes, there is an error when installing the `pygraphviz` in Linux. The
[workaround](https://cthoyt.com/2024/11/05/installing-pygraphviz.html) is to
use a macOS machine.

## Question 2

> What was the computer hardware (processor and main memory) that you have on
  your computer?

- **CPU:** Intel Core i5-10400
- **RAM:** 32GB DDR4

## Question 3

> How long did it take you to complete the installation?

Roughly an hour to modify:

- `research_plan_node` function to avoid `KeyError` when `content` is not found
  in current state.
- All `SqliteSaver` instances created using `with` statement.

## Question 4

> How long did it take AutoGen to complete the entire conversation of the AI
  Agents?

It takes two to three minutes to complete the conversation.

## Question 5

The first output confirms a state graph is created.

<img
  width="320"
  alt="Screenshot 1"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab2/screenshot1.png">

Then, the graph is displayed with PyGraphviz.

<img
  width="320"
  alt="Screenshot 2"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab2/screenshot2.png">

The conversation between five agents is shown in the Jupyter cell output.

<img
  width="320"
  alt="Screenshot 3.1"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab2/screenshot3_1.png">
<img
  width="320"
  alt="Screenshot 3.2"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab2/screenshot3_2.png">
<img
  width="320"
  alt="Screenshot 3.3"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab2/screenshot3_3.png">
<img
  width="320"
  alt="Screenshot 3.4"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab2/screenshot3_4.png">

Finally, the `helper.py` script is executed to show agent configuration with
Gradio UI.

<img
  width="320"
  alt="Screenshot 4"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab2/screenshot4.png">
