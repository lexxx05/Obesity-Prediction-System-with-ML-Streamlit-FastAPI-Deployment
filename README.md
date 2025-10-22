# AutoEncoder for Enhancing Noisy Images

## Project Description
This project focuses on building and optimizing an AutoEncoder to remove Gaussian noise from images. The model learns to reconstruct clean images from noisy inputs using deep learning techniques and evaluates performance through SSIM metrics.

---

## Objective
- Add random Gaussian noise to images (mean = 0.0, std = 0.1).  
- Train an AutoEncoder to denoise the images.  
- Fine-tune the model to achieve the best Structural Similarity Index (SSIM) score.

---

## Dataset Information
- Total images: 1,074  
- Image dimension: 100x100 (1:1 ratio)  
- Most images are dark-colored with moderate exposure and balanced contrast.  
- Dataset verified for consistency through EDA before preprocessing.

---

## Methodology

### 1. Exploratory Data Analysis (EDA)
- Verified image dimensions and ratios.  
- Analyzed pixel intensity and color histogram distribution.  
- Determined preprocessing strategies such as resizing and normalization.

### 2. Preprocessing
- Resized and normalized all images.  
- Split data into training, validation, and testing sets.  
- Applied Gaussian noise to all sets for training robustness.

### 3. Modeling
**Base AutoEncoder:**
- Kernel size: 3x3  
- Activation: ReLU (Sigmoid for output)  
- Optimizer: Adam  
- Loss function: Mean Squared Error (MSE)

### 4. Model Modifications
**Version 1:** Added skip connections (similar to U-Net) to retain key information lost during downsampling.  
**Version 2:** Changed first layer kernel from 3x3 to 5x5 for higher sensitivity to noise patterns.  
Each version was evaluated using SSIM metrics.

---

## Results and Findings
- Skip connections improved reconstruction quality and reduced loss.  
- Larger kernels helped the model detect and remove complex noise.  
- Denoised outputs showed smoother and more natural image restoration.

---

## Conclusion
This project demonstrates how AutoEncoders can effectively learn to remove image noise. Architectural adjustments, such as skip connections and larger kernels, enhanced the SSIM score and overall image quality, validating the potential of deep learning in noise reduction tasks.
