# __init__.py

from .nodes import empty_latent_preset, empty_latent_by_axis

NODE_CLASS_MAPPINGS = {
    "Empty Latent (Aspect Ratio Preset)": empty_latent_preset,
    "Empty Latent (Aspect Ratio by Axis)": empty_latent_by_axis,
}

NODE_DISPLAY_NAME = "ComfyUI Aspect Ratio Preset"