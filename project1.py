import numpy as np
import pandas as pd

while True:

    #files of cities to be uploaded
    city_data = {'Chicago':'chicago.csv','New York':'new_york_city.csv','Washington':'washington.csv'}

    print('\nHello! Let\'s explore some US bikeshare data!')
    #input the primary arguments
    #choosing city
    while True:
        city = input("\nCHOOSE city to view its data (Chicago, New York or Washington):   ")
        if city.title() in city_data:
            break
        else:
            print ('\n Invalid input, please try again.\n')
    print('\n')
    #recall city's data
    df_origin = pd.read_csv(city_data[city.title()])
    #changing date string to date values
    df_origin['Start Time'] = pd.to_datetime(df_origin['Start Time'])
    df_origin['month'] = df_origin['Start Time'].dt.month
    df_origin['day_of_week'] = df_origin['Start Time'].dt.day_name()
    df_origin['hour'] = df_origin['Start Time'].dt.hour

    #choosing month
    months = {'January':1, 'February':2 ,'March':3 ,'April':4 ,'May':5 ,'June':6 ,'All':0}
    while True:
        month = input("CHOOSE month [January, February, March, April, May or June] to view its data OR PRINT (all) to VIEW all months' data:    ")
        if month.title() in months:
            break
        else:
            print ('\n Invalid input, please try again.\n')

    if month.title() == 'All':
        df = df_origin
    else:
        df_origin = df_origin[df_origin['month'] == months[month.title()]]

    print('\n')

    #choosing day
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday' ,'Thursday', 'Friday', 'All']
    while True:
        day = input("CHOOSE day [Saturday, Sunday, Monday, Tuesday, Wednesday ,Thursday or Friday] to view its data OR PRINT (all) to VIEW all days' data:    ")
        if day.title() in days:
            break
        else:
            print ('\n Invalid input, please try again.\n')

    if day.title() == 'All':
        df = df_origin
    else:
        df_origin = df_origin[df_origin['day_of_week'] == day.title()]

    print('\n')

    #choosing hour
    while True:
        try:
            hour = input("CHOOSE hour 'Please, insert hour from 0 to 23'  to view its data OR PRINT (all) to VIEW all hours' data:    ")
            if hour.lower() == 'all' or (int(hour) >= 0 and int(hour) < 24):
                break
        except:
            print ('\n Invalid input, please try again.\n')

    if hour.lower() == 'all':
        df = df_origin
    else:
        df_origin = df_origin[df_origin['hour'] == int(hour)]

    print('\n')
    print(" O-^-O "*25)

    #statistic computed
    #1 popular time of travel
    def popular_time(df_origin):
        """Displays statistics on the most frequent times of travel."""

        print('\nPopular times of travel: \n')
        common_month = df_origin['month'].mode()[0]
        common_day = df_origin['day_of_week'].mode()[0]
        common_hour = df_origin['hour'].mode()[0]

        print("most common month {} \nmost common day of week {} \nmost common hour of day {}".format(common_month, common_day, common_hour))
        print('\n')
        print(" O-^-O "*25)
        return common_month, common_day, common_hour

    #2 Popular stations and trip
    def popular_station(df_origin):
        """Displays statistics on the most popular stations and trip."""

        print('\nPopular stations and trip: \n')
        start_station = df_origin['Start Station'].mode()[0]
        end_station = df_origin['End Station'].mode()[0]
        common_trip = (df_origin['Start Station'] + "  TO  " + df_origin['End Station']).mode()[0]

        print('most common start station:             {} \nmost common end station:               {} \nmost common trip from start to end:    {}'.format(start_station, end_station, common_trip))
        print('\n')
        print(" O-^-O "*25)
        return start_station, end_station, common_trip

    #3 Trip duration
    def trip_duration(df_origin):
        """Displays statistics on the total and average trip duration."""

        print('\nTrip duration: \n')
        total_time = df_origin['Trip Duration'].sum()
        average_time = df_origin['Trip Duration'].mean()

        print('total travel time {} sec\naverage travel time {} sec'.format(total_time, average_time))
        print('\n')
        print(" O-^-O "*25)
        return total_time, average_time

    #4 User info
    def user_info1(df_origin):
        """Displays statistics on bikeshare users."""

        print('\nUser info: \n')
        user_counts = df_origin['User Type'].value_counts()

        print('counts of each user type\n {} \n'.format(user_counts))
        return user_counts

    def user_info2(df_origin):
        """Displays statistics on bikeshare users for Chicago and New York."""

        gender_counts = df_origin['Gender'].value_counts()
        earliest_year = df_origin['Birth Year'].min()
        recent_year = df_origin['Birth Year'].max()
        common_year = df_origin['Birth Year'].mode()[0]

        print('counts of each gender \n {} \n\nearliest year of birth    {} \nmost recent year of birth {} \nmost common year of birth {} \n'.format(gender_counts, earliest_year, recent_year, common_year))
        return gender_counts, earliest_year, recent_year, common_year

    #Return statistic
    popular_time(df_origin)
    popular_station(df_origin)
    trip_duration(df_origin)
    user_info1(df_origin)
    if city.title() == 'Chicago' or city.title() == 'New York':
        user_info2(df_origin)


    restart = input('If you want to explore more print "yes", if not print "no"')
    if restart.lower() != 'yes':
        break
