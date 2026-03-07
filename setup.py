from setuptools import setup, find_packages


setup(
    name="predictive_maintenance",
    version="0.0.1",
    author="Madhav Manoj",
    author_email="",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "fastapi",
        "uvicorn",
        "joblib",
        "pyyaml",
        "tqdm"
    ]
)