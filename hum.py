import os
from scipy import io as sio
from scipy.spatial.distance import squareform
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
import h5py


def loadmat(matfile):
    try:
        f = h5py.File(matfile)
    except (IOError, OSError):
        return sio.loadmat(matfile)
    else:
        return {name: np.transpose(f.get(name)) for name in f.keys()}


def loadnpy(npyfile):
    return np.load(npyfile)


def load(data_file):
    root, ext = os.path.splitext(data_file)
    return {'.npy': loadnpy,
            '.mat': loadmat
            }.get(ext, loadnpy)(data_file)


def main(k=5):
    fmri_92 = load('humans/92/target_fmri.mat')
    fmri_118 = load('humans/118/target_fmri.mat')
    meg_92 = load('humans/92/target_meg.mat')
    meg_118 = load('humans/118/target_meg.mat')
    print(meg_118['MEG_RDMs_early'].mean(axis=1).mean(axis=0).shape)

    # fmri 92
    path = os.path.join('humans/92', 'fmri_92.txt')
    results = open(path, 'a+')
    results.write('EVC\nmean: {}, std: {}\n'.format(
        fmri_92['EVC_RDMs'].mean(), fmri_92['EVC_RDMs'].std()))
    sq_data = squareform(fmri_92['EVC_RDMs'].mean(
        axis=0), force='tovector', checks=False)
    min_idx = np.argpartition(sq_data, k)[:k]
    max_idx = np.argpartition(sq_data, -k)[-k:]

    min_data = sq_data[min_idx]
    max_data = sq_data[max_idx]
    min_std = (min_data - fmri_92['EVC_RDMs'].mean()
               ) // fmri_92['EVC_RDMs'].std()
    max_std = (max_data - fmri_92['EVC_RDMs'].mean()
               ) // fmri_92['EVC_RDMs'].std()
    results.write('Least 5 values: \n')
    for idx, val in enumerate(min_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            min_data[idx], val, val + 1))
    results.write('Top 5 values: \n')
    for idx, val in enumerate(max_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            max_data[idx], val, val + 1))

    results.write('IT\nmean: {}, std: {}\n'.format(
        fmri_92['IT_RDMs'].mean(), fmri_92['IT_RDMs'].std()))
    sq_data = squareform(fmri_92['IT_RDMs'].mean(
        axis=0), force='tovector', checks=False)
    min_idx = np.argpartition(sq_data, k)[:k]
    max_idx = np.argpartition(sq_data, -k)[-k:]

    min_data = sq_data[min_idx]
    max_data = sq_data[max_idx]
    min_std = (min_data - fmri_92['IT_RDMs'].mean()
               ) // fmri_92['IT_RDMs'].std()
    max_std = (max_data - fmri_92['IT_RDMs'].mean()
               ) // fmri_92['IT_RDMs'].std()
    results.write('Least 5 values: \n')
    for idx, val in enumerate(min_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            min_data[idx], val, val + 1))
    results.write('Top 5 values: \n')
    for idx, val in enumerate(max_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            max_data[idx], val, val + 1))
    results.close()

    # FMRI 118
    path = os.path.join('humans/118', 'fmri_118.txt')
    results = open(path, 'a+')
    results.write('EVC\nmean: {}, std: {}\n'.format(
        fmri_118['EVC_RDMs'].mean(), fmri_118['EVC_RDMs'].std()))
    sq_data = squareform(fmri_118['EVC_RDMs'].mean(
        axis=0), force='tovector', checks=False)
    min_idx = np.argpartition(sq_data, k)[:k]
    max_idx = np.argpartition(sq_data, -k)[-k:]

    min_data = sq_data[min_idx]
    max_data = sq_data[max_idx]
    min_std = (min_data - fmri_118['EVC_RDMs'].mean()
               ) // fmri_118['EVC_RDMs'].std()
    max_std = (max_data - fmri_118['EVC_RDMs'].mean()
               ) // fmri_118['EVC_RDMs'].std()
    results.write('Least 5 values: \n')
    for idx, val in enumerate(min_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            min_data[idx], val, val + 1))
    results.write('Top 5 values: \n')
    for idx, val in enumerate(max_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            max_data[idx], val, val + 1))

    results.write('IT\nmean: {}, std: {}\n'.format(
        fmri_118['IT_RDMs'].mean(), fmri_118['IT_RDMs'].std()))
    sq_data = squareform(fmri_118['IT_RDMs'].mean(
        axis=0), force='tovector', checks=False)
    min_idx = np.argpartition(sq_data, k)[:k]
    max_idx = np.argpartition(sq_data, -k)[-k:]

    min_data = sq_data[min_idx]
    max_data = sq_data[max_idx]
    min_std = (min_data - fmri_118['IT_RDMs'].mean()
               ) // fmri_118['IT_RDMs'].std()
    max_std = (max_data - fmri_118['IT_RDMs'].mean()
               ) // fmri_118['IT_RDMs'].std()
    results.write('Least 5 values: \n')
    for idx, val in enumerate(min_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            min_data[idx], val, val + 1))
    results.write('Top 5 values: \n')
    for idx, val in enumerate(max_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            max_data[idx], val, val + 1))
    results.close()

    # meg 92
    path = os.path.join('humans/92', 'meg_92.txt')
    results = open(path, 'a+')
    results.write('EVC\nmean: {}, std: {}\n'.format(
        meg_92['MEG_RDMs_early'].mean(), meg_92['MEG_RDMs_early'].std()))
    sq_data = squareform(meg_92['MEG_RDMs_early'].mean(
        axis=0).mean(axis=0), force='tovector', checks=False)
    min_idx = np.argpartition(sq_data, k)[:k]
    max_idx = np.argpartition(sq_data, -k)[-k:]

    min_data = sq_data[min_idx]
    max_data = sq_data[max_idx]
    min_std = (min_data - meg_92['MEG_RDMs_early'].mean()
               ) // meg_92['MEG_RDMs_early'].std()
    max_std = (max_data - meg_92['MEG_RDMs_early'].mean()
               ) // meg_92['MEG_RDMs_early'].std()
    results.write('Least 5 values: \n')
    for idx, val in enumerate(min_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            min_data[idx], val, val + 1))
    results.write('Top 5 values: \n')
    for idx, val in enumerate(max_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            max_data[idx], val, val + 1))

    results.write('IT\nmean: {}, std: {}\n'.format(
        meg_92['MEG_RDMs_late'].mean(), meg_92['MEG_RDMs_late'].std()))
    sq_data = squareform(meg_92['MEG_RDMs_late'].mean(
        axis=0).mean(axis=0), force='tovector', checks=False)
    min_idx = np.argpartition(sq_data, k)[:k]
    max_idx = np.argpartition(sq_data, -k)[-k:]

    min_data = sq_data[min_idx]
    max_data = sq_data[max_idx]
    min_std = (min_data - meg_92['MEG_RDMs_late'].mean()
               ) // meg_92['MEG_RDMs_late'].std()
    max_std = (max_data - meg_92['MEG_RDMs_late'].mean()
               ) // meg_92['MEG_RDMs_late'].std()
    results.write('Least 5 values: \n')
    for idx, val in enumerate(min_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            min_data[idx], val, val + 1))
    results.write('Top 5 values: \n')
    for idx, val in enumerate(max_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            max_data[idx], val, val + 1))
    results.close()

    # meg 118
    path = os.path.join('humans/118', 'meg_118.txt')
    results = open(path, 'a+')
    results.write('EVC\nmean: {}, std: {}\n'.format(
        meg_118['MEG_RDMs_early'].mean(), meg_118['MEG_RDMs_early'].std()))
    sq_data = squareform(meg_118['MEG_RDMs_early'].mean(
        axis=0).mean(axis=0), force='tovector', checks=False)
    min_idx = np.argpartition(sq_data, k)[:k]
    max_idx = np.argpartition(sq_data, -k)[-k:]

    min_data = sq_data[min_idx]
    max_data = sq_data[max_idx]
    min_std = (min_data - meg_118['MEG_RDMs_early'].mean()
               ) // meg_118['MEG_RDMs_early'].std()
    max_std = (max_data - meg_118['MEG_RDMs_early'].mean()
               ) // meg_118['MEG_RDMs_early'].std()
    results.write('Least 5 values: \n')
    for idx, val in enumerate(min_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            min_data[idx], val, val + 1))
    results.write('Top 5 values: \n')
    for idx, val in enumerate(max_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            max_data[idx], val, val + 1))

    results.write('IT\nmean: {}, std: {}\n'.format(
        meg_118['MEG_RDMs_late'].mean(), meg_118['MEG_RDMs_late'].std()))
    sq_data = squareform(meg_118['MEG_RDMs_late'].mean(
        axis=0).mean(axis=0), force='tovector', checks=False)
    min_idx = np.argpartition(sq_data, k)[:k]
    max_idx = np.argpartition(sq_data, -k)[-k:]

    min_data = sq_data[min_idx]
    max_data = sq_data[max_idx]
    min_std = (min_data - meg_118['MEG_RDMs_late'].mean()
               ) // meg_118['MEG_RDMs_late'].std()
    max_std = (max_data - meg_118['MEG_RDMs_late'].mean()
               ) // meg_118['MEG_RDMs_late'].std()
    results.write('Least 5 values: \n')
    for idx, val in enumerate(min_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            min_data[idx], val, val + 1))
    results.write('Top 5 values: \n')
    for idx, val in enumerate(max_std):
        results.write('The value {} lies in range {}σ and {}σ\n'.format(
            max_data[idx], val, val + 1))
    results.close()


if __name__ == '__main__':
    main()
