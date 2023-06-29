---
hide:
  - footer
---

# Welcome to the ComfyUI Community Docs!

This is the community-maintained repository of documentation related to [ComfyUI](https://github.com/comfyanonymous/ComfyUI), a powerful and modular stable diffusion GUI and backend. 

The aim of this page is to get you up and running with ComfyUI, running your first gen, and providing some suggestions for the next steps to explore.

## Installation

We won't be covering the installation of ComfyUI in detail, as the project is under active development. Instead, refer to [the README.md on GitHub](https://github.com/comfyanonymous/ComfyUI) and find the sections that are relevant to your install (Linux, macOS or Windows). There's also an [open PR for `docker compose`](https://github.com/comfyanonymous/ComfyUI/pull/190/files) if that's more your speed.

### Downloading a model

If you're entirely new to anything Stable Diffusion-related, the first thing you'll want to do is grabbing a model _checkpoint_ that you will use to generate your images. 

!!! tip "Experienced Users"

    If you already have files (model checkpoints, embeddings etc), there's no need to re-download those. You can keep them in the same location and just tell Comfy where to find them. To do this, locate the file called `extra_model_paths.yaml.example`, rename it to `extra_model_paths.yaml`, then edit the relevant lines and restart Comfy. Once that's done, skip to the next section.

You can find a large variety of models on websites like [CivitAI](https://civitai.com/). To start, grab a model _checkpoint_ that you like (it'll have a `checkpoint` tag) and place it in `models/checkpoints` (create the directory if it doesn't exist yet), then re-start Comfy.

## First steps with Comfy

At this stage, you should have Comfy up and running in a browser tab. The default flow that's loaded is a good starting place to get familiar with, it should look something like this:

<figure markdown>
  ![ComfyUI Default Workflow](media/default_flow.png){ width=450 }
  <figcaption>ComfyUI Default Workflow (open in new tab for higher resolution)</figcaption>
</figure>

To navigate the canvas, you can either drag the canvas around, or hold spacebar and move your mouse. You can zoom by scrolling. 

!!! tip "Accidents happen"

    If you mess something up, just hit `Load Default` in the menu to reset it to the inital state.

Before we run our default flow, let's make a small modification to preview our testing gens without saving them:

1. Right-click on the `Save Image` node, then select `Remove`
1. Double-click on an empty part of the canvas, type in `preview`, then click on the `PreviewImage` option
1. Locate the `IMAGE` output of the `VAE Decode` node and connect it to the `images` input of the `Preview Image` node you just added

This modification will preview your gens without immediately saving them to disk. Don't worry, if really like a gen you can still right-click the image and choose `Save Image` (this will also save the entire flow details, including weight, seeds and more, inside of the PNG image)!

Run your first gen by clicking `Queue Prompt` on the menu, or hitting `Cmd / Ctrl + Enter` on your keyboard, and that's it!

## Next Steps
This page should have given you a good intial overview of how to get started with Comfy. Thanks to the node-based interface, you can build workflows consisting of dozens of nodes, all doing different things, allowing for some really neat genning pipelines. 

It's also likely that you now have a lot of questions of what just happened, what each node does, and "how do I do X thing?"-type questions. These should hopefully be answered in the rest of these docs.