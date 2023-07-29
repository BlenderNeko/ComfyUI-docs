# KSampler

![KSampler node](media/KSampler.svg){ align=right width=450 }

The KSampler uses the provided model and positive and negative conditioning to generate a new version of the given latent. First the latent is noised up according to the given `seed` and `denoise` strength, erasing some of the latent image. then this noise is removed using the given `Model` and the `positive` and `negative` conditioning as guidance, "dreaming" up new details in places where the image was erased by noise.

## inputs

`Model`

:   The model used for denoising

`Positive`

:   The positive conditioning.

`Negative`

:   The negative conditioning.

`latent_image`

:   The latent that will be denoised.

`seed`

:   The random seed used in creating the noise.

`control_after_generate`

:   Provides the ability to change the seed number described above after each prompt. the node can `randomize`, `increment`, `decrement` or keep the seed number `fixed`.

`steps`

:   The number of steps to use during denoising. The more steps the sampler is allowed to make the more accurate the result will be. See the [samplers](samplers.md) page for good guidelines on how to pick an appropriate number of steps.

`cfg`

:   The classifier free guidance(cfg) scale determines how aggressive the sampler should be in realizing the content of the prompts in the final image. Higher scales force the image to better represent the prompt, but a scale that is set too high will negatively impact the quality of the image.

`sampler_name`

:   Which sampler to use, see the [samplers](samplers.md) page for more details on the available samplers.

`scheduler`

:   The type of schedule to use, see the [samplers](samplers.md) page for more details on the available schedules.

`denoise`

:   How much information of the latents should be erased by noise.


## outputs

`LATENT`

:   the denoised latent.

## example

The KSampler is the core of any workflow and can be used to perform text to image and image to image generation tasks. The example below shows how to use the KSampler in an image to image task, by connecting a model, a positive and negative embedding, and a latent image. Note that we use a denoise value of less than 1.0. This way parts of the original image are preserved when it is noised up, guiding the denoising process to similar looking images.

<div style="overflow: hidden;">
<img src="../../media/img2imgExample.png" style="transform: scale(1.2) translate(-5%, 15%);">
</div>