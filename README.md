### Requirements
    Install docker, docker-engine and docker-compose (> 1.8)

Metaviz.py is a python helper script to run docker containers.


### Password Change:
It is recommended to change the default password used for setting up neo4j and other services in the docker compose.yml file.


### Available commands:
<command>           <description>                   <params>
`build`         Build all containers                  None
`serve`         Load all containers                   None
`add`           Add a new datasource            <file location> <datasource name>
                    neo4j database  
`restart`       restarts a docker service           <docker service>    

### Helper function

`python metaviz.py -h` lists available options and commands you can run.

Help functions are also available for individual commands

example

`python metaviz.py add -h` 


### Docker services and port mapping
<service>                <port>                    <description>
    ui           http://localhost:5500          Metaviz UI container
    api          http://localhost:5000/api      python data provider
    db           http://localhost:7474          neo4j database


### To update subtree
`ui -> git subtree pull --prefix=metaviz_ui/ui http://github.com/epiviz/epiviz metaviz-4.1`
