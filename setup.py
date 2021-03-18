from setuptools import setup, find_packages

setup(
	name='custom_minigrid',
    version='0.1',
    description='Extension to gym-minigrid which supports simple custom generation of environments',
    packages=['custom_minigrid'], #['gym_minigrid', 'gym_minigrid.envs'],
    # packages=find_packages(),
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=[
        'gym==0.17.3',  # v0.18 has some bugs so far; use older version for safety
        'numpy>=1.15.0',
        'gym-minigrid>=1.0.2'
    ]
)
