import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Setting dataframe
loan_data = pd.read_csv('loan_payments.csv')

#1. Current status of the loans
# Data Dictionary for Column Descriptions
data_dictionary = {
    'id': 'Unique id of the loan',
    'member_id': 'Id of the member who took out the loan',
    'loan_amount': 'Amount of loan the applicant received',
    'funded_amount': 'The total amount committed to the loan at that point in time',
    'funded_amount_inv': 'The total amount committed by investors for that loan at that point in time',
    'term': 'The number of monthly payments for the loan',
    'int_rate': 'Annual (APR) interest rate of the loan',
    'instalment': 'The monthly payment owned by the borrower. This is inclusive of the interest.',
    'grade': 'Loan company (LC) assigned loan grade',
    'sub_grade': 'LC assigned loan sub grade',
    'employment_length': 'Employment length in years',
    'home_ownership': 'The home ownership status provided by the borrower',
    'annual_inc': 'The annual income of the borrower',
    'verification_status': 'Indicates whether the borrowers income was verified by the LC or the income source was verified',
    'issue_date': 'Issue date of the loan',
    'loan_status': 'Current status of the loan',
    'payment_plan': 'Indicates if a payment plan is in place for the loan. Indication borrower is struggling to pay.',
    'purpose': 'A category provided by the borrower for the loan request',
    'dti': 'A ratio calculated using the borrowers total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income',
    'delinq_2yr': 'The number of 30+ days past-due payments in the borrowers credit file for the past 2 years',
    'earliest_credit_line': 'The month the borrowers earliest reported credit line was opened',
    'inq_last_6mths': 'The number of inquiries in past 6 months (excluding auto and mortgage inquiries)',
    'mths_since_last_record': 'The number of months since the last public record',
    'open_accounts': 'The number of open credit lines in the borrowers credit file',
    'total_accounts': 'The total number of credit lines currently in the borrowers credit file',
    'out_prncp': 'Remaining outstanding principal for total amount funded',
    'out_prncp_inv': 'Remaining outstanding principal for portion of total amount funded by investors',
    'total_payment': 'Payments received to date for total amount funded',
    'total_rec_int': 'Interest received to date',
    'total_rec_late_fee': 'Late fees received to date',
    'recoveries': 'Post charge off gross recovery',
    'collection_recovery_fee': 'Post charge off collection fee',
    'last_payment_date': 'Date on which last month payment was received',
    'last_payment_amount': 'Last total payment amount received',
    'next_payment_date': 'Next scheduled payment date',
    'last_credit_pull_date': 'The most recent month LC pulled credit for this loan',
    'collections_12_mths_ex_med': 'Number of collections in 12 months excluding medical collections',
    'mths_since_last_major_derog': 'Months since the most recent 90-day or worse rating',
    'policy_code': 'Publicly available policy_code=1 new products not publicly available policy_code=2',
    'application_type': 'Indicates whether the loan is an individual application or a joint application with two co-borrowers'
}


# Calculate percentage of loans recovered against investor funding
total_recovery = loan_data['recoveries'].sum()
total_funded_by_investors = loan_data['funded_amount_inv'].sum()
percentage_recovered = (total_recovery / total_funded_by_investors) * 100

# Calculate total amount funded
total_funded_amount = loan_data['funded_amount'].sum()

# Calculate the percentage of total amount recovered in the next 6 months
future_date = pd.to_datetime('today') + pd.DateOffset(months=6)

# Converting 'last_payment_date' to timestamp objects (to prevent an error)
loan_data['last_payment_date'] = pd.to_datetime(loan_data['last_payment_date'])

future_recovery = loan_data[loan_data['last_payment_date'] <= future_date]['recoveries'].sum()

percentage_future_recovery = (future_recovery / total_funded_amount) * 100

print(f"Percentage of loans recovered against investor funding: {percentage_recovered:.2f}%")
print(f"Percentage of total amount to be recovered in next 6 months: {percentage_future_recovery:.2f}%")



