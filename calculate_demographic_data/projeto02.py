import pandas as pd

def calculate_demographic_data(print_data=True):
    # Ler os dados do arquivo do censo
    df = pd.read_csv("adult.data.csv")

    # 1. Quantas pessoas de cada raça estão representadas neste conjunto de dados?
    race_count = df['race'].value_counts()

    # 2. Qual é a média de idade dos homens?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Qual é a porcentagem de pessoas que têm um diploma de bacharel?
    total_people = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # 4. Pessoas com e sem educação superior (Bachelors, Masters, Doctorate)
    higher_education_degrees = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(higher_education_degrees)]
    lower_education = df[~df['education'].isin(higher_education_degrees)]

    # Porcentagem de pessoas com educação superior que ganham >50K
    higher_education_rich = round((len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)) * 100, 1)
    
    # Porcentagem de pessoas sem educação superior que ganham >50K
    lower_education_rich = round((len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)) * 100, 1)

    # 5. Qual é o número mínimo de horas que uma pessoa trabalha por semana?
    min_work_hours = df['hours-per-week'].min()

    # 6. Qual é a porcentagem das pessoas que trabalham o número mínimo de horas por semana e que têm um salário >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers)) * 100, 1)

    # 7. Qual país tem a maior porcentagem de pessoas que ganham >50K e qual é essa porcentagem?
    # Contamos quantas pessoas ganham >50K por país e dividimos pelo total de pessoas de cada país
    country_total = df['native-country'].value_counts()
    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()
    
    # Calculamos as porcentagens para cada país
    country_rich_percentages = (country_rich / country_total) * 100
    
    highest_earning_country = country_rich_percentages.idxmax()
    highest_earning_country_percentage = round(country_rich_percentages.max(), 1)

    # 8. Identifique a ocupação mais popular para aqueles que ganham >50K na Índia.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Highest earning country:", highest_earning_country)
        print(f"Highest earning country percentage: {highest_earning_country_percentage}%")
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }