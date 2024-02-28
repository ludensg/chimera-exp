# Implementing Experiment and Plotting Results with Chimera

## Overview
This guide outlines the process for profiling and visualizing the performance of BERT models using the Chimera framework.

## Steps

1. **Profiling with Nsight Systems**
   - Use `nsys_wrap.sh` to collect profiling data. This script is a wrapper for the main training script.

2. **SLURM Job for Profiling**
   - `prof_steps.sh` prepares the environment and parameters for BERT model training with Chimera, including GPU setup and profiling execution.

3. **Parsing Profiling Data**
   - `parse_nvtx_events.py` parses Nsight Systems generated SQLite files into Python pickle files, focusing on CUDA events timing information.

4. **Plotting the Timeline**
   - `plot_cuda_timeline.py` generates visual timelines from the parsed data, illustrating CUDA operations distribution across GPUs.

## Execution Workflow

- **Data Preparation**: Ensure dataset is preprocessed and accessible.
- **Training and Profiling**: Execute the SLURM job script (`prof_steps.sh`) to start training and profiling.
- **Data Parsing**: Use `parse_nvtx_events.py` for profiling data parsing.
- **Visualization**: Apply `plot_cuda_timeline.py` to create performance visualizations.

## Dependencies
- CUDA, PyTorch, NVIDIA Apex, Nsight Systems

## Note
Adjust script paths to your dataset and model configurations. Follow this workflow to analyze the performance of your BERT model training under the Chimera framework.
