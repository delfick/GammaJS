Messages
========

Gamma provides the ability to display messages to the player through
:api:`gma.hud`.

.. note:: When you create an instance of :api:`gma.manager`, an instance of
    :api:`gma.hud` is created for you which you can access through
    :prop:`manager.hud <gma.manager.hud>`

The function :metho:`gma.hud.displayMessage` accepts a string to display:

.. code-block:: javascript

    manager.hud.displayMessage("Greetings, traveller");

Use :metho:`gma.hud.hideMessage` to remove the message:

.. code-block:: javascript

    manager.hud.hideMessage();

You can specify an amount of time for the message to be displayed, after which
the message is removed:

.. code-block:: javascript

    // Message is displayed for 1 second (1000 milliseconds)
    manager.hud.displayMessage("Look out!", 1000);

Finally, you may specify a function to be called when the message is removed:

.. code-block:: javascript

    // Message is displayed for 1 second (1000 milliseconds)
    // ... then the character jumps
    manager.hud.displayMessage("Watch out, its jumping time!", 1000, function() {
        character.jump();
    });


Style the messages
------------------

The message can be styled using CSS. Eg:

.. code-block:: css

    #message {
        font-family: Arial, san-serif;
        background-color:black;
        color: #99c;
        background-color: rgba(0, 0, 0, 0.7); /* CSS 3 transparencies */
    }
