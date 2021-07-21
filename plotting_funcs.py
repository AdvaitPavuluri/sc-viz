import matplotlib.pyplot as plt

def _preflight_check(adata, coordinate_space):
    """"""
    assert coordinate_space is in adata.obsm_keys(), "Please choose from {}".format(adata.obsm_keys())

def plot_subset(adata, cell_index, coordinate_space='X_emb', labels=["monocytes","neutrophils"], color=["blue", "red"], alpha=0.2):
    """
    Function for plotting a subset of cells from AnnData (adata).
    Parameters:
    -----------
    adata [required]
        AnnData object. Documentation: https://anndata.readthedocs.io/en/latest/
    cell_index [required]
        type: numpy array or list
    coordinate_space [required]
        The choice of embedding. Should be found in adata.obsm_keys()
    """
    _preflight_check(adata, coordinate_space)
    emb = adata.obsm[coordinate_space]
    for subset_index in cell_index:
        x_emb, y_emb = emb[subset_index]
        plt.scatter(x_emb, y_emb, c=color, alpha=alpha, label=None)
    plt.legend()