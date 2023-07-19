import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('My-Uber-Drives-2016.csv')

df.info()
print(df)


# We will rename the columns.
df.rename(columns={'START_DATE*': 'Start Date',
                   'END_DATE*': 'End Date',
                   'CATEGORY*': 'Category',
                   'START*':'Start',
                   'STOP*':'Stop',
                   'MILES*':'Miles',
                   'PURPOSE*':'Purpose'}, inplace=True)
df.info()

# We will check for duplicate rows.
print(df[df.duplicated(keep=False)])
# There is only one duplicate, which we will drop.
df.drop_duplicates(inplace=True)
df.info()

# We will clean empty entries.
df['Purpose'].fillna('Not Provided',inplace=True)
df.info()
df.dropna(inplace=True)
df.info()

##################################################################################

# We may now begin to manipulate the data.  We start by changing relevant data types.
print(df['Category'].unique())
print(df['Purpose'].unique())
df['Category'] = df['Category'].astype('category')
df['Purpose'] = df['Purpose'].astype('category')
# We will convert the Start Date and End Date to datetime format.  By using errors='coerce' we could end up with many NaT entries.
# After converting it would be a good idea to check if there are still 1154 non-null entries.
df['Start Date']=pd.to_datetime(df['Start Date'], errors='coerce')
df['End Date']=pd.to_datetime(df['End Date'], errors='coerce')
# We check the number of non-null entries.
df.info()
print(df)

#################################################
# We will now add new columns for future use.

# We will add a column which tracks the total time the trip took (in minutes) and call it Trip Time
df['Trip Time'] = (df['End Date']-df['Start Date']).dt.total_seconds()/60
df.info()
print(df)
df['Trip Time']=df['Trip Time'].astype(int)
df.info()

# Now we add a column for average speed.
df['avg MPH']=round(((60*df['Miles'])/df['Trip Time']), 1)
df.info()
print("The minimum MPH is {}, and the maximum MPH is {}".format(df['avg MPH'].min(),df['avg MPH'].max()))
# We now see that some of the data does not make sense.  We will eliminate rows where the trip would have averaged over 80 MPH.
df.drop(df[df['avg MPH']>80].index, inplace=True) 
df.info()
print("The minimum MPH is now {}, and the maximum MPH is now {}".format(df['avg MPH'].min(),df['avg MPH'].max()))

# We will make new columns containing the day of the week and name of the month.

weekday_order = pd.CategoricalDtype(
    categories=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                'Friday','Saturday'],
    ordered= True)
df['Weekday'] = df['Start Date'].dt.day_name().astype(weekday_order)


month_order = pd.CategoricalDtype(
    categories=['January', 'February', 'March', 'April', 'May', 
                'June','July', 'August', 'September', 'October', 'November', 'December'],
    ordered= True)
df['Month'] = df['Start Date'].dt.month_name().astype(month_order)

# Finally we add a column, Window, to break the times of the day into bins.
# For our purposes 'Morning' is 6-10, 'Midday' is 10-14, 'Afternoon' is 14-18,
# 'Evening' is 18-22, 'Night' is 22-02, and 'Late' is 2-6.

df['Window'] = pd.cut(x=df['Start Date'].dt.hour, 
                             bins=[0,2,6,10,14,18,22,24], 
                             labels=['Night','Late','Morning','Midday','Afternoon','Evening','Night'],
                             ordered=False,
                             right=False)

window_order = pd.CategoricalDtype(
    categories=['Morning','Midday','Afternoon','Evening','Night','Late'],
    ordered= True)
df['Window']=df['Window'].astype(window_order)

df.info()
print(df)

# We will consider the correlation of the quantative factors.

print(df.corr(numeric_only=True))

# As one would expect, there is correlation between the number of Miles driven and the total Trip Time.

# We will save the cleaned data for hypothesis testing in a different module, and then start visualizing the current data.

df.to_csv('CleanedData.csv', index=False)

####################################################################################################################
print(df['Category'].value_counts())
# We start visualizing the current data.
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Category')
plt.gca().bar_label(plt.gca().containers[0])
# After testing the program once, the graph is more visible if we extend the vertical plotting area like so.
plt.gca().set_ylim([0, 1200])
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
sns.countplot(data=df, x='Purpose')
plt.gca().bar_label(plt.gca().containers[0])
# After testing the program once, the graph is more visible if we extend the vertical plotting area like so.
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Clearly most trips do not provide a purpose.  It might be easier to see the remaining data if we exclude this one column.
plt.figure(figsize=(8,6))
sns.countplot(data=df[df['Purpose']!="Not Provided"], x='Purpose')
plt.gca().bar_label(plt.gca().containers[0])
# After testing the program once, the graph is more visible if we extend the vertical plotting area like so.
plt.xticks(rotation=45)
plt.title('"Not Provided" removed')
plt.tight_layout()
plt.show()



