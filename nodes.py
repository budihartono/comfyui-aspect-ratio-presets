# nodes.py

import numpy as np
from .presets import PRESETS

# ─── Helpers ──────────────────────────────────────────────────────────

def _validate_dim(v: int):
    if v <= 0:
        raise ValueError("Dimension must be > 0")
    if v % 8 != 0:
        raise ValueError("Dimension must be divisible by 8")

# ─── Node 1: Preset ───────────────────────────────────────────────────

def empty_latent_preset(
    preset:     str,
    batch_size: int
) -> np.ndarray:
    """
    Empty Latent (Aspect Ratio Preset)

    preset:     e.g. "512x512 - 1:1 SD 1.5"
    batch_size: how many latents to produce
    """
    # find matching entry
    for model, lbl, W, H in PRESETS:
        key = f"{W}x{H} - {lbl.split()[0]} {model}"
        if key == preset:
            break
    else:
        raise ValueError(f"Unknown preset: {preset}")

    _validate_dim(W); _validate_dim(H)
    return np.zeros((batch_size, 4, H // 8, W // 8), dtype=np.float32)


def _preset_input_types():
    # Build the list of dropdown labels:
    choices = [
        f"{W}x{H} - {lbl.split()[0]} {model}"
        for model, lbl, W, H in PRESETS
    ]
    return {
        "required": {
            # A true dropdown of strings:
            "preset": (choices,),
            "batch_size": ("INT", {"default": 1, "min": 1})
        }
    }

empty_latent_preset.INPUT_TYPES  = _preset_input_types
empty_latent_preset.RETURN_TYPES = ("LATENT",)
empty_latent_preset.CATEGORY     = "ComfyUI Aspect Ratio Preset"


# ─── Node 2: By Axis ──────────────────────────────────────────────────

ASPECT_CHOICES = [
    ("1:1 Square",     (1, 1)),
    ("3:2 Landscape",  (3, 2)),
    ("2:3 Portrait",   (2, 3)),
    ("4:3 Landscape",  (4, 3)),
    ("3:4 Portrait",   (3, 4)),
    ("16:9 Landscape", (16, 9)),
    ("9:16 Portrait",  (9, 16)),
    ("5:4 Landscape",  (5, 4)),
    ("4:5 Portrait",   (4, 5)),
    ("21:9 Widescreen",(21, 9)),
    ("9:21 Portrait",  (9, 21)),
    ("7:5 Landscape",  (7, 5)),
    ("5:7 Portrait",   (5, 7)),
]

def empty_latent_by_axis(
    primary_dim:  int,
    reference:    str,
    aspect_ratio: str,
    batch_size:   int
) -> np.ndarray:
    """
    Empty Latent (Aspect Ratio by Axis)

    primary_dim:  numeric value for Width or Height
    reference:    "Width" or "Height"
    aspect_ratio: e.g. "3:2 Landscape"
    batch_size:   how many latents to produce
    """
    # Look up numeric ratio
    for lbl, (wr, hr) in ASPECT_CHOICES:
        if lbl == aspect_ratio:
            break
    else:
        raise ValueError(f"Unknown aspect ratio: {aspect_ratio}")

    _validate_dim(primary_dim)
    if reference == "Width":
        W = primary_dim
        H = round(primary_dim * hr / wr)
    else:
        H = primary_dim
        W = round(primary_dim * wr / hr)

    _validate_dim(W); _validate_dim(H)
    return np.zeros((batch_size, 4, H // 8, W // 8), dtype=np.float32)


def _byaxis_input_types():
    return {
        "required": {
            "primary_dim":  ("INT",    {"default": 512, "min": 8}),
            # A true dropdown of strings:
            "reference":    (["Width", "Height"],),
            "aspect_ratio": ([lbl for lbl, _ in ASPECT_CHOICES],),
            "batch_size":   ("INT",    {"default": 1,   "min": 1})
        }
    }

empty_latent_by_axis.INPUT_TYPES  = _byaxis_input_types
empty_latent_by_axis.RETURN_TYPES = ("LATENT",)
empty_latent_by_axis.CATEGORY     = "ComfyUI Aspect Ratio Preset"


# ─── Expose for ComfyUI ───────────────────────────────────────────────

NODE_CLASS_MAPPINGS = {
    "Empty Latent (Aspect Ratio Preset)":     empty_latent_preset,
    "Empty Latent (Aspect Ratio by Axis)":    empty_latent_by_axis,
}
NODE_DISPLAY_NAME = "ComfyUI Aspect Ratio Preset"