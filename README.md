# [Project title: the business question in plain words]

> **Question:** [e.g. How should a motor insurer price third-party liability cover?]
> **Answer:** [One or two sentences with the headline number, e.g. A Poisson–Gamma GLM ranks risk well (Gini 0.XX); a gradient-boosting model adds X points but is harder to explain.]

[One-paragraph summary a non-technical manager could follow: what you did, what you found, what it means.]

## Data

- **Source:** [name, link, licence]
- **Size:** [rows × columns, period covered]
- **Preparation:** [key cleaning steps, e.g. capped claim amounts at the 99.5th percentile]

Raw data isn't committed. See [`data/README.md`](data/README.md) for how to download it.

## Method

1. [Exploratory analysis: what you looked at and why]
2. [Model(s): e.g. Poisson frequency GLM, Gamma severity GLM, Tweedie GLM, gradient-boosting benchmark]
3. [Validation: e.g. 80/20 train–test split, lift and double-lift charts, Gini]

## Results

| Model | [Metric 1] | [Metric 2] | Notes |
| --- | --- | --- | --- |
| [Baseline] | | | |
| [Main model] | | | |

![Key chart](reports/figures/[file].png)

## Limitations and next steps

- [What the data or method can't tell you]
- [What you'd do with more time or better data]

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Then run the notebooks in `notebooks/` in order. Every random step uses the seed in `src/config.py`, so results reproduce exactly.

## Repository layout

```
data/raw/          downloaded data (git-ignored)
data/processed/    cleaned data (git-ignored)
notebooks/         analysis, numbered in run order (01_explore.ipynb, 02_model.ipynb, ...)
src/               reusable functions and config
reports/           write-up and figures
```
