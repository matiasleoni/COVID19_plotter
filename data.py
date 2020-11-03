'''
This module contains data related to the dataset from "Our World in Data"
'''

COUNTRIES = {'Montserrat', 'Georgia', 'Gabon', 'Croatia', 'Rwanda', 'Dominica', 'Azerbaijan', 'Burundi', 'Finland', 'Jordan', 'Mauritius', 'Philippines', 'Guyana', 'South Africa', 'Indonesia', 'Macedonia', 'Liechtenstein', 'Nicaragua', 'Ukraine', 'Kyrgyzstan', 'Falkland Islands', 'Morocco', 'Belarus', 'Myanmar', 'New Caledonia', 'Puerto Rico', 'South Sudan', "Cote d'Ivoire", 'Angola', 'Moldova', 'Belize', 'Australia', 'Maldives', 'Mexico', 'Guam', 'Chad', 'Gibraltar', 'Venezuela', 'Isle of Man', 'Greenland', 'Fiji', 'Mozambique', 'Iran', 'Laos', 'Israel', 'Timor', 'France', 'Thailand', 'Dominican Republic', 'Guatemala', 'Northern Mariana Islands', 'Estonia', 'Ecuador', 'Bosnia and Herzegovina', 'Malawi', 'Norway', 'Botswana', 'South Korea', 'Nepal', 'Canada', 'Oman', 'Cameroon', 'Kazakhstan', 'Papua New Guinea', 'Mauritania', 'Turks and Caicos Islands', 'Central African Republic', 'Uganda', 'Sint Maarten (Dutch part)', 'Uruguay', 'Turkey', 'Faeroe Islands', 'Taiwan', 'Malta', 'Lebanon', 'Bermuda', 'Honduras', 'Paraguay', 'Sweden', 'Egypt', 'Qatar', 'Brunei', 'Brazil', 'Iraq', 'Poland', 'Slovenia', 'Democratic Republic of Congo', 'Saint Vincent and the Grenadines', 'Monaco', 'Armenia', 'Afghanistan', 'Ireland', 'India', 'Lesotho', 'Romania', 'Barbados', 'Sri Lanka', 'San Marino', 'Syria', 'Serbia', 'Austria', 'Singapore', 'Bonaire Sint Eustatius and Saba', 'Germany', 'Western Sahara', 'Kosovo', 'Nigeria', 'Haiti', 'Portugal', 'Panama', 'Eritrea', 'Hungary', 'Sierra Leone', 'New Zealand', 'Guernsey', 'Argentina', 'Malaysia', 'Benin', 'Bulgaria', 'Cambodia', 'Andorra', 'Tunisia', 'Belgium', 'Bahamas', 'Bahrain', 'Cape Verde', 'Denmark', 'Bhutan', 'Cayman Islands', 'Japan', 'Mongolia', 'United States', 'Albania', 'Niger', 'Italy', 'Sudan', 'Togo', 'Tajikistan', 'Vietnam', 'United Kingdom', 'Madagascar', 'Chile', 'Wallis and Futuna', 'China', 'Switzerland', 'Saudi Arabia', 'Saint Lucia', 'Yemen', 'Zambia', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Jamaica', 'Equatorial Guinea', 'Peru', 'Uzbekistan', 'Algeria', 'Latvia', 'Bangladesh', 'Iceland', 'Palestine', 'Greece', 'Bolivia', 'Luxembourg', 'Tanzania', 'Antigua and Barbuda', 'International', 'Grenada', 'Hong Kong', 'Mali', 'Saint Kitts and Nevis', 'Comoros', 'Colombia', 'Netherlands', 'Solomon Islands', 'World', 'Spain', 'El Salvador', 'Russia', 'Namibia', 'Burkina Faso', 'Aruba', 'Cuba', 'Czech Republic', 'Jersey', 'Seychelles', 'Lithuania', 'Djibouti', 'Kuwait', 'Vatican', 'Ethiopia', 'Senegal', 'United States Virgin Islands', 'Swaziland', 'Pakistan', 'Cyprus', 'British Virgin Islands', 'Zimbabwe', 'Somalia', 'United Arab Emirates', 'French Polynesia', 'Gambia', 'Libya', 'Suriname', 'Slovakia', 'Curacao', 'Marshall Islands', 'Sao Tome and Principe', 'Trinidad and Tobago', 'Congo', 'Anguilla', 'Liberia', 'Ghana', 'Costa Rica', 'Montenegro'}

WEB = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
FILE = 'owid-covid-data.csv'

COLUMNS = ['iso_code', 'continent', 'location', 'date',
           'total_cases', 'new_cases', 'new_cases_smoothed', 'total_deaths',
           'new_deaths', 'new_deaths_smoothed', 'total_cases_per_million', 'new_cases_per_million',
           'new_cases_smoothed_per_million', 'total_deaths_per_million', 'new_deaths_per_million',
           'new_deaths_smoothed_per_million', 'total_tests', 'new_tests', 'total_tests_per_thousand',
           'new_tests_per_thousand', 'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
           'tests_per_case', 'positive_rate', 'tests_units', 'stringency_index', 'population',
           'population_density', 'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita',
           'extreme_poverty', 'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
           'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand', 'life_expectancy',
           'human_development_index']
