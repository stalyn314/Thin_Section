<h1 align="center">Automatic description of rock thin sections: a web application</h1>
<p align="center"><font size="7">Stalyn Paucar, Christian Mejía-Escobar, Víctor Collaguazo</font></p>
<p align="center" style="font-size: 14;">Universidad Central del Ecuador-Facultad de Ingeniería en Geología, Minas, Petróleos y Ambiental</p>

<div align="center">
<img src="https://img.shields.io/badge/Transformer-blue?link=https%3A%2F%2Farxiv.org%2Fabs%2F1706.03762" alt="Static Badge">
<img src="https://img.shields.io/badge/Convolutional%20Neural%20Network-green" alt="Convolutional Neural Network Badge">
<img src="https://img.shields.io/badge/Rock%20Thin%20Sections-red" alt="Rock Thin Sections Badge">
<img src="https://img.shields.io/badge/Artificial%20Intelligence-yellow" alt="Artificial Intelligence Badge">
  
</div>

<p align="center">
  <img width="460" height="300" src="https://github.com/stalyn314/Thin_Section/blob/main/tested_image/T_08495.jpg?raw=true">
</p>

<!--(https://shields.io/badges/static-badge) -->



## What are rock thin sections

In petrography and optical mineralogy, a thin section is a fine slice of a rock or mineral sample (30 μm thick), prepared in a laboratory to be used with a petrographic microscope.

Thin sections provide detailed information about the mineralogical composition of rocks. They are essential for analyzing textures, which aids in interpreting their formation and the processes that have affected their evolution.

They are an indispensable tool for geologists, offering a window into the microscopic world of rocks and providing valuable information for research and understanding geological processes.

## Automatic description (Image Captioning)

The rise of Artificial Intelligence has sparked widespread interest across various scientific disciplines for data analysis, including images, videos, text, and numerical data, with the aim of improving efficiency in study and research processes. This approach has caught the attention of geology, which seeks to leverage these technologies to optimize the interpretation and analysis of geological data, especially in areas such as mineral identification, structures, and textures in rock samples.

The goal of automatic image captioning is to generate a coherent and fluent sentence that accurately describes the content of the image.

**Convolutional Neural Network**  
This is a type of network specifically designed to process data with a grid-like structure, such as images.
It is responsible for extracting features from the input image, such as the locations, sizes, and colors of objects.

**Transformer**  
This is a neural network architecture primarily designed for natural language processing tasks. It was first proposed in the paper *"Attention is All You Need"* in 2017 by Vaswani et al.
Instead of relying on recurrences or convolutions, the Transformer uses attention mechanisms to process input and output sequences in a parallel and efficient manner.
The Transformer has become the foundation for many state-of-the-art models in the field of natural language processing, including BERT and GPT.

## Project Code and Dataset

The code for this project can be found in the following Google Colab link:
<a href="https://colab.research.google.com/drive/11ZR1QGw1H8uCoN7g2dHZSyh7f8OeHUwH?usp=sharing">
  <img src="https://img.shields.io/badge/Open%20in-Google%20Colab-blue?logo=googlecolab&logoColor=white" alt="Open in Google Colab">
</a>

You can also explore the application here:
<a href="https://stalynpaucar271828.wixsite.com/auto-descripcion">
  <img src="https://img.shields.io/badge/Visit%20Auto%20Description%20App-brightgreen" alt="Visit Auto-Description Web App">
</a>

For further details, you can access the related paper:
<a href="https://arxiv.org/abs/2402.15039">
  <img src="https://img.shields.io/badge/Research%20Paper-%20arXiv-red" alt="Research Paper">
</a>

## Reference Repository

This repository is a modification of the [Image-Captioning](https://github.com/TomatoFT/Image-Captioning) repository, which in turn is based on the work by Nain, A. (2021) in *Image captioning* (Code examples-Computer Vision). The source code is available at: [https://keras.io/examples/vision/image_captioning/](https://keras.io/examples/vision/image_captioning/). 

Adjustments and improvements have been made to tailor it to the specific needs of this project.


