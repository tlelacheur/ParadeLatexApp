#!/usr/bin/env python
import sys
sys.path.insert(0,"var/www/html/ParadeLatexApp/gmcApp")

from views import app as application
application.secret_key = 'MrLashVsGMC'
