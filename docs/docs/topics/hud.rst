Create a HUD
============

A HUD, or Heads Up Display, is a place where information about the game and
the user can be displayed whilst the game is being played. This is usually
textually based data and doesn't need to be rendered in 3D, which means we can
take advantage of the fact that the game is a in a webpage and provide the heads
up display using html and css.

Gamma provides the :api:`gma.hud` object, which will create the necessary html
for you and insert it into your webpage at runtime. It is then up to the
programmer to supply the necessary css such that the HUD appears where desired.

.. note:: An instance of :api:`gma.hud` is created for you when you create the
    manager and can be found on :prop:`manager.hud <gma.manager.hud>`

Structure of the HUD
--------------------

A HUD is broken down into sections which contain parts. Each part can hold one
or more items of information.

When the HUD is created, each section will be a ``div`` element. Each part
within this section will be a ``dl`` list and each item of information within
this will contain a ``dt``, ``dd`` pair.

Specifying the HUD
------------------

By default, there is no HUD and it is only after one is specified that any html
will be created for the HUD. To specify a hud in your game, you must call
:metho:`gma.hud.setup` on :prop:`manager.hud <gma.manager.hud>` with a
specification of what information you want displayed:

.. code-block:: javascript

    manager.hud.setup(specification);

Specifying Sections
++++++++++++++++++++

The specification is a Javascript object which contains both keys and values.
The keys specify the sections/parts to create and the value holds a javascript
object which contains the information you wish to be displayed:

.. code-block:: javascript

    var specification = {
        section1_part1: {},
        section1_part2: {}
    };

Each key must has an underscore in it's name. This is used to split the name
into two parts. The first part is the name of the section this part belongs to
and the second part is the name of the part itself.

The previous example would generate the following html:

.. code-block:: html

    <div id="section1_hud">
        <dl class="part1">
        </dl>

        <dl class="part2">
        </dl>
    </div>

As you shown above, each section is assigned an ``id`` of the first part of the
key with the string "\_hud", and each section contains a ``class`` attribute
equal to the second part of the key.

Specifiying information
++++++++++++++++++++++++

The information is a javascript object which contains a label with either a
value or a function:

.. code-block:: javascript

    {
        section1_part1: {
            item1 : 5
            item2 : "hi"
        },
        section1_part2: {
            item1 : function() { return new Date() }
        },

        section2_part1: {
            tHiNg : "blah"
        }
    }

If the value is static (i.e. not a function), then it will never be updated once
the HUD is created. However if you specify a function, then everytime the HUD
is refreshed (which happens as part of the :term:`Game Loop`), then the HUD will
be updated to reflect the result of calling the function again.

The example above information will generate the following html:

.. code-block:: html

    <div id="section1_hud">
        <dl class="part1">
            <dt id="hud_item1"><span>item1</span></dt>
            <dd>5</dd>

            <dt id="hud_item2"><span>item2</span></dt>
            <dd>hi</dd>
        </dl>

        <dl class="part2">
            <dt id="hud_item1"><span>item1</span></dt>
            <dd>Wed Oct 13 2010 21:57:41 GMT+0800 (WST)</dd>
        </dl>
    </div>

    <div id="section2_hud">
        <dl class="part1">
            <dt id="hud_thing"><span>tHiNg</span></dt>
            <dd>blah</dd>
        </dl>
    </div>

The dt generated will have an ``id`` attribute equal to the name of the item,
lowercase, prepended by the string "hud\_" holding a span with the label of the
information as it's value. The dd that is created is then given the value of the
item.

.. _stylingHud:

Styling the HUD
---------------

Gamma does not specify how a HUD should appear, instead it only creates some
semantic html and lets the game developer create the necessary css to make the
HUD appear as desired.

Below is some example css that will look for a ``top_hud`` and ``bottom_hud``
sections, and turn them into a bar at the top and bottom of the screen
respectively. Each of these sections contain parts named ``left`` and ``right``,
each appearing at their respective sides of the bars.

.. code-block:: css

    /* Setup the bars */

    #top_hud, #bottom_hud {
      height:2em;
      position:absolute;
      left:0em;
      width:100%;
      background-color:black;
      color: white;
      background-color: rgba(0, 0, 0, 0.7);
    }

    #top_hud {
      top:0em;
    }
    #bottom_hud {
      bottom:0em;
    }

    /* Setup left and right part of each bar */

    #bottom_hud dl, #top_hud dl {
      margin: 0.3em;
    }

    #bottom_hud dl.left, #top_hud dl.left {
      float: left;
    }
    #bottom_hud dl.right, #top_hud dl.right {
      float: right;
    }

    /* Setup labels for each itme */

    #bottom_hud dt, #top_hud dt,
    #bottom_hud dd, #top_hud dd {
      display: inline-block;
      line-height: 1.4em;
      margin: 0;
    }

    #bottom_hud dt, #top_hud dt {
	    padding-right: 0.5em;
    }

    #bottom_hud dd, #top_hud dd {
      text-align: right;
    }
    dl.left dd {
      padding-right: 1em;
    }
    dl.right dt {
      padding-left: 1em;
    }

.. note:: The :api:`gma.hud` object will hide parts that don't contain items
    and sections that don't contain any parts

We could create a HUD that uses this structure with the following code:

.. code-block:: javascript

    /*global require */
    require(['gma/base', 'gma/manager'],

        function(gma) {
            var manager = gma.manager({
                width : 600,
                height : 500
            });

            manager.hud.setup({
                top_left: {
                    //manager.getFPS is a function
                    //that returns the current fps when called
                    time : manager.getFPS
                },

                top_right: {
                    score : 1
                },

                bottom_left: {
                    test : "hello"
                }
            });
        }
    );

Customising the Labels
----------------------

We can also do some nice tricks with our css to change the apearance of each
item's label. For example, making it hidden, so only the value is visible.

.. code-block:: css

    #hud_fps span {
      display:none;
    }

Then, once the span is hidden, we can also replace the label with an image.
For example, the following rules (assuming you have an `fps.png`)

.. code-block:: css

    #hud_fps span {
      display:none;
    }

    #hud_fps {
      display: block;
      background: transparent url(fps.png) no-repeat top left scroll;
      height: 18px;
      width: 18px;
      min-width: 18px;
      position: relative;
    }

Hiding and Showing the HUD
--------------------------

You can also programmatically hide sections and/or parts of the HUD, and if you
are so inclined, show them again with the HUD's :metho:`gma.hud.hide` and
:metho:`gma.hud.show` methods.

Without any arguments, these functions will be applied to the HUD as a whole.
Alternatively, you call them with a string that either is the name of the
section you want to operate on, or the name of the part prepended by the name
of it's section and an underscore.

For example, say we have a HUD setup in a similar way as shown in
:ref:`stylingHud`, and we wanted to hide the ``right`` part of the ``top``
section, then we would call :metho:`gma.hud.hide` with the string "top_right".

.. note:: If, after hiding a particular part of a section, there are no more
    parts in that section, then the entire section will be hidden
