# Finger Counter with Voice Output — Single File Version

A real-time finger counting app that uses your laptop webcam and speaks the number of raised fingers aloud.

## Features
- Detects **1–10 fingers** across both hands using MediaPipe
- Speaks the number using **text-to-speech** (pyttsx3)
- Smooth detection with **stability buffering** (no flickering speech)
- Glowing digit overlay with word label
- FPS counter and voice toggle

## Requirements

```bash
pip install -r requirements.txt
```

| Package | Purpose |
|---|---|
| `opencv-python` | Webcam capture & display |
| `mediapipe` | Hand landmark detection |
| `pyttsx3` | Text-to-speech |
| `numpy` | Array operations |

## Run

```bash
python finger_counter.py
```

## Controls

| Key | Action |
|---|---|
| `Q` / `ESC` | Quit |
| `S` | Toggle voice on/off |
| `R` | Reset detection state |

## How it works

1. OpenCV captures webcam frames (mirrored)
2. MediaPipe Hands detects up to 2 hands and 21 landmarks per hand
3. Finger-up logic checks tip vs. PIP joint positions
4. A **StabilityBuffer** requires 8 consecutive identical counts before confirming
5. pyttsx3 speaks the English number word in a background thread
6. HUD overlays the digit, word, stability ring, and controls hint
