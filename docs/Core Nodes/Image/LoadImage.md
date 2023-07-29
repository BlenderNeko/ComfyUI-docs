# Load Image

![Load Image node](media/LoadImage.svg){ align=right width=450 }

The Load Image node can be used to to load an image. Images can be uploaded by starting the file dialog or by dropping an image onto the node. Once the image has been uploaded they can be selected inside the node.

!!! info
    by default images will be uploaded to the input folder of ComfyUI

## inputs

`image`

:   The name of the image to use.


## outputs

`IMAGE`

:   The pixel image.

`MASK`

:   The alpha channel of the image.

## example

In order to perform image to image generations you have to load the image with the load image node. In the example below an image is loaded using the load image node, and is then encoded to latent space with a [VAE encode](../Latent/VAEEncode.md) node, letting us perform image to image tasks.

(TODO: provide different example using mask)

<div style="overflow: hidden;">
<img src="../../media/img2imgExample.png" style="transform: scale(1.4) translate(15%, 0%);">
</div>