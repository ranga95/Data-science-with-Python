"""
@author: Jayaraman rp 
"""
from sklearn import tree
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],[177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']
clf= tree.DecisionTreeClassifier()
 print("enter the values of the height,weight,")
l = [int(x) for x in input().split()]
clf=clf.fit(X,Y)
prediction= clf.predict([l])
print(prediction)
 

