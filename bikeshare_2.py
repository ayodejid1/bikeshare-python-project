import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']


def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    name_of_city = ''
    while name_of_city not in CITY_DATA:
        name_of_city = input('what city would you like to analyze chicago, new york city or washington? please input one: ').lower()
        print('you have selected {}'.format(name_of_city))
        if name_of_city in CITY_DATA:
            #we are good to go
            city = CITY_DATA[name_of_city]
        else:
            print('sorry! we were unable to get the name of the city imputed, please try again by checking your imputation to make sure it is grammartically correct or tallies to the available city names!')


    # get user input for month (all, january, february, ... , june)
    name_of_month = ''
    while name_of_month not in MONTH_DATA:
        name_of_month = input("Which month of the year would you like to filter? january, february, march, april, may, june or all ?").lower()
        print('you have selected the month of {}'.format(name_of_month))
        if name_of_month in MONTH_DATA:
            #we are good to go
            month = name_of_month
        else:
            print('sorry! we were unable to get the name of month imputed, please try again by checking your imputation to make sure it is grammartically correct or tallies to the available months names!')
            

    # get user input for day of week (all, monday, tuesday, ... sunday)
    name_of_day = ''
    while name_of_day not in DAY_DATA:
        name_of_day = input("What day of the week((all, monday, tuesday, ... sunday)) would you like to analyze, please input a choice or input 'all' :").lower()
        print('you have selected {}'.format(name_of_day))
        if name_of_day in DAY_DATA:
            #we are good to go
            day = name_of_day
        else:
            print('sorry! we were unable to get the name of day imputed, please try again by checking your imputation to make sure it is grammartically correct or tallies to the available day names!')

    print('-'*40)
    return city, month, day
   

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is {}'.format(common_month))

    # display the most common day of week
    dow = df['day_of_week'].mode()[0]
    print('The most common day of the week is {}'.format(dow))


    # display the most common start hour
    mch = df['hour'].mode()[0]
    print('The most common start hour is the {}th hour'.format(mch))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    muss = df['Start Station'].mode()[0]
    mc1 = df['Start Station'].value_counts()[0]
    print('The most commonly used start station is the {}, \n with count:{}'.format(muss, mc1))

    # display most commonly used end station
    es = df['End Station'].mode()[0]
    mc2 = df['End Station'].value_counts()[0]
    print('The most commonly used End station is the {}, \n with count:{}'.format(es, mc2))

    # display most frequent combination of start station and end station trip
    df['muses'] = (df['Start Station'] + "||" + df['End Station']).value_counts().idxmax()
    pop_station = df['muses'].mode()[0]
    mc3 = (df['Start Station'] + "||" + df['End Station']).value_counts()[0]
    print('The most frequent combination of start station and end station trip is {}, \n with count:{}'.format(pop_station, mc3))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    ttt = df['Trip Duration'].sum()
    print('The Total travel time is {}'.format(ttt))


    # display mean travel time
    avg_tt = df['Trip Duration'].mean()
    print('The Average total travel time is {}'.format(avg_tt))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('The total counts of different User Types are: \n {}'.format(user_type_count))


    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print('The total counts by Gender are: \n {}'.format(gender_count))



    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        early = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        most_common_yob = int(df['Birth Year'].mode()[0])
        print('The earliest year of birth is: {}'.format(early))
        print('The most recent year of birth is: {}'.format(recent))
        print('The most common year of birth is: {}'.format(most_common_yob))
    if 'Birth Year' not in df.columns and 'Gender'  not in df.columns:
        print('\n\nSorry, there\'s no gender or birth year data for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data(city):
    """Shows raw data  based on user request.
    Args:
        (DataFrame) df - bikeshare Pandas DataFrame containing city data filtered by month and day
    """
    print('\n Raw data is available for viewing.\n')
    showing_raw_data = input('\nWould you like to see the next five row of raw data? Please enter yes or no!. \n').lower()
    while showing_raw_data != 'yes'and showing_raw_data != 'no':
        showing_raw_data =input('Invalid Input!, You may want to have a look on the raw data? Type yes or no\n').lower()
    while showing_raw_data == 'yes':
        try:
            chunksize=5
            for row in  pd.read_csv(city, chunksize = chunksize):
                pd.set_option('display.max_columns',200)
                print(row) 
                # repeating the question
                showing_raw_data = input('\nWould you like to see the next five row of raw data? Please enter yes or no!. \n').lower()
                if showing_raw_data != 'yes':
                     print('Thank You')
                     break

            break
        except KeyboardInterrupt:
            print('Thank you.')
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(city)
        
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
