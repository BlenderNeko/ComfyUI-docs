# Templates

The following guide provides patterns for core and custom nodes.

## Node Pages

Pages about nodes should always start with a brief explanation and image of the node. This is followed by two headings, inputs and outputs, with a note of absence if the node has none. At the end of the page can be an optional example(s) section:


``` md
# Node Name

![KSampler node](media/KSampler.png){ align=right width=450 }

Short description and explanation of the node

## inputs

`Lorem ipsum dolor sit amet`

:   Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus
    tellus non sem sollicitudin, quis rutrum leo facilisis.

`Cras arcu libero`

:   Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin
    ut eros sed sapien ullamcorper consequat. Nunc ligula ante.

    Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
    Nam vulputate tincidunt fringilla.
    Nullam dignissim ultrices urna non auctor.

## outputs

This node has no outputs.

## example

example usage text with workflow image
```

Examples Should be short, simple and not rely on custom nodes other than those in the nodepack to which the node on the manual page belongs to. Examples should come with an image that displays how the node fits into the example workflow, and the metadata of this image should encode the workflow depicted.

<!---
custom node packs, where to place them and tags (probably on another page?)
-->