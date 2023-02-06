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
    review_status: str

    class Config:
        orm_mode = True


class Company_Addition_Info_Form(BaseModel):
    user_account_id: int
    registration_number: str
    country: str
    region: str
    zip_code: str
    city: str

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


class Company_Legal_Document_Form(BaseModel):
    user_account_id: int
    legal_document: str

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
    candidate_personal_information_id: int
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
    interview_info_id: int
    company_id: int
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
    specialization: str
    department: str
    position: str
    employment_type: str
    salary_range: str
    zip_code: str
    city: str
    region: str
    country: str
    status: str
    user_account_id: int

    class Config:
        orm_mode = True


class AWS_Form(BaseModel):
    filename: str


class Login_Form(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

##
##
# new candidate
class Candidate_Personal_Information_Form(BaseModel):
    candidate_type: str
    first_name: str
    middle_name: str
    last_name: str
    suffix_name: str
    email: str
    birth_date: str
    sex: str
    block_number: str
    lot_number: str
    street: str
    barangay: str
    city: str
    zip_code: str
    region: str
    country: str
    nationality: str
    civil_status: str
    review_status: str
    candidate_image: str
    user_account_id: int

class Candidate_Job_Information_Form(BaseModel):
    department: str
    position: str
    employee_category: str
    employment_type: str
    specialization: str
    date_hired: str
    user_account_id: int

class Candidate_Job_History_Form(BaseModel):
    previous_job_title: str
    employer: str
    start_date: str
    end_date: str
    user_account_id: int

class Candidate_Education_Form(BaseModel):
    highest_educational_attainment: str
    institute_name: str
    institute_location: str
    field_of_study: str
    major: str
    date_graduated: str
    user_account_id: int

class Candidate_Family_Background_Form(BaseModel):
    mothers_name: str
    mothers_occupation: str
    mothers_birth_date: str
    fathers_name: str
    fathers_occupation: str
    fathers_birth_date: str
    number_of_siblings: str
    user_account_id: int

class Candidate_Experience_Detail_Form(BaseModel):
    experience_level: str
    work_experience: str
    personal_skills: str
    achievements: str
    certification: str
    user_account_id: int

class Candidate_Character_References_Form(BaseModel):
    char_ref_name_1: str
    position_1: str
    telephone_1: str
    company_1: str
    char_ref_name_2: str
    position_2: str
    telephone_2: str
    company_2: str
    char_ref_name_3: str
    position_3: str
    telephone_3: str
    company_3: str
    user_account_id: int

class Candidate_Emergency_Contact_Form(BaseModel):
    name: str
    relationship: str
    contact_number: str
    address: str
    user_account_id: int
