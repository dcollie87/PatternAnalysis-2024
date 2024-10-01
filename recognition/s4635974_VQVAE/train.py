# Hyperparameters
batch_size = 32
lr = 0.0002
num_hiddens = 128
num_residual_hiddens = 32
num_chanels = 1
num_embeddings = 512
dim_embedding = 64

# In your train.py
from dataset import HipMRILoader
import torchvision.transforms as transforms

# Directories for datasets
train_dir = '/home/groups/comp3710/HipMRI_Study_open/keras_slices_data/keras_slices_train'
test_dir = '/home/groups/comp3710/HipMRI_Study_open/keras_slices_data/keras_slices_test'
validate_dir = '/home/groups/comp3710/HipMRI_Study_open/keras_slices_data/keras_slices_validate'

# Define your transformations
transform = transforms.Compose([
    transforms.ToTensor(),  # Convert numpy array to PyTorch tensor
    transforms.Normalize((0.5,), (0.5,)),  # Normalize to [-1, 1]
    transforms.RandomHorizontalFlip(),  # Random horizontal flip
    transforms.RandomRotation(15),  # Random rotation within 15 degrees
])

# Instantiate the data loader
data_loader = HipMRILoader(train_dir, validate_dir, test_dir, batch_size=128, transform=transform)

# Get the loaders
train_loader, validate_loader, test_loader = data_loader.get_loaders()