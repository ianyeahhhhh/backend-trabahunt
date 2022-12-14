from datetime import datetime
import email
from email.policy import default
from enum import unique
from sqlite3 import Date
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BINARY, BLOB  
from database import Base


class Admin_Profile(Base):
    __tablename__ = "admin_profile"

    admin_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255))
    password = Column(String(255))
    first_name = Column(String(255))
    middle_name = Column(String(255))
    last_name = Column(String(255))
    suffix_name = Column(String(255))
    full_name = Column(String(255))
    admin_status = Column(String(10), default="Active")
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    created_by = Column(Integer)
    updated_by = Column(Integer)


class User_Account(Base):
    __tablename__ = "user_account"

    user_account_id = Column(Integer, primary_key=True, index=True)
    user_account_type = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    contact_number = Column(String(255))
    account_status = Column(String(255), default='Active')
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    created_by = Column(Integer)
    updated_by = Column(Integer)


class Candidate_Profile(Base):
    __tablename__ = "candidate_profile"

    candidate_profile_id = Column(Integer, primary_key=True, index=True)
    candidate_type = Column(String(255))
    first_name = Column(String(255))
    middle_name = Column(String(255))
    last_name = Column(String(255))
    suffix_name = Column(String(255))
    full_name = Column(String(255))
    age = Column(Integer)
    gender = Column(String(100))
    birth_date = Column(String(100))
    zip_code = Column(String(255))
    city = Column(String(255))
    region = Column(String(255))
    country = Column(String(255))
    nationality = Column(String(255))
    status_from_hr = Column(String(255))
    candidate_image = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    user_account_id = Column(Integer)
    created_by = Column(Integer)
    updated_by = Column(Integer)


class Candidate_Education_Detail(Base):
    __tablename__ = "candidate_education_detail"

    candidate_education_detail_id = Column(
        Integer, primary_key=True, index=True)
    institute_university_name = Column(String(255))
    highest_education_attainment = Column(String(255))
    institute_university_location = Column(String(255))
    field_of_study = Column(String(255))
    major = Column(String(255))
    graduation_date = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    user_account_id = Column(Integer)
    created_by = Column(Integer)
    updated_by = Column(Integer)


class Candidate_Experience_Detail(Base):
    __tablename__ = "candidate_experience_detail"

    candidate_experience_detail_id = Column(
        Integer, primary_key=True, index=True)
    experience_level = Column(String(255))
    experience_description = Column(String(255))
    year_month_work_experience = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    user_account_id = Column(Integer)
    created_by = Column(Integer)
    updated_by = Column(Integer)


class Candidate_Resume(Base):
    __tablename__ = "candidate_resume"

    candidate_resume_id = Column(Integer, primary_key=True, index=True)
    user_account_id = Column(Integer)
    resume = Column(String(255))


class Company_Profile(Base):
    __tablename__ = "company_profile"

    company_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(255))
    profile_description = Column(String(255))
    establishment_date = Column(String(255))
    company_website_url = Column(String(255))
    company_logo = Column(String(255))
    company_status = Column(String(100), default='Active')
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    user_account_id = Column(Integer)
    created_by = Column(Integer)
    updated_by = Column(Integer)


class Company_Addition_Info(Base):
    __tablename__ = "company_addition_info"

    company_addition_info_id = Column(Integer, primary_key=True, index=True)
    registration_number = Column(String(255))
    country = Column(String(255))
    region = Column(String(255))
    zip_code = Column(String(255))
    city = Column(String(255))
    company_contact_number = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    user_account_id = Column(Integer)
    created_by = Column(Integer)
    updated_by = Column(Integer)


class Company_Subscription(Base):
    __tablename__ = "company_subscription"

    company_subscription_id = Column(Integer, primary_key=True, index=True)
    subscription_date = Column(String(255))
    expiry_date = Column(String(255))
    package_quantity = Column(String(255))
    subscription_type = Column(String(255))
    subscription_type_code = Column(Integer)
    subscription_status = Column(String(255))
    updated_at = Column(DateTime)
    created_at = Column(DateTime)

    user_account_id = Column(Integer)
    company_id = Column(Integer)
    package_id = Column(Integer)
    updated_by = Column(Integer)
    created_by = Column(Integer)


