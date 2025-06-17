# [Lab 1](https://github.com/hanggrian/IIT-CS587/blob/assets/assignments/lab1.pdf)

> After you complete the tasks listed in the instructions document
  (`Lab_1 - Instructions-1.pdf`), submit (a link in this class discussion where
  anyone of your classmates will be able to watch) the Panopto Video Recording
  of a successful run on your computer.
>
> And provide you answers to the following prompts (your answer for every prompt
  shall not exceed 100 words):

[Screen recording](https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab1/screenrecord.mp4)

## Question 1

> Did you encounter any issue part of the setup process?

Yes, there is a [bug](https://github.com/microsoft/autogen/issues/3345) in
OpenAI key format where the key is not accepted when it has an underscore
character. I had to keep regenerating until I got a key without an underscore.

## Question 2

> What was the computer hardware (processor and main memory) that you have on
  your computer?

- **CPU:** Intel Core i5-10400
- **RAM:** 32GB DDR4

## Question 3

> How long did it take you to complete the installation?

Several hours figuring out why the OpenAI key was not working, and then about
30 minutes to complete the lesson.

## Question 4

> How long did it take AutoGen to complete the entire conversation of the AI
  Agents?

It takes one minute to complete each conversation, so two minutes in total.

## Question 5

The first conversation produces a CSV file about NVIDIA stock prices. However,
there are errors when plotting the data with Matplotlib. The generated code
produces `ValueError` in the first run and `TypeError` in the second run.

<img
  width="320"
  alt="Screenshot 1.1"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab1/screenshot1_1.png">
<img
  width="320"
  alt="Screenshot 1.2"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab1/screenshot1_2.png">
<img
  width="320"
  alt="Screenshot 1.3"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab1/screenshot1_3.png">
<img
  width="320"
  alt="Screenshot 1.4"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab1/screenshot1_4.png">
<img
  width="320"
  alt="Screenshot 1.5"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab1/screenshot1_5.png">
<img
  width="320"
  alt="Screenshot 1.6"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab1/screenshot1_6.png">

The second conversation presents the CSV data in Pandas DataFrame format, it
works as expected.

<img
  width="320"
  alt="Screenshot 2.1"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab1/screenshot2_1.png">
<img
  width="320"
  alt="Screenshot 2.2"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab1/screenshot2_2.png">
<img
  width="320"
  alt="Screenshot 2.3"
  src="https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/lab1/screenshot2_3.png">
