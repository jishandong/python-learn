'logging 模块'
import logging
def main():
    logging.basicConfig(
    filename='app.log',
    level=logging.ERROR
    )
    hostname='www.python.org'
    item = 'spam'
    filename ='data.csv'
    mode ='r'
    logging.critical('Host %s unknow',hostname)
    logging.error('Could not find %r',item)
    logging.warning('Feature is deprected')
    logging.info('opening file %r,more=%r',filename,mode)
    logging.debug('got here')
if __name__=='__main__':
    main()
