# Chimera Framework Experiments

This repository holds two experiments based on the Chimera Bidirectional Pipeline Paper. There are two main components:

1. **Main Experiment**: Located in the [chimera-eval](./chimera-eval) directory, this part of the repository contains the comprehensive experiment setup and results.
2. **Prior Experimental Test**: Located in the [test](./test/) directory, this is a preliminary test conducted to ensure the environment is correctly set up for the main experiment. Details can be found inside.

Additionally, the Chimera framework used in these experiments is sourced from their official repository, but the code in the [Chimera](./Chimera/) directory is changed to work in the HiperGator environment (mainly the using of different storages, the home storage for the code, and the blue storage for I/O, as well the translation of some comments in the code that were originally in Chinese). You can find the Chimera framework and its documentation here: [Chimera Repository](https://github.com/Shigangli/Chimera).

The [utilities](./utilities/) directory only contains miscellaneous scripts used for particular tasks while working on this project.

NOTES: 
- This project also uses the NVidia's Apex library for training.
- Home storage used for code, blue storage for I/O, see [plot_cuda_timeline.sh](./chimera-mods-backup/plot_cuda_timeline.sh) and [prof_steps](./chimera-mods-backup/prof_steps.sh) for details.

## 1. Simple Preliminary Experiment - [test](./test/)

### Objective
To validate the basic functionality of Chimera by training a small model on HiPerGator.

### Metrics to Collect
- Training Time, Throughput, Resource Utilization.

### Expected Outcomes
- Successful training and reasonable model accuracy.
- Insight into resource utilization and scalability.


## 2. Comprehensive Experiment Proposal - [chimera-eval](./chimera-eval/)

### Objective
To demonstrate the effectiveness and efficiency of Chimera's parallel processing capabilities, focusing specifically on its scalability, the utilization of bidirectional pipelines, and the performance of its hybrid parallelism strategy.

### Metrics to Collect
- Throughput, GPU Utilization, Training Time, Memory Usage.

### Data Analysis and Visualization
Compare throughput, training time, GPU utilization, and memory usage across configurations.

### Expected Outcomes
Demonstrate Chimera's contributions in scalability, efficiency, and performance benefits over traditional methods.
