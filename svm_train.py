import svm 
from svmutil import * 

#training data 
labels=[0,1,1,2]
samples=[[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 0, 0]]

param=svm_parameter()
param.C=10 
param.kernel_type=LINEAR 
param.kernel_type=LINEAR 
#instantiate the problem 
problem=svm_problem(labels,samples)
model=svm_train(problem,param)

svm_save_model('model_file',model)

testing=[[0,1,1],[1,0,1]]
p_labels, p_accs, p_vals = svm_predict([0]*len(test_data), test_data, model)
print p_labels
print p_accs
print p_vals
