# Save Image

![Save Image node](media/SaveImage.svg){ align=right width=450 }

The Save Image node can be used to save images. To simply preview an image inside the node graph use the [Preview Image](PreviewImage.md) node. To automatically insert the values of certain node widgets into the file name the following syntax can be used: `%node_name.widget_name%` e.g. if we wish to store images on a per resolution bases we could provide the node with the following string: `%Empty Latent Image.width%x%Empty Latent Image.height%/image`. For a more detailed look at this feature see [here](). TODO: make actual page about this and date feature (see https://github.com/comfyanonymous/ComfyUI/pull/321)


## inputs

`image`

:   The pixel image to preview.

`filename_prefix`

:   A prefix to put into the filename.


## outputs

This node has no outputs.

## example

example usage text with workflow image