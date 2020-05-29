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
3.1 introduces the key concepts of a neural network, including layers, networks, loss functions and optimisers.

3.2 to 3.4 are worked examples in some machine learning examples 

- 3.2 is a binary classification example (the **reviews** problem)
- 3.3 is a multiclass classification example (the **reuters** problem)
- 3.3b is a multiclass classification example (the **fashion** problem)
- 3.4 is a regression example (the **housing prices** problem)

#### 3.1 - Anatomy of a Neural Network
- `DLwP`
    - Chap 3.1
#### 3.2 - Classifying Movie Reviews: A Binary Classification Example
- `DLwP`
    - Chap 3.4
#### 3.3 - Classifying newswires: A Multiclass Classification Example
- `DLwP`
    - Chap 3.5
- `HandsML`
    - Building an Image Classifier Using the Sequential API
#### 3.4 - Predicting House Prices: A Regression Example
- `DLwP`
    - Chap 3.6
- `HandsML`
    - Building a Regression MLP Using the Sequential API
    - Building Complex Models usin Using the Functional API
    - Building Dynamic Models usin Using the Subclassing API
    - Saving and Restoring a Model
    
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