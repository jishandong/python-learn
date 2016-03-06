'read confige file '
from configparser import ConfigParser
import sys
cfg = ConfigParser()
print(cfg.read('C:\Python34\learn\config.ini'))
print(cfg.sections())
print(cfg.get('installation','library'))
print(cfg.getboolean('debug','log_errors'))
print(cfg.getint('server','port'))
print(cfg.get('server','signature'))
cfg.set('server','port','9090')
print (cfg.write(sys.stdout))
