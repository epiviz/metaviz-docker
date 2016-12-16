# imports if not using the bioconductor docker image
# source("https://bioconductor.org/biocLite.R")
# biocLite()

# install metavizr dependencies
# BiocInstaller::biocLite(c("metagenomeSeq", "biomformat", "epivizrStandalone"))

BiocInstaller::biocLite(c("biomformat", "devtools", "epiviz/metavizr@demo"), quiet=TRUE)

# # since metavizr is not in bioconductor, install from github
# install.packages("devtools")
# library(devtools)
# install_github("epiviz/metavizr@demo")

install.packages(c("RNeo4j", "RColorBrewer"), quiet=TRUE)

library(metavizr)
library(metagenomeSeq)
library(biomformat)
library(RNeo4j)

# load biom files
if(!file.exists("data.biom")) {
    stop("Biom file does not exist")
}

import_biom = load_biom("data.biom")

meta_obj = metavizr:::EpivizMetagenomicsData(import_biom)

db = Sys.getenv("NEO4J_DB")
db_user = Sys.getenv("NEO4J_USER")
db_pass = Sys.getenv("NEO4J_PASS")

## TODO: Get server URL of the neo4j instance
graph = startGraph(paste0(db, "/db/data/"), username=db_user, password=db_pass)

meta_obj$toNEO4JDb(graph)