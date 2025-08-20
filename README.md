# Learning Stan
Here Alon Kagan learns to use stan and Baysean statistics in General

I will follow this guide:

https://bob-carpenter.github.io/stan-getting-started/stan-getting-started.html

And also try to recreate the results of an unpublished paper (held private for now)

## Steps for instalation

Make sure you have python 3.12 or lower. And python is in your PATH.

Install Rtools, then open Rtools bash and type in `pacman -Sy mingw-w64-x86_64-make`

Put "C:\rtools45\mingw64\bin" to your PATH.

pip install -r requirements. You can also do in in VENV.

python -m "import cmdstanpy; cmdstanpy.install_cmdstan()"