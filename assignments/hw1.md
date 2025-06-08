<!-- KaTeX -->
<script
  type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: { inlineMath: [['$', '$']] }, messageStyle: 'none' });
</script>

<!-- Mermaid -->
<script
  type="text/javascript"
  src="https://cdn.jsdelivr.net/npm/mermaid@10.4.0/dist/mermaid.min.js">
</script>

# [Homework 1](https://github.com/hanggrian/IIT-CS587/blob/assets/assignments/hw1.pdf)

## Problem 1

> Feed the information provided in this handout in MS Project to create the
  Project Plan and the Network Diagram.

Below is the tasks with their durations calculated based on the information
provided in the handout. Indentation is used to indicate the hierarchy of tasks.
Task groups are indicated with **bold** text, they do not have assigned
resources or durations.

<div style="width: 240px;">Task</div> | Effort | Duration
--- | ---: | ---:
**Project plan** | |
&emsp;Write plan | $187\ \textsf{pages} / 5\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{37.4}\ \textbf{h}$ | $37.4\ \textsf{h} / 1\ \textsf{person} = \mathbf{37.4}\ \textbf{h}$
&emsp;**Review plan** | |
&emsp;&emsp;Preparation for review | $187\ \textsf{pages} / 4\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{46.75}\ \textbf{h}$ | $46.75\ \textsf{h} / 7\ \textsf{people} = \mathbf{6.64}\ \textbf{h}$
&emsp;&emsp;Review meeting | $187\ \textsf{pages} / 5\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{37.4}\ \textbf{h}$ | $37.4\ \textsf{h} / 6\ \textsf{people} = \mathbf{6.23}\ \textbf{h}$
&emsp;&emsp;Rework | $71\ \textsf{defects} / 5\ \frac{\textsf{defects}}{\textsf{h}} = \mathbf{14.2}\ \textbf{h}$ | $14.2\ \textsf{h} / 1\ \textsf{person} = \mathbf{14.2}\ \textbf{h}$
**Requirements** | |
&emsp;Write requirements | $156\ \textsf{Req} / 5\ \frac{\textsf{Req}}{\textsf{h}} = \mathbf{31.2}\ \textbf{h}$ | $31.2\ \textsf{h} / 2\ \textsf{people} = \mathbf{15.6}\ \textbf{h}$
&emsp;Write Use Case Model | $76\ \textsf{Use Cases} / 5\ \frac{\textsf{Use Cases}}{\textsf{h}} = \mathbf{15.2}\ \textbf{h}$ | $15.2\ \textsf{h} / 2\ \textsf{people} = \mathbf{7.6}\ \textbf{h}$
&emsp;**Review requirements** | |
&emsp;&emsp;Preparation for review | $156\ \textsf{Req} / 8 \frac{\textsf{Req}}{\textsf{h}} + 76\ \textsf{Use Cases} / 4\ \frac{\textsf{Use Cases}}{\textsf{h}} = 19.5 \textsf{h} + 19 \textsf{ h} = \mathbf{38.5}\ \textbf{h}$ | $38.5\ \textsf{h} / 4\ \textsf{people} = \mathbf{9.62}\ \textbf{h}$
&emsp;&emsp;Review meeting | $156\ \textsf{Req} / 8\ \frac{\textsf{Req}}{\textsf{h}} + 76\ \textsf{Use Cases} / 12\ \frac{\textsf{Use Cases}}{\textsf{h}} = 19.5\ \textsf{h} + 6.58\ \textsf{h} = \mathbf{26.08}\ \textbf{h}$ | $26.08\ \textsf{h} / 5\ \textsf{people} = \mathbf{5.21}\ \textbf{h}$
&emsp;Rework | $97\ \textsf{defects} / 5\ \frac{\textsf{defects}}{\textsf{h}} = \mathbf{19.4}\ \textbf{h}$ | $19.4\ \textsf{h} / 3\ \textsf{people} = \mathbf{6.46}\ \textbf{h}$
**Analysis** | |
&emsp;Write analysis document | $48\ \textsf{pages} / 5\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{9.6}\ \textbf{h}$ | $9.6\ \textsf{h} / 2\ \textsf{people} = \mathbf{4.8}\ \textbf{h}$
&emsp;**Review analysis document** | |
&emsp;&emsp;Preparation for analysis document | $48\ \textsf{pages} / 5\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{9.6}\ \textbf{h}$ | $9.6\ \textsf{h} / 4\ \textsf{people} = \mathbf{2.4}\ \textbf{h}$
&emsp;&emsp;Review meeting | $48\ \textsf{pages} / 8 \frac{\textsf{pages}}{\textsf{h}} = \mathbf{6}\ \textbf{h}$ | $6\ \textsf{h} / 5\ \textsf{people} = \mathbf{1.2}\ \textbf{h}$
&emsp;Rework | $66\ \textsf{defects} / 4\ \frac{\textsf{defects}}{\textsf{h}} = \mathbf{16.5}\ \textbf{h}$ | $16.5\ \textsf{h} / 2\ \textsf{people} = \mathbf{8.25}\ \textbf{h}$
**Design** | |
&emsp;Write DD | $134\ \textsf{pages} / 5\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{26.8}\ \textbf{h}$ | $26.8\ \textsf{h} / 1\ \textsf{person} = \mathbf{26.8}\ \textbf{h}$
&emsp;**Review DD** | |
&emsp;&emsp;Preparation for DD | $134\ \textsf{pages} / 3\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{44.67}\ \textbf{h}$ | $44.67\ \textsf{h} / 3\ \textsf{people} = \mathbf{14.89}\ \textbf{h}$
&emsp;&emsp;Review meeting | $134\ \textsf{pages} / 6\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{22.33}\ \textbf{h}$ | $22.33\ \textsf{h} / 4\ \textsf{people} = \mathbf{5.58}\ \textbf{h}$
&emsp;Rework | $88\ \textsf{defects} / 5\ \frac{\textsf{defects}}{\textsf{h}} = \mathbf{17.6}\ \textbf{h}$ | $17.6\ \textsf{h} / 1\ \textsf{person} = \mathbf{17.6}\ \textbf{h}$
&emsp;Write DM | $69\ \textsf{pages} / 1\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{69}\ \textbf{h}$ | $69\ \textsf{h} / 1\ \textsf{person} = \mathbf{69}\ \textbf{h}$
&emsp;**Review DM** | |
&emsp;&emsp;Preparation for DM | $69\ \textsf{pages} / 3\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{23}\ \textbf{h}$ | $23\ \textsf{h} / 3\ \textsf{people} = \mathbf{7.66}\ \textbf{h}$
&emsp;&emsp;Review meeting | $69\ \textsf{pages} / 5\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{13.8}\ \textbf{h}$ | $13.8\ \textsf{h} / 4\ \textsf{people} = \mathbf{3.45}\ \textbf{h}$
&emsp;Rework | $94\ \textsf{defects} / 5\ \frac{\textsf{defects}}{\textsf{h}} = \mathbf{18.8}\ \textbf{h}$ | $18.8\ \textsf{h} / 1\ \textsf{person} = \mathbf{18.8}\ \textbf{h}$
**Coding and unit test** | |
&emsp;Write code | $3450\ \textsf{SLOC} / 10\ \frac{\textsf{SLOC}}{\textsf{h}} = \mathbf{345}\ \textbf{h}$ | $345\ \textsf{h} / 4\ \textsf{people} = \mathbf{86.25}\ \textbf{h}$
&emsp;**Unit testing** | |
&emsp;&emsp;Prepare/execute test cases | $174\ \textsf{test cases} / 5\ \frac{\textsf{test cases}}{\textsf{h}} = \mathbf{34.8}\ \textbf{days}$ | $34.8\ \textsf{days} / 2\ \textsf{people} = \mathbf{17.4}\ \textbf{days}$
&emsp;&emsp;Fix found defects | $104\ \textsf{defects} / 4\ \frac{\textsf{defects}}{\textsf{h}} = \mathbf{26}\ \textbf{days}$ | $26\ \textsf{days} / 2\ \textsf{people} = \mathbf{13}\ \textbf{days}$
&emsp;&emsp;Test dixed defects | $104\ \textsf{defects} / 5\ \frac{\textsf{defects}}{\textsf{h}} = \mathbf{20.8}\ \textbf{days}$ | $20.8\ \textsf{days} / 2\ \textsf{people} = \mathbf{10.4}\ \textbf{days}$
&emsp;**Code inspection** | |
&emsp;&emsp;Preparation for code inspection | $3450\ \textsf{SLOC} / 110\ \frac{\textsf{SLOC}}{\textsf{h}} = \mathbf{31.36}\ \textbf{h}$ | $31.36\ \textsf{h} / 4\ \textsf{people} = \mathbf{7.84}\ \textbf{h}$
&emsp;&emsp;Code inspection meeting | $3450\ \textsf{SLOC} / 160\ \frac{\textsf{SLOC}}{\textsf{h}} = \mathbf{21.56}\ \textbf{h}$ | $21.56\ \textsf{h} / 5\ \textsf{people} = \mathbf{4.31}\ \textbf{h}$
&emsp;&emsp;Rework | $309\ \textsf{defects} / 5\ \frac{\textsf{defects}}{\textsf{h}} = \mathbf{61.8}\ \textbf{h}$ | $61.8\ \textsf{h} / 2\ \textsf{people} = \mathbf{30.9}\ \textbf{h}$
&emsp;**System integration testing** | |
&emsp;&emsp;Write test plan | $149\ \textsf{pages} / 5\ \frac{\textsf{pages}}{\textsf{day}} = \mathbf{29.8}\ \textbf{days}$ | $29.8\ \textsf{days} / 2\ \textsf{people} = \mathbf{14.9}\ \textbf{days}$
&emsp;&emsp;**Review TP** | |
&emsp;&emsp;&emsp;Preparation for TP | $149\ \textsf{pages} / 5\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{29.8}\ \textbf{h}$ | $29.8\ \textsf{h} / 4\ \textsf{people} = \mathbf{7.45}\ \textbf{h}$
&emsp;&emsp;&emsp;Review TP meeting | $149\ \textsf{pages} / 6\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{24.83}\ \textbf{h}$ | $24.83\ \textsf{h} / 5\ \textsf{people} = \mathbf{4.97}\ \textbf{h}$
&emsp;&emsp;&emsp;Rework | $99\ \textsf{defects} / 4\ \frac{\textsf{defects}}{\textsf{h}} = \mathbf{24.75}\ \textbf{h}$ | $24.75\ \textsf{h} / 2\ \textsf{people} = \mathbf{12.38}\ \textbf{h}$
&emsp;&emsp;Execute TP | $138\ \textsf{test cases} / 30\ \frac{\textsf{test cases}}{\textsf{day}} = \mathbf{4.6}\ \textbf{days}$ | $4.6\ \textsf{days} / 2\ \textsf{people} = \mathbf{2.3}\ \textbf{days}$
&emsp;&emsp;Fix found defects | $77\ \textsf{defects} / 4\ \frac{\textsf{defects}}{\textsf{day}} = \mathbf{19.25}\ \textbf{days}$ | $19.25\ \textsf{days} / 2\ \textsf{people} = \mathbf{9.63}\ \textbf{days}$
&emsp;&emsp;Test fixed defects | $77\ \textsf{defects} / 10\ \frac{\textsf{defects}}{\textsf{day}} = \mathbf{7.7}\ \textbf{days}$ | $7.7\ \textsf{days} / 2\ \textsf{people} = \mathbf{3.85}\ \textbf{days}$
&emsp;**Load, stress and performance Testing** | |
&emsp;&emsp;Write test plan | $201\ \textsf{pages} / 4\ \frac{\textsf{pages}}{\textsf{day}} = \mathbf{50.25}\ \textbf{days}$ | $50.25\ \textsf{days} / 2\ \textsf{people} = \mathbf{25.13}\ \textbf{days}$
&emsp;&emsp;**Review TP** | |
&emsp;&emsp;&emsp;Preparation for TP | $201\ \textsf{pages} / 3\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{67}\ \textbf{h}$ | $67\ \textsf{h} / 4\ \textsf{people} = \mathbf{16.75}\ \textbf{h}$
&emsp;&emsp;&emsp;Review TP meeting | $201\ \textsf{pages} / 6\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{33.5}\ \textbf{h}$ | $33.5\ \textsf{h} / 5\ \textsf{people} = \mathbf{6.7}\ \textbf{h}$
&emsp;&emsp;&emsp;Rework | $88\ \textsf{defects} / 3\ \frac{\textsf{defects}}{\textsf{h}} = \mathbf{29.33}\ \textbf{h}$ | $29.33\ \textsf{h} / 2\ \textsf{people} = \mathbf{14.67}\ \textbf{h}$
&emsp;&emsp;Execute TP | $192\ \textsf{test cases} / 10\ \frac{\textsf{test cases}}{\textsf{day}} = \mathbf{19.2}\ \textbf{days}$ | $19.2\ \textsf{days} / 2\ \textsf{people} = \mathbf{9.6}\ \textbf{days}$
&emsp;&emsp;Fix found defects | $74\ \textsf{defects} / 5\ \frac{\textsf{defects}}{\textsf{day}} = \mathbf{14.8}\ \textbf{days}$ | $14.8\ \textsf{days} / 2\ \textsf{people} = \mathbf{7.4}\ \textbf{days}$
&emsp;&emsp;Test fixed defects | $74\ \textsf{defects} / 8\ \frac{\textsf{defects}}{\textsf{day}} = \mathbf{9.25}\ \textbf{days}$ | $9.25\ \textsf{days} / 2\ \textsf{people} = \mathbf{4.63}\ \textbf{days}$
&emsp;**Documentation** | |
&emsp;&emsp;User documentation | $141\ \textsf{pages} / 5\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{28.2}\ \textbf{h}$ | $28.2\ \textsf{h} / 2\ \textsf{people} = \mathbf{14.1}\ \textbf{h}$
&emsp;&emsp;**Review UD** | |
&emsp;&emsp;&emsp;Preparation for UD Review | $141\ \textsf{pages} / 4\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{35.25}\ \textbf{h}$ | $35.25\ \textsf{h} / 4\ \textsf{people} = \mathbf{8.06}\ \textbf{h}$
&emsp;&emsp;&emsp;Review UD meeting | $141\ \textsf{pages} / 10\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{14.1}\ \textbf{h}$ | $14.1\ \textsf{h} / 5\ \textsf{people} = \mathbf{2.82}\ \textbf{h}$
&emsp;&emsp;&emsp;Rework | $203\ \textsf{defects} / 10\ \frac{\textsf{defects}}{\textsf{h}} = \mathbf{20.3}\ \textbf{h}$ | $20.3\ \textsf{h} / 2\ \textsf{people} = \mathbf{10.15}\ \textbf{h}$
&emsp;**Training material** | |
&emsp;&emsp;Tutorial | $266\ \textsf{pages} / 4\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{66.5}\ \textbf{h}$ | $66.5\ \textsf{h} / 2\ \textsf{people} = \mathbf{33.25}\ \textbf{h}$
&emsp;&emsp;**Review tutorial** | |
&emsp;&emsp;&emsp;Preparation for tutorial review | $266\ \textsf{pages} / 5\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{53.2}\ \textbf{h}$ | $53.2\ \textsf{h} / 4\ \textsf{people} = \mathbf{13.3}\ \textbf{h}$
&emsp;&emsp;&emsp;Review tutorial meeting | $266\ \textsf{pages} / 10\ \frac{\textsf{pages}}{\textsf{h}} = \mathbf{26.6}\ \textbf{h}$ | $26.6\ \textsf{h} / 5\ \textsf{people} = \mathbf{5.32}\ \textbf{h}$
&emsp;&emsp;&emsp;Rework | $168\ \textsf{defects} / 10\ \frac{\textsf{defects}}{\textsf{h}} = \mathbf{16.8}\ \textbf{h}$ | $16.8\ \textsf{h} / 2\ \textsf{people} = \mathbf{8.4}\ \textbf{h}$

