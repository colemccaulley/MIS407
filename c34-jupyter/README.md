# Intro to Python Data Analytics

We are now in the last section of this course. In this section, we look at using the tools of Python to conduct data analysis. Next to R, Python is becoming one of the most popular platforms for conducting data analysis.

## The "big" four technologies

1. Jupyter Notebooks
2. Numpy
3. Pandas
4. Matplotlib (and other plotting libraries)


## Jupyter introduction

### iPython and Jupyter

#### iPython
iPython Is a command shell for interactive Python programming. It presents a more user-friendly interactive framework that the standard command line.

iPython evolved from command line interface to a fully fledged interactive development environment.

https://en.wikipedia.org/wiki/IPython

#### Project Jupyter

Jupyter is a spin-off project of IPython. Within jupyter, IPython is one of the many kernels for Jupyter. Jupyter attempts to provide a language-agnostic language-agnostic iPython notebook interface that supports many different languages (i.e. Julia, R, Haskell, Ruby, and lately, C++).

[Gallery of Interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#data-visualization-and-plotting)

## Jupyter Installation

There is specialized distribution of Python that focus on support for Jupyter, iPython and data analysis (i.e. Anaconda). One of the pros of such distributions is that many common libraries for data analysis are already included (some of which are difficult to install within the standard Python distribution). The cons include that these distros can also involve managing a separate package distribution and installation system (conda). To keep this simple, in this course we will be - and are using - the standard python distribution.

The instructions below apply only to the standard python distribution.


## Install Jupyter, Numpy, Pandas, Matplotlib, and Bokeh

__NOTE: These instructions are for Windows only.__

There are a few modules that we will commonly use when working with data in Jupyter -- Numpy, Scipy, Pandas, and MatplotLib.

Since these packages involve C code, there are binaries required for your specific operating system. Support for installing these libraries via pip has improved in the past couple of years, and they should be able to be installed by pip. Previously, users had to either compile binaries for their OS or download precompiled binaries for their specific platform (i.e. Windows 10 x64). If you run into trouble using pip to install these packages on your Windows platform, you can find pre-build binaries available as "wheel files" from the following site
 http://www.lfd.uci.edu/~gohlke/pythonlibs/

BUT, for our purposes, and platform, we should find that regular pip install commands work fine.

```
pip install numpy
pip install pandas
pip install jupyter
pip install matplotlib
```

Matplotlib has been around for sometime, and therefore, is well documented. But it is often considered difficult to work with (but, nonetheless, it is arguably the most versatile/powerful package for plotting and graphing), and could be made to look a little better. There are many new plotting libraries coming available for python and the jupyter environment. We'll use one called bokeh:

```
pip install bokeh
```

# Starting and using jupyter notebook

Jupyter is great for exploratory data analysis.

To start jupyter, from your bash prompt:

```
jupyter notebook
```

In class, I'll walk through a live example of how to work with Jupyter. If you need more information, there are plenty of resources out there - for instance, many your tube videos.


## Appendix:

Useful resources:

* https://github.com/wesm/pydata-book
* http://nbviewer.jupyter.org/
