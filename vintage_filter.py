import cv2
import numpy as np

def apply_vintage_filter(image_path, output_path):
    # Read image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image at {image_path}")

    # Convert to float for calculations
    img = img.astype(np.float32) / 255.0

    # Step 1: Apply a sepia/vintage tone using a color matrix
    sepia_matrix = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])
    img_sepia = cv2.transform(img, sepia_matrix)
    img_sepia = np.clip(img_sepia, 0, 1)

    # Step 2: Reduce contrast slightly
    alpha = 0.85  # Contrast control
    beta = 0.05   # Brightness control
    img_vintage = img_sepia * alpha + beta
    img_vintage = np.clip(img_vintage, 0, 1)

    # Step 3: Add noise
    noise_strength = 0.03
    noise = np.random.randn(*img_vintage.shape) * noise_strength
    img_noisy = img_vintage + noise
    img_noisy = np.clip(img_noisy, 0, 1)

    # Step 4: Convert back to uint8
    img_out = (img_noisy * 255).astype(np.uint8)

    # Save the result
    cv2.imwrite(output_path, img_out)
    print(f"Vintage image saved to {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python vintage_filter.py input_image output_image")
        exit(1)
    apply_vintage_filter(sys.argv[1], sys.argv[2])
