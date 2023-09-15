from setuptools import setup, find_packages

with open("README.md", 'r', encoding="utf-8") as ld:
    long_description = ld.read()

setup(name="line_plan_visualization",
      version="0.0.4",
      author="Macroda",
      author_email="SteppePrince@outlook.com",
      description="A visualization tool for line plan",
      long_description_content_type="text/markdown",
      long_description=long_description,
      url="https://github.com/SteppePrince/LinePlanVisualization",
      packages=find_packages(),
      install_requires=["matplotlib>=3.7.3"],
      python_requires=">=3.9"
      )