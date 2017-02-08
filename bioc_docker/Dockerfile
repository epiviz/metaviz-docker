FROM bioconductor/release_base
MAINTAINER "Jayaram Kancherla" jkanche@umiacs.umd.edu

RUN mkdir /rhome
COPY $PWD/db/data.biom /rhome
COPY $PWD/db/dbname.txt /rhome
COPY $PWD/scripts/myscript.R /rhome
WORKDIR /rhome

CMD ["Rscript", "myscript.R"]
# CMD ["true"]
