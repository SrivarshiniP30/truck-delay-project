import setuptools

# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Truck_Delay_Classification"
AUTHOR_USER_NAME = "RahulReddy20"
SRC_REPO = "Truck_Delay_Classification"
AUTHOR_EMAIL = "rahulreddy2036@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="End to end ML implementation of truck delay classification problem",
    # long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)