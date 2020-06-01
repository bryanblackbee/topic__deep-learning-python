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
#### 3.5 - Building Complex and Dynamic Models
3.5 is a topic deep dive for TF, including building more complex and dynamic NN architectures, saving / loading a model, using callbacks during training and visualising training results using Tensorboard.
- `HandsML` 
    - Chapter 10
        - Building Complex Models Using the Functional API
        - Building Dynamic Models Using the Subclassing API
        - Saving and Restoring a Model
        - Using Callbacks
        - Visualization using TensorBoard
    
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