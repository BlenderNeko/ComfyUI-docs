# Text Prompts

ComfyUI Provides a variety of ways to finetune your prompts to better reflect your intention.

## up and down weighting

The importance of parts of the prompt can be up or down-weighted by enclosing the specified part of the prompt in brackets using the following syntax: `(prompt:weight)`. E.g. if we have a prompt `flowers inside a blue vase` and we want the diffusion model to empathize the flowers we could try reformulating our prompt into: `(flowers:1.2) inside a blue vase`. Nested loops multiply the weights inside them, e.g. in the prompt `((flowers:1.2):.5) inside a blue vase` flowers end up with a weight of 0.6. Using only brackets without specifying a weight is shorthand for `(prompt:1.1)`, e.g. `(flower)` is equal to `(flower:1.1)`. To use brackets inside a prompt they have to be escaped, e.g. `\(1990\)`. ComfyUI can also add the appropriate weighting syntax for a selected part of the prompt via the keybinds ++ctrl+arrow-up++ and ++ctrl+arrow-down++. The amount by which these shortcuts up or down-weight can be adjusted in the settings.

## using textual inversion embeddings

Textual inversions are custom made CLIP embeddings that embody certain concepts. Textual inversions can be referenced inside a prompt by use the following syntax: `embedding:name` where name is the name of the embedding file.

## adding random choices

It is possible to let ComfyUI choose random parts of a prompt when it is queued up using the following syntax `{choice1|choice2|...}`. E.g. if we want ComfyUI to randomly select one of a set of colors we can add the following to our prompt: `{red|blue|yellow|green}`.