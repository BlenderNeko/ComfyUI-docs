# Conditioning

In ComfyUI Conditionings are used to guide the diffusion model to generate certain outputs. All conditionings start with a text prompt embedded by CLIP using a [Clip Text Encode](CLIPTextEncode.md) node. These conditions can then be further augmented or modified by the other nodes that can be found in this segment. 

Examples of such are guiding the process towards certain compositions using the [Conditioning (Set Area)](ConditioningSetArea.md), [Conditioning (Set Mask)](ConditioningSetArea.md), or [GLIGEN Textbox Apply](GLIGENTextboxApply.md) node.

Or providing additional visual hints through nodes such as the [Apply Style Model](ApplyStyleModel.md), [Apply ControlNet](ApplyControlNet.md) or [unCLIP Conditioning](unCLIPConditioning.md) node. A full list of relevant nodes can be found in the sidebar.