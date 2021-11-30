import argparse

import matplotlib as mpl
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np


def plot_hist2d_heatmap(points, cmap, bins=500):
    """Plot points density heatmap.

    Parameters
    ----------
    points : np.ndarray of shape (n_points, 2)
        2-dimensional points.
    cmap : str
        Colormap available in `plt.colormaps()`.
    bins : int or [int, int]
        Number of bins in each dimension.
    """
    fig, ax = plt.subplots()
    *_, hist = ax.hist2d(
        x=points[:, 0],
        y=points[:, 1],
        cmap=cmap,
        bins=bins,
        norm=mcolors.LogNorm(),
    )

    cbar = fig.colorbar(hist, ax=ax, label='Density')
    density = cbar.get_ticks()
    cbar.mappable.set_clim(density.min(), density.max())

    ax.set_xlim(0, 1)
    ax.set_xticks(np.arange(0, 1.1, 0.1))
    ax.set_xlabel('Entropy ($H$)')
    ax.set_ylim(0, 90)
    ax.set_yticks(np.arange(0, 100, 10))
    ax.set_yticklabels([rf'${i}^\circ$' for i in np.arange(0, 100, 10)])
    ax.set_ylabel(r'Angle ($\alpha$)')
    ax.set_title(cmap)
    ax.set_frame_on(False)

    ax.set_aspect(1 / ax.get_data_ratio())
    plt.savefig(f'{cmap}.png', transparent=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Demo about how to plot hist2d heatmap.')
    parser.add_argument('--cmap',
                        type=str,
                        default='tab20b',
                        help='colormap available in `plt.colormaps()`, set to `tab20b` by default')
    parser.add_argument('--text-color',
                        type=str,
                        default='#777777',
                        help='hex color code of figure text, set to gray by default')
    args = parser.parse_args()

    color = args.text_color
    mpl.rcParams['text.color'] = color
    mpl.rcParams['axes.labelcolor'] = color
    mpl.rcParams['xtick.color'] = color
    mpl.rcParams['ytick.color'] = color

    points = np.load('points.npy')
    plot_hist2d_heatmap(points, cmap=args.cmap)
