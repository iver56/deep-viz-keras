from setuptools import setup

setup(
    name='KerasDeepViz',
    version='0.1',
    packages=['keras_deep_viz', ],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[
        'numpy',
        'Keras',
        'Pillow',
        'matplotlib',
    ],
    extras_require={
        "tf": ["tensorflow>=1.0.0"],
        "tf_gpu": ["tensorflow-gpu>=1.0.0"],
    }
)
