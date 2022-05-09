# cs5293sp22project3

Hello, hope you are doing well. Thank you for grading my project.

I have used pandas to load the data in a dataframe
Code Structure:
1. The code reads the tsv file and loads it in a dataframe
2. The data is then processed to remove special characters and punctuations and saves 
it as 'clean_text'. The names are also processed and saved in 'redacted_names' column. 
3. Now that we have the desired df, we remove the unwanted columns from the dataframe.
4. We then count the number of letters on the redacted names
5. Similarly, we count the number of spaces in the redacted names column.
6. Now the data is split into train , validate and test.
7. Then we get the text features using the CountVectorizer.
8. We get features for space and letters.
9. The text, letter and space features are then merged using hstack
10. Finally, for the output, I have made use of KNeighborsClassifier. I tried with 
DecisionTree, svm and MultinomialNB, but i did not get desired result.
11. The result function prints the data frame with unredacted names.

How to run the code?
I would recommend using jupyter notebook for running this code. I have attached the 
ipynb file along with the pdf of the outputs of every function. You must run each 
function seperately in jupyter. Hope you get the desired output.

Functions -
All the suggested output commands are in the code, but just in case the are required,
I have added them here.
1. get_data()
This function reads the 'unredactor.tsv' file into a dataframe and adds the following 
'username','file_type','names','redacted_text'.
for output for this function in jupyter, you can use 
			df=get_data('unredactor.tsv')

2. process()
The purpose of this function is to process the data from names and redacted_text.
It takes two arguments - dat1 and dat2 and processes to remove special characters 
and punctuation to clean the data. Then this data is stored in 'clean_text" and 
'redacted_names' respectively.
For this you can use, 
		label,a = process(df['redacted_text'],df['names'])
		df['clean_text'] = a
		df['redacted_names'] = label
and df to check the updated dataframe.
3. remove_columns()
This function, as it says, removes the previous columns (unprocessed) and 
updates the dataframe with only the required data.
You can use,
		df = remove_columns(df,'username','names','redacted_text')
		df
4. letter_count()
This function counts the number of letters of the redacted text, and updates in
the dataframe.
		d = letter_count(df['redacted_names'])
		df['letter_count'] = d
		df
5. space_count()
This function,as the previous one, counts the spaces in the redacted names and updates
the dataframe
c = space_count(df['redacted_names'])
df['space_count'] = c

6. split()
Now, we proceed to split the data in train validate and test data. It takes
the 'file_type' column and seperates the training, validating and testing datas.
It is then saved in the data frame.

7. vect()
It vectorizes the 'clean_text' data using count vectorizer. You can view them using
X_tr_text, X_val_text, X_test_text
		
8. letter_features() and space_features() does the same for number of letters
and spaces.

9. def merge()
This functions uses hstack to merge the text_features(), letter_features() and space_features() 
to merge the data and saves it in merge_train, merge_validte, merge_test respectively
merge_train = merge(X_tr_text,X_let_train,X_spc_train)
merge_validate = merge(X_val_text,X_let_validate,X_spc_validate)
merge_test = merge(X_test_text, X_spc_test, X_spc_test)

At this point if you like to see what the dataframe looks like, you can use 'df'
to view it. Hope it looks good!

10. create_model()
This function, creates a prediction model using KNeighborsClassifier
11. prediction()
This function uses the KNeighborsClassifier model to predict the unredacted word which when you type the 'predict_y_test', should show you the results.
12. evaluate()
Finally the evaluate functions returns the precision, recall and f1 scores
	train_precision_score, val_precision_score, train_recall_score, val_recall_score, train_f1_score, val_f1_score = evaluate(model,predict_y_train,predict_y_val,y_train,y_val)

Sorry, but I was not able to add all the tests. But the code should run correct. 

Thanks you again for grading my code


 
