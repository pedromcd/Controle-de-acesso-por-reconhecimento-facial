# Facial Recognition Access Control

**Real-time face-recognition system for access control using Python, OpenCV, InsightFace/ArcFace, ONNX Runtime, and SQLite.**

This academic computer-vision project implements a complete enrollment and recognition pipeline. Users are enrolled from camera captures, converted into facial embeddings, stored locally, and later compared with live camera input to determine whether access should be granted.

## System pipeline

```text
Enrollment
Camera frame
    ↓
Face detection
    ↓
ArcFace embedding
    ↓
SQLite storage

Recognition
Camera frame
    ↓
Face detection
    ↓
ArcFace embedding
    ↓
Similarity comparison
    ↓
Threshold decision
    ↓
Recognized / Not recognized
```

## Main features

- camera-based user enrollment;
- extraction of facial embeddings;
- persistent local storage in SQLite;
- real-time face detection and recognition;
- configurable similarity threshold;
- separation between database, face-processing, enrollment, and recognition modules;
- simple application entry point.

## Tech stack

- Python 3.10+
- OpenCV
- InsightFace / ArcFace
- ONNX Runtime
- SQLite

## Repository structure

```text
.
├── app.py          # Application entry point
├── config.py       # Camera and threshold configuration
├── db_utils.py     # SQLite persistence
├── face_utils.py   # Face detection / embedding utilities
├── enroll.py       # Enrollment workflow
├── recognize.py    # Real-time recognition
├── requirements.txt
└── README.md
```

## Configuration

The recognition threshold and camera index are configured in `config.py`.

A stricter threshold reduces false matches but can increase false rejections. A more permissive threshold has the opposite tradeoff. This makes threshold selection an important part of evaluating the system.

## Running the project

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The enrollment flow captures multiple face samples for a user and stores their embeddings. The recognition flow compares embeddings extracted from live camera frames with the enrolled database.

## Machine-learning / research considerations

The project is intentionally simple, but it provides a practical base for studying several computer-vision questions:

- similarity-threshold calibration;
- false acceptance vs. false rejection tradeoffs;
- robustness under changes in lighting, pose, and camera quality;
- embedding-distance distributions;
- evaluation across different recognition models;
- liveness detection and spoofing resistance;
- privacy-preserving storage of biometric representations.

A stronger experimental version could add a labeled evaluation dataset, ROC/DET curves, precision/recall metrics, and systematic threshold selection instead of relying on manual tuning.

## Authors

Pedro Marques Correa Domingues  
Lucas Bucci Borges
