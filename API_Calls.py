import requests

api_key = 'CACD6CDB88B24EE18E9EE3F8418F9133'
#Term Codes: W25 = 1251 | S25 = 1255 | F25 = 1259
#CLASS SCHEDULES
#############################################################################################################
def get_class_ids_for_term(api_key, term_code):
    url = f"https://openapi.data.uwaterloo.ca/v3/ClassSchedules/{term_code}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_class_by_course_id(api_key, term_code, course_id):
    url = f"https://openapi.data.uwaterloo.ca/v3/ClassSchedules/{term_code}/{course_id}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_class_by_subject(api_key, term_code, subject, catalog_number):
    url = f"https://openapi.data.uwaterloo.ca/v3/ClassSchedules/{term_code}/{subject}/{catalog_number}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()
#############################################################################################################

#Courses
#############################################################################################################
def get_courses_for_term(term_code):
    url = f"https://openapi.data.uwaterloo.ca/v3/Courses/{term_code}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_course_by_id(api_key, term_code, course_id):
    url = f"https://openapi.data.uwaterloo.ca/v3/Courses/{term_code}/{course_id}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_course_by_offer_number(api_key, term_code, course_id, offer_number):
    url = f"https://openapi.data.uwaterloo.ca/v3/Courses/{term_code}/{course_id}/{offer_number}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_courses_by_subject(api_key, term_code, subject):
    url = f"https://openapi.data.uwaterloo.ca/v3/Courses/{term_code}/{subject}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_course_by_subject_and_catalog(api_key, term_code, subject, catalog_number):
    url = f"https://openapi.data.uwaterloo.ca/v3/Courses/{term_code}/{subject}/{catalog_number}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()
#############################################################################################################

#Exam Schedules
#############################################################################################################
def get_exam_schedule_current(api_key):
    url = "https://openapi.data.uwaterloo.ca/v3/ExamSchedules"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_exam_schedule_for_term(api_key, code):
    url = f"https://openapi.data.uwaterloo.ca/v3/ExamSchedules/{code}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()
#############################################################################################################

#Food Services
#############################################################################################################
def get_food_outlets(api_key):
    url = "https://openapi.data.uwaterloo.ca/v3/FoodServices/outlets"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_food_outlet_by_id(api_key, outlet_id):
    url = f"https://openapi.data.uwaterloo.ca/v3/FoodServices/outlets/{outlet_id}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_food_outlet_by_name(api_key, name):
    url = f"https://openapi.data.uwaterloo.ca/v3/FoodServices/outlets/{name}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_food_franchises(api_key):
    url = "https://openapi.data.uwaterloo.ca/v3/FoodServices/franchises"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_food_franchise_by_id(api_key, franchise_id):
    url = f"https://openapi.data.uwaterloo.ca/v3/FoodServices/franchises/{franchise_id}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_food_franchise_by_name(api_key, name):
    url = f"https://openapi.data.uwaterloo.ca/v3/FoodServices/franchises/{name}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()
#############################################################################################################

#Holiday Dates
#############################################################################################################
def get_paid_holidays(api_key):
    url = "https://openapi.data.uwaterloo.ca/v3/HolidayDates/paidholidays"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_paid_holidays_by_year(api_key, year):
    url = f"https://openapi.data.uwaterloo.ca/v3/HolidayDates/paidholidays/{year}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_paid_holidays_ics():
    url = "https://openapi.data.uwaterloo.ca/v3/HolidayDates/paidholidays/ics"
    # no API key needed
    return requests.get(url).text
#############################################################################################################

#Important Dates
#############################################################################################################
def get_important_dates(api_key):
    url = "https://openapi.data.uwaterloo.ca/v3/ImportantDates"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()
#############################################################################################################

#Locations
#############################################################################################################
def get_locations(api_key):
    url = "https://openapi.data.uwaterloo.ca/v3/Locations"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_locations_geojson(api_key):
    url = "https://openapi.data.uwaterloo.ca/v3/Locations/geojson"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_location_by_code(api_key, code):
    url = f"https://openapi.data.uwaterloo.ca/v3/Locations/{code}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_location_by_code_geojson(api_key, code):
    url = f"https://openapi.data.uwaterloo.ca/v3/Locations/{code}/geojson"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def search_location_by_name(api_key, name):
    url = f"https://openapi.data.uwaterloo.ca/v3/Locations/search/{name}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def search_location_by_name_geojson(api_key, name):
    url = f"https://openapi.data.uwaterloo.ca/v3/Locations/search/{name}/geojson"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()
#############################################################################################################

#Subjects
#############################################################################################################
def get_subjects(api_key):
    url = "https://openapi.data.uwaterloo.ca/v3/Subjects"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_subject_by_code(api_key, code):
    url = f"https://openapi.data.uwaterloo.ca/v3/Subjects/{code}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_subjects_for_organization(api_key, organization_code):
    url = f"https://openapi.data.uwaterloo.ca/v3/Subjects/associatedto/{organization_code}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()
#############################################################################################################

#Terms
#############################################################################################################
def get_all_terms(api_key):
    url = "https://openapi.data.uwaterloo.ca/v3/Terms"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_current_term(api_key):
    url = "https://openapi.data.uwaterloo.ca/v3/Terms/current"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_term_by_code(api_key, code):
    url = f"https://openapi.data.uwaterloo.ca/v3/Terms/{code}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_terms_for_academic_year(api_key, year):
    url = f"https://openapi.data.uwaterloo.ca/v3/Terms/foracademicyear/{year}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()
#############################################################################################################

#WCMS
#############################################################################################################
def get_wcms_sites(api_key):
    url = "https://openapi.data.uwaterloo.ca/v3/Wcms"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_wcms_by_id(api_key, site_id):
    url = f"https://openapi.data.uwaterloo.ca/v3/Wcms/{site_id}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_wcms_latest_news(api_key, max_items):
    url = f"https://openapi.data.uwaterloo.ca/v3/Wcms/latestnews/{max_items}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_wcms_latest_events(api_key, max_items):
    url = f"https://openapi.data.uwaterloo.ca/v3/Wcms/latestevents/{max_items}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_wcms_latest_posts(api_key, max_items):
    url = f"https://openapi.data.uwaterloo.ca/v3/Wcms/latestposts/{max_items}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_wcms_latest_opportunities(api_key, max_items):
    url = f"https://openapi.data.uwaterloo.ca/v3/Wcms/latestopportunities/{max_items}"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_wcms_news_by_id(api_key, site_id):
    url = f"https://openapi.data.uwaterloo.ca/v3/Wcms/{site_id}/news"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_wcms_posts_by_id(api_key, site_id):
    url = f"https://openapi.data.uwaterloo.ca/v3/Wcms/{site_id}/posts"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_wcms_opportunities_by_id(api_key, site_id):
    url = f"https://openapi.data.uwaterloo.ca/v3/Wcms/{site_id}/opportunities"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()

def get_wcms_events_by_id(api_key, site_id):
    url = f"https://openapi.data.uwaterloo.ca/v3/Wcms/{site_id}/events"
    headers = {"X-API-KEY": api_key}
    return requests.get(url, headers=headers).json()
#############################################################################################################