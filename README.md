# CI-Assignment-IC-Batch4

This repository contains the **API** and **Worker** services along with CI/CD workflows for building, linting, testing, scanning, and deploying the services.

---

## Project Structure

- `api/` - API service codebase  
- `worker/` - Background worker service codebase  
- `.github/workflows/` - GitHub Actions workflows for CI and CD  
- `requirements.txt` & `requirements-dev.txt` - Python dependencies  
- `mypy.ini`, `.flake8`, `.isort.cfg` - Configuration for linters and type checking  

---

## Tools & Technologies Used

### Development & Runtime
- **Python 3.11** - Programming language used  
- **Flask** - Web framework for API service  
- **SQLAlchemy** - ORM for database interaction  
- **Redis** and **ElasticMQ** - Caching and message queue services  

### Linting & Formatting
- **Flake8** - Python code linting to enforce coding standards  
- **Black** - Opinionated Python code formatter  
- **Isort** - Tool to sort and organize Python imports  

### Type Checking
- **Mypy** - Static type checker for Python  

### Testing & Coverage
- **Pytest** - Python testing framework  
- **Codecov** - Code coverage reports and analysis  

### Security Scanning
- **Bandit** - Security linter for Python (included in dev requirements)  
- **Trivy** - Container image and Dockerfile vulnerability scanner  

### Continuous Integration & Deployment
- **GitHub Actions** - Automated workflows for build, lint, test, scan, and deploy  
- **Docker** - Containerization for API and Worker services  

---

## How to Use

1. Clone the repository  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
