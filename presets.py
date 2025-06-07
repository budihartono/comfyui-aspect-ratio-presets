# presets.py

PRESETS = [
    # model, label, w, h
    ("SD15",  "1:1 Square",    512, 512),
    ("SD15",  "3:2 Landscape", 768, 512),
    ("SD15",  "4:3 Landscape", 768, 576),
    ("SD15",  "16:9 Landscape",912, 512),
    ("SD15",  "2:3 Portrait",  512, 768),
    ("SD15",  "3:4 Portrait",  576, 768),
    ("SD15",  "9:16 Portrait", 512, 912),
    ("SDXL",    "1:1 Square",    1024,1024),
    ("SDXL",    "3:2 Landscape", 1152,768),
    ("SDXL",    "4:3 Landscape", 1152,864),
    ("SDXL",    "16:9 Landscape",1360,768),
    ("SDXL",    "2:3 Portrait",  768,1152),
    ("SDXL",    "3:4 Portrait",  864,1152),
    ("SDXL",    "9:16 Portrait", 768,1360),
    ("Flux/HiD","3:2 Landscape", 1216,832),
    ("Flux/HiD","2:3 Portrait",  832,1216),
    ("Flux/HiD","1:1 Square",    1408,1408),
    ("Flux/HiD","4:3 Landscape", 1664,1216),
    ("Flux/HiD","16:9 Landscape",1920,1088),
    ("Flux/HiD","9:21 Portrait", 960,2176),
    ("HiDream", "1:1 Square",    1280,1280),
    ("HiDream", "1:1 Square",    1536,1536),
]