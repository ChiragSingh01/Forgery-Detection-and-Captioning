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
```
## 🧪 Dataset
### 📦 CASIA 2.0 & CASIA 1.0
All images undergo ELA transformation.

Model trained on tampered vs authentic images with region mask supervision.

## 🔧 Setup Instructions
### 1. Clone the repository
bash
```
git clone https://github.com/ChiragSingh01/Forgery-Detection-and-Captioning.git
cd Forgery-Detection-and-Captioning
```
### 2. Create a virtual environment
bash
```
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```
### 3. Install dependencies
bash
```
pip install -r requirements.txt
```
## 🧠 Model Architecture
ViT Backbone: For ELA-based visual feature learning

BLIP-2: Used for visual-linguistic alignment and captioning

Fusion Module: Combines visual embeddings and ELA signals

Losses: BCE Loss (region prediction), Captioning Loss (language generation)

## 💻 Usage
Train
```
bash
python train.py --config config.yaml
```
Evaluate
```
bash
python evaluate.py --checkpoint output_dir/best_model.pth
```
Visualize ELA
```
bash
python utils/ela_visualize.py --image path/to/image.jpg
```
## 🧾 Sample Output


## 📊 Metrics
Detection: F1 Score, IoU, Pixel Accuracy

Captioning: BLEU, METEOR, CIDEr

## 📦 Pretrained Weights
Place pretrained ViT/BLIP-2 weights in:
```
bash
pretrained-weights/
├── vit.pth
├── blip2.pth
```
You may use MAE or HuggingFace BLIP-2 weights depending on availability.

## 🙋‍♂️ Author
Chirag Singh
B.Tech IT | Delhi Technological University
📧 chiragsingh@example.com
🌐 LinkedIn | GitHub

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
