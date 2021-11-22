import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    len_df = len(df['education'])
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men_df = df[df['sex'] == 'Male']
    average_age_men = round(average_age_men_df['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    len_bachelors = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((len_bachelors / len_df) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_edu_df = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_edu_df = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education = higher_edu_df[higher_edu_df['salary'] == '>50K']
    lower_education = lower_edu_df[lower_edu_df['salary'] == '>50K']

    # percentage with salary >50K
    higher_education_rich = round((len(higher_education) / len(higher_edu_df)) * 100, 1)
    lower_education_rich = round((len(lower_education) / len(lower_edu_df)) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hrs_df = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = len(min_hrs_df)

    rich_percentage = (len(min_hrs_df[min_hrs_df['salary'] == '>50K']) / num_min_workers) * 100
    
    # What country has the highest percentage of people that earn >50K?
    higher_salary = df[df['salary'] == '>50K']
    people = df['native-country'].value_counts() 
    rich = higher_salary['native-country'].value_counts()
    rich_df = ((rich / people) * 100)
    rich_per = rich_df.max()
    highest_earning_country_percentage = round(rich_per, 1)
    highest_earning_country = rich_df[rich_df == rich_per].index[0]

    # Identify the most popular occupation for those who earn >50K in India.
    indian_people = higher_salary[higher_salary['native-country'] == 'India']
    top_IN_occupation = indian_people['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
