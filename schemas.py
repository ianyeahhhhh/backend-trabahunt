import email
from typing import Optional
from pydantic import BaseModel


class Admin_Profile_form(BaseModel):
    email: str
    password: str
    first_name: str
    middle_name: str
    last_name: str
    suffix_name: str
    full_name: str
    admin_status: str

    class Config:
        orm_mode = True


class User_Account_Form(BaseModel):
    email: str
    password: str
    contact_number: str
    user_account_type: str
    account_status: str

    class Config:
        orm_mode = True


class Candidate_Profile_Form(BaseModel):
    user_account_id: int
    candidate_type: str
    first_name: str
    middle_name: str
    last_name: str
    suffix_name: str
    age: int
    gender: str
    birth_date: str
    zip_code: str
    city: str
    region: str
    country: str
    nationality: str
    candidate_image: str
    status_from_hr: str

    class Config:
        orm_mode = True


class Candidate_Education_Detail_Form(BaseModel):
    user_account_id: int
    institute_university_name: str
    highest_education_attainment: str
    institute_university_location: str
    field_of_study: str
    major: str
    graduation_date: str

    class Config:
        orm_mode = True
    

class Candidate_Experience_Detail_Form(BaseModel):
    user_account_id: int
    experience_level: str
    experience_description: str
    year_month_work_experience: str

    class Config:
        orm_mode = True


class Candidate_Resume_Form(BaseModel):
    user_account_id: int
    resume: str

    class Config:
        orm_mode = True


class Company_Profile_Form(BaseModel):
    user_account_id: int
    company_name: str
    profile_description: str
    establishment_date: str
    company_website_url: str
    company_logo: str

    class Config:
        orm_mode = True


class Company_Addition_Info_Form(BaseModel):
    user_account_id: int
    registration_number: str
    country: str
    region: str
    zip_code: str
    city: str
    company_contact_number: str

    class Config:
        orm_mode = True
        

class Company_Subscription_Form(BaseModel):
    subscription_date: str
    expiry_date: str
    package_quantity: str
    subscription_status: str
    subscription_type_code: int
    subscription_type: str
    company_id: int
    package_id: int
    user_account_id: int

    class Config:
        orm_mode = True


class Job_Post_Form(BaseModel):
    job_description: str
    job_post_status: str
    job_title: str
    job_position_level: str
    salary: str
    user_account_id: int
    job_location_id: int
    company_id: int

    class Config:
        orm_mode = True


class Job_Additional_Info_Form(BaseModel):
    job_type_name: str
    job_specialization_name: str
    job_qualification: str
    career_level: str
    job_post_id: int

    class Config:
        orm_mode = True


class Job_Location_Form(BaseModel):
    city: str
    region: str
    country: str
    zip_code: str
    job_post_id: int

    class Config:
        orm_mode = True


class Interview_Info_Form(BaseModel):
    candidate_profile_id: int
    interview_date: str
    interview_time: str
    interview_location: str
    interview_additional_info: str
    interview_status: str
    interview_remarks: str
    created_by: int
    updated_by: int

    class Config:
        orm_mode = True


class Job_Application_Form(BaseModel):
    full_name: str
    email: str
    contact_number: str
    job_application_status: str
    candidate_id: int
    employer_id: int
    job_post_id: int

    class Config:
        orm_mode = True


class Employee_Info_Form(BaseModel):
    full_name: str
    position: str
    hired_by: int
    candidate_id: str

    class Config:
        orm_mode = True


class Job_Offer_Form(BaseModel):
    offered_to: int
    job_title: str
    job_position: str
    salary: str
    city: str
    region: str
    zip_code: str
    country: str
    job_offer_description: str
    job_offer_status: str
    interview_info_id : int
    company_id : int
    created_by: int
    updated_by: int

    class Config:
        orm_mode = True



class Payment_Form(BaseModel):
    payment_description: str
    payment_type: str
    payment_status: str
    company_id: int
    company_subscription_id: int


class Session_Info_Form(BaseModel):
    user_account_id: int
    time_of_login: str
    time_of_logout: str

    class Config:
        orm_mode = True


class Request_Form_Form(BaseModel):
    user_account_id: int
    job_position: str
    job_specialization_name: str
    zip_code: str
    city: str
    region: str
    country: str
    salary_range: str
    job_type_name: str
    status: str

    class Config:
        orm_mode = True


class Login_Form(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