class Payment(Base):
    __tablename__ = "payment"

    payment_id = Column(Integer, primary_key=True, index=True)
    payment_description = Column(String(255))
    payment_type = Column(String(255))
    payment_status = Column(String(10), default="Pending")
    updated_at = Column(DateTime)
    created_at = Column(DateTime)

    company_id = Column(Integer)
    company_subscription_id = Column(Integer)
    created_by = Column(Integer)
    updated_by = Column(Integer)


class Package(Base):
    __tablename__ = "package"

    package_id = Column(Integer, primary_key=True, index=True)
    package_name = Column(String(255))
    package_description = Column(String(255))
    package_price = Column(String(255))
    package_status = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    created_by = Column(Integer)
    updated_by = Column(Integer)


class Job_Post(Base):
    __tablename__ = "job_post"

    job_post_id = Column(Integer, primary_key=True, index=True)
    job_description = Column(String(255))
    job_post_status = Column(String(255))
    job_title = Column(String(255))
    job_position_level = Column(String(255))
    salary = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    user_account_id = Column(Integer)
    job_location_id = Column(Integer)
    company_id = Column(Integer)
    created_by = Column(Integer)
    updated_by = Column(Integer)


class Job_Additional_Info(Base):
    __tablename__ = "job_additional_info"

    job_additional_info_id = Column(Integer, primary_key=True, index=True)
    job_type_name = Column(String(255))
    job_specialization_name = Column(String(255))
    job_qualification = Column(String(255))
    career_level = Column(String(255))
    job_post_id = Column(Integer)


class Job_Location(Base):
    __tablename__ = "job_location"

    job_location_id = Column(Integer, primary_key=True, index=True)
    city = Column(String(255))
    region = Column(String(255))
    country = Column(String(255))
    zip_code = Column(String(255))
    job_post_id = Column(Integer)


class Job_Application(Base):
    __tablename__ = "job_application"

    job_application_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255))
    email = Column(String(255))
    contact_number = Column(String(255))
    candidate_id = Column(Integer)
    employer_id = Column(Integer)
    job_application_status = Column(String(255), default='Pending')
    job_post_id = Column(Integer)
    created_at = Column(DateTime)


class Interview_Info(Base):
    __tablename__ = "interview_info"

    interview_info_id = Column(Integer, primary_key=True, index=True)
    candidate_profile_id = Column(Integer)
    interview_date = Column(String(255))
    interview_time = Column(String(255))
    interview_location = Column(String(255))
    interview_additional_info = Column(String(255))
    interview_status = Column(String(255))
    interview_remarks = Column(String(255))
    created_by = Column(Integer)
    updated_by = Column(Integer)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)


class Job_Offer(Base):
    __tablename__ = "job_offer"

    job_offer_id = Column(Integer, primary_key=True, index=True)
    offered_to = Column(Integer)
    job_title = Column(String(255))
    job_position = Column(String(255))
    salary = Column(String(255))
    city = Column(String(255))
    region = Column(String(255))
    zip_code = Column(String(255))
    country = Column(String(255))
    job_offer_description = Column(String(255))
    job_offer_status = Column(String(255))
    interview_info_id = Column(Integer)
    company_id = Column(Integer)
    created_by = Column(Integer)
    updated_by = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Employee_Info(Base):
    __tablename__ = "employee_info"

    employee_id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer)
    full_name = Column(String(255))
    position = Column(String(255))
    date_hired = Column(DateTime)
    hired_by = Column(Integer)
    created_by = Column(Integer)
    updated_by = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Session_Info(Base):
    __tablename__ = "session_info"

    session_info_id = Column(Integer, primary_key=True, index=True)
    user_account_id = Column(Integer)
    time_of_login = Column(String(255))
    time_of_logout = Column(String(255))


class Files(Base):
    __tablename__ = "files"

    file_id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(255))
    file_content = Column(String(100000))
    created_by = Column(Integer)
    updated_by = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Request_Form(Base):
    __tablename__ = "request_form"

    request_id = Column(Integer, primary_key=True, index=True)
    user_account_id = Column(Integer)
    job_position = Column(String(255))
    job_specialization_name = Column(String(255))
    zip_code = Column(String(255))
    city = Column(String(255))
    region = Column(String(255))
    country = Column(String(255))
    salary_range = Column(String(255))
    job_type_name = Column(String(255))
    status = Column(String(255))
    created_by = Column(Integer)
    updated_by = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
