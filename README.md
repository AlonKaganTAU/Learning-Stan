# 📊 Learning Stan

Welcome! This repo documents Alon Kagan's journey learning **Stan** and **Bayesian statistics** in general.

## 📘 Learning Resources

I'm following this guide:

- [Stan Getting Started Guide by Bob Carpenter](https://bob-carpenter.github.io/stan-getting-started/stan-getting-started.html)

Additionally, I will try to recreate results from an **unpublished paper** (kept private for now).

Lastly, there is probably a youtube course worth watching, [here](https://www.youtube.com/playlist?list=PLCrWEzJgSUqwL85xIj1wubGdY15C5Gf7H) (if I have spare time)

---

## ⚙️ Installation Instructions

### 1. Install WSL (Windows Subsystem for Linux)

If you're using WSL for the first time, update and install required packages:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip build-essential git wget unzip
sudo apt install -y python3-venv
```

### 2. Set Up Python Virtual Environment for CmdStanPy

```bash
python3 -m venv ~/cmdstanpy-env
source ~/cmdstanpy-env/bin/activate
```
### 3. Upgrade Pip
```bash
pip install --upgrade pip
```
### 4. Install Required Python Packages
Make sure you have a requirements.txt file in your directory, then run:

```bash
pip install -r requirements.txt
```

5. Install CmdStan via CmdStanPy
```bash
python -c "import cmdstanpy; cmdstanpy.install_cmdstan()"
```

---

✅ You're All Set!
From now on, whenever you want to use CmdStanPy, just:

```bash
source ~/cmdstanpy-env/bin/activate
```

And you're good to go!

## Usage

open a new session:

```bash
wsl
source ~/cmdstanpy-env/bin/activate
```

## 🧠 Author
Alon Kagan — Exploring Bayesian inference and Stan one model at a time. (This joke was made by ChatGPT when I told it to make this page look nicer)
