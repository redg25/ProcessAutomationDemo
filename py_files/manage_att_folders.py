import os
import datetime as dt

def get_folder_path(attachment_dir):
        '''
        Check if the current date folder exists under the root folder given as input'\
        If not, creates the folder'''

        current_year = str(dt.datetime.now().year)
        current_month = str(dt.datetime.now().month)
        current_day = str(dt.datetime.now().day)
        attachment_dir = f'{attachment_dir}/'
        year_path = os.path.join(attachment_dir, f'{current_year}')
        if not os.path.exists(year_path):
            os.makedirs(year_path)
        month_path = os.path.join(attachment_dir, f'{current_year}/{current_month}')
        if not os.path.exists(month_path):
            os.makedirs(month_path)
        day_path = os.path.join(attachment_dir, f'{current_year}/{current_month}/{current_day}/')
        if not os.path.exists(day_path):
            os.makedirs(day_path)
        return day_path
