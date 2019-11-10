.. _advancedInstall:

Developing with Gamma
=====================

Gamma is a modular library that is split into many files.
Whilst you can use a combined and :term:`minified` version of the library, as
shown in the :ref:`getting started section <install>`, it's a lot easier to
develop and debug your game if you can view the full source code.
This allows you to see the code where errors originate from and set breakpoints
in the Gamma library.

To make the process even easier, you can also
:ref:`use the development server <devServer>` found in the support directory of
the repository.
However, for just executing your game, you can just create a html file as
explained below. Either method still requires a copy of the source code, which
can be gotten by running ``git clone git://github.com/Royce/GammaJS.git``.

To make your own html boilerplate files :

* Follow the :ref:`getting started section <install>`.

* Download :ref:`RequireJS <requireJSNS>` from
  `here <http://requirejs.org/docs/release/0.2.1/minified/require-jquery-1.4.4.js>`_

* Get the ``libs.js`` from the ``support/lib/compiled`` directory.

* Inside ``game.html``, replace the ``head`` element with the following:

    .. code-block:: html

        <head>

            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <title>My Awesome Game</title>

            <!-- Include any style sheets here -->

            <!-- Tell requirejs where to find your code -->
            <script type="text/javascript">
                var require = {
                    baseUrl: "",
                    waitSeconds: 15
                };
            </script>

            <!-- Include the necessary libraries -->
            <script type="text/javascript" src="require.js"></script>
            <script type="text/javascript" src="libs.js"></script>

        </head>

* Change baseUrl to point to the folder that contains the ``gma`` folder.
  So if you have the following folder structure, then baseUrl would be "GammaJS".

    .. code-block:: javascript

        game.html
        game.js
        require.js
        libs.js
        GammaJS/
            gma/
            support/
            docs/
            examples/
            media/

* That's it!

Running the Tests
=================

To Run the tests, you must first preprocess them to convert them from the JSpec
dsl to normal javascript. For this to then work with RequireJS, we need to fetch
the tests, run the JSpec preprocessor over them and change the usage of require
to define a dependency name (we're lazy and don't think we should have to define
the dependency for each tests manually). Unfortunately this means XMLHttpRequest
errors unless everything is served using HTTP.

In turn, this means you need the development server to be able to run the tests.
However, once you have it setup, running the tests is literally as simple as
clicking a link.

.. _devServer:

Running the Development server
==============================

Different parts of the development server require some environment variables to
be set that point to where you have different parts of the code. If you keep the
same structure as found in the repository, then the following environment
variables should work.

.. code-block:: sh

    GMA = /path/to/GammaJS
    GMA_SRC = $GMA/gma
    GMA_SUPPORT = $GMA/support
    GMA_MEDIA = $GMA/media

To be able to run tests and examples:
    * Install python-setuptools
    * Use setuptools and do ``easy_install werkzeug paste django``
    * Execute ``run.sh`` found in the support folder and go to
      ``http://localhost:8000`` in your webgl enabled web browser.

To be able to run js-coverage (linux and mac only):
    * install autoconf and g++
    * ``svn co http://svn.siliconforks.com/jscoverage/trunk jscoverage``
    * ``cd jscoverage``
    * ``./bootstrap.sh``
    * ``make``
    * ``make install``
    * Execute ``coverage.sh`` inside the support directory
    * Go to the development server and either click the ``coverage`` link next
      to the test you want to get coverage data from. Or click the ``Coverage``
      button at the top of the page and choose your desired test from the drop
      down list.

To be able to make the documentation:
    * ``easy_install sphinx``
    * Go into the docs directory and run ``make html``

To build a minified, single file version of Gamma:
    * Install Java
    * Unzip the `RequireJS Optimisation tool <http://requirejs.org/docs/release/0.14.2/requirejs-0.14.2.zip>`_
      somewhere
    * Create an environment variable called ``REQUIRE`` that points to where you
      unzipped the optimisation tool
    * Run ``python build.py`` inside the support directory
    * The result can be found in $GMA_SUPPORT/lib/compiled

For an explanation of how it all works and general notes about the code, read
the readme files that exist inside the support folder.
