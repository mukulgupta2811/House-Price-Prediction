import numpy as np

from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

X = np.array([
    [850, 2, 1, 15, 12, 1],
    [900, 2, 2, 12, 10, 1],
    [1000, 2, 2, 10, 9, 1],
    [1100, 3, 2, 8, 8, 1],
    [1200, 3, 2, 7, 7, 1],
    [1300, 3, 2, 6, 6, 2],
    [1400, 3, 3, 5, 6, 2],
    [1500, 3, 3, 5, 5, 2],
    [1600, 4, 3, 4, 5, 2],
    [1700, 4, 3, 3, 4, 2],
    [1800, 4, 3, 3, 4, 2],
    [1900, 4, 4, 2, 3, 2],
    [2000, 4, 4, 2, 3, 2],
    [2100, 4, 4, 2, 3, 2],
    [2200, 5, 4, 1, 2, 3],
    [2300, 5, 4, 1, 2, 3],
    [2400, 5, 4, 1, 2, 3],
    [2500, 5, 5, 1, 2, 3],
    [2600, 5, 5, 1, 1, 3],
    [2800, 6, 5, 1, 1, 3],
    [3000, 6, 5, 1, 1, 3],
    [3200, 6, 6, 0, 1, 3],
    [3400, 7, 6, 0, 1, 3],
    [3600, 7, 6, 0, 1, 4],
    [3800, 7, 7, 0, 1, 4],
    [4000, 8, 7, 0, 1, 4]
])

y = np.array([
    42, 48, 55, 62, 68, 75, 82, 90, 98,
    108, 115, 125, 135, 142, 152, 162, 170,
    182, 195, 215, 235, 255, 275, 295, 315, 340

])


from sklearn.model_selection import train_test_split

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2 , random_state=42)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train , y_train)

train_data = model.predict(X_train)
train_score = r2_score(y_train,train_data)

test_data = model.predict(X_test)
test_score = r2_score(y_test,test_data)

mae = mean_absolute_error(y_test,test_data)
mse = mean_squared_error(y_test,test_data)

# a = int(input("Enter the Area :- "))
# b = int(input("Enter the bedrooms :- "))
# c = int(input("Enter the Bathrooms :- "))
# d = int(input("Enter the House_age :- "))
# e = int(input("Enter the Distance :- "))
#
#
# print(model.predict([[a,b,c,d,e]]))
print(f"Trained Data Score = {train_score}")
print(f"Test Data Score = {test_score}")
print(f"MAE Score = {mae}")
print(f"MSE Score = {mse}")