.. _install:

Quick install guide
===================

The Gamma Javascript library requires a browser that supports WebGL.
The nightly builds of
`Firefox <http://en.wikipedia.org/wiki/Mozilla_Firefox>`_,
`Chromium <http://en.wikipedia.org/wiki/Chromium_(web_browser)>`_,
and `Safari <http://en.wikipedia.org/wiki/Safari_(web_browser)>`_ support
`WebGL <http://en.wikipedia.org/wiki/WebGL>`_.
Information about getting a WebGL enabled browser is maintained on the
`khronos website <http://www.khronos.org/webgl/wiki/Getting_a_WebGL_Implementation>`_.

Using Gamma
-----------

This page will show you how to use the minified version of Gamma.
If you need the full source (for debugging) follow the instructions
:ref:`to set up a development environment <advancedInstall>`. OK, let's go:

* Create a HTML file with the following text It will be used to load in the
  necessary JavaScript and CSS. This can be named whatever you want.

    .. code-block:: html

        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
        <head>

            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <title>My Awesome Game</title>

            <!--
                Include any style sheets here
                <link rel="stylesheet" type="text/css" href="gamma.css" media="all"/>
            -->

            <!-- Include the Gamma Library -->
            <script type="text/javascript" src="gma-min.js"></script>

        </head>

        <body>

            <!-- The element to contain the rendering canvas is called #gamma by default -->
            <div id="gamma"></div>

            <!-- This javascript file contains the game specification -->
            <script type="text/javascript" src="game.js"></script>

        </body>
        </html>

* `Download gamma <https://github.com/downloads/Royce/GammaJS/gma-min.js>`_
  and place the gma-min.js file in the same directory as the HTML file you just
  created.

* Create a JavaScript file that holds the JavaScript that defines and starts
  your game. We'll call this file ``game.js``.
  The minimal JavaScript should contain:

  .. code-block:: javascript

      require(['gma/base', 'gma/manager'],

          function(gma) {
              // The game specification is contained within this function.
              var manager = gma.manager();
              manager.storeLevels({});
              manager.init();
          }
      );

  .. note:: If you want the game file to be called something else, then make
    sure to edit the HTML (above) so that it includes the correct file.
    Look for ``<script type="text/javascript" src="game.js"></script>``.

Now you've setup all that is necessary to create your game. Let's get started
with a tutorial :ref:`making a simple game <tutorials>`.

Enjoy :D
