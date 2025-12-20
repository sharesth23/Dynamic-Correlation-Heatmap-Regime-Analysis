# Dynamic-Correlation-Heatmap-Regime-Analysis
“We study how correlations between equities, FX, rates, and commodities evolve over time using rolling correlation matrices. We visualize correlation heatmaps and identify regime shifts such as risk-on and risk-off periods.”

# Dynamic Cross-Asset Correlation Structure, Regime Dynamics & Systemic Risk Decomposition

## Abstract

This project develops a **cross-asset correlation research framework** to study the **time-varying dependence structure** between equities, foreign exchange, rates, and commodities.  

Using **rolling correlation matrices**, **heatmap visualizations**, and **eigen-decomposition via Principal Component Analysis (PCA)**, the framework analyzes:

- Regime-dependent diversification behavior  
- Stress-induced correlation convergence  
- Systemic risk concentration across asset classes  
- Structural changes in correlation dynamics pre- and post-COVID  

The project is designed to mirror **real-world macro research and portfolio risk diagnostics**, focusing on **dependence structure rather than return forecasting**.

---

## Research Motivation

Modern portfolio construction relies heavily on correlation assumptions.  
However, empirical evidence consistently shows that:

- Correlations are **non-stationary**
- Diversification benefits **collapse during crises**
- Cross-asset relationships shift structurally after major macro events

This project addresses a fundamental risk management question:

> *How stable is diversification when markets transition between regimes?*

By explicitly modeling correlation dynamics, we aim to **quantify when and why diversification fails**.

---

## Conceptual Framework

Let \( R_t \in \mathbb{R}^{N} \) denote the vector of asset returns at time \( t \).  
For a rolling window \( W \), define the correlation matrix:

\[
C_t = \text{Corr}(R_{t-W:t})
\]

Rather than treating \( C_t \) as static, we analyze its **temporal evolution** and **spectral properties**.

---

## Asset Universe & Macro Rationale

| Asset Class | Instrument | Role in System |
|------------|-----------|----------------|
| Equities | S&P 500, NASDAQ, DAX | Risk-on growth exposure |
| FX | EUR/USD, USD/JPY | Risk sentiment & funding flows |
| Rates | US 10Y Treasury Yield | Policy & discounting channel |
| Commodities | Gold, Crude Oil | Inflation hedge & growth sensitivity |

The universe is chosen to capture **global risk transmission mechanisms** across regions and asset classes.

---

## Data Engineering

- Source: Yahoo Finance (`yfinance`)
- Frequency: Daily
- Price series: Adjusted close
- Returns: Percentage returns
- Synchronization: Intersection of valid trading days
- Missing data: Dropped to ensure valid correlation estimation

This ensures **consistent covariance structure estimation**.

---

## Methodology

### 1. Rolling Correlation Estimation

For each time \( t \), a rolling correlation matrix \( C_t \in \mathbb{R}^{N \times N} \) is computed.

Key properties:
- Symmetric
- Unit diagonal
- Time-indexed dependence structure

This produces a **time series of correlation matrices** rather than a single static estimate.

---

### 2. Heatmap-Based Dependence Visualization

Each \( C_t \) is visualized via a heatmap:

- Centered color scale at zero
- Red → positive dependence
- Blue → negative dependence

Rolling (animated) heatmaps allow direct observation of:
- Correlation clustering
- Breakdown of traditional hedges
- Crisis-driven co-movement

Visualization is treated as a **diagnostic tool**, not presentation fluff.

---

### 3. Regime Interpretation via Dependence Structure

Rather than classifying regimes using returns or volatility alone, regimes are interpreted **directly from correlation behavior**.

**Risk-Off Regime Characteristics**
- Elevated equity-equity correlations
- Increased cross-asset co-movement
- Reduced effectiveness of defensive assets

**Risk-On Regime Characteristics**
- Lower average correlations
- Greater dispersion in dependence structure
- Functional diversification

This aligns with empirical macro-financial literature.

---

### 4. PCA on Correlation Matrices (Systemic Risk Extraction)

Each correlation matrix is decomposed:

\[
C_t = V_t \Lambda_t V_t^\top
\]

where:
- \( \Lambda_t \) contains eigenvalues
- \( V_t \) contains eigenvectors

The **first principal component (PC1)** explains the maximum proportion of correlation variance.

#### Interpretation

- High PC1 explained variance → correlation concentration → systemic risk
- Low PC1 explained variance → diversified dependence structure

PC1 is treated as a **low-dimensional proxy for market-wide co-movement**.

This approach is commonly used in:
- Risk parity validation
- Macro stress monitoring
- Correlation regime analysis

---

### 5. Pre- vs Post-COVID Structural Shift Analysis

The sample is split into two regimes:

- **Pre-COVID:** 2015–2019
- **Post-COVID:** 2020 onwards

For each period:
- Average correlation matrices are computed
- Structural differences are analyzed

This allows identification of **persistent changes**, not just transient crisis effects.

---

## Implementation Architecture
dynamic-correlation-regimes/
│
├── README.md
├── requirements.txt
│
├── data/
│ └── tickers.py # Cross-asset universe definition
│
├── src/
│ ├── data_loader.py # Data ingestion & returns construction
│ ├── correlation.py # Rolling correlation engine
│ ├── regimes.py # Regime interpretation heuristics
│ ├── visualization.py # Heatmaps & animations
│ └── pca_analysis.py # Eigen-decomposition & systemic risk
│
├── notebooks/
│ └── correlation_analysis.ipynb
│
└── run.py # End-to-end execution pipeline


The codebase intentionally separates:
- **Data engineering**
- **Statistical computation**
- **Visualization**
- **Research logic**

This mirrors professional research environments.

---

## Execution

### Installation
```bash
pip install -r requirements.txt

Full Pipeline
python run.py

Outputs

Time-indexed rolling correlation matrices

Static & animated correlation heatmaps

Systemic risk time series (PC1 explained variance)

Pre- vs post-COVID correlation structure comparison

Empirical Observations

Cross-asset correlations rise sharply during crises

Diversification benefits are regime-dependent

PC1 captures systemic stress effectively

Post-COVID markets exhibit elevated baseline correlations

Practical Applications

Portfolio diversification diagnostics

Stress-testing correlation assumptions

Macro regime monitoring

Risk parity validation

Asset allocation robustness checks

Limitations & Assumptions

Linear correlation only (no tail dependence)

PCA assumes linear structure

Regime classification is heuristic

No causal inference is implied

Potential Extensions

Dynamic Conditional Correlation (DCC-GARCH)

Copula-based dependence modeling

Correlation network graphs

Hidden Markov Models for regime detection

Bayesian time-varying correlation models

Integration with portfolio optimization frameworks

Relevance to Quantitative Roles

This project demonstrates:

Systemic risk awareness

Portfolio-level quantitative thinking

Statistical maturity

Clear separation of research logic and implementation

Ability to translate market structure into measurable signals

It reflects workflows used in macro research, risk management, and systematic asset allocation teams.

Disclaimer

This project is intended for educational and research purposes only and does not constitute investment advice.


---


