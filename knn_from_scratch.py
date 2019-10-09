{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.spatial import distance as dis\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "class classifier():\n",
    "    \n",
    "    def euc_dist(self,a,b):\n",
    "        return dis.euclidean(a,b)\n",
    "    \n",
    "    def fit(self,x_train,y_train):\n",
    "        self.x_train=x_train\n",
    "        self.y_train=y_train\n",
    "        \n",
    "        \n",
    "    def predict(self,x_test):\n",
    "        predictions=[]\n",
    "        for row in x_test:\n",
    "            label=self.closest(row)\n",
    "            predictions.append(label)\n",
    "        return predictions\n",
    "    \n",
    "    def closest(self,row):\n",
    "        b_index=0\n",
    "        b_dist=euc_dist(row,self.x_train[0])\n",
    "        \n",
    "        for i in range(len(self.x_train)):\n",
    "            d=euc_dist(row,self.x_train[i])\n",
    "            if(d<b_dist):\n",
    "                b_dist=d\n",
    "                b_index=i\n",
    "        return (self.y_train[b_index])\n",
    "    \n",
    "    def score(self,x_test,y_test):\n",
    "        y_pre=self.predict(x_test)\n",
    "        return accuracy_score(y_test,y_pre)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import datasets\n",
    "\n",
    "iris=datasets.load_iris()\n",
    "x=iris.data\n",
    "y=iris.target\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)\n",
    "clf=classifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "clf.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "printing the accuracy\n",
      "0.9666666666666667\n"
     ]
    }
   ],
   "source": [
    "print(\"printing the accuracy\")\n",
    "print(clf.score(x_test,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DAMNNNNNNNNNNNN OMG!!!!!!! WTF!!!!!!\n"
     ]
    }
   ],
   "source": [
    "print(\"DAMNNNNNNNNNNNN OMG!!!!!!! WTF!!!!!!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
