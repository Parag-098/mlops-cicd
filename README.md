# Assignment 7 — MLOps CI/CD with GitHub Actions

Train a Logistic Regression classifier on Iris, verify its accuracy with pytest, and run a main-branch deployment simulation only after the test job passes. The workflow runs on pushes and pull requests targeting `main`; deployment is skipped for pull requests and failed tests.

Repository: [Parag-098/mlops-cicd](https://github.com/Parag-098/mlops-cicd)

## Project structure

```text
.github/workflows/ci-cd.yml  GitHub Actions build, test and deploy-simulation jobs
src/model.py                 Iris model training and evaluation
tests/test_model.py          Accuracy threshold test
app.py                       Local application entry point
requirements.txt             scikit-learn and pytest
```

## Run in PowerShell

```powershell
python -m pip install -r requirements.txt
python src/model.py
python app.py
python -m pytest -v
```

The passing test requires accuracy >= 0.80. The GitHub failure gate was verified on `main` by temporarily raising the threshold to `1.01`: Actions run [44774528333](https://github.com/Parag-098/mlops-cicd/actions/runs/44774528333) failed at **Run Unit Tests** and skipped **Deploy Application**. The `0.80` threshold has been restored; the workflow deploy job depends on successful tests.

## GitHub Actions

The workflow file is `.github/workflows/ci-cd.yml`. On pushes to `main`, it checks out the repository, sets up Python 3.11, installs dependencies, compiles the application, runs it and runs pytest. The deploy job then prints a deployment simulation message. Pull requests to `main` run validation but skip deployment.

Verified execution and workflow status are recorded in `execution_log.txt`. The pushed GitHub Actions run passed both jobs. GitHub Actions screenshots are listed in `SCREENSHOT_CHECKLIST.md`.
