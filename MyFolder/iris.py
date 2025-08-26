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

### Project-specific code

M = 100 if DRAFT else 10_000

def prepare_iris_data_for_stan(df):
    N = df.shape[0]
    petal_width = df['petal_width']
    petal_length = df['petal_length']
    species = 1 + pd.Series(df['species']).astype('category').cat.codes
    num_species = 3
    data = {'N': N,
            'K': num_species,
            'species': species,
            'petal_width': petal_width,
            'petal_length': petal_length,}
    return data

### Load and show plain data

plain_iris_data = pd.read_csv('../stan-getting-started/stan/iris-data.csv')
data_plot = (
  pn.ggplot(plain_iris_data, pn.aes(x='petal_width', y='petal_length',
                       color='species')) +
  pn.geom_point() +
  pn.labs(x = "petal width (cm)", y = "petal length (cm)")
)
data_plot.save('iris_collected_data_plot.png')

### Fit a linear regression model

stan_iris_data = prepare_iris_data_for_stan(plain_iris_data)
linear_regression_model = csp.CmdStanModel(stan_file = '../stan-getting-started/stan/iris-petals.stan')
sample = linear_regression_model.sample(data = stan_iris_data, seed = 123,
                      iter_warmup = M, iter_sampling = M,       
                      show_progress = False, show_console = False)
print(sample.summary(sig_figs = 2))

## Plot some regression lines to get a sense of the fit

alpha_draws = sample.stan_variable('alpha')
beta_draws = sample.stan_variable('beta')
data_plot_with_fit = data_plot
for a, b in zip(alpha_draws[0:20], beta_draws[0:20]):
    data_plot_with_fit += pn.geom_abline(intercept = a, slope = b,
                                 alpha = 0.5, size = 0.2)
data_plot_with_fit.save('iris_collected_data_with_fit_plot.png')