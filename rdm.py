import os
from scipy import io as sio
from scipy.spatial.distance import squareform
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm


class Rdm:
    def __init__(self, path):
        self.fpath = path
        self.file_name = os.path.join(self.fpath, 'submit_fmri.mat')
        self.data = squareform(self.loadmat(), force='tovector', checks=False)
        self.mean = self.find_mean()
        self.std = self.find_std()

    def loadmat(self):
        data = sio.loadmat(self.file_name)
        return data['EVC_RDMs']

    def find_mean(self):
        return np.mean(self.data)

    def find_std(self):
        return np.std(self.data)

    def analyse(self, k=5):
        min_idx = np.argpartition(self.data, k)[:k]
        max_idx = np.argpartition(self.data, -k)[-k:]

        min_data = self.data[min_idx]
        max_data = self.data[max_idx]
        self.plot(min_idx)
        self.plot(max_idx, is_min=False)
        min_std = (min_data - self.mean) // self.std
        max_std = (max_data - self.mean) // self.std

        path = os.path.join(self.fpath, 'analysis.txt')
        results = open(path, 'a+')
        results.write('Arch: {}, mean: {}, std: {}\n'.format(
            self.fpath.split('/')[-2], self.mean, self.std))
        results.write('Least 5 values: \n')
        for idx, val in enumerate(min_std):
            results.write('The value {} lies in range {}σ and {}σ\n'.format(
                min_data[idx], val, val + 1))
        results.write('Top 5 values: \n')
        for idx, val in enumerate(max_std):
            results.write('The value {} lies in range {}σ and {}σ\n'.format(
                max_data[idx], val, val + 1))
        results.close()

    def plot(self, data, is_min=True):
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(6, 3))
        image_set = self.fpath.split('/')[-3]

        for idx, item in enumerate(tqdm(data)):
            if image_set == '92':
                i = item // 92
                j = item % 92
            else:
                i = item // 118
                j = item % 118

            img1, img2 = self.get_img(i + 1, j + 1, image_set)
            fig.suptitle("RDM value: "+str(self.data[item]))
            axes[0].imshow(img1)
            axes[1].imshow(img2)
            if is_min:
                save_path = 'sim-{}.png'.format(idx)
            else:
                save_path = 'dis-{}.png'.format(idx)
            plt.savefig(os.path.join(self.fpath, save_path))
        plt.close(fig)

    def get_img(self, i, j, image_set):
        if image_set == '92':
            i = str(i) if i > 9 else '0' + str(i)
            j = str(j) if j > 9 else '0' + str(j)
        else:
            if i < 10:
                i = '00' + str(i)
            elif i < 100:
                i = '0' + str(i)
            else:
                i = str(i)

            if j < 10:
                j = '00' + str(j)
            elif j < 100:
                j = '0' + str(j)
            else:
                j = str(j)

        img1 = plt.imread(
            'data/{}images/image_{}.jpg'.format(image_set, i))
        img2 = plt.imread(
            'data/{}images/image_{}.jpg'.format(image_set, j))
        return img1, img2
