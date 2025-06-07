# aspect_ratio_nodes.py

import numpy as np
import modules.scripts as scripts
from modules import shared
from modules.ui import create_node, create_node_callbacks
from presets import PRESETS

def _validate_dim(v):
    if v <= 0:
        raise ValueError("Dimension must be > 0")
    if v % 8 != 0:
        raise ValueError("Dimension must be divisible by 8")

class EmptyLatentAspectPreset(scripts.Script):
    title = "Empty Latent (Aspect Ratio Preset)"
    ui_category = "ComfyUI Aspect Ratio Preset"

    def ui(self):
        self.resolution = self.ui.dropdown(
            label="Resolution Preset",
            choices=[f"{m} {w}×{h} ({lbl})" for m, lbl, w, h in PRESETS],
            default=0,
            tooltip="Choose a predefined resolution + aspect ratio"
        )
        self.batch_size = self.ui.int_field(
            label="Batch Size",
            default=1,
            minimum=1,
            tooltip="How many blank latents to produce"
        )

    def run(self, p):
        model, lbl, W, H = PRESETS[self.resolution]
        _validate_dim(W); _validate_dim(H)
        B = self.batch_size
        C = shared.sd_model.cond_stage_model.latent_channels  # usually 4
        shape = (B, C, H // 8, W // 8)
        return np.zeros(shape, dtype=np.float32)


class EmptyLatentAspectByAxis(scripts.Script):
    title = "Empty Latent (Aspect Ratio by Axis)"
    ui_category = "ComfyUI Aspect Ratio Preset"

    ASPECT_CHOICES = [
        ("1:1 Square", (1,1)),
        ("3:2 Landscape", (3,2)),
        ("2:3 Portrait", (2,3)),
        ("4:3 Landscape", (4,3)),
        ("3:4 Portrait", (3,4)),
        ("16:9 Landscape", (16,9)),
        ("9:16 Portrait", (9,16)),
        ("5:4 Landscape", (5,4)),
        ("4:5 Portrait", (4,5)),
        ("21:9 Widescreen", (21,9)),
        ("9:21 Portrait", (9,21)),
        ("7:5 Landscape", (7,5)),
        ("5:7 Portrait", (5,7)),
    ]

    def ui(self):
        self.primary = self.ui.int_field(
            label="Primary Dimension",
            default=512,
            tooltip="Your value for the chosen Reference Axis"
        )
        self.axis = self.ui.dropdown(
            label="Reference Axis",
            choices=["Width","Height"],
            default="Width",
            tooltip="Which side does the Primary Dimension refer to?"
        )
        self.aspect = self.ui.dropdown(
            label="Aspect Ratio",
            choices=[lbl for lbl,_ in self.ASPECT_CHOICES],
            default=0,
            tooltip="Select X:Y ratio and orientation"
        )
        self.batch_size = self.ui.int_field(
            label="Batch Size",
            default=1,
            minimum=1,
            tooltip="How many blank latents to produce"
        )

    def run(self, p):
        val = self.primary
        _validate_dim(val)
        w_ratio, h_ratio = self.ASPECT_CHOICES[self.aspect][1]

        if self.axis == "Width":
            W = val
            H = round(val * (h_ratio / w_ratio))
        else:
            H = val
            W = round(val * (w_ratio / h_ratio))

        _validate_dim(W); _validate_dim(H)

        B = self.batch_size
        C = shared.sd_model.cond_stage_model.latent_channels
        shape = (B, C, H // 8, W // 8)
        return np.zeros(shape, dtype=np.float32)