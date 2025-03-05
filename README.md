# Wiener Filtering for Image Reconstruction  

This project was created as part of a course assignment for the **DIP (Digital Image Processing)** class at **ECE, AUTH University**.

This project explores the **Wiener filter** and its effectiveness in reconstructing degraded images.  

### **Overview**  
The Wiener filter is applied to two given images to evaluate how well it restores them after degradation. The images are artificially degraded by adding:  
- **Motion blur**  
- **Noise at a specified level**  

The results can be analyzed to determine how effectively the Wiener filter can reconstruct the images under different conditions. The Mean Squared Error (MSE) between the original and reconstructed images is also calculated for various values of **K** (a parameter of the Wiener filter).  


## **Files**  

- **`wiener_filtering.py`**: Implements the Wiener filtering algorithm for image reconstruction.  
- **`demo.py`**:  
  - Applies the Wiener filter to an image with added noise and motion blur.  
  - Computes the Mean Squared Error (MSE) for different **K** values.  
  - Outputs the original, degraded, and reconstructed images for visualization.  


## **Usage**  

Ensure your image file is named named input_img.png and is in the same directory as the scripts.  

Run the demo script:  
```bash
python demo.py
```

## **Future Work**

- Optimize the Wiener filter for adaptive noise levels.
- Experiment with different types of degradation beyond motion blur and noise.
- Implement the Wiener filter using the Discrete Fourier Transform (DFT) instead of the Fast Fourier Transform (FFT) for improved performance.
