FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary dependence
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get install -y openjdk-8-jdk git wget unzip curl pip libdbi-perl subversion vim && \
    echo "export _JAVA_OPTIONS=-Xverify:none" >> ~/.bashrc && \
    export export _JAVA_OPTIONS=-Xverify:none

# Install Defects4j v2.0
RUN git clone https://github.com/rjust/defects4j.git && \
    cd defects4j && \
    ./init.sh && \
    echo "export PATH=\$PATH:/defects4j/framework/bin" >> ~/.bashrc && \
    export PATH=$PATH:/defects4j/framework/bin

# Install CatenaD4J
RUN git clone https://github.com/universetraveller/CatenaD4J.git && \
    echo "export PATH=\$PATH:/CatenaD4J" >> ~/.bashrc && \
    export PATH=$PATH:/CatenaD4J && \
    echo "export DEFECTS4J_HOME=/defects4j" >> ~/.bashrc && \
    export DEFECTS4J_HOME=/defects4j

# Set Working Director
WORKDIR /

# Default container initialization
CMD ["/bin/bash && source ~/.bashrc"]
