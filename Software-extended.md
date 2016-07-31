## [Google deepdream](https://github.com/google/deepdream)
This repository contains IPython Notebook with sample code, complementing Google Research blog post about Neural Network art. See original gallery for more examples.

### Dependencies ###
This notebook is designed to have as few dependencies as possible:
- Standard Python scientific stack: NumPy, SciPy, PIL, IPython. Those libraries can also be installed as a part of one of the scientific - packages for Python, such as Anaconda or Canopy.
- Caffe deep learning framework
- Google protobuf library that is used for Caffe model manipulation.

### Models ###
not required. Just [start Jupyter](https://github.com/mrzl/MLDIY/wiki/Running-Jupyter-notebooks-remotely) open the browser and go.

## [neural-style](https://github.com/jcjohnson/neural-style)
This is a torch implementation of the paper A Neural Algorithm of Artistic Style by Leon A. Gatys, Alexander S. Ecker, and Matthias Bethge.
The paper presents an algorithm for combining the content of one image with the style of another image using convolutional neural networks.

### Depedencies ###
- torch7
- loadcaffe

### Models ###
Script downloads original VGG-19 model

## [synthesizing](https://github.com/Evolving-AI-Lab/synthesizing)
Synthesizing preferred inputs via deep generator networks.
This repository contains source code necessary to reproduce some of the main results in the paper:

### Dependencies ###
- Install Caffe
- Build the Python bindings for Caffe
- If you have an NVIDIA GPU, you can optionally build Caffe with the GPU option to make it run faster
- Make sure the path to your caffe/python folder in settings.py is correct
- Install ImageMagick command-line interface on your system.

### Models ###
Models are downloaded with a script
- BVLC reference CaffeNet: cd nets/caffenet
- BVLC GoogLeNet: cd nets/googlenet
- AlexNet CNN trained on MIT Places dataset

## [skip-thoughts](https://github.com/ryankiros/skip-thoughts)
Sent2Vec encoder and training code from the paper Skip-Thought Vectors.

### Dependencies ###
This code is written in python. To use it you will need:
- Python 2.7
- Theano 0.7
- NumPy and SciPy
- scikit-learn
- NLTK 3
- Keras (for Semantic-Relatedness experiments only)
- gensim (for vocabulary expansion when training new models)

### Model files ###
You will first need to download the model files and word embeddings. The embedding files (utable and btable) are quite large (>2GB) so make sure there is enough space available. The encoder vocabulary can be found in dictionary.txt.
links in the repo

## [text2image](https://github.com/emansim/text2image)
Generating Images from Captions with Attention
Code for paper Generating Images from Captions with Attention by Elman Mansimov, Emilio Parisotto, Jimmy Ba and Ruslan Salakhutdinov; ICLR 2016.
We introduce a model that generates image blobs from natural language descriptions. The proposed model iteratively draws patches on a canvas, while attending to the relevant words in the description.

### Dependencies ###
- Python 2.7
- Theano 0.7 (mostly tested using commit from June/July 2015)
- numpy and scipy
- h5py (HDF5 (>= 1.8.11))
- skip-thoughts

### Models? ###

### Data ###
Data sets are gigabytes big. there are several. links in the repo

## [neural-storyteller](https://github.com/ryankiros/neural-storyteller) ##

neural-storyteller is a recurrent neural network that generates little stories about images. This repository contains code for generating stories with your own images, as well as instructions for training new models.

### The whole approach contains 4 components: ###

- skip-thought vectors
- image-sentence embeddings
- conditional neural language models
- style shifting (described in this project)

### Dependencies ###
This code is written in python. To use it you will need:
- Python 2.7
- A recent version of NumPy and SciPy
- Lasagne
- A version of Theano that Lasagne supports

### Models? ###
