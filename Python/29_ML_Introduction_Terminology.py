"""
Key Machine Learning Terminology

Descriptive - What Happened
Predictive - What will happen
Prescriptive - What to do 


Prediction can be of two types 
1. Continuous values ( Regression Model )
2. Discrete Values   ( Classification Model )


Label = variable we're predecting, typically represented by variable y
Feature = Input variables describing the data, represented by variables {x1,x2,x3....xn}
Model = Piece of Software or Mapping function ( maps examples to predicted labels )

ML = Process of training the Model for prediction on never-before-seen dataset

Supervised learning = Is a type of ML where the model is 
                      provided with labeled training data.

Example is a particular instance of data X
Labelled example has { feature,label } : {x,y}, it is used to train the model
UnLabelled example has { feature,? } : {x,?}, used to make predictions on new data 

Give ( Classification )Example of Spam Detection of Email to explain the below concept
In the spam detector example, the features could include the following:
    (feature)          words in the email text
    (feature)          sender's address
    (feature)          time of day the email was sent
    (feature)          email contains the phrase "one weird trick."
    (label )           Whether the email is SPAM or HAM

Another ( Regression )Example is the Housing Prices in Jaipur
housingMedianAge            (feature)
totalRooms                  (feature)
totalBedrooms               (feature)
medianHouseValue            (label)





Hands On 1:
Suppose you want to develop a supervised machine learning model to predict 
whether a given email is "spam" or "not spam." 
Which of the following statements are true? 

1. We'll use unlabeled examples to train the model. ( FALSE)
2. Emails not marked as "spam" or "not spam" are unlabeled examples ( TRUE)
3. Words in the subject header will make good labels. ( FALSE )
4. The labels applied to some examples might be unreliable. ( TRUE )


Hands On  2:
Suppose an online shoe store wants to create a supervised ML model that will 
provide personalized shoe recommendations to users. 
That is, the model will recommend certain pairs of shoes to Marty and different 
pairs of shoes to Janet. 
Which of the following statements are true? 
    
1. "Shoe beauty" is a useful feature. ( FALSE )
2. "The user clicked on the shoe's description" is a useful label. ( TRUE )
3. "Shoe size" is a useful feature. ( TRUE )
4. "Shoes that a user adores" is a useful label. ( FALSE )



Example of amateur botanist ( to define features and label)
Leaf Width 	Leaf Length 	Species
2.7 	    4.9 	        small-leaf
3.2 	    5.5 	        big-leaf
2.9 	    5.1 	        small-leaf
3.4 	    6.8 	        big-leaf

Leaf width and leaf length are the features (which is why they are both labeled X), 
while the species is the label.

Features are measurements or descriptions; the label is essentially the "answer."

For example, the goal of the data set is to help other botanists answer the question, 
"Which species is this plant?"




In Supervised Machine Learning

Training = Feeding the features and their corresponding labels into an algorithm

During training, the algorithm gradually determines the relationship (mapping fucntion)
between features and their corresponding labels. 
This relationship is called the model.


Real World Example of Supervised Learning
Study from Stanford University to detect skin cancer in images
training set contained images of skin labeled by dermatologists as having one of several diseases. 
The ML system found signals that indicate each disease from its training set
and used those signals to make predictions on new, unlabeled images.


In Unsupervised Machine Learning
In unsupervised learning, the goal is to identify meaningful patterns in the data. 
To accomplish this, the machine must learn from an unlabeled data set.
In other words, the model has no hints how to categorize each piece of data 
and must infer its own rules for doing so.


In Reinforcement Learning ( RL )
In RL you don't collect examples with labels.
Imagine you want to teach a machine to play a very basic video game and never lose. 
You set up the model (often called an agent in RL) with the game, and you tell 
the model not to get a "game over" screen. 
During training, the agent receives a reward when it performs this task, 
which is called a reward function. With reinforcement learning, 
the agent can learn very quickly how to outperform humans. 

However, designing a good reward function is difficult, and RL models are less stable 
and predictable than supervised approaches.
 

Types of ML Problems
    
    Type of ML Problem	Description	                  Example
Classification 	    Pick one of N labels 	      Cat, dog, horse, or bear

Regression 	        Predict numerical values 	  Click-through rate

Clustering 	        Group similar examples 	      Most relevant documents (unsupervised)

Association         Infer likely association      If you buy hamburger buns,
rule learning 	    patterns in data 	          you're likely to buy hamburgers (unsupervised)

Structured output 	Create complex output 	      Natural language parse trees, image recognition bounding boxes

Ranking 	        Identify position on a  	      Search result ranking
                    scale or status


How ML powers Google Photos: 
Find a specific photo by keyword search without manual tagging
ML powers the search behind Google Photos to classify people, places, and things.

Smart Reply Feature of Gmail

Give a use case of WholesaleBox Recommendation Old logic and
How we enabled it using Machine Learning Techniques

With these examples in mind ask yourself the following questions:

What problem is my product facing?
Would it be a good problem for ML?

ML is better at making decisions than giving you insights.

Prediction	
What video the learner wants to watch next.	

Decision
Show those videos in the recommendation bar.

"""



