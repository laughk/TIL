from setuptools import setup


setup(
    name='gmail_tool',
    version='201907.14.1.dev',
    py_modules=['cli', 'modules'],
    install_requires=[
        'google-api-python-client==1.7.9',
        'google-auth-httplib2==0.0.3',
        'google-auth-oauthlib==0.3.0',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            "g2s = cli:main",
        ]
    }
)
