# Simple Preliminary Experiment with Chimera on HiPerGator using BERT

## Objective
To validate the basic functionality of Chimera by training a BERT model on a subset of data on HiPerGator.

## Experimental Setup

### Model
- BERT (Bidirectional Encoder Representations from Transformers) for a text classification task.

### Dataset
- A small subset of a text dataset compatible with BERT, such as a portion of the Wikipedia dataset provided by Chimera.

### Hardware Configuration
- Utilize a small number of GPUs on HiPerGator.

### Chimera Configuration
- Leverage pipeline parallelism to efficiently train BERT with a focus on a simple setup.

## Metrics to Collect
- **Training Time:** Total time taken for the model to train.
- **Throughput:** Number of text samples processed per second during training.
- **Resource Utilization:** GPU and memory utilization during the experiment.

## Procedure

1. **Setup the Environment and Prepare the Model and Dataset:**
   - Ensure Chimera and all dependencies, including NVIDIA's Apex library for PyTorch and NVIDIA Nsight Systems for profiling, are installed.
   - Use the provided script or instructions by Chimera to prepare a small subset of the Wikipedia dataset for BERT training.

2. **Configure Chimera for Pipeline Parallelism:**
   - Adjust Chimera's configuration to use a small number of stages and GPUs, appropriate for the scale of the experiment.

3. **Execute the Training and Collect Metrics:**
   - Run the training process using the SLURM workload manager, focusing on collecting training time, throughput, and resource utilization metrics.

## Expected Outcomes
- Successful training of the BERT model with reasonable accuracy on the subset dataset.
- Insights into the scalability and resource efficiency of using Chimera for training complex models like BERT on HiPerGator.

## Notes
- This experiment is intended as a preliminary test to validate Chimera's setup and functionality. Adjustments may be necessary based on the initial results and observations.
- Ensure that all paths to datasets, models, and output directories are correctly set according to the HiPerGator and Chimera documentation.
