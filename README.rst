Figures plugin for `Tutor <https://docs.tutor.overhang.io>`_
============================================================

⚠️ THIS PLUGIN IS IN MAINTENANCE MODE. Because the underlying Figures application lags behind the latest Open edX release, we are unable to provide continued support for this plugin. If you manage to get Figures to work on Koa (Tutor v11) and later, please open a pull request on this repository to share your findings.

`Figures <https://github.com/appsembler/figures>`_ is a data retrieval and reporting app for Open edX; this is a plugin for Tutor that allows quick and easy integration in an Open edX platform. It works both locally and on a Kubernetes-based platform.

This plugin was developed and open sourced to the community thanks to the generous support of `E-ducation <https://www.e-ducation.cn/>`_. Thank you!

Installation
------------

This plugin requires tutor>=3.5.0. Also, you should have installed tutor from source, and not from a pre-compiled binary.

::

    pip install tutor-figures

Then, to enable this plugin, run::

    tutor plugins enable figures

You will have to re-generate the environment and rebuild the "openedx" docker image::

    tutor config save
    tutor images build openedx

You will then have to run LMS migrations. To do so, run::

    tutor local init

This last step is unnecessary if you run instead ``tutor local launch``.

You should then be able to access the Figures dashboard at ``http://<your lms host>/figures``. On a local instance, you should be able to access it at http://localhost/figures.

Installing a fork of Figures
----------------------------

By default, Figures is installed from `Appsembler's repository <https://github.com/appsembler/figures.git>`__. To change this, you can define the repository and version at build time::

    tutor images build \
        --build-arg FIGURES_REPOSITORY=git+https://github.com/myusername/figures.git \
        --build-arg FIGURES_VERSION=alpha \
        openedx