#2. Calculating loans

# Filter Charged Off Loans
charged_off_loans = loan_data[loan_data['loan_status'] == 'Charged Off']

#Calculate Percentage of Charged Off Loans
total_loans = len(loan_data)
charged_off_percentage = (len(charged_off_loans) / total_loans) * 100

#Calculate Total Amount Paid Towards Charged Off Loans
total_amount_paid_charged_off = charged_off_loans['total_payment'].sum()

#Results:
print(f"Percentage of charged off loans historically: {charged_off_percentage:.2f}%")
print(f"Total amount paid towards charged off loans: ${total_amount_paid_charged_off:.2f}")



#3. Calculate project loss

#Filter Charged Off Loans
charged_off_loans = loan_data[loan_data['loan_status'] == 'Charged Off']

#Calculate Remaining Term and Projected Loss

# Extracting the numeric part using regular expressions
charged_off_loans['term_numeric'] = charged_off_loans['term'].str.extract('(\d+)')

# Turining values into numeric
charged_off_loans['term_numeric'] = pd.to_numeric(charged_off_loans['term_numeric'])

#Adding 'remaining_term' values, calculated as substraction of the number of payments already made from the total term 
charged_off_loans['remaining_term'] = charged_off_loans['term_numeric'] - charged_off_loans['total_payment'] / charged_off_loans['instalment']

# Calculate projected loss in revenue
charged_off_loans['projected_loss'] = charged_off_loans['remaining_term'] * charged_off_loans['instalment']

total_projected_loss = charged_off_loans['projected_loss'].sum()


#Visualisation
plt.figure(figsize=(10, 6))
sns.barplot(x='remaining_term', y='projected_loss', data=charged_off_loans, estimator=sum)
plt.xlabel('Remaining Term')
plt.ylabel('Projected Loss')
plt.title('Projected Loss Over Remaining Term')
plt.show()

#4. Possible loan

# Step 1: Identify customers currently behind on payments
loan_data['loan_status'].unique()

late_customers = loan_data[loan_data['loan_status'].str.contains('Late', na=False)]
late_customers.head()


# Step 2: Calculate metrics
total_loans = len(loan_data)
percentage_late_customers = (len(late_customers) / total_loans) * 100

#late_customers_to_charged_off = late_customers[late_customers['loan_status'] == 'Charged Off']
total_late_customers = len(late_customers)

#Total loss if late customers become charged off
loss_if_charged_off = late_customers['total_payment'].sum()

# Extracting the numeric part using regular expressions
late_customers['term_numeric'] = late_customers['term'].str.extract('(\d+)')

#Turining values into numeric
late_customers['term_numeric'] = pd.to_numeric(late_customers['term_numeric'])

#Adding 'remaining_term' values, calculated as substraction of the number of payments already made from the total term 
late_customers['remaining_term'] = late_customers['term_numeric'] - late_customers['total_payment'] / late_customers['instalment']

projected_loss_if_completed = late_customers['remaining_term'] * late_customers['instalment']

# # Step 3: Calculate percentage of total expected revenue
charged_off_loans = loan_data[loan_data['loan_status'] == 'Charged Off']

charged_off_customers = charged_off_loans
percentage_expected_revenue = ((len(charged_off_customers) + len(late_customers)) / total_loans) * 100


# #4. Indicators of loss

charged_off_subset = charged_off_loans
late_subset = late_customers 


columns_of_interest = ['grade', 'purpose', 'home_ownership']


for column in columns_of_interest:
    plt.figure(figsize=(10, 6))
    sns.countplot(x=column, data=charged_off_subset, hue='loan_status', palette='Set1')
    plt.title(f'Comparison of {column} for Charged Off Users and Late Users')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(title='Loan Status', labels=['Charged Off', 'Late'])
    plt.show()
