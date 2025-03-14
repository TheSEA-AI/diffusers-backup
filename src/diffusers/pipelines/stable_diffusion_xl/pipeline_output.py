from dataclasses import dataclass
from typing import List, Optional, Union # thesea modified for safty checker

import numpy as np
import PIL.Image

from ...utils import BaseOutput, is_flax_available

@dataclass
class StableDiffusionXLPipelineOutput(BaseOutput):
    """
    Output class for Stable Diffusion pipelines.

    Args:
        images (`List[PIL.Image.Image]` or `np.ndarray`)
            List of denoised PIL images of length `batch_size` or numpy array of shape `(batch_size, height, width,
            num_channels)`. PIL images or numpy array present the denoised images of the diffusion pipeline.
        nsfw_content_detected (`List[bool]`)
            List indicating whether the corresponding generated image contains "not-safe-for-work" (nsfw) content or
            `None` if safety checking could not be performed.
    """

    images: Union[List[PIL.Image.Image], np.ndarray]
    # thesea modified for safty checker
    nsfw_content_detected: Optional[List[bool]]


if is_flax_available():
    import flax

    @flax.struct.dataclass
    class FlaxStableDiffusionXLPipelineOutput(BaseOutput):
        """
        Output class for Flax Stable Diffusion XL pipelines.

        Args:
            images (`np.ndarray`)
                Array of shape `(batch_size, height, width, num_channels)` with images from the diffusion pipeline.
            nsfw_content_detected (`List[bool]`):
                List indicating whether the corresponding generated image contains "not-safe-for-work" (nsfw) content
                or `None` if safety checking could not be performed.
        """

        images: np.ndarray
        # thesea modified for safty checker
        nsfw_content_detected: Optional[List[bool]]
