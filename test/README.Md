# Simple Preliminary Experiment with Chimera on HiPerGator

## Objective
The objective of this experiment is to validate the basic functionality of Chimera by training a simple convolutional neural network (CNN) model for image classification on HiPerGator.

## Experimental Setup

### Model
- A simple CNN for image classification.

### Dataset
- A small subset of CIFAR-10.

### Hardware Configuration
- Utilize a small number of GPUs on HiPerGator.

### Chimera Configuration
- Focus on leveraging pipeline parallelism for a simple and efficient setup.

## Metrics to Collect
- **Training Time:** Total time taken for the model to train.
- **Throughput:** Number of images processed per second during training.
- **Resource Utilization:** GPU and memory utilization during the experiment.

## Procedure

1. **Setup the Environment and Prepare the Model and Dataset:**
   - Ensure Chimera and all dependencies are installed.
   - Prepare a small subset of CIFAR-10 for the experiment.

2. **Configure Chimera for Pipeline Parallelism:**
   - Configure Chimera to use pipeline parallelism tailored to the hardware configuration available on HiPerGator.

3. **Execute the Training and Collect Metrics:**
   - Run the training process using the configured setup.
   - Collect and document the metrics as defined above.

## Expected Outcomes
- The experiment should result in successful training of the model with reasonable accuracy.
- Provide insights into the efficiency of resource utilization and the scalability potential of the setup.

## Notes
- Ensure all paths and environment variables are correctly set up according to HiPerGator's documentation and Chimera's requirements.
- Adjust the number of GPUs and other parameters based on the available resources and experiment requirements.
