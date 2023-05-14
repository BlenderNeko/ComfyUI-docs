# Writing Style Guide

below the writing style guide of the [Blender manual](https://docs.blender.org/manual/en/latest/contribute/guides/writing_guide.html), adapted for this project.

## Primary Goals

The main goals for this manual are as follows:

`User Focused`

:   The Manual is written for people with a basic understanding of using Stable Diffusion in currently available software with a basic grasp of node based programming. While some areas of machine learning and generative models are highly technical, this manual shall be kept understandable by non-technical users.

`Complete`

:    The manual provides detailed functional description of all nodes and features in ComfyUI. For each node or feature the manual should provide information on how to use it, and its purpose. More background information should be provided when necessary to give deeper understanding of the generative process.

`Concise`

:    Machine Learning is an incredibly interesting field, however, expanding into details can add unnecessary content. Keep the text concise, relevant to the topic at hand and factual.

`Maintainable`

:    Keep in mind that ComfyUI has frequent updates, so try to write content that will not have to be redone the moment some small change is made.

## Content Guidelines

In order to maintain a consistent writing style within the manual, please keep this page in mind and only deviate from it when you have a good reason to do so.

Rules of thumb:

- Spell checking is strongly recommended.
- Use American English.
- Take care about grammar, appropriate wording and use simple English.
- Keep sentences short and clear, resulting in text that is easy to read, objective and to the point.
- If you are unsure about how a feature works, ask someone else or find out who developed it and ask them.

To be avoided:

- Avoid writing in first person perspective, about yourself or your own opinions.
- Avoid [weasel words](https://en.wikipedia.org/wiki/Weasel_word) and being unnecessarily vague.
- Avoid documenting bugs. 
- Avoid product placements, i.e. unnecessarily promoting specific models. Keep content neutral where possible.
- Avoid technical explanations about the mathematical/algorithmic implementation of a feature if there is a simpler way to explain it.
- Avoid repetition of large portions of text. Simply explain it once, and from then on refer to that explanation.

# Screenshot Guidelines

Individual nodes shall be captured using the [Workflow SVG script](https://github.com/pythongosssss/ComfyUI-Custom-Scripts/tree/main), and sliced to a width of 400 pixels. These nodes shall be of the default width and using the default dark mode theme.

Images displaying example workflows shall clearly display the nodes in question and contain the workflow as part of their meta-data such that users can easily access the workflows. Workflows shall not be presented to users in the form of a json file, or as output images of a prompt.