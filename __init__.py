from .nodes import EmptyLatentAspectPreset, EmptyLatentAspectByAxis

NODE_CLASS_MAPPINGS = {
    "Empty Latent (Aspect Ratio Preset)":      EmptyLatentAspectPreset,
    "Empty Latent (Aspect Ratio by Axis)":     EmptyLatentAspectByAxis,
}

NODE_DISPLAY_NAME = "ComfyUI Aspect Ratio Preset"