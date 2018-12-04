from setuptools import setup, find_packages

setup(
    name='openproject_google_calendar',
    version='0.1',
    packages=find_packages(),
    install_requires=["requests", "oauth2client"],
    zip_safe=True,
    url='https://cat.celad.com',
    license='MIT',
    author='olricson',
    author_email='homermen@hotmail.com',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: MIT"
        ],
    description="Export your OpenProject work packages to google calendar"
)