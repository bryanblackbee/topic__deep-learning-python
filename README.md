# Deep Learning with Python Study Notes
A stack of study notes for deep learning.
## References
The following textbooks are used for topical references. The book short-form e.g. `DLwP` will be used as the book title reference in chapter descriptions. If you think the notebooks are insufficient for learning / implementation, please refer to the textbook topics directly.

- Deep Learning with Python (François Chollet, 2018) --> `DLwP`
- Hands-On Machine Learning with Scikit-Learn (Geron, 2019) --> `HandsML`

## Chapters

### 2. The Mathematical Building Blocks of Neural Networks
2.1 shows the implementation of a neural network to solve the **handwritten-digit** MNIST problem, a popular classification problem in the deep learning space.

2.2 introduces concepts in neural networks, including tensors, tensor operations (element-wise, dot product, broadcasting, reshaping), mini-batch SGD and backpropogation that are useful to understand how the MNIST problem in 2.1 is solved.
#### 2.1 - The MNIST Problem
- `DLwP`
    - Chap 2.1
#### 2.2 - Intoduction to Tensors & Tensor Operations
- `DLwP`
    - Chap 2.2, 2.3, 3.4, 2.5
    
### 3. Getting Started with Neural Networks
#### 3.1 - Anatomy of a Neural Network
3.1 introduces the key concepts of a neural network, including layers, networks, loss functions and optimisers.
- `DLwP`
    - Chap 3.1
#### 3.2 - Binary Classification
3.2 is a binary classification example (the **reviews** problem)
- `DLwP`
    - Chap 3.4
#### 3.3 - Multiclass Classification
3.3a is an applied Multiclass Classification on the **reuters** problem. This introuduces the Keras implementation to solve the problem.

3.3b is an another applied Multiclass Classification on the **fashion** problem. This introduces training using `tf2.keras`.
##### 3.3a
- `DLwP`
    - Chap 3.5
##### 3.3b
- `HandsML` 
    - Chapter 10
        - Building an Image Classifier Using the Sequential API
#### 3.4 - Regression
3.4 is an applied Regression (the **housing prices** problem) using the Keras implementation. There are both implmentations using Keras and `tf2.keras`. Since the problem involves a small dataset, this problem also involves k-fold validation.
- `DLwP`
    - Chap 3.6
- `HandsML` 
    - Chapter 10
        - Building a Regression MLP Using the Sequential API
    
### 4. Fundamentals of Machine Learning
Here, some key concepts of general machine learning are covered. They cover the overview for 
- branches of ML
- train-test split / k-fold cross-validation and Model Evaluation
- Data Preprocessing for neural networks
- Overfitting, Underfitting, Model Selection and Regularisation
- The ML Workflow

#### 4.1 - ML Fundamentals
- `DLwP`
    - Chap 4.1, 4.2, 4.3
    
#### 4.2 - The ML Workflow
- `DLwP`
    - Chap 4.4, 4.5

### 5. Deep Learning for Computer Vision
#### 5.1
5.1 introduces the convolutional neural network (CNN) and applies it to the **handwritten-digit** problem. It then explains the key concepts of the CNN including convolution layers and maxpooling layers.
- `DLwP`
    - Chap 5.1
#### 5.2
5.2 introduces training a small CNN from scratch to tackle the **dogs-vs-cats** Kaggle problem. It also introduces the concepts of generating new images using data augmentation.
- `DLwP`
    - Chap 5.2
#### 5.3
5.3 introduces the concept of using a pretrained convnet to tackle the **dogs-vs-cats** problem. In particular, it introduces the method of feature extraction using a pretrained convolutional base, and finetuning the last layer(s) of the convolutional base before classification.
- `DLwP`
    - Chap 5.3
#### 5.4
5.4 allows us to peek into what a convnet learns. In particular, activations of intermediate layers, studying the filters and looking at heatmaps of class activation.
- `DLwP`
    - Chap 5.4

### 6. Deep Learning for Text and Sequences

#### 6.1
6.1 explores using word embeddings to handle the **reviews** classification problem. It adds a preprocessing step called word embedding to learn semantic relationship between words. Furthermore, it introduces using pretrained word embeddings to learn from more generic semantic relationships, much like using a pretrained convnet in chapter 5.
- `DLwP`
    - Chap 6.1
    
### 7. Advanced Deep Learning Best Practices    
#### 7.1 - The Keras Functional API
- `DLwP` 
    - Chap 7.1
- `HandsML` 
    - Chapter 10
        - Building Complex Models Using the Functional API
        - Building Dynamic Models Using the Subclassing API
        - Saving and Restoring a Model
#### 7.2 - Callbacks & TensorBoard
- `DLwP` 
    - Chap 7.2
- `HandsML` 
    - Chapter 10
        - Using Callbacks
        - Visualization using TensorBoard    