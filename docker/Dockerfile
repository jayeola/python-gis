FROM fedora:35
ENV MINICONDA_URL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
ENV MY_USER  tester
ENV HOME /home/tester
ENV PATH $HOME/miniconda/bin/:$PATH

RUN dnf update --refresh -y && \
    dnf clean all

RUN dnf install -y \
    bzip2 \
    boost-devel \
    coin-or-Ipopt-devel \
    eigen3-devel \
    ninja-build \
    pybind11-devel \
    vim-minimal && \
    dnf groupinstall -y 'Development Tools' && \
    dnf clean all && \
    rm -rf /var/cache/dnf

SHELL [ "/bin/bash", "-l", "-c" ]
RUN useradd $MY_USER
USER $MY_USER
WORKDIR $HOME

RUN curl $MINICONDA_URL -o $HOME/miniconda.sh && \
    bash $HOME/miniconda.sh -b -p $HOME/miniconda && \
    rm -f $HOME/miniconda.sh

RUN source $HOME/miniconda/bin/activate && \
    conda clean --all --verbose --yes && \
    conda update conda --verbose --yes && \
    conda install --verbose --yes \
    ipython \
    mkl-devel \
    numpy \
    scipy \
    pandas \
    tbb-devel \
    matplotlib \
    scikit-learn \
    networkx \
    bokeh \
    jupyter \
    statsmodels && \
    conda install -y -c conda-forge pyspark && \
    conda install -y -c conda-forge geopandas && \
    conda install -y -c conda-forge cartopy

RUN pip  install dash && \
    pip  install dash-renderer && \
    pip  install dash-html-components && \
    pip  install dash-core-components && \
    pip  install plotly --upgrade

#ADD projects /home/tester/projects
#ADD test-dir /home/tester/test-dir
#
#USER root
#RUN chown -R $MY_USER:$MY_USER /home/tester/projects /home/tester/test-dir
#USER $MY_USER
EXPOSE 8000
