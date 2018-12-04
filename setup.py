from setuptools import setup, find_packages

setup(
    name='openproject_google_calendar',
    version='0.2',
    packages=find_packages(),
    install_requires=["requests", "oauth2client"],
    entry_points={
        'console_scripts': ['op2gc=openproject_google_calendar.main:main']
    },
    zip_safe=True,
    url='https://github.com/olricson/openproject_google_calendar',
    license='MIT',
    author='olricson',
    author_email='homermen@hotmail.com',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
        ],
    description="Export your OpenProject work packages to google calendar"
)