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
