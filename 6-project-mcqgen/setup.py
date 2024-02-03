from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='vivek',
    author_email='viveknaidu6677@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)