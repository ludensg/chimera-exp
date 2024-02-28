# Chimera Framework Experiments

This repository holds two experiments based on the Chimera Bidirectional Pipeline Paper. There are two main components:

1. **Main Experiment**: Located in the [chimera-eval](./chimera-eval) directory, this part of the repository contains the comprehensive experiment setup and results.
2. **Prior Experimental Test**: Located in the [test](./test/) directory, this is a preliminary test conducted to ensure the environment is correctly set up for the main experiment. Details can be found inside.

Additionally, the Chimera framework used in these experiments is sourced from their official repository, but the code in the [Chimera](./Chimera/) directory is changed to work in the HiperGator environment (mainly the using of different storages, the home storage for the code, and the blue storage for I/O). You can find the Chimera framework and its documentation here: [Chimera Repository](https://github.com/Shigangli/Chimera).


## 1. Comprehensive Experiment Proposal

### Objective
To demonstrate the effectiveness and efficiency of Chimera's parallel processing capabilities, focusing specifically on its scalability, the utilization of bidirectional pipelines, and the performance of its hybrid parallelism strategy.

### Experimental Setup
- **Models and Datasets:** Large-scale models like GPT-3 on common datasets.
- **Hardware Configuration:** A range of GPU configurations.
- **Chimera Configuration:** Tests for scalability, bidirectional pipeline efficiency, and hybrid parallelism.

### Metrics to Collect
- Throughput, GPU Utilization, Training Time, Memory Usage.

### Procedure
1. Establish baseline performance.
2. Conduct scalability tests with increasing GPUs.
3. Test bidirectional pipeline efficiency.
4. Evaluate hybrid parallelism performance.

### Data Analysis and Visualization
Compare throughput, training time, GPU utilization, and memory usage across configurations.

### Expected Outcomes
Demonstrate Chimera's superior scalability, efficiency, and performance benefits over traditional methods.

## 2. Simple Preliminary Experiment

### Objective
To validate the basic functionality of Chimera by training a small neural network model on HiPerGator.

### Experimental Setup
- **Model:** A simple CNN for image classification.
- **Dataset:** A small subset of CIFAR-10.
- **Hardware Configuration:** A small number of GPUs.
- **Chimera Configuration:** Focus on pipeline parallelism for a simple setup.

### Metrics to Collect
- Training Time, Throughput, Resource Utilization.

### Procedure
1. Setup the environment and prepare the model and dataset.
2. Configure Chimera for pipeline parallelism.
3. Execute the training and collect metrics.

### Expected Outcomes
- Successful training and reasonable model accuracy.
- Insight into resource utilization and scalability.
