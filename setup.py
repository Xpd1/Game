from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
	options = {'py2exe': {'bundle_files': 1, 'compressed': True,"includes":["pygame"]}},
	
    windows = [{'script': "Game.py"}],
	data_files=[('.', 'SDL.dll'), ('.', 'SDL_image'), ('.', 'SDL_mixer.dll'), ('.', 'SDL_ttf'), ('.', 'smpeg.dll')],
    zipfile = None,
)