## Problem 2

> Create a WBS with the required phases and activities to complete this project.

Below is the work breakdown structure with progression and task dependencies
for the project.

```mermaid
graph LR
  A[Project plan] --> B(Write plan)
  B --> C(Preparation for review)
  C --> D(Review meeting)
  D --> E(Rework)
  E --> F[Requirements]
```

```mermaid
graph LR
  A[Requirements] --> B(Write requirements)
  A --> C(Write use case model)
  B --> D(Preparation for review)
  C --> D
  D --> E(Rework)
  E --> F[Analysis]
```

```mermaid
graph LR
  A[Analysis] --> B(Write analysis document)
  B --> C(Preparation for review)
  C --> D(Review meeting)
  D --> E(Rework)
  E --> F[Design]
```

```mermaid
graph LR
  A[Design] --> B(Write DD)
  A --> C(Write DM)
  B --> D(Preparation for DD)
  C --> E(Preparation for DM)
  D --> G(Review meeting)
  E --> H(Review meeting)
  G --> I(Rework)
  H --> J(Rework)
  I --> K[Coding]
  J --> K
```

```mermaid
graph LR
  A[Coding] --> B(Write code)
  B --> C(Prepare/execute test cases)
  B --> D(Preparation for code inspection)
  C --> E(Fix found defects)
  D --> F(Code inspection meeting)
  E --> G(Test fixed defects)
  F --> H(Rework)
  G --> I[System integration]
  H --> I
```

