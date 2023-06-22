import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'text_summarization_nlp'
AUTHOR_USER_NAME = 'vaidatascientist'
SRC_REPO = 'text_summarization'
AUTHOR_EMAIL = 'marioandluigi1010@gmail.com'

setuptools.setup(
    name=f"{SRC_REPO}",
    version=__version__,
    author=f"{AUTHOR_USER_NAME}",
    author_email=f"{AUTHOR_EMAIL}",
    description="Small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)