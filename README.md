# Vintage Filter Python Script

This Python script applies a "vintage" filter to images by adjusting their colors and adding noise, creating a classic retro effect.

## Features

- **Sepia Tone:** Applies a sepia color matrix for a vintage look.
- **Contrast Adjustment:** Slightly reduces contrast for authenticity.
- **Noise Addition:** Adds random noise for film grain effect.

## Requirements

- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/)
- [NumPy](https://pypi.org/project/numpy/)

Install dependencies:
```bash
pip install opencv-python numpy
```

## Usage

```bash
python vintage_filter.py input_image.jpg output_image.jpg
```

- `input_image.jpg`: Path to the input image.
- `output_image.jpg`: Path where the filtered image will be saved.

## Example

```bash
python vintage_filter.py sample.jpg sample_vintage.jpg
```

## How It Works

1. **Reads the image** from disk.
2. **Applies a sepia/vintage color transformation** using a matrix.
3. **Reduces contrast** and slightly increases brightness.
4. **Adds random noise** to simulate film grain.
5. **Saves the processed image** to the specified output path.

## License

MIT License
