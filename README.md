# bangsaenai.github.io
Official website of BangsaenAI: Advanced Flight Control Software using Koopman Operator Technology (Python). Open Source GPL v3.0.

# 📉 Financial Stability Monitor: A Koopman Operator Approach

> *"While the world asks AI to guess the price, we use Physics to measure the energy."*

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=google-cloud)](https://project-x-engine-653731256449.asia-southeast1.run.app/)
[![Python](https://img.shields.io/badge/Made%20With-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Control Theory](https://img.shields.io/badge/Powered%20By-Koopman%20Operator-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/Koopman_operator)

## 🧐 The Problem: AI Slop vs. Physics
The current market is flooded with Generative AI "hallucinations" that try to predict stock prices based on text patterns. They are black boxes, computationally expensive, and often wrong.

**Project X** takes a different approach. We treat financial markets as **Dynamic Systems**. Instead of predicting the *future price*, we analyze the **current system stability**.

## 📐 The Math (The Secret Sauce)
We utilize **Koopman Operator Theory** and **Dynamic Mode Decomposition (DMD)** to lift non-linear market data into a linear infinite-dimensional observable space.

1.  **Data Ingestion:** Construct **Hankel Matrices** from time-series price data (Time-Delay Embedding).
2.  **Linear Approximation:** Compute the best-fit linear operator $K$ such that:
    $$g(x_{t+1}) \approx K g(x_t)$$
3.  **Spectral Analysis:** Extract **Eigenvalues ($\lambda$)** from the operator $K$.

### 🚦 The Stability Criterion
We map the market status directly to the complex plane:
* **$|\lambda| < 1.0$ (Converging):** System is losing energy. The price is stable or consolidating. (**Safe**)
* **$|\lambda| \approx 1.0$ (Limit Cycle):** System is in equilibrium.
* **$|\lambda| > 1.0$ (Diverging):** System is gaining energy exponentially. A volatility explosion or crash is imminent. (**Critical Risk**)

## 🛠 Tech Stack
* **Engine:** Python (NumPy, SciPy) for SVD and Eigenvalue decomposition.
* **Backend:** FastAPI (High-performance async).
* **Infrastructure:** Google Cloud Run (Serverless, Autoscaling).
* **Frontend:** Server-side rendered HTML dashboard with real-time visitor tracking.

## 🚀 Live Demo & Usage
The system currently monitors 10 major assets (BTC, ETH, DOGE, etc.) with a **Zero-Tolerance** risk threshold ($|\lambda| > 1.000$).

**[👉 Access the Live Dashboard Here](https://project-x-engine-653731256449.asia-southeast1.run.app/)**

---
*Developed by Bangsaen AI Engineering Team.*
---

## ⚡ Methodology Comparison: Why "Bangsaen Koopman"?

While we acknowledge the pioneering work of *Steven Brunton et al.* in **Deep Koopman** (using Autoencoders to discover observables), our implementation takes a radically different approach optimized for **High-Frequency Trading (HFT)** and **Real-time Crisis Detection**.

We prioritize **speed** and **stability** over the flexibility of deep learning. By replacing the "Neural Network Black Box" with physics-based constraints, we achieve execution speeds that are orders of magnitude faster.

| Feature | 🧠 Deep Koopman (Brunton et al.) | 🚀 Bangsaen Koopman (Our Tech) |
| :--- | :--- | :--- |
| **Core Architecture** | **Deep Learning** (Autoencoders + EDMD). <br>Uses NN to "learn" the coordinate transformation. | **Pure Linear Algebra** (Physics-Informed). <br>Uses mathematical insight to define observables directly. |
| **Inference Speed** | **High Latency (~50-200ms)** <br>Requires passing data through deep neural layers. | **Ultra-Low Latency (< 1ms)** <br>Instant Matrix Multiplication ($X' = AX$). |
| **Computational Cost** | **Heavy (GPU Required)** <br>Expensive to train and run real-time. | **Lightweight (CPU / Serverless)** <br>Runs efficiently on Google Cloud Run (Autoscaling). |
| **Explainability** | **Black Box** <br>Latent space dynamics are hard to interpret physically. | **White Box** <br>Eigenvalues directly correlate to market energy & stability. |
| **Stability** | **Variable** <br>Neural networks can hallucinate or overfit noise. | **Robust** <br>Physics-constrained; filters out market noise naturally. |
| **Primary Use Case** | Offline Analysis, Fluid Dynamics, Reconstruction. | **Live "Fire Alarm"**, Crash Prediction, HFT Execution. |

### 💡 The "Speed" Advantage
In financial markets, **Time = Alpha**. 

* **Deep Koopman:** `Input` -> `Encoder (NN)` -> `Koopman` -> `Decoder (NN)` -> `Output` (Too slow for crash detection).
* **Bangsaen Koopman:** `Input` -> `Matrix Op` -> `Output` (Instant).

We don't need to "guess" the physics using AI; we **apply** the physics directly. This allows **Bangsaen AI** to detect instability (Eigenvalues > 1.0) *before* the price crash occurs, with zero lag.


---
layout: dark-academic
title: Linear Algebra for AI & Control
description: The mathematical engine behind modern predictive control.
---

# The Math Behind The Magic
> **"Mathematics is not about numbers, equations, computations, or algorithms: it is about understanding."** — William Paul Thurston

ยินดีต้อนรับสู่ **BangsaenAI Academy**.
ที่นี่เราไม่ได้สอน Linear Algebra เพื่อให้คุณไปสอบไล่ แต่เราสอนเพื่อให้คุณ **"สร้าง"**
โลกยุคเก่าของ PID Control จบลงแล้ว ยุคแห่งการทำนาย (Prediction) ขับเคลื่อนด้วยเมทริกซ์และเวกเตอร์
นี่คือภาษาของ **Bangsaen Core**

---

## Part 1: From Scalar to Vector
### (ทำไม PID ถึงตาย และ Vector คือทางรอด)

ในระบบควบคุมแบบดั้งเดิม (Classical Control) หรือ PID เรามองโลกผ่านรูเข็ม เราสนใจค่าเพียงค่าเดียว คือ **Error** ($e(t)$)
$$e(t) = \text{SetPoint} - \text{ProcessVariable}$$

นี่คือ **Scalar** (ปริมาณสเกลาร์) — ตัวเลขตัวเดียวที่ไร้ทิศทาง ไร้มิติ และมองไม่เห็นภาพรวม

แต่ในโลกความเป็นจริง ระบบมีความซับซ้อน (Complex Systems) การเปลี่ยนแปลงของอุณหภูมิส่งผลต่อความดัน ความดันส่งผลต่ออัตราการไหล
การจะคุมสิ่งเหล่านี้ให้อยู่หมัด เราต้องมองให้เห็น **"State"** ทั้งหมดพร้อมกัน

เราจึงต้องใช้ **Vector** ($\mathbf{x}$):

$$\mathbf{x} = \begin{bmatrix} \text{Temperature} \\ \text{Pressure} \\ \text{Flow Rate} \end{bmatrix}$$



### 💻 Python Representation

ใน Python เราไม่ใช้ List ธรรมดา แต่เราใช้ `NumPy` เพื่อประสิทธิภาพสูงสุด

```python
import numpy as np

# Scalar (Old School PID view)
error = 5.0

# Vector (Modern State-Space view)
# นี่คือวิธีที่ Bangsaen Core มองเห็นระบบของคุณ
x_state = np.array([
    [120.5],  # Temp
    [15.2],   # Pressure
    [0.8]     # Flow
])

print(f"System State Shape: {x_state.shape}")
# Output: (3, 1) -> 3 Dimensions, 1 State
