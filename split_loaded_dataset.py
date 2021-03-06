from torchvision import transforms, datasets
from torch.utils.data import SubsetRandomSampler, DataLoader
import numpy as np

def load_train_valid_loader(data_dir='CIFAR10',
                            batch_size=16,
                            random_seed=1,
                            valid_size=0.9,
                            shuffle=True,
                            pin_memory=False,
                            download_allowed=True):
    r"""written by: Mustafa Mohammadi
    After creating Dataset, you can benefit from iter(..) function to load data/valid set batch wise:

    :param data_dir: dataset path
    :param batch_size: int
    :param random_seed: int
    :param valid_size: [0.0, 1.0]; between 0 to 1
    :param shuffle: boolean
    :param num_workers: int = should be 0 for spiliting the dataset( in my experiences)
    :param pin_memory: boolean. it's used for GPU
    :param download_allowed: boolean
    :return: trainset and validset loader
    """
    num_workers = 0
    transform = transforms.Compose([transforms.ToTensor(),
                                    transforms.Normalize((0.5, 0.5, 0.5),
                                                         (0.5, 0.5, 0.5))])

    train_dataset = datasets.CIFAR10(root=data_dir, train=True, transform=transform, download=download_allowed)
    valid_dataset = datasets.CIFAR10(root=data_dir, train=True, transform=transform, download=download_allowed)

    num_train = len(train_dataset)
    indices = list(range(num_train))
    spilit = int(np.floor(num_train * valid_size))

    if shuffle:
        np.random.seed(random_seed)
        np.random.shuffle(indices)

    train_idx = indices[spilit:]
    valid_idx = indices[:spilit]

    train_sampler = SubsetRandomSampler(indices=train_idx)
    valid_sampler = SubsetRandomSampler(indices=valid_idx)

    train_loader = DataLoader(dataset=train_dataset,
                                               batch_size=batch_size,
                                               shuffle=False,
                                               sampler=train_sampler,
                                               num_workers=num_workers,
                                               pin_memory=pin_memory)
    valid_loader = DataLoader(dataset=valid_dataset,
                                               batch_size=batch_size,
                                               shuffle=False,
                                               sampler=valid_sampler,
                                               num_workers=num_workers,
                                               pin_memory=pin_memory)

    return train_loader, valid_loader


def load_test_loader(data_dir='CIFAR10',
                     batch_size=16,
                     shuffle=True,
                     pin_memory=False):
    transform = transforms.Compose([transforms.ToTensor(),
                                    transforms.Normalize((0.5, 0.5, 0.5),
                                                         (0.5, 0.5, 0.5))])
    num_workers = 0

    dataset = datasets.CIFAR10(root=data_dir,
                               train=False,
                               download=True,
                               transform=transform)

    data_loader = DataLoader(dataset=dataset,
                                              batch_size=batch_size,
                                              shuffle=shuffle,
                                              num_workers=num_workers,
                                              pin_memory=pin_memory)

    return data_loader

dataset_path = 'CIFAR10'
trainset, validset = load_train_valid_loader(data_dir=dataset_path, batch_size=256, random_seed=1,
                                             valid_size=0.9, shuffle=False, pin_memory=False,
                                             download_allowed=True)

dataiter = iter(trainset)
for i in enumerate(dataiter):
    samples, labels = dataiter.next()
    print(samples.shape)
    print(labels.shape)
