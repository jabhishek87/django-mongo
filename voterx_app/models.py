from django.db import models
from django.views.generic import ListView

from django.db import models

from djangotoolbox.fields import ListField, EmbeddedModelField


class Name(models.Model):
    voters_firstname = models.CharField()
    voters_middlename = models.CharField()
    voters_lastname = models.CharField()
    voters_namesuffix = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "voters_firstname": self.voters_firstname,
            # other stuff
        }


class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True) # <---
    title = models.CharField(max_length=255)
    text = models.TextField()
    tags = ListField()
    comments = ListField(EmbeddedModelField('Comment'))

    def as_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "text": self.text,
            "tags": [tag for tag in self.tags],
            "comments": [comment.as_dict() for comment in self.comments],
            # other stuff
        }

class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    author = EmbeddedModelField('Author')
    text = models.TextField()

    def as_dict(self):

        return {
            "id": self.id,
            "author": self.author.name if self.author else '',
            "text": self.text,
            # other stuff
        }

class Author(models.Model):
    name = models.CharField()

"""

from time import time
from mongoengine import *
from datetime import datetime
import uuid
# from datetime import timedelta
# import numpy as np

from mongoengine.queryset import QuerySet
from bson import json_util

# from backend_app.models.engine import *
# from backend_app.models.utilities import *
# from backend_app.ims import mongo, app
# with app.app_context():
#     IMSdb = mongo.db.get_collection('IMS')

TEST = False

##############
# Mongo Engine


class Residence(Document):

    Residence_Addresses_AddressLine = StringField(default='None')
    Residence_Addresses_ExtraAddressLine = StringField(default='None')
    Residence_Addresses_City = StringField(default='None')
    Residence_Addresses_State = StringField(default='None')
    Residence_Addresses_Zip = StringField(default='None')
    Residence_Addresses_ZipPlus4 = StringField(default='None')
    Residence_Addresses_HouseNumber = StringField(default='None')
    Residence_Addresses_PrefixDirection = StringField(default='None')
    Residence_Addresses_StreetName = StringField(default='None')
    Residence_Addresses_Designator = StringField(default='None')
    Residence_Addresses_SuffixDirection = StringField(default='None')
    Residence_Addresses_ApartmentNum = StringField(default='None')
    Residence_Addresses_ApartmentType = StringField(default='None')
    Residence_Addresses_CensusTract = StringField(default='None')
    Residence_Addresses_CensusBlockGroup = StringField(default='None')
    Residence_Addresses_CensusBlock = StringField(default='None')
    Residence_Families_FamilyID = StringField(default='None')
    Residence_Families_HHCount = StringField(default='None')
    Residence_HHGender_Description = StringField(default='None')
    Residence_HHParties_Description = StringField(default='None')

    Mailing_Addresses_AddressLine = StringField(default='None')
    Mailing_Addresses_ExtraAddressLine = StringField(default='None')
    Mailing_Addresses_City = StringField(default='None')
    Mailing_Addresses_State = StringField(default='None')
    Mailing_Addresses_Zip = StringField(default='None')
    Mailing_Addresses_ZipPlus4 = StringField(default='None')
    Mailing_Addresses_HouseNumber = StringField(default='None')
    Mailing_Addresses_PrefixDirection = StringField(default='None')
    Mailing_Addresses_StreetName = StringField(default='None')
    Mailing_Addresses_Designator = StringField(default='None')
    Mailing_Addresses_SuffixDirection = StringField(default='None')
    Mailing_Addresses_ApartmentNum = StringField(default='None')
    Mailing_Addresses_ApartmentType = StringField(default='None')
    Mailing_Families_FamilyID = StringField(default='None')
    Mailing_Families_HHCount = StringField(default='None')
    Mailing_HHGender_Description = StringField(default='None')
    Mailing_HHParties_Description = StringField(default='None')

    meta = {'allow_inheritance': True}


class PhoneNumber(Document):

    Phone = FloatField(default=0000000000)
    PhnMatch = FloatField(default=0)
    Telconfidencecode = FloatField(default=0)
    telcellflag = IntField(default=0)
    Voters_StateVoterID = StringField(default='None')
    Voters_CountyVoterID = StringField(default='None')
    VoterTelephones_FullPhone = IntField(default=0)
    VoterTelephones_Phone10 = IntField(default=0)
    VoterTelephones_TelConfidenceCode = IntField(default=0)
    VoterTelephones_TelCellFlag = BooleanField(default=False)
    View_Ops_CellPhone_Phone10 = IntField(default=0)
    View_Ops_CellPhone_FullPhone = IntField(default=0)

    meta = {'allow_inheritance': True}


class Email(Document):
    L2_EmailAddress = EmailField(default='UNK@UNK.UNK') #default='UNK@UNK'
    EmailAddresses_EmailAddress = EmailField(default='UNK@UNK.UNK')

    meta = {'allow_inheritance': True}


class Demographics(Document):
    military_status = {}
    marital_status = {}
    Voters_Gender = StringField(default='UNK')
    Voters_Age = FloatField(default=0,min_value=0,max_value=120)
    Voters_BirthDate = StringField(default='UNK')
    Voters_PlaceOfBirth = StringField(default='UNK')
    Languages_Description = StringField(default='English')
    MilitaryStatus_Description = StringField(default='UNK')
    MaritalStatus_Description = StringField(default='UNK')

    meta = {'allow_inheritance': True}


class Commercial(Document):

    CommercialData_PresenceOfChildrenCode = StringField(default='UNK')
    CommercialData_ISPSA = FloatField(default=0)
    CommercialData_DwellingType = StringField(default='UNK')
    CommercialData_DwellingUnitSize = StringField(default='UNK')
    CommercialData_EstimatedIncomeAmount = DecimalField(precision=2, min_value=0, default=0)
    CommercialData_EstimatedIncome = DecimalField(precision=2, min_value=0, default=0)
    CommercialData_Education = StringField(default='UNK')
    CommercialData_Occupation = StringField(default='UNK')
    CommercialData_HomePurchasePrice = DecimalField(precision=2, min_value=0, default=0)
    CommercialData_HomePurchaseDate = DateTimeField(default=datetime.utcnow())
    CommercialData_LandValue = DecimalField(precision=2, min_value=0, default=0)
    CommercialData_PropertyType = StringField(default='UNK')
    CommercialData_EstHomeValue = DecimalField(precision=2, min_value=0, default=0)
    CommercialData_HHComposition = StringField(default='UNK')

    meta = {'allow_inheritance': True}


class Party(Document):

    Parties_Description = StringField(default='UNK')
    CountyEthnic_Description = StringField(default='UNK')
    Ethnic_Description = StringField(default='UNK')
    Religions_Description = StringField(default='UNK')
    Voters_CalculatedRegDate = StringField(default='UNK')
    Voters_OfficialRegDate = StringField(default='UNK')

    meta = {'allow_inheritance': True}


class District(Document):
    US_Congressional_District = FloatField(default=0)
    State_House_District = FloatField(default=0)
    State_Legislative_District = FloatField(default=0)
    State_Senate_District = FloatField(default=0)
    County = StringField(default='UNK')
    City = StringField(default='UNK')
    City_Council_Commissioner_District = StringField(default='UNK')
    City_Mayoral_District = StringField(default='UNK')
    City_Ward = StringField(default='UNK')
    Village = StringField(default='UNK')
    Village_Ward = StringField(default='UNK')
    Town_District = StringField(default='UNK')
    Town_Ward = StringField(default='UNK')
    Township = StringField(default='UNK')
    Township_Ward = StringField(default='UNK')
    Borough = StringField(default='UNK')
    Borough_Ward = StringField(default='UNK')
    Hamlet_Community_Area = StringField(default='UNK')
    Board_of_Education_District = StringField(default='UNK')
    Board_of_Education_SubDistrict = StringField(default='UNK')
    City_School_District = StringField(default='UNK')
    Community_College = StringField(default='UNK')
    Community_College_Commissioner_District = StringField(default='UNK')
    Community_College_SubDistrict = StringField(default='UNK')
    Congressional_Township = StringField(default='UNK')
    County_Board_of_Education_District = StringField(default='UNK')
    County_Commissioner_District = StringField(default='UNK')
    County_Fire_District = StringField(default='UNK')
    County_Hospital_District = StringField(default='UNK')
    County_Legislative_District = StringField(default='UNK')
    County_Library_District = StringField(default='UNK')
    County_Sewer_District = StringField(default='UNK')
    County_Superintendent_of_Schools_District = StringField(default='UNK')
    County_Supervisorial_District = StringField(default='UNK')
    County_Unified_School_District = StringField(default='UNK')
    County_Water_District = StringField(default='UNK')
    County_Water_SubDistrict = StringField(default='UNK')
    Designated_Market_Area_DMA = StringField(default='UNK')
    District_Attorney = StringField(default='UNK')
    Educational_Service_District = StringField(default='UNK')
    Educational_Service_Subdistrict = StringField(default='UNK')
    Elementary_School_District = StringField(default='UNK')
    Elementary_School_SubDistrict = StringField(default='UNK')
    Emergency_Communication_911_District = StringField(default='UNK')
    Emergency_Communication_911_SubDistrict = StringField(default='UNK')
    Fire_District = StringField(default='UNK')
    Fire_Protection_District = StringField(default='UNK')
    Fire_Protection_SubDistrict = StringField(default='UNK')
    Fire_SubDistrict = StringField(default='UNK')
    Health_District = StringField(default='UNK')
    High_School_District = StringField(default='UNK')
    High_School_SubDistrict = StringField(default='UNK')
    Hospital_District = StringField(default='UNK')
    Hospital_SubDistrict = StringField(default='UNK')
    Irrigation_District = StringField(default='UNK')
    Irrigation_SubDistrict = StringField(default='UNK')
    Judicial_Appellate_District = StringField(default='UNK')
    Judicial_Chancery_Court = StringField(default='UNK')
    Judicial_Circuit_Court_District = StringField(default='UNK')
    Judicial_County_Court_District = StringField(default='UNK')
    Judicial_District = StringField(default='UNK')
    Judicial_District_Court_District = StringField(default='UNK')
    Judicial_Family_Court_District = StringField(default='UNK')
    Judicial_Jury_District = StringField(default='UNK')
    Judicial_Magistrate_Division = StringField(default='UNK')
    Judicial_Sub_Circuit_District = StringField(default='UNK')
    Judicial_Superior_Court_District = StringField(default='UNK')
    Justice_of_the_Peace = StringField(default='UNK')
    Levee_District = StringField(default='UNK')
    Library_District = StringField(default='UNK')
    Library_SubDistrict = StringField(default='UNK')
    Lighting_District = StringField(default='UNK')
    Metro_Service_District = StringField(default='UNK')
    Metro_Service_Subdistrict = StringField(default='UNK')
    Metro_Transit_District = StringField(default='UNK')
    Metropolitan_Water_District = StringField(default='UNK')
    Middle_School_District = StringField(default='UNK')
    Municipal_Advisory_Council_District = StringField(default='UNK')
    Municipal_Court_District = StringField(default='UNK')
    Municipal_Utility_District = StringField(default='UNK')
    Municipal_Utility_SubDistrict = StringField(default='UNK')
    Municipal_Water_District = StringField(default='UNK')
    Municipal_Water_SubDistrict = StringField(default='UNK')
    Park_District = StringField(default='UNK')
    Park_SubDistrict = StringField(default='UNK')
    Police_District = StringField(default='UNK')
    Port_District = StringField(default='UNK')
    Port_SubDistrict = StringField(default='UNK')
    Precinct = StringField(default='UNK')
    Public_Utility_District = StringField(default='UNK')
    Public_Utility_SubDistrict = StringField(default='UNK')
    Rapid_Transit_District = StringField(default='UNK')
    Reclamation_District = StringField(default='UNK')
    Recreation_District = StringField(default='UNK')
    Recreational_SubDistrict = StringField(default='UNK')
    Sanitary_District = StringField(default='UNK')
    Sanitary_SubDistrict = StringField(default='UNK')
    School_Board_District = StringField(default='UNK')
    School_District = StringField(default='UNK')
    School_District_Vocational = StringField(default='UNK')
    School_Subdistrict = StringField(default='UNK')
    Sewer_District = StringField(default='UNK')
    Sewer_Maintenance_District = StringField(default='UNK')
    Sewer_SubDistrict = StringField(default='UNK')
    Soil_AND_Water_District = StringField(default='UNK')
    Special_Tax_District = StringField(default='UNK')
    State_Board_of_Equalization = StringField(default='UNK')
    Superintendent_of_Schools_District = StringField(default='UNK')
    Transit_District = StringField(default='UNK')
    Transit_SubDistrict = StringField(default='UNK')
    Unified_School_District = StringField(default='UNK')
    Unified_School_SubDistrict = StringField(default='UNK')
    Wastewater_District = StringField(default='UNK')
    Water_Agency = StringField(default='UNK')
    Water_Agency_SubDistrict = StringField(default='UNK')
    Water_Conservation_District = StringField(default='UNK')
    Water_Conservation_SubDistrict = StringField(default='UNK')
    Water_District = StringField(default='UNK')
    Water_SubDistrict = StringField(default='UNK')
    Weed_District = StringField(default='UNK')

    meta = {'allow_inheritance': True}

class Commercial2(Document):
    CommercialDataLL_Gun_Owner = StringField(default='UNK')
    CommercialDataLL_Veteran = StringField(default='UNK')
    CommercialDataLL_Affordable_Care_Act = StringField(default='UNK')
    CommercialDataLL_Church_Attendee = StringField(default='UNK')
    CommercialDataLL_Election_of_Conservative_Judges = StringField(default='UNK')
    CommercialDataLL_Gay_Marriage = StringField(default='UNK')
    CommercialDataLL_Gun_Control = StringField(default='UNK')
    CommercialDataLL_Immigration_Loosen_Restrictions = StringField(default='UNK')
    CommercialDataLL_Lawsuit_Damages_Should_be_Limited = StringField(default='UNK')
    CommercialDataLL_Privatize_Social_Security = StringField(default='UNK')
    CommercialDataLL_Pro_Choice = StringField(default='UNK')
    CommercialDataLL_Pro_Life = StringField(default='UNK')
    CommercialDataLL_School_Choice = StringField(default='UNK')
    CommercialDataLL_Social_Views = StringField(default='UNK')
    CommercialDataLL_Taxes_Raise = StringField(default='UNK')
    CommercialDataLL_Donates_to_Animal_Welfare = StringField(default='UNK')
    CommercialDataLL_Donates_to_Arts_and_Culture = StringField(default='UNK')
    CommercialDataLL_Donates_to_Childrens_Causes = StringField(default='UNK')
    CommercialDataLL_Donates_to_Healthcare = StringField(default='UNK')
    CommercialDataLL_Donates_to_International_Aid_Causes = StringField(default='UNK')
    CommercialDataLL_Donates_to_Veterans_Causes = BooleanField(default=False)
    CommercialDataLL_Home_Owner_Or_Renter = StringField(default='UNK')
    CommercialDataLL_Net_Worth = StringField(default='UNK')
    CommercialDataLL_Business_Owner = StringField(default='UNK')
    CommercialDataLL_Investor = BooleanField(default=False)
    CommercialDataLL_Donates_to_Wildlife_Preservation = StringField(default='UNK')
    CommercialDataLL_Donates_to_Conservative_Causes = StringField(default='UNK')
    CommercialDataLL_Donates_to_Liberal_Causes = StringField(default='UNK')
    CommercialDataLL_Donates_to_Local_Community = BooleanField(default=False)
    CommercialDataLL_PetOwner_Horse = BooleanField(default=False)
    CommercialDataLL_PetOwner_Cat = BooleanField(default=False)
    CommercialDataLL_PetOwner_Dog = BooleanField(default=False)
    CommercialDataLL_PetOwner_Other = BooleanField(default=False)
    CommercialDataLL_Home_Office = StringField(default='UNK')
    CommercialDataLL_Hispanic_Country_Origin = StringField(default='UNK')
    CommercialDataLL_Household_Primary_Language = StringField(default='UNK')
    CommercialData_OccupationIndustry = StringField(default='UNK')

    meta = {'allow_inheritance': True}


class CommercialFEC(Document):
    FECDonors_NumberOfDonations = FloatField(default=0)
    FECDonors_TotalDonationsAmount = DecimalField(precision=2, min_value=0, default=0)
    FECDonors_TotalDonationsAmt_Range = DecimalField(precision=2, min_value=0, default=0)
    FECDonors_LastDonationDate = DateTimeField(default=datetime.utcnow())
    FECDonors_AvgDonation = DecimalField(precision=2, min_value=0, default=0)
    FECDonors_AvgDonation_Range = DecimalField(precision=2, min_value=0, default=0)
    FECDonors_PrimaryRecipientOfContributions = StringField(default='UNK')

    meta = {'allow_inheritance': True}


class CommercialInterests(Document):
    CommercialDataLL_Reading_General_In_Household = BooleanField(default=False)
    CommercialDataLL_Reading_Religious_In_Household = BooleanField(default=False)
    CommercialDataLL_Reading_Science_Fiction_In_Household = BooleanField(default=False)
    CommercialDataLL_Reading_Magazines_In_Household = BooleanField(default=False)
    CommercialDataLL_Reading_Audio_Books_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_History_Military_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Current_Affairs_Politics_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Religious_Inspirational_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Science_Space_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Education_Online_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Electronic_Gaming_In_Household = BooleanField(default=False)
    CommercialDataLL_Buyer_Antiques_In_Household = BooleanField(default=False)
    CommercialDataLL_Buyer_Art_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Theater_Performing_Arts_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_the_Arts_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Musical_Instruments_In_Household = BooleanField(default=False)
    CommercialDataLL_Collector_General_In_Household = BooleanField(default=False)
    CommercialDataLL_Collector_Stamps_In_Household = BooleanField(default=False)
    CommercialDataLL_Collector_Coins_In_Household = BooleanField(default=False)
    CommercialDataLL_Collector_Arts_In_Household = BooleanField(default=False)
    CommercialDataLL_Collector_Antiques_In_Household = BooleanField(default=False)
    CommercialDataLL_Collector_Avid_In_Household = BooleanField(default=False)
    CommercialDataLL_Collector_Sports_In_Household = BooleanField(default=False)
    CommercialDataLL_Collector_Military_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Home_Repair_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Auto_Work_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Sewing_Knitting_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Woodworking_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Photography_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Aviation_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_House_Plants_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Crafts_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Gardening_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Photography_Video_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Smoking_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Home_Furnishings_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Home_Improvement_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Food_Wines_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Cooking_General_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Cooking_Gourmet_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Foods_Natural_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_BoardGames_Puzzles_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Gaming_Casino_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Sweepstakes_Contests_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Travel_Domestic_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Travel_International_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Travel_Cruise_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Exercise_Health_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Exercise_Running_Jogging_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Exercise_Walking_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Exercise_Aerobic_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_SpectatorSports_Auto_Racing_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_SpectatorSports_on_TV_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_SpectatorSports_Football_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_SpectatorSports_Baseball_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_SpectatorSports_Basketball_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_SpectatorSports_Hockey_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_SpectatorSports_Soccer_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Tennis_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Golf_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Snow_Skiing_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Motorcycling_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Nascar_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Boating_Sailing_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Scuba_Diving_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Sports_Leisure_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Hunting_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Fishing_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Camping_Hiking_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Shooting_In_Household = BooleanField(default=False)
    CommercialDataLL_Interest_in_Automotive_Parts_Accessories_In_Household = BooleanField(default=False)
    CommercialDataLL_Gun_Owner_Concealed_Permit = BooleanField(default=False)

    meta = {'allow_inheritance': True}


class CommercialHomePurchasing(Document):
    CommercialData_UpscaleBuyerInHome = BooleanField(default=False)
    CommercialData_UpscaleMaleBuyerInHome = BooleanField(default=False)
    CommercialData_UpscaleFemaleBuyerInHome = BooleanField(default=False)
    CommercialData_BookBuyerInHome = BooleanField(default=False)
    CommercialData_FamilyMagazineInHome = BooleanField(default=False)
    CommercialData_FemaleOrientedMagazineInHome = BooleanField(default=False)
    CommercialData_ReligiousMagazineInHome = BooleanField(default=False)
    CommercialData_GardeningMagazineInHome = BooleanField(default=False)
    CommercialData_CulinaryInterestMagazineInHome = BooleanField(default=False)
    CommercialData_HealthFitnessMagazineInHome = BooleanField(default=False)
    CommercialData_DoItYourselferMagazineInHome = BooleanField(default=False)
    CommercialData_FinancialMagazineInHome = BooleanField(default=False)
    CommercialData_ReligiousContributorInHome = BooleanField(default=False)
    CommercialData_PoliticalContributerInHome = BooleanField(default=False)
    CommercialData_DonatesEnvironmentCauseInHome = BooleanField(default=False)
    CommercialData_DonatesToCharityInHome = BooleanField(default=False)
    CommercialData_PresenceOfPremCredCrdInHome = BooleanField(default=False)
    CommercialData_ComputerOwnerInHome = BooleanField(default=False)
    CommercialData_StateIncomeDecile = DecimalField(precision=2, min_value=0, default=0)
    CommercialData_PcntHHWithChildren = FloatField(default=0)
    CommercialData_PcntHHMarriedCoupleWithChild = FloatField(default=0)
    CommercialData_PcntHHMarriedCoupleNoChild = FloatField(default=0)
    CommercialData_PcntHHSpanishSpeaking = FloatField(default=0)
    CommercialData_MedianEducationYears = FloatField(default=0)
    CommercialData_MosaicZ4 = StringField(default='UNK')
    CommercialData_LikelyUnion = BooleanField(default=False)

    meta = {'allow_inheritance': True}


class VoteHistory(Document):
    Vote_Frequency = FloatField(default=0)
    General_2000_11_XX = BooleanField(default=False)
    General_2001_11_XX = BooleanField(default=False)
    General_2002_11_XX = BooleanField(default=False)
    General_2003_11_XX = BooleanField(default=False)
    General_2004_11_XX = BooleanField(default=False)
    General_2005_11_XX = BooleanField(default=False)
    General_2006_11_XX = BooleanField(default=False)
    General_2007_11_XX = BooleanField(default=False)
    General_2008_11_XX = BooleanField(default=False)
    General_2009_11_XX = BooleanField(default=False)
    General_2010_11_XX = BooleanField(default=False)
    General_2011_11_XX = BooleanField(default=False)
    General_2012_11_XX = BooleanField(default=False)
    General_2013_11_XX = BooleanField(default=False)
    General_2014_11_XX = BooleanField(default=False)
    Primary_2000_XX_XX = BooleanField(default=False)
    Primary_2001_XX_XX = BooleanField(default=False)
    Primary_2002_XX_XX = BooleanField(default=False)
    Primary_2003_XX_XX = BooleanField(default=False)
    Primary_2004_XX_XX = BooleanField(default=False)
    Primary_2005_XX_XX = BooleanField(default=False)
    Primary_2006_XX_XX = BooleanField(default=False)
    Primary_2007_XX_XX = BooleanField(default=False)
    Primary_2008_XX_XX = BooleanField(default=False)
    Primary_2009_XX_XX = BooleanField(default=False)
    Primary_2010_XX_XX = BooleanField(default=False)
    Primary_2011_XX_XX = BooleanField(default=False)
    Primary_2012_XX_XX = BooleanField(default=False)
    Primary_2013_XX_XX = BooleanField(default=False)
    Primary_2014_XX_XX = BooleanField(default=False)
    Presidential_Primary_2000_XX_XX = BooleanField(default=False)
    Presidential_Primary_2004_XX_XX = BooleanField(default=False)
    Presidential_Primary_2008_XX_XX = BooleanField(default=False)
    Presidential_Primary_2012_XX_XX = BooleanField(default=False)
    PRI_BLT_2000_XX_XX = StringField(default='UNK')
    PRI_BLT_2001_XX_XX = StringField(default='UNK')
    PRI_BLT_2002_XX_XX = StringField(default='UNK')
    PRI_BLT_2003_XX_XX = StringField(default='UNK')
    PRI_BLT_2004_XX_XX = StringField(default='UNK')
    PRI_BLT_2005_XX_XX = StringField(default='UNK')
    PRI_BLT_2006_XX_XX = StringField(default='UNK')
    PRI_BLT_2007_XX_XX = StringField(default='UNK')
    PRI_BLT_2008_XX_XX = StringField(default='UNK')
    PRI_BLT_2009_XX_XX = StringField(default='UNK')
    PRI_BLT_2010_XX_XX = StringField(default='UNK')
    PRI_BLT_2011_XX_XX = StringField(default='UNK')
    PRI_BLT_2012_XX_XX = StringField(default='UNK')
    PRI_BLT_2013_XX_XX = StringField(default='UNK')
    PRI_BLT_2014_XX_XX = StringField(default='UNK')
    Voters_Active = StringField(default='UNK')

    meta = {'allow_inheritance': True}


class CS_DRTV_Voter(Document):

    Email = EmailField(default='UNK@UNK.UNK')
    State = StringField(default='UNK')
    UID = FloatField(default=0)
    VoterID = FloatField(default=0)
    IsRegistered = BooleanField(default=False)
    IsMostRecentRegistration = BooleanField(default=False)

    Salutation = StringField(default='UNK',max_length=3,choices=('UNK','Mr','Mrs','Ms','Miss'))
    FirstName = StringField(default='UNK')
    MiddleName = StringField(default='UNK')
    LastName = StringField(default='UNK')
    Suffix = StringField(default='UNK')
    Gender = StringField(default='UNK')
    DOB = DateTimeField(default=datetime.utcnow())
    DOB_Year = DateTimeField(default=datetime.utcnow())
    DOB_Month = DateTimeField(default=datetime.utcnow())
    DOB_Day = DateTimeField(default=datetime.utcnow())
    AgeRange = FloatField(default=0)

    HHMember_FirstName = StringField(default='UNK')
    HHMember_MiddleName = StringField(default='UNK')
    HHMember_LastName = StringField(default='UNK')
    Individual_Order = FloatField(default=0)
    M_HouseHoldID = FloatField(default=0)
    M_NumberInHH = FloatField(default=0)
    Ethnicity = StringField(default='UNK')
    Religion = StringField(default='UNK')
    Language = StringField(default='UNK')
    RegRace = StringField(default='UNK')
    Race = StringField(default='UNK')
    IsDeceased = BooleanField(default=False)

    Phone = FloatField(default=0)
    PhoneSource = StringField(default='UNK')
    PhoneLineType = StringField(default='UNK')
    CellPhone = FloatField(default=0)
    CellPhoneSource = StringField(default='UNK')

    CY = FloatField(default=0)
    CName = StringField(default='UNK')
    CD = FloatField(default=0)
    SD = StringField(default='UNK')
    LD = FloatField(default=0)
    JD = FloatField(default=0)
    MuniC = StringField(default='UNK')
    MuniN = StringField(default='UNK')
    Township = StringField(default='UNK')
    Ward = StringField(default='UNK')
    PR = FloatField(default=0)
    PRSplit = FloatField(default=0)
    BB = StringField(default='UNK')
    PName = StringField(default='UNK')
    Vintage = StringField(default='UNK')

    AddressDifferent = BooleanField(default=False)
    RLocationID = FloatField(default=0)
    R_AddrLine1 = StringField(default='UNK')
    R_AddrLine2 = StringField(default='UNK')
    R_City = StringField(default='UNK')
    R_State = StringField(default='UNK')
    R_Zip5 = FloatField(default=0)
    R_USPSZip4 = FloatField(default=0)
    R_FIPS = FloatField(default=0)
    R_CountyName = StringField(default='UNK')

    MLocationID = FloatField(default=0)
    M_AddrLine1 = StringField(default='UNK')
    M_AddrLine2 = StringField(default='UNK')
    M_City = StringField(default='UNK')
    M_State = StringField(default='UNK')
    M_Zip5 = FloatField(default=0)
    M_USPSZip4 = FloatField(default=0)
    M_FIPS = FloatField(default=0)
    M_CountyName = StringField(default='UNK')

    NCOA = StringField(default='UNK')
    NCOA_Type = StringField(default='UNK')
    NCOA_Date = FloatField(default=0)
    RDate = DateTimeField(default=datetime.utcnow())
    Party = StringField(default='UNK')
    RActive = StringField(default='UNK')
    PABS = StringField(default='UNK')
    PBF = FloatField(default=0)

    VH15G = IntField(default=0)
    VH15P = IntField(default=0)
    VH15MG = IntField(default=0)
    VH15MP = IntField(default=0)
    VH15SG = IntField(default=0)
    VH15SP = IntField(default=0)
    VH14G = IntField(default=0)
    VH14P = IntField(default=0)
    VH14MG = IntField(default=0)
    VH14MP = IntField(default=0)
    VH14SG = IntField(default=0)
    VH14SP = IntField(default=0)
    VH13G = IntField(default=0)
    VH13P = IntField(default=0)
    VH13MG = IntField(default=0)
    VH13MP = IntField(default=0)
    VH13SG = IntField(default=0)
    VH13SP = IntField(default=0)
    VH12G = IntField(default=0)
    VH12P = IntField(default=0)
    VH12PP = IntField(default=0)
    VH12MG = IntField(default=0)
    VH12MP = IntField(default=0)
    VH12SG = IntField(default=0)
    VH12SP = IntField(default=0)
    VH11G = IntField(default=0)
    VH11P = IntField(default=0)
    VH11MG = IntField(default=0)
    VH11MP = IntField(default=0)
    VH11SG = IntField(default=0)
    VH11SP = IntField(default=0)
    VH10G = IntField(default=0)
    VH10P = IntField(default=0)
    VH10MG = IntField(default=0)
    VH10MP = IntField(default=0)
    VH10SG = IntField(default=0)
    VH10SP = IntField(default=0)
    VH09G = IntField(default=0)
    VH09P = IntField(default=0)
    VH09MG = IntField(default=0)
    VH09MP = IntField(default=0)
    VH09SG = IntField(default=0)
    VH09SP = IntField(default=0)
    VH08G = IntField(default=0)
    VH08P = IntField(default=0)
    VH08MG = IntField(default=0)
    VH08MP = IntField(default=0)
    VH08PP = IntField(default=0)
    VH08SG = IntField(default=0)
    VH08SP = IntField(default=0)
    VH07G = IntField(default=0)
    VH07P = IntField(default=0)
    VH07MG = IntField(default=0)
    VH07MP = IntField(default=0)
    VH07SG = IntField(default=0)
    VH07SP = IntField(default=0)
    VH06G = IntField(default=0)
    VH06P = IntField(default=0)
    VH06MG = IntField(default=0)
    VH06MP = IntField(default=0)
    VH06SG = IntField(default=0)
    VH06SP = IntField(default=0)
    VH05G = IntField(default=0)
    VH05P = IntField(default=0)
    VH05MG = IntField(default=0)
    VH05MP = IntField(default=0)
    VH05SG = IntField(default=0)
    VH05SP = IntField(default=0)
    VH04G = IntField(default=0)
    VH04P = IntField(default=0)
    VH04MG = IntField(default=0)
    VH04MP = IntField(default=0)
    VH04PP = IntField(default=0)
    VH04SG = IntField(default=0)
    VH04SP = IntField(default=0)
    VH03G = IntField(default=0)
    VH03P = IntField(default=0)
    VH03MG = IntField(default=0)
    VH03MP = IntField(default=0)
    VH03SG = IntField(default=0)
    VH03SP = IntField(default=0)
    VH02G = IntField(default=0)
    VH02P = IntField(default=0)
    VH02MG = IntField(default=0)
    VH02MP = IntField(default=0)
    VH02SG = IntField(default=0)
    VH02SP = IntField(default=0)
    VH01G = IntField(default=0)
    VH01P = IntField(default=0)
    VH01MG = IntField(default=0)
    VH01MP = IntField(default=0)
    VH01SG = IntField(default=0)
    VH01SP = IntField(default=0)
    VH00G = IntField(default=0)
    VH00P = IntField(default=0)
    VH00PP = IntField(default=0)
    VH00SG = IntField(default=0)
    VH00SP = IntField(default=0)

    AffinityModel = DecimalField(precision=9, default=0)
    PropensityModel = DecimalField(precision=9, default=0)
    SoConLife = DecimalField(precision=9, default=0)
    SoConMarriage = DecimalField(precision=9, default=0)
    FisConTax = DecimalField(precision=9, default=0)
    FisconSpending = DecimalField(precision=9, default=0)
    HealthCareModel = DecimalField(precision=9, default=0)

    meta = {'allow_inheritance': True}


class R7_L2_Voter(VoteHistory,CommercialHomePurchasing,CommercialInterests,CommercialFEC,Commercial,District,Party,\
            Commercial2,Demographics,Email,PhoneNumber,Residence,Name):

    mseq = FloatField(default=0)
    seq = FloatField(default=0)
    SomeDate = DateTimeField(default=datetime.utcnow())
    Round = FloatField(default=0)
    Caller_ID = FloatField()
    Time_Stamp = DateTimeField(default=datetime.utcnow())
    Poling_Result = StringField(default='UNK')
    Sheet = StringField(default='UNK')
    State = StringField(default='UNK')
    LALVoterID = StringField(default='UNK')
    LALID = StringField(default='UNK')
    AbsenteeTypes_Description = StringField(default='UNK')
    Source = StringField(default='None')

    meta = {'allow_inheritance': True}

class AggregatedVoter(Document):

    Aggregate_ID = StringField(default=str(uuid.uuid1()))
    Aggregate_Name = StringField(default='UNK')
    # SourceIDs = ListField(default=[0])
    # R7_L2_Dedupe = ListField(default=[0])
    # CS_DRTV_Dedupe = ListField(default=[0])
    # Aggregate_Dedupe = ListField(default=[0])
"""
