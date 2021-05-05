#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
from matplotlib.pyplot import rcParams
# rcParams['figure.figsize'] = 10,6 # To set the figure size
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import f1_score
import pickle


# In[2]:


data=pd.read_csv('LoanData.csv')


# In[3]:


data.shape


# In[4]:


data.head(10)


# In[5]:


data.describe()


# In[6]:


fig,ax=plt.subplots(figsize=(4,5))
sns.countplot(x = "Education", data=data, order = data["Education"].value_counts().index)
plt.show()


# In[7]:


fig = plt.figure(figsize=(20,2))
plt.style.use('seaborn-ticks')
sns.countplot(y="Married", data=data)


# In[ ]:





# In[8]:


data['Loan_Status'].value_counts()


# In[9]:


data.isnull().sum()


# In[10]:


data['Gender']=data['Gender'].fillna(data['Gender'].mode()[0])
data['Married']=data['Married'].fillna(data['Married'].mode()[0])
data['Dependents']=data['Dependents'].fillna(data['Dependents'].mode()[0])
data['Self_Employed']=data['Self_Employed'].fillna(data['Self_Employed'].mode()[0])


# In[11]:


data['LoanAmount']=data['LoanAmount'].fillna(data['LoanAmount'].median())
data['Loan_Amount_Term']=data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].median())
data['Credit_History']=data['Credit_History'].fillna(data['Credit_History'].median())


# In[12]:


data.isnull().sum()


# In[13]:


plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize']=(15,4)

plt.subplot(1,3,1)
sns.boxplot(data['ApplicantIncome'])

plt.subplot(1,3,2)
sns.boxplot(data['CoapplicantIncome'])

plt.subplot(1,3,3)
sns.boxplot(data['LoanAmount'])

plt.suptitle('Outliers')
plt.show()


# In[14]:


print("Before removing outliers",data.shape)
data=data[data['ApplicantIncome']<25000]
print("After removing outliers",data.shape)


# In[15]:


print("Before removing outliers",data.shape)
data=data[data['LoanAmount']<400]
print("After removing outliers",data.shape)


# In[16]:


data=data.drop(['Loan_ID'],axis=1)


# In[17]:


data.head()


# In[18]:


data.head()
data.select_dtypes('object').columns
data['Gender']=data['Gender'].replace(('Male','Female'),(1,0))
data['Married']=data['Married'].replace(('Yes','No'),(1,0))
data['Education']=data['Education'].replace(('Graduate','Not Graduate'),(1,0))
data['Self_Employed']=data['Self_Employed'].replace(('Yes','No'),(1,0))
data['Loan_Status']=data['Loan_Status'].replace(('Y','N'),(1,0))
data['Property_Area']=data['Property_Area'].replace(('Urban','Semiurban','Rural'),(1,1,0))
data['Dependents']=data['Dependents'].replace(('0','1','2','3+'),(0,1,1,1))
data.select_dtypes('object').columns


# In[19]:


data.head()


# In[20]:


y=data['Loan_Status']
x=data.drop(['Loan_Status'],axis=1)
print("Shape of x:",x.shape)
print("Shape of y:",y.shape)


# In[21]:


print(x)


# In[22]:


X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


# In[23]:


model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)


# In[ ]:





# In[24]:


y_pred=model.predict(X_test)
print("Training Accuracy:",model.score(X_train,y_train))
print("Testing Accuracy:",model.score(X_test,y_test))


# In[25]:


model=DecisionTreeClassifier(max_depth=3)
model.fit(X_train,y_train)


# In[26]:


tree.plot_tree(model)
plt.show()


# In[27]:


y_pred=model.predict(X_test)
print("Training Accuracy:",model.score(X_train,y_train))
print("Testing Accuracy:",model.score(X_test,y_test))


# In[28]:


print("F1 Score:",f1_score(y_test,y_pred))


# In[29]:


output = pd.DataFrame({'Test': y_test, 'Loan Status Prediction': y_pred})
output.to_csv('results.csv', index=False)
print("CSV successfully saved!")


# In[30]:


# import joblib
# filename = 'loan.h5'
# joblib.dump(model, filename)


# In[31]:


pickle.dump(model,open('model.pkl','wb'))


# In[32]:


model=pickle.load(open('model.pkl','rb'))

