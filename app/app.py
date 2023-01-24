# AUTOGENERATED! DO NOT EDIT! File to edit: ../04_ch_pt_2.ipynb.

# %% auto 0
__all__ = ['mnist_path', 'nines', 'sixes', 'nines_tens', 'sixes_tens', 'stacked_nines', 'stacked_sixes', 'mean_stacked_nines',
           'mean_stacked_sixes', 'im_9', 'im_6', 'train_x', 'train_y', 'dset', 'x', 'y', 'valid_x', 'valid_y',
           'valid_dset', 'bias', 'corrects', 'init_params', 'linear1']

# %% ../04_ch_pt_2.ipynb 2
from ipywidgets import interact
from fastai.vision import *
from fastbook import *

matplotlib.rc('image', cmap='Greys')
plt.rc('figure', dpi=90)


# %% ../04_ch_pt_2.ipynb 5
mnist_path = untar_data(URLs.MNIST)

# %% ../04_ch_pt_2.ipynb 6
Path.BASE_PATH = mnist_path

# %% ../04_ch_pt_2.ipynb 10
nines = (mnist_path/'training'/'9').ls().sorted()
sixes = (mnist_path/'training'/'6').ls().sorted()

# %% ../04_ch_pt_2.ipynb 15
nines_tens = [tensor(Image.open(o)) for o in nines]
sixes_tens = [tensor(Image.open(o)) for o in sixes]

# %% ../04_ch_pt_2.ipynb 17
stacked_nines = torch.stack(nines_tens).float()/255
stacked_sixes = torch.stack(sixes_tens).float()/255

# %% ../04_ch_pt_2.ipynb 20
mean_stacked_nines = stacked_nines.mean(0)
mean_stacked_sixes = stacked_sixes.mean(0)

# %% ../04_ch_pt_2.ipynb 23
im_9 = stacked_nines[2]
im_6 = stacked_sixes[2]

# %% ../04_ch_pt_2.ipynb 128
train_x = torch.cat([stacked_nines, stacked_sixes]).view(-1, 28*28)

# %% ../04_ch_pt_2.ipynb 130
train_y = tensor([1]*len(nines) + [0]*len(sixes)).unsqueeze(1)

# %% ../04_ch_pt_2.ipynb 138
dset = list(zip(train_x, train_y))
x,y = dset[0]

# %% ../04_ch_pt_2.ipynb 142
valid_x = torch.cat([valid_nines_tens, valid_sixes_tens]).view(-1,784)

# %% ../04_ch_pt_2.ipynb 144
valid_y = tensor([1]*len(valid_nines_tens) + [0]*len(valid_sixes_tens)).unsqueeze(1)

# %% ../04_ch_pt_2.ipynb 146
valid_dset = list(zip(valid_x, valid_y))

# %% ../04_ch_pt_2.ipynb 148
x, y = dset[0]

# %% ../04_ch_pt_2.ipynb 151
def init_params(size, std=1.0):
    return (torch.randn(size)*std).requires_grad_()

# %% ../04_ch_pt_2.ipynb 154
bias = init_params(1)

# %% ../04_ch_pt_2.ipynb 158
def linear1(xb):
    return xb@weights + bias

# %% ../04_ch_pt_2.ipynb 162
corrects = (preds>0.0).float() == train_y

