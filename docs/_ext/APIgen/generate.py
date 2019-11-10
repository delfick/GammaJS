########################
###
###   IMPORTS
###
########################

    ########################
    ###   BUILTIN
    ########################
    
from datetime import date
import codecs
import shutil
import time
import sys
import re
import os

    ########################
    ###   LOCAL
    ########################

from APIgen.utility import mkdir
from APIgen.containers import *
from APIgen.const import *

    ########################
    ###   LOGGING
    ########################

import logging, logging.config

try:
    logging.config.fileConfig(os.path.join(sys.path[0], LOGCONFIG))
except:
    pass

log = logging.getLogger('parser.generate')

here = os.sep.join(__file__.split(os.sep)[:-1])

########################
###
###   TEMPLATES
###
########################

def createPage(filename, templates, context):
    from django.template import loader

    t = loader.select_template(templates)
    with open(filename, "w") as f:
        log.info("Creating page %s" % filename)
        f.write(t.render(context))

########################
###
###   GENERATOR
###
########################

class Generator(object):

    def __init__(self
        , outDir   = os.path.join(here, "docs")
        , tempdir  = os.path.join(here, "tmp")
        , assetDirs    = None
        , showPrivate  = False
        , templateDirs = None
        ):
        
        self.outDir       = os.path.abspath(outDir)
        self.tempDir      = os.path.abspath(tempdir)
        self.assetDirs    = []
        self.showPrivate  = showPrivate
        self.templateDirs = templateDirs
        if not self.templateDirs:
            self.templateDirs = [os.path.join(here, "templates"), ""]
        
        for new, onKls in [(templateDirs, self.templateDirs), (assetDirs, self.assetDirs)]:
            if new:
                if isinstance(new, str):
                    new = (new, )
                
                for directory in new:
                    directory = os.path.abspath(directory)
                    if os.path.exists(directory) and directory not in onKls:
                        onKls.append(directory)

    ########################
    ###   UTILITY
    ########################

    def createPage(self, information, filename, templates, **context):
        context['information'] = information
        filename = os.path.join(self.outDir, filename)
        if isinstance(templates, str):
            templates = (templates, )
        createPage(filename, templates, context)
    
    ########################
    ###   PROCESS
    ########################

    def process(self, information):
        # Setup django for templates
        os.environ['DJANGO_SETTINGS_MODULE'] = "APIgen.django_settings"

        import django
        django.setup()

        from django.conf import settings
        settings.TEMPLATES = [
              { 'BACKEND': 'django.template.backends.django.DjangoTemplates'
              , "DIRS": self.templateDirs
              , "APP_DIRS": False
              }
            ]
        
        # Reset temp dir        
        if os.path.exists(self.tempDir):
            shutil.rmtree(self.tempDir)
        
        # Make sure we have out and temp directories
        mkdir(self.outDir)
        mkdir(self.tempDir)

        # Copy assets to output
        for directory in self.assetDirs:
            shutil.copytree(directory, self.tempDir, ignore=shutil.ignore_patterns(IGNORE_PATTERNS))

        log.info("\n---------------------GENERATING------------------------\n")
        
        for module in information[MODULES].values():
            self.gen_module(information, module)
            
        log.info("\n---------------------DONE------------------------\n")
    
    def gen_module(self, information, module):
        moduleName = module[NAME]
        self.createPage(
              information
            , "%s.rst" % moduleName
            , [ os.sep.join(['modules', moduleName, 'module.rst'])
              , 'module.rst'
              ]
            , module = module
            , current = module
            , fullname = moduleName
            )
        
        moduleDir = os.path.join(self.outDir, moduleName)
        mkdir(moduleDir)
        
        for kls in module[CLASS_LIST]:
            klsName = kls[NAME]
            fullName = "%s.%s" % (moduleName, klsName)
            if moduleName == klsName:
                fullName = klsName
                
            self.createPage(
                  information
                , os.sep.join([moduleName, "%s.rst" % klsName])
                , [ os.sep.join(["classes", "%s.rst" % klsName])
                  , os.sep.join(["classes", moduleName, "%s.rst" % klsName])
                  , os.sep.join(["modules", moduleName, "class.rst"])
                  , os.sep.join(["modules", moduleName, "classes", "%s.rst" % klsName])
                  , "class.rst"
                  ]
                , module = module
                , current = kls
                , fullname = fullName
                )
                
        
