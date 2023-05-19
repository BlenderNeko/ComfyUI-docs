# CLIP Text Encode (Prompt)

![CLIP Text Encode (Prompt) node](media/CLIPTextEncodePrompt.svg){ align=right width=450 }

The CLIP Text Encode node can be used to encode a text prompt using a CLIP model into an embedding that can be used to guide the diffusion model towards generating specific images.

The importance of parts of the prompt can be up or downweighted by enclosing the specified part of the prompt in brackets using the following syntax: `(prompt:weight)`. E.g. if we have a prompt `flowers inside a blue vase` and we want the diffusion model to empathize the flowers we could try reformulating our prompt into: `(flowers:1.2) inside a blue vase`. Nested loops multiply the weights inside them, e.g. in the prompt `((flowers:1.2):.5) inside a blue vase` flowers end up with a weight of 0.6. Using only brackets without specifying a weight is shorthand for `(prompt:1.1)`, e.g. `(flower)` is equal to `(flower:1.1)`. To use brackets inside a prompt they have to be escaped, e.g. `\(1990\)`. ComfyUI can also add the appropriate weighting syntax for a selected part of the prompt via the keybinds ++ctrl+arrow-up++ and ++ctrl+arrow-down++.

It is also possible to use textual inversions inside a prompt. Textual inversions are custom made CLIP embeddings that embody certain concepts. Textual inversions can be referenced inside a prompt by use the following syntax: `embedding:name` where name is the name of the embedding file.


## inputs

`clip`

:   The CLIP model used for encoding the text.

`text`

:   The text to be encoded.

## outputs

`CONDITIONING`

:   A Conditioning containing the embedded text used to guide the diffusion model.

## example

example usage text with workflow image