import os
import numpy as np
from PIL import Image, ImageDraw

def generate_logo():
    # Load original logo
    orig = Image.open('img/hexastormlogo_backup.webp').convert('RGB')
    arr = np.array(orig)
    h, w, _ = arr.shape
    
    # Mathematical un-compositing:
    # Original background is approximately C_bg = 45
    # Text is pure white (255, 255, 255)
    # alpha = (C - C_bg) / (255 - C_bg)
    r = arr[:, :, 0].astype(float)
    alpha = np.clip((r - 42.0) / (215.0 - 42.0) * 255.0, 0, 255).astype(np.uint8)
    
    # Create static base layer for text (HEXA on left, STORM on right)
    static_rgba = np.zeros((h, w, 4), dtype=np.uint8)
    static_rgba[:, :, :3] = 255
    static_rgba[:, :, 3] = alpha
    
    # Erase hexagon region (cols 282 to 392)
    static_rgba[:, 282:392, 3] = 0
    static_img = Image.fromarray(static_rgba)
    
    # Hexagon parameters measured from original logo
    cx, cy = 341.0, 43.0
    radius = 47.2
    
    # 30 frames for a smooth 60-degree rotation
    # (Since hexagon has 6-fold symmetry, 60 deg is a mathematically seamless loop)
    n_frames = 30
    duration_ms = 50 # 30 * 50ms = 1.5s per face advance (9s for full 360 deg)
    
    frames = []
    scale = 4 # 4x supersampling for buttery smooth anti-aliased edges
    canvas_w, canvas_h = w * scale, h * scale
    hr_cx, hr_cy = cx * scale, cy * scale
    hr_r = radius * scale
    
    for i in range(n_frames):
        angle_deg = (i / n_frames) * 60.0
        angle_rad = np.radians(angle_deg)
        
        frame_hr = Image.new('RGBA', (canvas_w, canvas_h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(frame_hr)
        
        pts = []
        for k in range(6):
            a = angle_rad + np.radians(k * 60.0)
            px = hr_cx + hr_r * np.cos(a)
            py = hr_cy + hr_r * np.sin(a)
            pts.append((px, py))
            
        draw.polygon(pts, fill=(255, 255, 255, 255))
        hex_layer = frame_hr.resize((w, h), Image.Resampling.LANCZOS)
        
        composed = Image.alpha_composite(static_img, hex_layer)
        frames.append(composed)
        
    out_path = 'img/hexastormlogo.webp'
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=duration_ms, loop=0, quality=95)
    print(f"Generated {out_path} with {n_frames} frames, size: {os.path.getsize(out_path)} bytes")

if __name__ == '__main__':
    generate_logo()
