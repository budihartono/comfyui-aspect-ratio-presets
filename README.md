# ComfyUI Aspect Ratio Presets

Two custom ComfyUI nodes to kick-start your latent workflows:

* **Empty Latent (Aspect Ratio Preset)**
  Choose from a curated list of popular model resolutions and aspect ratios.

* **Empty Latent (Aspect Ratio by Axis)**
  Specify one dimension and an X\:Y ratio; the node computes the other side automatically.

---

## Features

* **Preset Mode**: Dropdown of Standard Diffusion, SDXL, Flux/HiD, HiDream resolutions.
* **Axis Mode**: Enter a “primary dimension” (width or height) plus any common aspect ratio (1:1, 3:2, 16:9, 21:9, etc.).
* **Validation**: Enforces positive values divisible by 8 to match VAE down-sampling.
* **Batch Support**: Produce multiple blank latents in one go.
* **Tooltips**: In-UI guidance for each parameter.

---

## Installation

1. Clone into your ComfyUI `custom_nodes/` directory:

   ```bash
   git clone https://github.com/yourusername/comfyui-aspect-ratio-presets.git
   ```
2. (Optional) Install dependencies:

   ```bash
   pip install -r custom_nodes/comfyui-aspect-ratio-presets/requirements.txt
   ```
3. Restart ComfyUI. The new nodes appear under **ComfyUI Aspect Ratio Preset**.

---

## Usage

1. **Empty Latent (Aspect Ratio Preset)**

   * Open the node and pick a resolution like `SDXL 1152×768 (3:2 Landscape)`.
   * Set your batch size (default 1).
   * Connect the output into your generation graph.

2. **Empty Latent (Aspect Ratio by Axis)**

   * Enter a primary value (e.g. `1024`) and choose whether that’s your **Width** or **Height**.
   * Select an aspect ratio label (e.g. `16:9 Landscape`).
   * Adjust batch size if needed.
   * Use the output tensor as a blank latent canvas.

---

## Presets

All built-in presets live in `presets.py` and follow the format:

```
(Model name, "X:Y Orientation", width, height)
```

Feel free to extend or override this list in your fork.

---

## License

This project is released under the [MIT License](LICENSE). Feel free to use, modify, and redistribute!
