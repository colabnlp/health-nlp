import configparser

config = configparser.RawConfigParser()
config.read('./project.cfg')

solr_url = config.get('solr', 'url')
conn_string = "host='%s' dbname='%s' user='%s' password='%s' port=%s" % (config.get('pg', 'host'),
                                                                         config.get('pg', 'dbname'),
                                                                         config.get('pg', 'user'),
                                                                         config.get('pg', 'password'),
                                                                         str(config.get('pg', 'port')))

mongo_host = config.get('mongo', 'host')
mongo_port = int(config.get('mongo', 'port'))
mongo_db = config.get('mongo', 'db')
mongo_working_index = config.get('mongo', 'working_index')
mongo_working_collection = config.get('mongo', 'working_collection')

tmp_dir = config.get('tmp', 'dir')