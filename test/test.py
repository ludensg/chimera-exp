import subprocess
import os
import pandas as pd
import matplotlib.pyplot as plt

# Paths setup
chimera_script_path = "../Chimera/scripts/prof_steps.sh"
pytorch_dist_script_path = "./dist_training.sh"  # Path to the new PyTorch distributed training script
log_dir = "/blue/gtyson.fsu/dg16r.fsu/chimera-data/logs/"  # Log directory in the blue storage
os.makedirs(log_dir, exist_ok=True)

# Placeholder log file names
chimera_log_file = os.path.join(log_dir, "chimera_log.txt")
pytorch_dist_log_file = os.path.join(log_dir, "pytorch_dist_log.txt")

# Function to execute training scripts
def run_training(script_path, log_file_name):
    print(f"Executing training script: {script_path}")
    with open(log_file_name, "w") as log_file:
        subprocess.run(["sbatch", script_path], stdout=log_file)

# Function to read and parse log files
def parse_logs(log_file_name):
    # Placeholder for actual parsing logic
    # Assume log file structure with key metrics for simplicity
    data = pd.read_csv(log_file_name, sep=":", header=None, names=["Metric", "Value"])
    return data.set_index("Metric")["Value"]

# Function to plot performance metrics
def plot_metrics(chimera_metrics, pytorch_metrics):
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    
    # Plotting training time
    axs[0].bar(["Chimera", "PyTorch Distributed"], [chimera_metrics["Training Time"], pytorch_metrics["Training Time"]])
    axs[0].set_ylabel('Training Time (s)')
    axs[0].set_title('Training Time Comparison')

    # Plotting throughput
    axs[1].bar(["Chimera", "PyTorch Distributed"], [chimera_metrics["Throughput"], pytorch_metrics["Throughput"]])
    axs[1].set_ylabel('Throughput (samples/s)')
    axs[1].set_title('Throughput Comparison')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Execute training scripts and generate logs
    run_training(chimera_script_path, chimera_log_file)
    run_training(pytorch_dist_script_path, pytorch_dist_log_file)

    # Parse logs
    chimera_metrics = parse_logs(chimera_log_file)
    pytorch_metrics = parse_logs(pytorch_dist_log_file)

    # Plot metrics
    plot_metrics(chimera_metrics, pytorch_metrics)
