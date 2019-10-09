from scipy.spatial import distance as dis
from sklearn.metrics import accuracy_score

class classifier():
    
    def euc_dist(self,a,b):
        return dis.euclidean(a,b)
    
    def fit(self,x_train,y_train):
        self.x_train=x_train
        self.y_train=y_train
        
        
    def predict(self,x_test):
        predictions=[]
        for row in x_test:
            label=self.closest(row)
            predictions.append(label)
        return predictions
    
    def closest(self,row):
        b_index=0
        b_dist=self.euc_dist(row,self.x_train[0])
        
        for i in range(len(self.x_train)):
            d=self.euc_dist(row,self.x_train[i])
            if(d<b_dist):
                b_dist=d
                b_index=i
        return (self.y_train[b_index])
    
    def score(self,x_test,y_test):
        y_pre=self.predict(x_test)
        return accuracy_score(y_test,y_pre)




from sklearn import datasets

iris=datasets.load_iris()
x=iris.data
y=iris.target

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
clf=classifier()
clf.fit(x_train,y_train)
print("printing the accuracy")
print(clf.score(x_test,y_test))
