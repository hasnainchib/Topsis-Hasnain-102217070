from setuptools import setup, find_packages

setup(
    name="Topsis-YourName-RollNumber",  # Package name
    version="1.0.0",  # Version number
    author="Your Name",  # Your name
    author_email="youremail@example.com",  # Your email
    description="A Python package for TOPSIS decision-making.",
    long_description=open("README.md").read(),  # Read the README file
    long_description_content_type="text/markdown",
    url="https://github.com/YourGitHubUsername/Topsis-YourName-RollNumber",  # Link to your GitHub (optional)
    packages=find_packages(),  # Automatically find your package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas",  # Add dependencies here
        "numpy",
    ],
)