```mermaid
graph LR
  A[System integration] --> B(Write test plan)
  B --> C(Preparation for TP)
  C --> D(Review TP meeting)
  D --> E(Rework)
  E --> F(Fix found defects)
  F --> G(Test fixed defects)
  G --> I[Performance testing]
```

```mermaid
graph LR
  A[Performance testing] --> B(Write test plan)
  B --> C(Preparation for TP)
  C --> D(Review TP meeting)
  D --> E(Rework)
  E --> F(Execute TP)
  F --> G(Fix found defects)
  G --> H(Test fixed defects)
  H --> I[Documentation]
```

```mermaid
graph LR
  A[Documentation] --> B(User documentation)
  B --> C(Preparation for UD review)
  C --> D(Review UD meeting)
  D --> E(Rework)
  E --> F[Training Material]
```

```mermaid
graph LR
  A[Training Material] --> B(Tutorial)
  B --> C(Preparation for tutorial review)
  C --> D(Review tutorial meeting)
  D --> E(Rework)
  E --> F[End]
```

## Problem 3

> Assign the Resources to the Tasks making any assumptions you consider
  appropriate (Your assumptions should be based on Software Engineering
  Assumptions).

Task | Resource | Note
--- | --- | ---
**Project plan** | |
&emsp;Write plan | PM3
&emsp;**Review plan** | |
&emsp;&emsp;Preparation for review | PM4, PM5, RE1, SE1, DE1, PE1, TE1 | PM3 absent
&emsp;&emsp;Review meeting | PM3, DE105, PE7, RE2, SE2, TE2 | PM3 returns
&emsp;&emsp;Rework | PM3
**Requirements** | |
&emsp;Write requirements | RE1, RE2
&emsp;Write use case model | RE7, RE8
&emsp;**Review requirements** | |
&emsp;&emsp;Preparation for review | RE102, RE103, RE117, RE118 | RE1, RE2, RE7 absent
&emsp;&emsp;Review meeting | RE1, RE2, RE7, RE103, RE119 | RE1, RE2, RE7 returns
&emsp;Rework | RE1, RE2, RE7
**Analysis** | |
&emsp;Write analysis document | SE1, SE2
&emsp;**Review analysis document** | |
&emsp;&emsp;Preparation for analysis document | SE7, SE8, SE204, SE205 | SE1, SE2 absent
&emsp;&emsp;Review meeting | SE1, SE2, SE7, SE205, SE501 | SE1, SE2 returns
&emsp;Rework | SE1, SE2
**Design** | |
&emsp;Write DD | SE7
&emsp;**Review DD** | |
&emsp;&emsp;Preparation for DD | SE1, SE2, SE8 | SE7 absent
&emsp;&emsp;Review meeting | SE1, SE2, SE7, SE8 | SE7 returns
&emsp;Rework | SE7
&emsp;Write DM | SE9
&emsp;**Review DM** | |
&emsp;&emsp;Preparation for DM | SE204, SE205, SE501 | SE9 absent
&emsp;&emsp;Review meeting | SE9, SE204, SE205, SE501 | SE9 returns
&emsp;Rework | SE9
**Coding and unit test** | |
&emsp;Write code | PE1, PE7, PE8, PE9
&emsp;**Unit testing** | |
&emsp;&emsp;Prepare/execute test cases | TE1, TE2
&emsp;&emsp;Fix found defects | PE1, PE202
&emsp;&emsp;Test fixed defects | TE3, TE4
&emsp;**Code inspection** | |
&emsp;&emsp;Preparation for code inspection | PE8, PE9, PE203, PE205 | PE1, PE7 absent
&emsp;&emsp;Code inspection meeting | PE1, PE7, PE10, PE203, PE202 | PE1, PE7 returns
&emsp;&emsp;Rework | PE1, PE7
&emsp;**System integration testing** | |
&emsp;&emsp;Write test plan | TE1, TE2
&emsp;&emsp;**Review TP** | |
&emsp;&emsp;&emsp;Preparation for TP | TE3, TE4, TE302, TE404 | TE1, TE2 absent
&emsp;&emsp;&emsp;Review TP meeting | TE1, TE2403, TE404, TE405, TE2 | TE1, TE2 returns
&emsp;&emsp;&emsp;Rework | TE1, TE2
&emsp;&emsp;Execute TP | TE302, TE2403
&emsp;&emsp;Fix found defects | PE202, PE203
&emsp;&emsp;Test fixed defects | TE404, TE405
&emsp;**Load, stress and performance testing** | |
&emsp;&emsp;Write test plan | TE3, TE4
&emsp;&emsp;**Review TP** | |
&emsp;&emsp;&emsp;Preparation for TP | TE302, TE404, TE405, TE2403 | TE3, TE4 absent
&emsp;&emsp;&emsp;Review TP meeting | TE1, TE2, TE3, TE4, TE2403 | TE3, TE4 returns
&emsp;&emsp;&emsp;Rework | TE3, TE4
&emsp;&emsp;Execute TP | TE2, TE302
&emsp;&emsp;Fix found defects | PE9, PE10
&emsp;&emsp;Test fixed defects | TE2403, TE405
&emsp;**Documentation** | |
&emsp;&emsp;User documentation | DE1, DE105
&emsp;&emsp;**Review UD** | |
&emsp;&emsp;&emsp;Preparation for UD Review | DE203, DE204, DE205, DE206 | DE1, DE105 absent
&emsp;&emsp;&emsp;Review UD meeting | DE1, DE206, DE105, DE204, DE205 | DE1, DE105 returns
&emsp;&emsp;&emsp;Rework | DE1, DE105
&emsp;**Training material** | |
&emsp;&emsp;Tutorial | DE203 DE204
&emsp;&emsp;**Review tutorial** | |
&emsp;&emsp;&emsp;Preparation for tutorial review | DE1, DE105, DE205, DE206 | DE203, DE204 absent
&emsp;&emsp;&emsp;Review tutorial meeting | DE203, DE204, DE1, DE206, DE105 | DE203, DE204 returns
&emsp;&emsp;&emsp;Rework | DE203, DE204

## Problem 4

> What is the earliest finish date for this project if it is scheduled to start
  on **6/3/25?**

Based on the projection on Microsoft Project document, it is reasonable to
expect that the project will finish on **February 3, 2026**, exactly 8 months
after the start date.

## Problem 5

> Submit a single ZIP file that has MS-Project and PDF document report.

> Submit your MS Project File.

> Create PDF Document Report that has the following:

Included in this submission **hw1.zip**:

- Homework report: **hw1.md**
- Homework PDF conversion: **report.pdf**
- Microsoft Project file: **hw1.mpp**
- Microsoft Project PDF conversion: **output.pdf**
