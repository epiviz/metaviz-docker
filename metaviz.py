#!/usr/bin/python

import sys
import argparse
import subprocess
from shutil import copyfile, move, copy2
from os.path import basename
import json
from time import sleep

class MetavizParser(object):

    def __init__(self):

        parser = argparse.ArgumentParser(
            description = 'Build tool for metaviz',
            usage = '''
                metaviz <command> [<args>]

                Available commands are:
                    build       Build all docker containers
                    serve       Run existing docker instances
                    add         Add new datasource to the existing graph database instance
                    restart     Restarts a docker instance

                Docker compose containers and port mapping:
                    Name                port                        description
                    ui           http://localhost:5500       Metaviz UI container
                    api          http://localhost:5000/api   python data provider
                    db           http://localhost:7474       neo4j database
            ''')

        parser.add_argument('command', help = 'command to run. check help for individual commands', choices=['build', 'serve', 'add', 'restart'])
        args = parser.parse_args(sys.argv[1:2])
        getattr(self, args.command)()

    def build(self):

        # TODO: build takes list of containers
        # ?? set username and password for neo4j ??

        parser = argparse.ArgumentParser(description = 'Build all metaviz containers')
        args = parser.parse_args(sys.argv[2:])
        try:
            subprocess.check_call(['docker-compose', 'build', '--no-cache'])
        except Exception as e:
            print('docker-compose error')
            sys.exit(1)

    def serve(self):

        # TODO: serve takes list of containers

        parser = argparse.ArgumentParser(description = 'Serve existing data from neo4j instance and run ui')
        args = parser.parse_args(sys.argv[2:])
        try:
            subprocess.check_call(['docker-compose', 'up', '-d', 'ui'])
            # subprocess.check_call(['docker-compose', 'restart', 'ui'])
        except Exception as e:
            print('docker-compose error')
            sys.exit(1)

    def restart(self):

        # TODO: restart takes list of containers

        parser = argparse.ArgumentParser(description = 'restart a docker container')
        parser.add_argument('container', help = 'container to restart', choices = ['db', 'api', 'ui'])
        args = parser.parse_args(sys.argv[2:])
        try:
            subprocess.check_call(['docker-compose', 'restart', args.container])
        except Exception as e:
            print('docker-compose error')
            sys.exit(1)

    def add(self):

        parser = argparse.ArgumentParser(description = 'Add new data source to neo4j')
        parser.add_argument('file', help = 'biom file location')
        parser.add_argument('datasourceName', help='biom file name', nargs="?")
        args = parser.parse_args(sys.argv[2:])
        try:

            print "stopping Bioconductor container if running..."
            subprocess.check_call(['docker-compose', 'stop', 'bioc'])

            print "start Neo4j database container if not running..."
            # start if not running already
            subprocess.check_call(['docker-compose', 'up', '-d', 'db'])
            sleep(30)

            # read input file, copy file to bioc volume
            fname = basename(args.file)
            copy2(args.file, "./bioc_docker/db/data.biom")

            # load existing site-settings from ui volume
            with open('metaviz_ui/site-ds.json') as site_ds:
                f = site_ds.read()
                data = json.loads(f)

            ds = args.datasourceName

            if not ds:
                ds = fname

            # add new data source
            data.append({
                "dataProvider": "epiviz.data.EpivizApiDataProvider",
                "datasourceName": ds,
                "url": "http://localhost:5000/api/",
                "metadata": [],
                "icicleDepth": 3,
                "icicleAggregation": {
                    "3": 2
                }
            })

            # backup site-config
            with open('metaviz_ui/site-ds.json', 'w') as site_ds:
                json.dump(data, site_ds)

            # write new site-settings file

            settingsStr = "epiviz.Config.SETTINGS.dataServerLocation = 'http://metaviz.cbcb.umd.edu/data/';"
            settingsStr = settingsStr + "epiviz.Config.SETTINGS.dataProviders = ["

            for d in data:
                print d
                temp = ["'epiviz.data.EpivizApiDataProvider'", '"{}"'.format(str(d['datasourceName'])) , '"{}"'.format(str(d['url'])) , '[]', str(3), "{'3': 2}"]
                tempStr = ",".join(temp)
                settingsStr = settingsStr + "[" + tempStr + "],"
            
            settingsStr = settingsStr[:-1]
            settingsStr = settingsStr + "];"
            settingsStr = settingsStr + "epiviz.Config.SETTINGS.workspacesDataProvider = sprintf('epiviz.data.WebServerDataProvider,%s,%s','workspaces_provider','http://metaviz.cbcb.umd.edu/data/main.php');"
        
            with open('metaviz_ui/ui/site-settings.js', 'w') as site_js:
                site_js.write(settingsStr)

	    with open('bioc_docker/db/dbname.txt', 'w') as neo_dbname:
		neo_dbname.write(ds)

            subprocess.check_call(['docker-compose', 'build', '--no-cache', 'bioc'])
            subprocess.check_call(['docker-compose', 'up', '-d', 'bioc'])
            subprocess.check_call(['docker-compose', 'stop', 'ui'])
            subprocess.check_call(['docker-compose', 'build', '--no-cache', 'ui'])
            subprocess.check_call(['docker-compose', 'up', '-d', 'ui'])
            print "please Wait for the R scipt to finish loading the biom file"
            print "to check the status - `docker-compose logs bioc`"

            print "open localhost:5500 in your browser to run metaviz"
        except Exception as e:
            print e
            sys.exit(1)

if __name__ == "__main__":
    MetavizParser()

