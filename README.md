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
10. Finally, for the output, I have made use of DecisionTree Classifier. I tried with 
KNeighborsClassifier, svm and MultinomialNB, but i did not get desired result.
11. The reult function prints the data frame with unredacted names.

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
		train_x,train_y,validate_x,validate_y,test_x,test_y=split(df)

7. text_features()
It vectorizes the 'clean_text' data using count vectorizer
		X_feat_train,X_feat_validate,X_feat_test = text_features(train_x['clean_text'],validate_x['clean_text'],test_x['clean_text'])

8. letter_features() and space_features() does the same for number of letters
and spaces.

9. def merge()
This functions uses hstack to merge the text_features(), letter_features() and space_features() 
to merge the data and saves it in merge_train, merge_validte, merge_test respectively

At this point if you like to see what the dataframe looks like, you can use 'df'
to view it. Hope it looks good!

10. calculate_scores()
Finally, we get to calculate the precision, recall and f1 scores. I have used the
DecisionTreeClassifier here. As mentioned before, using the KNeighborsClassifier, svm and MultinomialNB
features did not give a satisfied result.

 
