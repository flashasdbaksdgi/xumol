python -m pip install condacolab
python -c "import condacolab; condacolab.install()"

git clone https://github.com/flashasdbaksdgi/GeoMol.git

conda env create --file /content/GeoMol/devtools/environment.yml

source /usr/local/bin/activate GeoMol

python -m pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

PIP_VERBOSE=1 python -m pip install torch-scatter==2.0.5 torch-sparse==0.6.8  torch-geometric==1.6.3 -f https://pytorch-geometric.com/whl/torch-1.7.1.html

conda install cudatoolkit-dev=11.0 -n GeoMol -c conda-forge

pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

PIP_VERBOSE=1  FORCE_ONLY_CUDA=1  python -m pip install torch-sparse==0.6.9 torch-scatter==2.0.6  -f "https://pytorch-geometric.com/whl/torch-1.7.1%2Bcu110.html"

python -m pip install  torch-geometric==1.7.2 --force-reinstall