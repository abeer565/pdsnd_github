import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    day=0
    x='True'
    print("Hello! Let\'s explore some US bikeshare data!")
    try:
      while  x=='True':
        city= input("Would you like to see data for Chicago, New York, or Washington ??").lower()
        city_name = city
        if city!="chicago"  and  city!="new york" and city!="washington":
         print("that is not a valid value!")
        else:
         while  x=='True':
             month = input("Would you like to filter the data by month, day, or not at all? Type 'none' for no time filter.").lower()
             if month !='month' and month!='day' and month!='none':
                print("that is not a valid value!")
             elif  month =='none':
                month ==''
                day=0
                x='false'
             elif month =='month':
               while  x=='True':
                 month = input("Which month? January, February, March, April, May, or June?").lower()
                 if month !='january'and month !='february' and month !='march' and month !='pril' and month !='may' and  month !='june':
                    print("that is not a valid value!")
                 else:
                    month=month
                    day=0
                    x='false'
             elif month=='day':
                while x=='True':
                  day = int(input("Which day? Please type your response as an integer (e.g.,1=Sunday)."))
                  if day!=1 and day!=2 and day!=3 and day!=4 and day!=5 and day!=6 and day!=7:
                    print("\nNot valid number ,please try again")
                    x='true'
                  else:
                    day=day
                    month=''
                    x='false'
    except ValueError:
            print("that\s not a valid number!")
    except KeyboardInterrupt:
            print("\nNo input taken")
    finally:
                    print("\nAttempted Input\n")
    return city, month, day
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if   month == 'none'and day==0:
            month = ''
            day = 0
    elif month != '':
    # extract month and day of week from Start Time to create new columns
       df['month'] = df['Start Time'].dt.month
     # use the index of the months list to get the corresponding int
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
    # filter by month to create the new dataframe
       df = df[df['month'] == month]
    elif  day!=0:
        df['day_of_week'] = df['Start Time'].dt.weekday_name
    return df
#
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_used_start_station = df['Start Station'].mode()[0]
    print('\nMost Common Used Start Station \n',common_used_start_station)
    # TO DO: display most commonly used end station
    common_used_end_station = df['End Station'].mode()[0]
    print('\nMost Common Used End Station \n',common_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination_g = df.groupby(['Start Station','End Station']).size().idxmax()
    print('\nMost Common most frequent combination of start station and end station trip \n',frequent_combination_g)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#
def time_stats(df):
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
#
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:',  total_travel_time)


    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print('Average  Travel Time:',  mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
      # print value counts of each gender (only available for NYC and Chicago)
    if  city=="new york":
            # print value counts for each user type
            user_types = df['User Type'].value_counts()
            user_gender = df['Gender'].value_counts()
            print('\ncounts of each user gender \n',user_gender,'\ncounts of user types \n',user_types)
            #earliest, most recent, most common year of birth (only available for NYC and Chicago)
            df['Birth_Year'] = df['Birth Year'].dropna()
            common_Birth_Year = df['Birth_Year'].mode()[0]
            common_Birth_Year_int = int(common_Birth_Year)
            print('\nmost common year of birth \n',common_Birth_Year_int)
    elif city == "chicago":
            # print value counts for each user type
            user_types = df['User Type'].value_counts()
            user_gender = df['Gender'].value_counts()
            print('\ncounts of each user gender \n',user_gender,'\ncounts of user types \n',user_types)
            #earliest, most recent, most common year of birth (only available for NYC and Chicago)
            df['Birth_Year'] = df['Birth Year'].dropna()
            common_Birth_Year = df['Birth_Year'].mode()[0]
            common_Birth_Year_int = int(common_Birth_Year)
            print('\nmost common year of birth \n',common_Birth_Year_int)
    else:
        user_types = df['User Type'].value_counts()
        print('\ncounts of user types here \n',user_types)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def individual_trip(df):
    while True:
        i=5
        print(df.head(i))
        i=i*2
def main():
    start='true'
    r='true'
    z='true'
    restart=''
    while start=='true':
        city, month, day = get_filters()
        df = load_data(city, month, day)
        station_stats(df)
        time_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        while z=='true':
            restart = input('\nWould you like to view individual trip data? Type yes or no\n\n').lower()
            if restart !="no"and restart!="yes":
             print("that is not a valid value! please enter Yes or No option")
            elif (restart.lower() == 'no'):
                restart = input('\nWould you like to restart with the same process ? Type restart or exit \n')
                if restart !="restart"and restart!="exit":
                  print("that is not a valid value! please enter Restart or No option")
                elif restart.lower() == 'exit':
                   z='false'
                   r='false'
                   start='false'
                elif restart.lower() == 'restart':
                    #z='false'
                    r='false'
                    break
            elif restart.lower() == 'yes':
             aa=0
             x=5+aa
             print(df.head(x))
             while r=='true':
                if restart == 'restart':
                   z='false'
                x=5+x
                y=x+1
                i=y+1
                z=i+1
                a=z+1
                restart = input('\nWould you like to view individual trip data? Type yes or no here \n').lower()
                if restart !="yes"and restart!="no":
                    print("that is not a valid value! please enter Yes or No option")
                elif restart.lower() == 'yes':
                    print(df.iloc[[x,y,i,z,a]])
                elif  restart.lower() == 'no':
                  while z=='true':
                      restart = input('\nWould you like to restart with the same process ? Type restart or exit \n')
                      if restart !="restart"and restart!="exit":
                        print("that is not a valid value! please enter Restart or No option")
                      elif restart.lower() == 'exit':
                        z='false'
                        r='false'
                        break
                      elif restart.lower() == 'restart':
                        z='false'
                        r='false'
if __name__ == "__main__":
	main()
