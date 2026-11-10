import seaborn as sns
import matplotlib.pyplot as plt

# data = ["Anil", "Ramesh" , "Sunaina" , "Anil" , "Sunil" , "Ramesh", "Ramesh"]

# sns.countplot(x =  data)

# # plt.show()


# data = [10,20,30,40,69,89,56,67,546,35,89,43]
# sns.displot(data)

# plt.show()


x = [10,20,30,40,68,56,89,90]

y= [57,87,90,46,35,67,90,78,]

sns.lineplot(x = x , y = y)

plt.show()


print(help(str.lower))