# PROJECT SETUP
# set DRAFT = False for final output; DRAFT = True is faster
DRAFT = True

import itertools
import logging
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings( "ignore", module = "plotnine\..*" )

import cmdstanpy as csp
csp.utils.get_logger().setLevel(logging.ERROR)

import numpy as np
import statistics as stat
import pandas as pd
import plotnine as pn
import patchworklib as pw
import time

class StopWatch:
    def __init__(self):
        self.start()
    def start(self):
        self.start_time = time.time()
    def elapsed(self):
        return time.time() - self.start_time
timer = StopWatch()
