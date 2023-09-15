from setuptools import setup, find_packages

setup(name="line_plan_visualization",
      version="0.0.3",
      author="Macroda",
      author_email="SteppePrince@outlook.com",
      description="A visualization tool for line plan",
      packages=find_packages(),
      install_requires=["matplotlib>=3.7.3"],
      python_requires=">=3.9"
      )