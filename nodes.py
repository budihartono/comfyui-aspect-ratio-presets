import torch
from .presets import PRESETS

def _validate_dim(v: int):
    if v <= 0 or v % 8 != 0:
        raise ValueError("Dimension must be >0 and divisible by 8")


class EmptyLatentAspectPreset:
    """Creates a blank latent using one of the predefined presets."""
    def __init__(self):
        # Build lookup from dropdown key to (W, H)
        self._map = {
            f"{w}x{h} - {lbl} - {model}": (w, h)
            for model, lbl, w, h in PRESETS
        }

    @classmethod
    def INPUT_TYPES(cls):
        choices = [
            f"{w}x{h} - {lbl} - {model}"
            for model, lbl, w, h in PRESETS
        ]
        return {
            "required": {
                "preset":     (choices,),
                "batch_size": ("INT", {"default": 1, "min": 1})
            }
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("LATENT",)
    FUNCTION     = "generate"
    CATEGORY     = "latent"    # moved into ComfyUI's built-in "latent" category

    def generate(self, preset: str, batch_size: int):
        if preset not in self._map:
            raise ValueError(f"Unknown preset: {preset}")
        w, h = self._map[preset]

        _validate_dim(w)
        _validate_dim(h)

        latent = torch.zeros([batch_size, 4, h // 8, w // 8], dtype=torch.float32)
        return ({"samples": latent},)


class EmptyLatentAspectByAxis:
    """Creates a blank latent by fixing one axis and computing the other from an aspect ratio."""
    ASPECT_CHOICES    = [
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
    REFERENCE_CHOICES = ["Width", "Height"]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "primary_dim":  ("INT",    {"default": 512, "min": 8}),
                "reference":    (cls.REFERENCE_CHOICES,),
                "aspect_ratio": ([lbl for lbl,_ in cls.ASPECT_CHOICES],),
                "batch_size":   ("INT",    {"default": 1,   "min": 1})
            }
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("LATENT",)
    FUNCTION     = "generate"
    CATEGORY     = "latent"    # now appears under the built-in latent category

    def generate(self, primary_dim: int, reference: str, aspect_ratio: str, batch_size: int):
        ratio_map = dict(self.ASPECT_CHOICES)
        if aspect_ratio not in ratio_map:
            raise ValueError(f"Unknown aspect ratio: {aspect_ratio}")
        wr, hr = ratio_map[aspect_ratio]

        _validate_dim(primary_dim)
        if reference == "Width":
            w, h = primary_dim, round(primary_dim * hr / wr)
        else:
            h, w = primary_dim, round(primary_dim * wr / hr)

        _validate_dim(w)
        _validate_dim(h)

        latent = torch.zeros([batch_size, 4, h // 8, w // 8], dtype=torch.float32)
        return ({"samples": latent},)