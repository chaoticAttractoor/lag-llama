from setuptools import setup, find_packages

setup(
    name='lag_llama',  # Replace with your package's name
    version='0.1.0',  # Replace with your package's version
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    description='A short description of your package',  # Provide a short description
    long_description=open('README.md').read(),  # This will read your README.md file as the long description
    long_description_content_type='text/markdown',  # Specifies that the long description is in Markdown
    url='https://github.com/YourGitHubUsername/YourRepository',  # Replace with your repository's URL
    packages=['lag_llama'],  # Automatically find and include all packages in your project
    install_requires=[
        
        'gluonts',
        'numpy==1.23.5',
        'pytorch_lightning',
        'torch>=2.0.0',
        'wandb',
        'scipy',
        'pandas==2.1.4',
        'huggingface_hub[cli]'
  
    ],
    classifiers=[
        # Choose classifiers that describe your project.
        # Full list: https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify which Python versions are supported
)