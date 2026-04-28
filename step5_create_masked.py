"""
Step 5: Apply the block-letter mask to the stippled image (selection bias metaphor).
"""

import numpy as np


def create_masked_stipple(
    stipple_img: np.ndarray,
    mask_img: np.ndarray,
    threshold: float = 0.5,
) -> np.ndarray:
    """
    Remove stipple dots wherever the mask is dark (letter region).

    Parameters
    ----------
    stipple_img : np.ndarray
        Stippled image, shape (H, W), values in [0, 1]; dots are dark.
    mask_img : np.ndarray
        Mask with same shape; letter is dark (~0), background is light (~1).
    threshold : float
        Mask pixels strictly below this value are cleared to white (1.0).

    Returns
    -------
    np.ndarray
        Same shape as inputs; stipples inside the mask region set to 1.0.
    """
    result = stipple_img.copy()
    masked_region = mask_img < threshold
    result[masked_region] = 1.0
    return result
