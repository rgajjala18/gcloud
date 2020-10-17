#!/bin/bash
python3 images.py
python3 image_to_bucket.py
GRN='\033[0;32m'
BLU='\033[0;34m'
NC='\033[0m' # No Color
printf "${BLU}status: ${GRN}success${NC}\n"