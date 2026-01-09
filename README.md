# VisionAct  
### Vision-Driven UI Automation for No-API Systems

<p align="center">
  <img src="https://img.shields.io/badge/status-stable-brightgreen" />
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" />
  <img src="https://img.shields.io/badge/opencv-vision-orange" />
  <img src="https://img.shields.io/badge/automation-ui--based-informational" />
  <img src="https://img.shields.io/badge/license-educational-lightgrey" />
</p>

---

## Overview

**VisionAct** is a vision-based UI automation engine that interacts with applications purely through **visual context**, without relying on APIs, DOM access, or browser-specific automation tools.

It is designed for environments where:
- APIs do not exist  
- Traditional automation (e.g., Selenium) is ineffective  
- Human-like interaction is required  

VisionAct observes the screen using **OpenCV**, verifies UI elements using **confidence-based matching**, and performs safe, controlled actions using **PyAutoGUI**.

---

## Why VisionAct?

Most automation frameworks assume structured access to systems (APIs, DOM trees, or internal hooks).  
In practice, many real-world systems offer **none of these**.

VisionAct treats automation as a **last-resort engineering solution**, mimicking how a human:
1. Sees the screen  
2. Identifies known visual elements  
3. Acts only when sufficiently confident  

This makes it suitable for:
- Legacy desktop software  
- Restricted or anti-bot environments  
- One-off productivity automation  
- Proof-of-concept tooling  

---

## Architecture

Screen Capture
↓
OpenCV (Visual Detection)
↓
Confidence Evaluation
↓
Decision Logic
↓
PyAutoGUI (Human-Like Interaction)


Each layer is intentionally isolated to ensure clarity, safety, and extensibility.

---

## Project Structure

VisionAct/
│
├── src/
│ ├── main.py # Core engine loop (decision logic)
│ ├── vision.py # Screen analysis and detection
│ ├── actions.py # Controlled UI interaction
│ ├── config.py # Tunable safety parameters
│
├── assets/
│ └── target.png # Reference UI element
│
├── requirements.txt
└── README.md

---

## How It Works

1. A screenshot of the current screen is captured.  
2. OpenCV performs template matching against a known UI element.  
3. A confidence score (0.0–1.0) is calculated.  
4. Actions are executed **only if confidence exceeds a predefined threshold**.  
5. The system exits safely after task completion.  

This prevents blind clicking and unintended actions.

---

## Configuration

All safety-critical parameters are defined in `config.py`:

- **Confidence Threshold** – minimum acceptable match quality  
- **Scan Interval** – frequency of screen analysis  
- **Action Delay** – pacing for human-like interaction  

This separation avoids hard-coded behavior and enables safe tuning.

---

## Installation

```bash
pip install -r requirements.txt

---

## Running VisionAct

1. Capture a **tight screenshot** of the target UI element you want to automate.
2. Save the image as `assets/target.png`.
3. Open the application or website you want to automate.
4. Run the engine:

```bash
python src/main.py
VisionAct will continuously observe the screen and act only when the target element is confidently detected.

---

## Safety Mechanisms

VisionAct is designed with safety-first automation principles:

- **Confidence-based decision making**
- **Single-action execution** (prevents infinite loops)
- **PyAutoGUI emergency failsafe** (move mouse to top-left corner to abort)
- **Explicit delays** to prevent race conditions  

These are **deliberate engineering choices**, not afterthoughts.

---

## Limitations (Important)

VisionAct is **not** a universal automation solution.

Known limitations include:
- Sensitivity to UI changes  
- Dependency on screen resolution and DPI scaling  
- Not suitable for mission-critical automation  
- Intended for controlled and predictable environments  

These trade-offs are **intrinsic to vision-based automation**.

---

## When NOT to Use VisionAct

Do **not** use VisionAct:
- When an official API exists  
- When DOM-level automation is possible  
- When absolute reliability is required  
- When UI elements change frequently  

In such cases, traditional automation tools are superior.

---

## Learning Outcomes

This project demonstrates:
- Practical application of computer vision  
- Confidence-driven decision systems  
- Fail-safe automation design  
- Engineering trade-off awareness  
- Modular and extensible architecture  

---

## Roadmap

Planned improvements include:
- JSON/YAML-based task pipelines  
- OCR integration for text-based decisions  
- Multi-template detection  
- Structured logging and screenshots  
- Performance optimization using region-of-interest scanning  

---

## License

This project is intended for **educational and experimental use**.
