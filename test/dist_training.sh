#!/bin/bash
#SBATCH --job-name=pytorch_dist_training
#SBATCH --output=dist_training_%j.log
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --mem=4G
#SBATCH --time=01:00:00

module load python/3.8 cuda/11.0 cudnn/8.0.4
source /chimera-exp/chimera-env/bin/activate

srun python ./dist_train.py
