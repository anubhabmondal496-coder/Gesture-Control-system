# Mediapipe Hand Magic

This repository contains an enhanced MediaPipe hand‑tracking demo that visualises the connections between two hands with:

- **Dynamic RGB colour cycling** based on a sinusoidal timer.
- **Glowing lines** using a blurred overlay for a neon‑like effect.
- **Particle bursts** that emanate from each landmark connection and fade away.
- **Trailing effect** that leaves a faint motion trail behind the hands.
- **Subtle dark gradient background** for better contrast.

## Requirements

- Python 3.8+ 
- `opencv-python` 
- `mediapipe` (the task‑based version) 
- `numpy`

You can install the dependencies with:
```bash
pip install opencv-python mediapipe numpy
```

## Running the demo

```bash
python joining_both_hands.py
```

Press **`q`** to quit the window.

Feel free to tweak the configuration constants at the top of the script (`PARTICLE_COUNT`, `TRAIL_DECAY`, `GLOW_KERNEL`, etc.) to customise the visual style.
