# Finger Counter with Voice Output — Modular Version (20 files)

Same app as the single-file version, split into **20 focused modules** for clean architecture and GitHub contributions.

## File Structure

```
finger_counter_modular/
├── main.py                  # Entry point
├── config.py                # All configuration constants
├── logger_setup.py          # Logging initialisation
├── camera_manager.py        # Webcam lifecycle
├── finger_detector.py       # MediaPipe hand & finger detection
├── voice_engine.py          # Thread-safe TTS wrapper
├── stability_buffer.py      # Flicker-prevention filter
├── fps_counter.py           # Smoothed FPS calculation
├── number_words.py          # Integer → English/Nepali word map
├── hud_renderer.py          # All on-screen overlays
├── speech_controller.py     # Cooldown & dedup for speech
├── keyboard_handler.py      # Key → Action mapping
├── session_stats.py         # Runtime statistics & summary
├── frame_processor.py       # Per-frame pipeline orchestration
├── window_manager.py        # OpenCV window lifecycle
├── app_builder.py           # Dependency injection / factory
├── event_loop.py            # Main capture → display → input loop
├── cli.py                   # argparse CLI
├── tests/
│   ├── test_stability_buffer.py
│   └── test_number_words.py
└── requirements.txt
```

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py                        # default
python main.py --camera 1             # use second webcam
python main.py --no-voice             # silent mode
python main.py --language nepali      # speak Nepali
python main.py --stable-frames 12     # slower confirmation
python main.py --help                 # all options
```

## Run Tests

```bash
python -m pytest tests/ -v
```

## Controls

| Key | Action |
|---|---|
| `Q` / `ESC` | Quit |
| `S` | Toggle voice on/off |
| `R` | Reset detection state |

## Architecture

```
main.py
  └── cli.py           (parse args)
  └── app_builder.py   (wire all components)
  └── event_loop.py    (run the loop)
        ├── camera_manager.py
        ├── frame_processor.py
        │     ├── finger_detector.py
        │     ├── stability_buffer.py
        │     ├── speech_controller.py
        │     │     ├── voice_engine.py
        │     │     └── number_words.py
        │     ├── hud_renderer.py
        │     ├── fps_counter.py
        │     └── session_stats.py
        ├── window_manager.py
        └── keyboard_handler.py
```
