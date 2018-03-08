from distutils.core import setup

setup(
    name='KerasDeepViz',
    version='0.1',
    packages=['keras_deep_viz',],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[
        'numpy',
        'Keras',
        'Pillow',
        'matplotlib',
        'tensorflow',
    ]
)
