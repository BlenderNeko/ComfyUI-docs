# Load VAE

![Load VAE node](media/LoadVAE.svg){ align=right width=450 }

The Load VAE node can be used to load a specific VAE model, VAE models are used to encoding and decoding images to and from latent space. Although the [Load Checkpoint](LoadCheckpoint.md) node provides a VAE model alongside the diffusion model, sometimes it can be useful to use a specific VAE model.

## inputs

`vae_name`

:   The name of the VAE.

## outputs

`VAE`

:   The VAE model used for encoding and decoding images to and from latent space.

## example

example usage text with workflow image