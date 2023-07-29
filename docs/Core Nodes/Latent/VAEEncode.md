# VAE Encode

![VAE Encode node](media/VAEEncode.svg){ align=right width=450 }

The VAE Encode node can be used to encode pixel space images into latent space images, using the provided VAE.

## inputs

`pixels`

:   The pixel space images to be encoded.

`vae`

:   The VAE to use for encoding the pixel images.


## outputs

`LATENT`

:   The encoded latent images.

## example

In order to use images in e.g. image to image tasks, they first need to be encoded into latent space. In the below example the VAE encode node is used to convert a pixel image into a latent image so that we can re-and de-noise this image into something new.

<div style="overflow: hidden;">
<img src="../../media/img2imgExample.png" style="transform: scale(1.4) translate(15%, 0%);">
</div>