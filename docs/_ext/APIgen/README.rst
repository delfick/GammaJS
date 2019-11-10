Author : Stephen Moore <delfick755@gmail.com>

APIGen
======

ApiGen is a tool based off YUIDoc (http://developer.yahoo.com/yui/yuidoc/) that
is used to look at JavaScript code and create API documentation.

It does this by looking for particular expressive comments (using a style
similar to JavaDoc) to discover how the application is structured.
This is done instead of getting the data straight from the code so that the
programmer may not be tied to any particular way of writing their code,
which in JavaScript, can vary quite significantly.

APIGen differs form YUIDoc in that it uses python Objects to store information,
rather than in a single massive Json object.
This allows us to customize behaviour in a much less hacky fashion.
It also differs in that it outputs restructuredText instead of html, which can
then be fed to sphinx (http://sphinx.pocoo.org/) to create html from.

I also use django templates rather than Jinja. This is because I find it easier
to work with django templates and I find any performance concerns irrelevant
and insignificant.

It is also designed to be a lot more modular and easier to customize.

Current State
=============

Currently it works, however I believe it could be a lot better.

It uses a hard-coded central dispatcher when it parses documents
(found in parser.py/Parser/parse) to register the information with all the
container objects. Whilst this is a massive improvement over the 523 line
function that YUIDoc has for the same purpose (I split it into many functions),
I believe it still could be a lot better.

I also believe that whilst the container objects (most of containers.py) serve
their purpose quite well, they still seem a little hacky, and need some love and
attention.

Planned Future
==============

I plan to make APIGen it's own project that is seperate to Gamma, make it a lot
more elegant and make it available for anyone to use.

I plan to make it so the container objects are asked to determine what to do
with the comments as they are parsed instead of some hardcoded dispatcher.
I believe this will allow custom tags that mean different things to different
other tags/contexts to be a lot easier to add/implement.

I also plan to make the container objects a lot more declerative and elegant.

Beyond those two main points, I haven't put much more thought into what I plan
for APIGen due to a complete lack of time.

Usage
=====

Look at main.py
