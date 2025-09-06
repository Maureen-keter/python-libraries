import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

my_arr=np.array(range(1,11))
mean=my_arr.mean()
print(mean)
                 
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 22, 21, 23],
    "Grade": [45, 67, 85, 74]
}

df=pd.DataFrame(data)
print("Summary Statistics:\n", df.describe())


try:
    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data=response.json()
    btc_price_usd = btc_data["bpi"]["USD"]["rate"]
    print("\nCurrent Bitcoin Price (USD):", btc_price_usd)
except Exception as e:
    print("\nAPI fetch skipped (no internet). Error:", e)


x=[1,2,3,4,5]
y=[10,20,25,30,40]
 
# Create a line plot
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")                
plt.ylabel("Y-axis")
plt.show() 
