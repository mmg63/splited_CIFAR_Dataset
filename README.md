# splited_CIFAR_Dataset
Split CIFAR dataset to Train set, Valid set and test set based on your fragmentation need

This file is so as to split datasets which has not valid dataset to three different dataset such as trainset, validset and testset dataset.
I my opinion valid test need to set True the train properties too.
If you want use multiple workers on your dataset, I'm afraid that base on my experice this functions are unable to help you.
My function work with just one worker per DataLoader.

I hope this code would be helpfull for all you. Besides, I would appriciate if anyone can help me to sort out my issue in set num_worker more than zero.
