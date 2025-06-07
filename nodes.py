# nodes.py

import numpy as np
from .presets import PRESETS

def _validate_dim(v:int):
    if v <= 0:
        raise ValueError("Dimension must be > 0")
    if v % 8 != 0:
        raise ValueError("Dimension must be divisible by 8")

# --- Node 1 -----------------------------------------------------------

def empty_latent_preset(resolution_index:int, batch_size:int) -> np.ndarray:
    model, label, W, H = PRESETS[resolution_index]
    _validate_dim(W); _validate_dim(H)
    return np.zeros((batch_size, 4, H//8, W//8), dtype=np.float32)

def _preset_input_types():
    return {
        "required": {
            "resolution_index": (
                "INT", {
                    "default": 0,
                    "choices": [
                        f"{m} {w}×{h} ({lbl})"
                        for m,lbl,w,h in PRESETS
                    ]
                }
            ),
            "batch_size": ("INT", {"default":1, "min":1})
        }
    }

empty_latent_preset.INPUT_TYPES  = _preset_input_types
empty_latent_preset.RETURN_TYPES = ("LATENT",)
empty_latent_preset.CATEGORY     = "ComfyUI Aspect Ratio Preset"

# --- Node 2 -----------------------------------------------------------

ASPECT_CHOICES = [
  ("1:1 Square",(1,1)), ("3:2 Landscape",(3,2)), ("2:3 Portrait",(2,3)),
  # ... etc ...
]

def empty_latent_by_axis(primary_dim:int, reference:str, aspect_index:int, batch_size:int) -> np.ndarray:
    w_ratio,h_ratio = ASPECT_CHOICES[aspect_index][1]
    _validate_dim(primary_dim)
    if reference == "Width":
        W,H = primary_dim, round(primary_dim * h_ratio / w_ratio)
    else:
        H,W = primary_dim, round(primary_dim * w_ratio / h_ratio)
    _validate_dim(W); _validate_dim(H)
    return np.zeros((batch_size, 4, H//8, W//8), dtype=np.float32)

def _byaxis_input_types():
    return {
        "required": {
            "primary_dim":  ("INT",    {"default":512, "min":8}),
            "reference":    ("STRING", {"default":"Width", "choices":["Width","Height"]}),
            "aspect_index": ("INT",    {
                "default":0,
                "choices":[lbl for lbl,_ in ASPECT_CHOICES]
            }),
            "batch_size":   ("INT",    {"default":1, "min":1})
        }
    }

empty_latent_by_axis.INPUT_TYPES  = _byaxis_input_types
empty_latent_by_axis.RETURN_TYPES = ("LATENT",)
empty_latent_by_axis.CATEGORY     = "ComfyUI Aspect Ratio Preset"

# ─── Expose for ComfyUI ────────────────────────────────────────────────