"""
# Show Image ML_SalesPriceVsFootage

Show the Graph of House Price ( label on Y axis ) and 
House Square Footage ( Feature on X Axis )

y = b  +  w1x1

Create a straight line so that the line tries to pass through all the points

Introduce the concept of loss and try to find the loss for those points which are not on the line

A convienient loss function for Regression 

L2 loss for a given example  is also called squared error
= square of the diff between prediction and label
= ( observation - prediciton )square 2
= (y - y') square 2

  

#Show the image of ML_Cricket.jpg

Data on chirps-per-minute and temperature
 
y' = w0 +   ( w1 * x1 ) 

y' = Predicted Label
w0 = bias
w1 = weight of feature x1
x1 = feature (input)
  

Training and Loss:
    
Training a model simply means learning (determining) good values for all the 
weights and the bias from labeled examples. 

In supervised learning, a machine learning algorithm builds a model by examining
many examples (training) and attempting to find a model that minimizes loss; 
this process is called empirical risk minimization.


Loss is the penalty for a bad prediction. 

That is, loss is a number indicating how bad the model's prediction was on a single example.

Loss Function = squared loss (also known as L2 loss)
= the square of the difference between the label and the prediction
= (observation - prediction(x))2
= (y - y')square 2

  

  

Mean square error (MSE) is the average squared loss per example over the whole dataset.
#https://medium.freecodecamp.org/machine-learning-mean-squared-error-regression-line-c7dde9a26b93

Code Challenge to find the MSE for a given datset


Show ML_MSE3.jpg

Let’s take 4 points, (-2,-3), (-1,-1), (1,2), (4,3).
Let’s find M and B for the equation y=mx+b.
Sum the x values and divide by n
xbar=(-2)+(-1)+1+4 / 4 = 1/2                     #Sum the x values and divide by n
ybar = (-3)+(-1)+2+3 / 4 = 1/4                   #Sum the y values and divide by n

xybar = (-2)*(-3) + (-1)*(-1) + 1*2 + 4*3 /4     #Sum the xy values and divide by n
      = 21 / 4
      
x square bar = 4 + 1 + 1 + 16  /4 = 11 / 2       #Sum the x² values and divide by n
      

Slope calculation
m = (21/4 - 1/2*1/4 ) / 11/2 - (1/2)²
  = 41/42
  
y-intercept calculation
b = 1/4 - 41/42*1/2
  = -5/21


Let’s take those results and set them inside line equation y=mx+b.

y = (41/42)*x - (5/12)


Now let’s draw the line and see how the line passes through the lines in such a
 way that it minimizes the squared distances.


Show ML_MSE4.jpg

As you can see, the whole idea is simple. 
We just need to understand the main parts and how we work with them.

You can work with the formulas to find the line on another graph, 
and perform a simple calculation and get the results for the slope and y-intercept.




Reducing Loss :

An iterative approach is one widely used method for reducing loss, 
and is as easy and efficient as walking down a hill.
    
"""
