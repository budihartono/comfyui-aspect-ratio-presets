from .nodes import EmptyLatentAspectPreset, EmptyLatentAspectByAxis

NODE_CLASS_MAPPINGS = {
    "CAS Empty Latent Aspect Ratio from Preset":      EmptyLatentAspectPreset,
    "CAS Empty Latent Aspect Ratio by Axis":     EmptyLatentAspectByAxis,
}

NODE_DISPLAY_NAME = "latent"