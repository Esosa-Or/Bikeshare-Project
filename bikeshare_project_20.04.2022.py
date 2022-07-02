import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = ['Chicago','New York City', 'Washington']
    while True:
      city = input("Would you like to see data from New York City, Chicago or Washington?: ").lower()
      if city.title() not in cities:
        print("Sorry, that's not a valid option. Please try again!")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'all']
    while True:
      month = input("What month would you like to see? January, February, March, April, May, June or all?: ").lower()
      if month.title() not in months:
        print("Sorry, that's not a valid option. Please try again!")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'all']
    while True:
      day = input("What day would you like to see? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?: ").lower()
      if day.title() not in days:
        print("Sorry, that's not a valid option. Please try again!")
        continue
      else:
        break

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
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
    print('Most Common Month:', common_month)


    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common day of the week:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()
    print("Most common used Start Station: ", start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()
    print('Most commonly used end station: ', end_station)

    # display most frequent combination of start station and end station trip
    combo_station = (start_station, "&", end_station)
    print('Most Commonly used combination is: ', combo_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total Travel Time is: ', total_travel_time)
    

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel TIme is: ', mean_travel_time)    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nGender Count:\n', gender_count)
    except KeyError:
        print("Sorry, there is no gender data available for this month!")


    # Display earliest, most recent, and most common year of birth
    try:
        eyb = df['Birth Year'].min()
        print('\nThe Earliest Year of Birth is :', eyb)
    except KeyError:
        print("Sorry, there is no data available for your selection!")
    #Most recent year of birth
    try:
        mry= df['Birth Year'].max()
        print('\nMost Recent Year of Birth is:', mry)
    except KeyError:
        print("Sorry, there is no data available for your selection!.")
        
    #Most common year of birth
    try:
        mcy = df['Birth Year'].mode()
        print('Most Common Year of Birth:', mcy)
    except KeyError:
        print("Sorry, there is no data available for your selection!")

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data (df):
    """ Displays data for first five selections"""
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
