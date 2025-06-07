# comfyui-aspect-ratio-presets/__init__.py

from .nodes import empty_latent_preset, empty_latent_by_axis

NODE_CLASS_MAPPINGS = {
    # Display name : Python callable
    "Empty Latent (Aspect Ratio Preset)": empty_latent_preset,
    "Empty Latent (Aspect Ratio by Axis)":   empty_latent_by_axis,
}

# This is the category under which they appear in the ComfyUI UI
NODE_DISPLAY_NAME = "ComfyUI Aspect Ratio Preset"