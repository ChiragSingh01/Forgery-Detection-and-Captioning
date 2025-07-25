# 🔍 Forgery Detection and Image Captioning using ELA, ViT, and BLIP-2

This repository contains a comprehensive solution for **detecting forged regions in images** and generating **context-aware captions** using:
- **Error Level Analysis (ELA)** for preprocessing,
- **Vision Transformer (ViT)** for feature extraction,
- **BLIP-2** for multimodal captioning.

---

## 📌 Features

- 🖼️ **Forgery Detection** using ELA heatmaps and ViT-based classification/localization
- 🧠 **Caption Generation** with BLIP-2 to describe manipulated content
- 📈 Supports CASIA 2.0 (training) and CASIA 1.0 (testing)
- 🚀 Compatible with GPU for efficient training/inference
- 📦 Modular, clean PyTorch code

---

## 🗂️ Project Structure

```bash
Forgery-Detection-and-Captioning/
├── data/                     # Dataset loading and preprocessing
├── models/                   # ViT + BLIP-2 model definitions
├── utils/                    # Helper functions (metrics, ELA, visualization)
├── output_dir/               # Training outputs (checkpoints, logs)
├── pretrained-weights/       # Pretrained weights (ViT, BLIP-2)
├── notebooks/                # Jupyter notebooks for demo/training
├── train.py                  # Main training script
├── evaluate.py               # Evaluation script
├── config.yaml               # Configuration file
└── README.md                 # You're here
