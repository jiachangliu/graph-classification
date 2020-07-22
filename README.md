# graph-classification 

A collection of graph classiifcation methods.

All methods are more or less modified to accept graph data from [https://ls11-www.cs.tu-dortmund.de/staff/morris/graphkerneldatasets]() 
Codes are adapted from [https://github.com/fanyun-sun/graph-classification]() and [https://github.com/horacepan/MLGkernel]()

Download data to `./data` and refer to `go.sh` under every directory for example usage.
To compile successfully, it's better to do a full compiling by doing both "make clean" and "make all"

Methods
* DGK: [Deep Graph Kernels](http://www.mit.edu/~pinary/kdd/YanVis15.pdf) [[source](http://www.mit.edu/~pinary/kdd/)]
* MLGkernel: [Multiscale Laplacian Graph Kernel](https://arxiv.org/abs/1603.06186) [[source](https://github.com/horacepan/MLGkernel)]
* graph2vec\_tf: [graph2vec: Learning distributed representations of graphs](https://arxiv.org/pdf/1707.05005.pdf) [[source](https://github.com/MLDroid/graph2vec_tf)]
* diffpool: [Hierarchical Graph Representation Learning with Differentiable Pooling](https://arxiv.org/pdf/1806.08804.pdf) [[source](https://github.com/RexYing/diffpool)]
* sub2vec: [Sub2Vec: Feature Learning for Subgraphs](http://people.cs.vt.edu/~badityap/papers/sub2vec-pakdd18.pdf) [[source](http://people.cs.vt.edu/~bijaya/)]
* kcnn: [Kernel Graph Convolutional Neural Networks](https://link.springer.com/chapter/10.1007/978-3-030-01418-6_3) [[source](https://github.com/giannisnik/cnn-graph-classification)]
* kernel\_methods: Various graph kernels implementation using [GraKel](https://github.com/ysig/GraKeL)
