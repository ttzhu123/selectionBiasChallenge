"""
Assemble the four-panel statistics meme (Reality → Model → Selection Bias → Estimate).
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyArrowPatch


def create_statistics_meme(
    original_img: np.ndarray,
    stipple_img: np.ndarray,
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str,
    dpi: int = 150,
    background_color: str = "white",
) -> None:
    """
    Assemble four panels into a professional statistics meme PNG.

    Parameters
    ----------
    original_img : np.ndarray
        Grayscale array for the "Reality" panel.
    stipple_img : np.ndarray
        Stippled array for the "Your Model" panel.
    block_letter_img : np.ndarray
        Block letter for the "Selection Bias" panel.
    masked_stipple_img : np.ndarray
        Masked stipple for the "Estimate" panel.
    output_path : str
        Path to write the PNG.
    dpi : int
        Output resolution (default 150).
    background_color : str
        Figure face color (default "white").
    """
    panels = [original_img, stipple_img, block_letter_img, masked_stipple_img]
    labels = ["Reality", "Your Model", "Selection Bias", "Estimate"]

    fig = plt.figure(figsize=(18, 5.5), facecolor=background_color)
    fig.suptitle(
        "Statistics Meme: Selection Bias & Missing Data",
        fontsize=18,
        fontweight="bold",
        y=1.01,
        color="#222222",
    )

    gs = gridspec.GridSpec(
        1,
        4,
        figure=fig,
        left=0.03,
        right=0.97,
        top=0.88,
        bottom=0.08,
        wspace=0.06,
    )

    for i, (panel, label) in enumerate(zip(panels, labels)):
        ax = fig.add_subplot(gs[0, i])
        ax.imshow(panel, cmap="gray", vmin=0, vmax=1, aspect="equal")
        ax.axis("off")

        ax.text(
            0.04,
            0.97,
            str(i + 1),
            transform=ax.transAxes,
            fontsize=13,
            fontweight="bold",
            color="white",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#444444", edgecolor="none"),
            va="top",
            ha="left",
        )

        ax.set_title(
            label,
            fontsize=14,
            fontweight="bold",
            color="#111111",
            pad=7,
            loc="center",
        )

        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_edgecolor("#cccccc")
            spine.set_linewidth(1)

    # FancyArrowPatch: Figure has no .annotate() on some matplotlib versions
    for i in range(3):
        ax_left = fig.axes[i]
        ax_right = fig.axes[i + 1]
        pos_l = ax_left.get_position()
        pos_r = ax_right.get_position()
        x_left = pos_l.x1
        x_right = pos_r.x0
        y_mid = (pos_l.y0 + pos_l.y1) / 2
        arr = FancyArrowPatch(
            (x_left, y_mid),
            (x_right, y_mid),
            transform=fig.transFigure,
            arrowstyle="->",
            color="#888888",
            linewidth=1.5,
            mutation_scale=12,
            clip_on=False,
        )
        fig.add_artist(arr)

    plt.savefig(
        output_path,
        dpi=dpi,
        bbox_inches="tight",
        facecolor=background_color,
        edgecolor="none",
    )
    plt.close(fig)
    print(f"✅ Meme saved to: {output_path}")
