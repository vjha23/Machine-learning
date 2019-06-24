#loading digits data
from sklearn.datasets import load_digits
digit_data=load_digits() #loaded data
#exploring data
print(dir(digit_data))
#output that we want
output=digit_data.target_names
print(output)
#describing data
digit_data.DESCR
#training data
training_data=digit_data.data
#shape
training_data.shape
#label
label=digit_data.target
#actial images
images=digit_data.images
print(images[0])
#visiual of zero
import matplotlib.pyplot as plt
show34=plt.imshow(images[2])
plt.show()