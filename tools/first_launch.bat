@echo off

python -m pip install --upgrade pip
pip install pytest
pytest ../tests

