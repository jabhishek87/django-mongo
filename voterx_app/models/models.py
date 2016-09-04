from datetime import datetime

from django.db import models
from django.views.generic import ListView
from djangotoolbox.fields import ListField, EmbeddedModelField


class Name(models.Model):
    voters_firstname = models.CharField()
    voters_middlename = models.CharField()
    voters_lastname = models.CharField()
    voters_namesuffix = models.CharField()
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    created_on = models.DateTimeField(auto_now_add=True)
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "voters_firstname": self.voters_firstname,
            "voters_middlename": self.voters_middlename,
            "voters_lastname": self.voters_lastname,
            "voters_namesuffix": self.voters_namesuffix,
            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }


class Residence(models.Model):

    residence_addresses_addressline = models.CharField(default='None')
    residence_addresses_extraaddressline = models.CharField(default='None')
    residence_addresses_city = models.CharField(default='None')
    residence_addresses_state = models.CharField(default='None')
    residence_addresses_zip = models.CharField(default='None')
    residence_addresses_zipplus4 = models.CharField(default='None')
    residence_addresses_housenumber = models.CharField(default='None')
    residence_addresses_prefixdirection = models.CharField(default='None')
    residence_addresses_streetname = models.CharField(default='None')
    residence_addresses_designator = models.CharField(default='None')
    residence_addresses_suffixdirection = models.CharField(default='None')
    residence_addresses_apartmentnum = models.CharField(default='None')
    residence_addresses_apartmenttype = models.CharField(default='None')
    residence_addresses_censustract = models.CharField(default='None')
    residence_addresses_censusblockgroup = models.CharField(default='None')
    residence_addresses_censusblock = models.CharField(default='None')
    residence_families_familyid = models.CharField(default='None')
    residence_families_hhcount = models.CharField(default='None')
    residence_hhgender_description = models.CharField(default='None')
    residence_hhparties_description = models.CharField(default='None')

    mailing_addresses_addressline = models.CharField(default='None')
    mailing_addresses_extraaddressline = models.CharField(default='None')
    mailing_addresses_city = models.CharField(default='None')
    mailing_addresses_state = models.CharField(default='None')
    mailing_addresses_zip = models.CharField(default='None')
    mailing_addresses_zipplus4 = models.CharField(default='None')
    mailing_addresses_housenumber = models.CharField(default='None')
    mailing_addresses_prefixdirection = models.CharField(default='None')
    mailing_addresses_streetname = models.CharField(default='None')
    mailing_addresses_designator = models.CharField(default='None')
    mailing_addresses_suffixdirection = models.CharField(default='None')
    mailing_addresses_apartmentnum = models.CharField(default='None')
    mailing_addresses_apartmenttype = models.CharField(default='None')
    mailing_families_familyid = models.CharField(default='None')
    mailing_families_hhcount = models.CharField(default='None')
    mailing_hhgender_description = models.CharField(default='None')
    mailing_hhparties_description = models.CharField(default='None')
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "residence_addresses_addressline": self.residence_addresses_addressline ,
            "residence_addresses_extraaddressline": self.residence_addresses_extraaddressline ,
            "residence_addresses_city": self.residence_addresses_city ,
            "residence_addresses_state": self.residence_addresses_state ,
            "residence_addresses_zip": self.residence_addresses_zip ,
            "residence_addresses_zipplus4": self.residence_addresses_zipplus4 ,
            "residence_addresses_housenumber": self.residence_addresses_housenumber ,
            "residence_addresses_prefixdirection": self.residence_addresses_prefixdirection ,
            "residence_addresses_streetname": self.residence_addresses_streetname ,
            "residence_addresses_designator": self.residence_addresses_designator ,
            "residence_addresses_suffixdirection": self.residence_addresses_suffixdirection ,
            "residence_addresses_apartmentnum": self.residence_addresses_apartmentnum ,
            "residence_addresses_apartmenttype": self.residence_addresses_apartmenttype ,
            "residence_addresses_censustract": self.residence_addresses_censustract ,
            "residence_addresses_censusblockgroup": self.residence_addresses_censusblockgroup ,
            "residence_addresses_censusblock": self.residence_addresses_censusblock ,
            "residence_families_familyid": self.residence_families_familyid ,
            "residence_families_hhcount": self.residence_families_hhcount ,
            "residence_hhgender_description": self.residence_hhgender_description ,
            "residence_hhparties_description": self.residence_hhparties_description ,

            "mailing_addresses_addressline": self.mailing_addresses_addressline ,
            "mailing_addresses_extraaddressline": self.mailing_addresses_extraaddressline ,
            "mailing_addresses_city": self.mailing_addresses_city ,
            "mailing_addresses_state": self.mailing_addresses_city ,
            "mailing_addresses_zip": self.mailing_addresses_zip ,
            "mailing_addresses_zipplus4": self.mailing_addresses_zipplus4 ,
            "mailing_addresses_housenumber": self.mailing_addresses_housenumber ,
            "mailing_addresses_prefixdirection": self.mailing_addresses_prefixdirection ,
            "mailing_addresses_streetname": self.mailing_addresses_streetname ,
            "mailing_addresses_designator": self.mailing_addresses_designator ,
            "mailing_addresses_suffixdirection": self.mailing_addresses_suffixdirection ,
            "mailing_addresses_apartmentnum": self.mailing_addresses_apartmentnum ,
            "mailing_addresses_apartmenttype": self.mailing_addresses_apartmenttype ,
            "mailing_families_familyid": self.mailing_families_familyid ,
            "mailing_families_hhcount": self.mailing_families_hhcount ,
            "mailing_hhgender_description": self.mailing_hhgender_description ,
            "mailing_hhparties_description": self.mailing_hhparties_description ,
            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }


class Demographics(models.Model):
    #military_status = {}
    #marital_status = {}
    voters_gender = models.CharField(default='UNK')
    voters_age = models.FloatField(default=0)
    voters_birthdate = models.CharField(default='UNK')
    voters_placeofbirth = models.CharField(default='UNK')
    languages_description = models.CharField(default='English')
    militarystatus_description = models.CharField(default='UNK')
    maritalstatus_description = models.CharField(default='UNK')
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "voters_gender": self.voters_gender ,
            "voters_age": self.voters_age ,
            "voters_birthdate": self.voters_birthdate ,
            "voters_placeofbirth": self.voters_placeofbirth ,
            "languages_description": self.languages_description ,
            "militarystatus_description": self.militarystatus_description ,
            "maritalstatus_description": self.maritalstatus_description ,

            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }


class PhoneNumber(models.Model):

    phone = models.FloatField(default=0000000000)
    phnmatch = models.FloatField(default=0)
    telconfidencecode = models.FloatField(default=0)
    telcellflag = models.IntegerField(default=0)
    voters_statevoterid = models.CharField(default='None')
    voters_countyvoterid = models.CharField(default='None')
    votertelephones_fullphone = models.IntegerField(default=0)
    votertelephones_phone10 = models.IntegerField(default=0)
    votertelephones_telconfidencecode = models.IntegerField(default=0)
    votertelephones_telcellflag = models.BooleanField(default=False)
    view_ops_cellphone_phone10 = models.IntegerField(default=0)
    view_ops_cellphone_fullphone = models.IntegerField(default=0)
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "phnmatch": self.phnmatch,
            "telconfidencecode": self.telconfidencecode,
            "telcellflag": self.telcellflag,
            "voters_statevoterid": self.voters_statevoterid,
            "voters_countyvoterid": self.voters_countyvoterid,
            "votertelephones_fullphone": self.votertelephones_fullphone,
            "votertelephones_phone10": self.votertelephones_phone10,
            "votertelephones_telconfidencecode": self.votertelephones_telconfidencecode,
            "votertelephones_telcellflag": self.votertelephones_telcellflag,
            "view_ops_cellphone_fullphone": self.view_ops_cellphone_fullphone,
        }


class Email(models.Model):

    l2_emailaddress = models.EmailField(default='UNK@UNK.UNK') #default='UNK@UNK'
    emailaddresses_emailaddress = models.EmailField(default='UNK@UNK.UNK')
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "l2_emailaddress": self.l2_emailaddress,
            "emailaddresses_emailaddress": self.emailaddresses_emailaddress,
        }


class Commercial(models.Model):

    commercialdata_presenceofchildrencode = models.CharField(default='unk')
    commercialdata_ispsa = models.FloatField(default=0)
    commercialdata_dwellingtype = models.CharField(default='unk')
    commercialdata_dwellingunitsize = models.CharField(default='unk')
    commercialdata_estimatedincomeamount = models.DecimalField(decimal_places=2,  default=0)
    commercialdata_estimatedincome = models.DecimalField(decimal_places=2,  default=0)
    commercialdata_education = models.CharField(default='unk')
    commercialdata_occupation = models.CharField(default='unk')
    commercialdata_homepurchaseprice = models.DecimalField(decimal_places=2,  default=0)
    commercialdata_homepurchasedate = models.DateTimeField(default=datetime.utcnow())
    commercialdata_landvalue = models.DecimalField(decimal_places=2,  default=0)
    commercialdata_propertytype = models.CharField(default='unk')
    commercialdata_esthomevalue = models.DecimalField(decimal_places=2,  default=0)
    commercialdata_hhcomposition = models.CharField(default='unk')
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "commercialdata_presenceofchildrencode": self.commercialdata_presenceofchildrencode ,
            "commercialdata_ispsa": self.commercialdata_ispsa ,
            "commercialdata_dwellingtype": self.commercialdata_dwellingunitsize ,
            "commercialdata_estimatedincomeamount": self.commercialdata_estimatedincomeamount ,
            "commercialdata_estimatedincome": self.commercialdata_estimatedincome ,
            "commercialdata_education": self.commercialdata_education ,
            "commercialdata_occupation": self.commercialdata_occupation ,
            "commercialdata_homepurchaseprice": self.commercialdata_homepurchaseprice ,
            "commercialdata_homepurchasedate": self.commercialdata_homepurchasedate ,
            "commercialdata_landvalue": self.commercialdata_landvalue ,
            "commercialdata_propertytype": self.commercialdata_propertytype ,
            "commercialdata_esthomevalue": self.commercialdata_esthomevalue ,
            "commercialdata_hhcomposition": self.commercialdata_hhcomposition ,

            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }


class Party(models.Model):

    parties_description = models.CharField(default='unk')
    countyethnic_description = models.CharField(default='unk')
    ethnic_description = models.CharField(default='unk')
    religions_description = models.CharField(default='unk')
    voters_calculatedregdate = models.CharField(default='unk')
    voters_officialregdate = models.CharField(default='unk')
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "parties_description": self.parties_description ,
            "countyethnic_description": self.countyethnic_description ,
            "ethnic_description": self.ethnic_description ,
            "religions_description": self.religions_description ,
            "voters_calculatedregdate": self.voters_calculatedregdate ,
            "voters_officialregdate": self.voters_officialregdate ,
            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }


class District(models.Model):
    us_congressional_district = models.FloatField(default=0)
    state_house_district = models.FloatField(default=0)
    state_legislative_district = models.FloatField(default=0)
    state_senate_district = models.FloatField(default=0)
    county = models.CharField(default='unk')
    city = models.CharField(default='unk')
    city_council_commissioner_district = models.CharField(default='unk')
    city_mayoral_district = models.CharField(default='unk')
    city_ward = models.CharField(default='unk')
    village = models.CharField(default='unk')
    village_ward = models.CharField(default='unk')
    town_district = models.CharField(default='unk')
    town_ward = models.CharField(default='unk')
    township = models.CharField(default='unk')
    township_ward = models.CharField(default='unk')
    borough = models.CharField(default='unk')
    borough_ward = models.CharField(default='unk')
    hamlet_community_area = models.CharField(default='unk')
    board_of_education_district = models.CharField(default='unk')
    board_of_education_subdistrict = models.CharField(default='unk')
    city_school_district = models.CharField(default='unk')
    community_college = models.CharField(default='unk')
    community_college_commissioner_district = models.CharField(default='unk')
    community_college_subdistrict = models.CharField(default='unk')
    congressional_township = models.CharField(default='unk')
    county_board_of_education_district = models.CharField(default='unk')
    county_commissioner_district = models.CharField(default='unk')
    county_fire_district = models.CharField(default='unk')
    county_hospital_district = models.CharField(default='unk')
    county_legislative_district = models.CharField(default='unk')
    county_library_district = models.CharField(default='unk')
    county_sewer_district = models.CharField(default='unk')
    county_superintendent_of_schools_district = models.CharField(default='unk')
    county_supervisorial_district = models.CharField(default='unk')
    county_unified_school_district = models.CharField(default='unk')
    county_water_district = models.CharField(default='unk')
    county_water_subdistrict = models.CharField(default='unk')
    designated_market_area_dma = models.CharField(default='unk')
    district_attorney = models.CharField(default='unk')
    educational_service_district = models.CharField(default='unk')
    educational_service_subdistrict = models.CharField(default='unk')
    elementary_school_district = models.CharField(default='unk')
    elementary_school_subdistrict = models.CharField(default='unk')
    emergency_communication_911_district = models.CharField(default='unk')
    emergency_communication_911_subdistrict = models.CharField(default='unk')
    fire_district = models.CharField(default='unk')
    fire_protection_district = models.CharField(default='unk')
    fire_protection_subdistrict = models.CharField(default='unk')
    fire_subdistrict = models.CharField(default='unk')
    health_district = models.CharField(default='unk')
    high_school_district = models.CharField(default='unk')
    high_school_subdistrict = models.CharField(default='unk')
    hospital_district = models.CharField(default='unk')
    hospital_subdistrict = models.CharField(default='unk')
    irrigation_district = models.CharField(default='unk')
    irrigation_subdistrict = models.CharField(default='unk')
    judicial_appellate_district = models.CharField(default='unk')
    judicial_chancery_court = models.CharField(default='unk')
    judicial_circuit_court_district = models.CharField(default='unk')
    judicial_county_court_district = models.CharField(default='unk')
    judicial_district = models.CharField(default='unk')
    judicial_district_court_district = models.CharField(default='unk')
    judicial_family_court_district = models.CharField(default='unk')
    judicial_jury_district = models.CharField(default='unk')
    judicial_magistrate_division = models.CharField(default='unk')
    judicial_sub_circuit_district = models.CharField(default='unk')
    judicial_superior_court_district = models.CharField(default='unk')
    justice_of_the_peace = models.CharField(default='unk')
    levee_district = models.CharField(default='unk')
    library_district = models.CharField(default='unk')
    library_subdistrict = models.CharField(default='unk')
    lighting_district = models.CharField(default='unk')
    metro_service_district = models.CharField(default='unk')
    metro_service_subdistrict = models.CharField(default='unk')
    metro_transit_district = models.CharField(default='unk')
    metropolitan_water_district = models.CharField(default='unk')
    middle_school_district = models.CharField(default='unk')
    municipal_advisory_council_district = models.CharField(default='unk')
    municipal_court_district = models.CharField(default='unk')
    municipal_utility_district = models.CharField(default='unk')
    municipal_utility_subdistrict = models.CharField(default='unk')
    municipal_water_district = models.CharField(default='unk')
    municipal_water_subdistrict = models.CharField(default='unk')
    park_district = models.CharField(default='unk')
    park_subdistrict = models.CharField(default='unk')
    police_district = models.CharField(default='unk')
    port_district = models.CharField(default='unk')
    port_subdistrict = models.CharField(default='unk')
    precinct = models.CharField(default='unk')
    public_utility_district = models.CharField(default='unk')
    public_utility_subdistrict = models.CharField(default='unk')
    rapid_transit_district = models.CharField(default='unk')
    reclamation_district = models.CharField(default='unk')
    recreation_district = models.CharField(default='unk')
    recreational_subdistrict = models.CharField(default='unk')
    sanitary_district = models.CharField(default='unk')
    sanitary_subdistrict = models.CharField(default='unk')
    school_board_district = models.CharField(default='unk')
    school_district = models.CharField(default='unk')
    school_district_vocational = models.CharField(default='unk')
    school_subdistrict = models.CharField(default='unk')
    sewer_district = models.CharField(default='unk')
    sewer_maintenance_district = models.CharField(default='unk')
    sewer_subdistrict = models.CharField(default='unk')
    soil_and_water_district = models.CharField(default='unk')
    special_tax_district = models.CharField(default='unk')
    state_board_of_equalization = models.CharField(default='unk')
    superintendent_of_schools_district = models.CharField(default='unk')
    transit_district = models.CharField(default='unk')
    transit_subdistrict = models.CharField(default='unk')
    unified_school_district = models.CharField(default='unk')
    unified_school_subdistrict = models.CharField(default='unk')
    wastewater_district = models.CharField(default='unk')
    water_agency = models.CharField(default='unk')
    water_agency_subdistrict = models.CharField(default='unk')
    water_conservation_district = models.CharField(default='unk')
    water_conservation_subdistrict = models.CharField(default='unk')
    water_district = models.CharField(default='unk')
    water_subdistrict = models.CharField(default='unk')
    weed_district = models.CharField(default='unk')
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "us_congressional_district": self.us_congressional_district,
            "state_house_district": self.state_house_district,
            "state_legislative_district": self.state_legislative_district,
            "state_senate_district": self.state_senate_district,
            "county": self.county,
            "city": self.city,
            "city_council_commissioner_district": self.city_council_commissioner_district,
            "city_mayoral_district": self.city_mayoral_district,
            "city_ward": self.city_ward,
            "village": self.village,
            "village_ward": self.village_ward,
            "town_district": self.town_district,
            "town_ward": self.town_ward,
            "township": self.township,
            "township_ward": self.township_ward,
            "borough": self.borough,
            "borough_ward": self.borough_ward,
            "hamlet_community_area": self.hamlet_community_area,
            "board_of_education_district": self.board_of_education_district,
            "board_of_education_subdistrict": self.board_of_education_subdistrict,
            "city_school_district": self.city_school_district,
            "community_college": self.community_college,
            "community_college_commissioner_district": self.community_college_commissioner_district,
            "community_college_subdistrict": self.community_college_subdistrict,
            "congressional_township": self.congressional_township,
            "county_board_of_education_district": self.county_board_of_education_district,
            "county_commissioner_district": self.county_commissioner_district,
            "county_fire_district": self.county_fire_district,
            "county_hospital_district": self.county_hospital_district,
            "county_legislative_district": self.county_legislative_district,
            "county_library_district": self.county_library_district,
            "county_sewer_district": self.county_sewer_district,
            "county_superintendent_of_schools_district": self.county_superintendent_of_schools_district,
            "county_supervisorial_district": self.county_supervisorial_district,
            "county_unified_school_district": self.county_unified_school_district,
            "county_water_district": self.county_water_district,
            "county_water_subdistrict": self.county_water_subdistrict,
            "designated_market_area_dma": self.designated_market_area_dma,
            "district_attorney": self.district_attorney,
            "educational_service_district": self.educational_service_district,
            "educational_service_subdistrict": self.educational_service_subdistrict,
            "elementary_school_district": self.elementary_school_district,
            "elementary_school_subdistrict": self.elementary_school_subdistrict,
            "emergency_communication_911_district": self.emergency_communication_911_district,
            "emergency_communication_911_subdistrict": self.emergency_communication_911_subdistrict,
            "fire_district": self.fire_district,
            "fire_protection_district": self.fire_protection_district,
            "fire_protection_subdistrict": self.fire_protection_subdistrict,
            "fire_subdistrict": self.fire_subdistrict,
            "health_district": self.health_district,
            "high_school_district": self.high_school_district,
            "high_school_subdistrict": self.high_school_subdistrict,
            "hospital_district": self.hospital_district,
            "hospital_subdistrict": self.hospital_subdistrict,
            "irrigation_district": self.irrigation_district,
            "irrigation_subdistrict": self.irrigation_subdistrict,
            "judicial_appellate_district": self.judicial_appellate_district,
            "judicial_chancery_court": self.judicial_chancery_court,
            "judicial_circuit_court_district": self.judicial_circuit_court_district,
            "judicial_county_court_district": self.judicial_county_court_district,
            "judicial_district": self.judicial_district,
            "judicial_district_court_district": self.judicial_district_court_district,
            "judicial_family_court_district": self.judicial_family_court_district,
            "judicial_jury_district": self.judicial_jury_district,
            "judicial_magistrate_division": self.judicial_magistrate_division,
            "judicial_sub_circuit_district": self.judicial_sub_circuit_district,
            "judicial_superior_court_district": self.judicial_superior_court_district,
            "justice_of_the_peace": self.justice_of_the_peace,
            "levee_district": self.levee_district,
            "library_district": self.library_district,
            "library_subdistrict": self.library_subdistrict,
            "lighting_district": self.lighting_district,
            "metro_service_district": self.metro_service_district,
            "metro_service_subdistrict": self.metro_service_subdistrict,
            "metro_transit_district": self.metro_transit_district,
            "metropolitan_water_district": self.metropolitan_water_district,
            "middle_school_district": self.middle_school_district,
            "municipal_advisory_council_district": self.municipal_advisory_council_district,
            "municipal_court_district": self.municipal_court_district,
            "municipal_utility_district": self.municipal_utility_district,
            "municipal_utility_subdistrict": self.municipal_utility_subdistrict,
            "municipal_water_district": self.municipal_water_district,
            "municipal_water_subdistrict": self.municipal_water_subdistrict,
            "park_district": self.park_district,
            "park_subdistrict": self.park_subdistrict,
            "police_district": self.police_district,
            "port_district": self.port_district,
            "port_subdistrict": self.port_subdistrict,
            "precinct": self.precinct,
            "public_utility_district": self.public_utility_district,
            "public_utility_subdistrict": self.public_utility_subdistrict,
            "rapid_transit_district": self.rapid_transit_district,
            "reclamation_district": self.reclamation_district,
            "recreation_district": self.recreation_district,
            "recreational_subdistrict": self.recreational_subdistrict,
            "sanitary_district": self.sanitary_district,
            "sanitary_subdistrict": self.rapid_transit_district,
            "school_board_district": self.school_board_district,
            "school_district": self.school_district,
            "school_subdistrict": self.school_subdistrict,
            "sewer_district": self.sewer_district,
            "sewer_maintenance_district": self.sewer_maintenance_district,
            "sewer_subdistrict": self.sewer_subdistrict,
            "soil_and_water_district": self.soil_and_water_district,
            "special_tax_district": self.special_tax_district,
            "state_board_of_equalization": self.state_board_of_equalization,
            "superintendent_of_schools_district": self.superintendent_of_schools_district,
            "transit_district": self.transit_district,
            "transit_subdistrict": self.transit_subdistrict,
            "unified_school_district": self.unified_school_district,
            "unified_school_subdistrict": self.unified_school_subdistrict,
            "wastewater_district": self.wastewater_district,
            "water_agency": self.water_agency,
            "water_agency_subdistrict": self.water_agency_subdistrict,
            "water_conservation_district": self.water_conservation_district,
            "water_conservation_subdistrict": self.water_conservation_subdistrict,
            "water_district": self.water_district,
            "water_subdistrict": self.water_subdistrict,
            "weed_district": self.weed_district,
            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }

class Commercial2(models.Model):
    commercialdatall_gun_owner = models.CharField(default='unk')
    commercialdatall_veteran = models.CharField(default='unk')
    commercialdatall_affordable_care_act = models.CharField(default='unk')
    commercialdatall_church_attendee = models.CharField(default='unk')
    commercialdatall_election_of_conservative_judges = models.CharField(default='unk')
    commercialdatall_gay_marriage = models.CharField(default='unk')
    commercialdatall_gun_control = models.CharField(default='unk')
    commercialdatall_immigration_loosen_restrictions = models.CharField(default='unk')
    commercialdatall_lawsuit_damages_should_be_limited = models.CharField(default='unk')
    commercialdatall_privatize_social_security = models.CharField(default='unk')
    commercialdatall_pro_choice = models.CharField(default='unk')
    commercialdatall_pro_life = models.CharField(default='unk')
    commercialdatall_school_choice = models.CharField(default='unk')
    commercialdatall_social_views = models.CharField(default='unk')
    commercialdatall_taxes_raise = models.CharField(default='unk')
    commercialdatall_donates_to_animal_welfare = models.CharField(default='unk')
    commercialdatall_donates_to_arts_and_culture = models.CharField(default='unk')
    commercialdatall_donates_to_childrens_causes = models.CharField(default='unk')
    commercialdatall_donates_to_healthcare = models.CharField(default='unk')
    commercialdatall_donates_to_international_aid_causes = models.CharField(default='unk')
    commercialdatall_donates_to_veterans_causes = models.BooleanField(default=False)
    commercialdatall_home_owner_or_renter = models.CharField(default='unk')
    commercialdatall_net_worth = models.CharField(default='unk')
    commercialdatall_business_owner = models.CharField(default='unk')
    commercialdatall_investor = models.BooleanField(default=False)
    commercialdatall_donates_to_wildlife_preservation = models.CharField(default='unk')
    commercialdatall_donates_to_conservative_causes = models.CharField(default='unk')
    commercialdatall_donates_to_liberal_causes = models.CharField(default='unk')
    commercialdatall_donates_to_local_community = models.BooleanField(default=False)
    commercialdatall_petowner_horse = models.BooleanField(default=False)
    commercialdatall_petowner_cat = models.BooleanField(default=False)
    commercialdatall_petowner_dog = models.BooleanField(default=False)
    commercialdatall_petowner_other = models.BooleanField(default=False)
    commercialdatall_home_office = models.CharField(default='unk')
    commercialdatall_hispanic_country_origin = models.CharField(default='unk')
    commercialdatall_household_primary_language = models.CharField(default='unk')
    commercialdata_occupationindustry = models.CharField(default='unk')
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "commercialdatall_gun_owner": self.commercialdatall_gun_owner,
            "commercialdatall_veteran": self.commercialdatall_veteran,
            "commercialdatall_affordable_care_act": self.commercialdatall_affordable_care_act,
            "commercialdatall_church_attendee": self.commercialdatall_church_attendee,
            "commercialdatall_election_of_conservative_judges": self.commercialdatall_election_of_conservative_judges,
            "commercialdatall_gay_marriage": self.commercialdatall_gay_marriage,
            "commercialdatall_gun_control": self.commercialdatall_gun_control,
            "commercialdatall_immigration_loosen_restrictions": self.commercialdatall_immigration_loosen_restrictions,
            "commercialdatall_lawsuit_damages_should_be_limited": self.commercialdatall_lawsuit_damages_should_be_limited,
            "commercialdatall_privatize_social_security": self.commercialdatall_privatize_social_security,
            "commercialdatall_pro_choice": self.commercialdatall_pro_choice,
            "commercialdatall_pro_life": self.commercialdatall_pro_life,
            "commercialdatall_school_choice": self.commercialdatall_school_choice,
            "commercialdatall_social_views": self.commercialdatall_social_views,
            "commercialdatall_taxes_raise": self.commercialdatall_taxes_raise,
            "commercialdatall_donates_to_animal_welfare": self.commercialdatall_donates_to_animal_welfare,
            "commercialdatall_donates_to_arts_and_culture": self.commercialdatall_donates_to_arts_and_culture,
            "commercialdatall_donates_to_childrens_causes": self.commercialdatall_donates_to_childrens_causes,
            "commercialdatall_donates_to_healthcare": self.commercialdatall_donates_to_healthcare,
            "commercialdatall_donates_to_international_aid_causes": self.commercialdatall_donates_to_international_aid_causes,
            "commercialdatall_donates_to_veterans_causes": self.commercialdatall_donates_to_veterans_causes,
            "commercialdatall_home_owner_or_renter": self.commercialdatall_home_owner_or_renter,
            "commercialdatall_net_worth": self.commercialdatall_net_worth,
            "commercialdatall_business_owner": self.commercialdatall_business_owner,
            "commercialdatall_investor": self.commercialdatall_investor,
            "commercialdatall_donates_to_wildlife_preservation": self.commercialdatall_donates_to_wildlife_preservation,
            "commercialdatall_donates_to_conservative_causes": self.commercialdatall_donates_to_conservative_causes,
            "commercialdatall_donates_to_liberal_causes": self.commercialdatall_donates_to_liberal_causes,
            "commercialdatall_donates_to_local_community": self.commercialdatall_donates_to_local_community,
            "commercialdatall_petowner_horse": self.commercialdatall_petowner_horse,
            "commercialdatall_petowner_cat": self.commercialdatall_petowner_cat,
            "commercialdatall_petowner_dog": self.commercialdatall_petowner_dog,
            "commercialdatall_petowner_other": self.commercialdatall_petowner_other,
            "commercialdatall_home_office": self.commercialdatall_home_office,
            "commercialdatall_hispanic_country_origin": self.commercialdatall_hispanic_country_origin,
            "commercialdatall_household_primary_language": self.commercialdatall_household_primary_language,
            "commercialdata_occupationindustry": self.commercialdata_occupationindustry,
            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }


class Commercialfec(models.Model):
    fecdonors_numberofdonations = models.FloatField(default=0)
    fecdonors_totaldonationsamount = models.DecimalField(decimal_places=2,  default=0)
    fecdonors_totaldonationsamt_range = models.DecimalField(decimal_places=2,  default=0)
    fecdonors_lastdonationdate = models.DateTimeField(default=datetime.utcnow())
    fecdonors_avgdonation = models.DecimalField(decimal_places=2,  default=0)
    fecdonors_avgdonation_range = models.DecimalField(decimal_places=2,  default=0)
    fecdonors_primaryrecipientofcontributions = models.CharField(default='unk')
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "fecdonors_numberofdonations": self.fecdonors_numberofdonations,
            "fecdonors_totaldonationsamount": self.fecdonors_totaldonationsamount,
            "fecdonors_totaldonationsamt_range": self.fecdonors_totaldonationsamt_range,
            "fecdonors_lastdonationdate": self.fecdonors_lastdonationdate,
            "fecdonors_avgdonation": self.fecdonors_avgdonation,
            "fecdonors_avgdonation_range": self.fecdonors_avgdonation_range,
            "fecdonors_primaryrecipientofcontributions": self.fecdonors_primaryrecipientofcontributions,
            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }


class Commercialinterests(models.Model):
    commercialdatall_reading_general_in_household = models.BooleanField(default=False)
    commercialdatall_reading_religious_in_household = models.BooleanField(default=False)
    commercialdatall_reading_science_fiction_in_household = models.BooleanField(default=False)
    commercialdatall_reading_magazines_in_household = models.BooleanField(default=False)
    commercialdatall_reading_audio_books_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_history_military_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_current_affairs_politics_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_religious_inspirational_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_science_space_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_education_online_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_electronic_gaming_in_household = models.BooleanField(default=False)
    commercialdatall_buyer_antiques_in_household = models.BooleanField(default=False)
    commercialdatall_buyer_art_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_theater_performing_arts_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_the_arts_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_musical_instruments_in_household = models.BooleanField(default=False)
    commercialdatall_collector_general_in_household = models.BooleanField(default=False)
    commercialdatall_collector_stamps_in_household = models.BooleanField(default=False)
    commercialdatall_collector_coins_in_household = models.BooleanField(default=False)
    commercialdatall_collector_arts_in_household = models.BooleanField(default=False)
    commercialdatall_collector_antiques_in_household = models.BooleanField(default=False)
    commercialdatall_collector_avid_in_household = models.BooleanField(default=False)
    commercialdatall_collector_sports_in_household = models.BooleanField(default=False)
    commercialdatall_collector_military_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_home_repair_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_auto_work_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_sewing_knitting_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_woodworking_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_photography_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_aviation_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_house_plants_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_crafts_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_gardening_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_photography_video_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_smoking_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_home_furnishings_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_home_improvement_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_food_wines_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_cooking_general_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_cooking_gourmet_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_foods_natural_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_boardgames_puzzles_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_gaming_casino_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_sweepstakes_contests_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_travel_domestic_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_travel_international_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_travel_cruise_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_exercise_health_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_exercise_running_jogging_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_exercise_walking_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_exercise_aerobic_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_spectatorsports_auto_racing_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_spectatorsports_on_tv_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_spectatorsports_football_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_spectatorsports_baseball_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_spectatorsports_basketball_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_spectatorsports_hockey_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_spectatorsports_soccer_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_tennis_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_golf_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_snow_skiing_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_motorcycling_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_nascar_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_boating_sailing_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_scuba_diving_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_sports_leisure_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_hunting_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_fishing_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_camping_hiking_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_shooting_in_household = models.BooleanField(default=False)
    commercialdatall_interest_in_automotive_parts_accessories_in_household = models.BooleanField(default=False)
    commercialdatall_gun_owner_concealed_permit = models.BooleanField(default=False)
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "commercialdatall_reading_general_in_household": self.commercialdatall_reading_general_in_household,
            "commercialdatall_reading_religious_in_household": self.commercialdatall_reading_religious_in_household,
            "commercialdatall_reading_science_fiction_in_household": self.commercialdatall_reading_science_fiction_in_household,
            "commercialdatall_reading_magazines_in_household": self.commercialdatall_reading_magazines_in_household,
            "commercialdatall_reading_audio_books_in_household": self.commercialdatall_reading_audio_books_in_household,
            "commercialdatall_interest_in_history_military_in_household": self.commercialdatall_interest_in_history_military_in_household,
            "commercialdatall_interest_in_current_affairs_politics_in_household": self.commercialdatall_interest_in_current_affairs_politics_in_household,
            "commercialdatall_interest_in_religious_inspirational_in_household": self.commercialdatall_interest_in_religious_inspirational_in_household,
            "commercialdatall_interest_in_science_space_in_household": self.commercialdatall_interest_in_science_space_in_household,
            "commercialdatall_interest_in_education_online_in_household": self.commercialdatall_interest_in_education_online_in_household,
            "commercialdatall_interest_in_electronic_gaming_in_household": self.commercialdatall_interest_in_electronic_gaming_in_household,
            "commercialdatall_buyer_antiques_in_household": self.commercialdatall_buyer_antiques_in_household,
            "commercialdatall_buyer_art_in_household": self.commercialdatall_buyer_art_in_household,
            "commercialdatall_interest_in_theater_performing_arts_in_household": self.commercialdatall_interest_in_theater_performing_arts_in_household,
            "commercialdatall_interest_in_the_arts_in_household": self.commercialdatall_interest_in_the_arts_in_household,
            "commercialdatall_interest_in_musical_instruments_in_household": self.commercialdatall_interest_in_musical_instruments_in_household,
            "commercialdatall_collector_general_in_household": self.commercialdatall_collector_general_in_household,
            "commercialdatall_collector_stamps_in_household": self.commercialdatall_collector_stamps_in_household,
            "commercialdatall_collector_coins_in_household": self.commercialdatall_collector_coins_in_household,
            "commercialdatall_collector_arts_in_household": self.commercialdatall_collector_arts_in_household,
            "commercialdatall_collector_antiques_in_household": self.commercialdatall_collector_antiques_in_household,
            "commercialdatall_collector_avid_in_household": self.commercialdatall_collector_avid_in_household,
            "commercialdatall_collector_sports_in_household": self.commercialdatall_collector_sports_in_household,
            "commercialdatall_collector_military_in_household": self.commercialdatall_collector_military_in_household,
            "commercialdatall_interest_in_home_repair_in_household": self.commercialdatall_interest_in_home_repair_in_household,
            "commercialdatall_interest_in_auto_work_in_household": self.commercialdatall_interest_in_auto_work_in_household,
            "commercialdatall_interest_in_sewing_knitting_in_household": self.commercialdatall_interest_in_sewing_knitting_in_household,
            "commercialdatall_interest_in_woodworking_in_household": self.commercialdatall_interest_in_woodworking_in_household,
            "commercialdatall_interest_in_photography_in_household": self.commercialdatall_interest_in_photography_in_household,
            "commercialdatall_interest_in_aviation_in_household": self.commercialdatall_interest_in_aviation_in_household,
            "commercialdatall_interest_in_house_plants_in_household": self.commercialdatall_interest_in_house_plants_in_household,
            "commercialdatall_interest_in_crafts_in_household": self.commercialdatall_interest_in_crafts_in_household,
            "commercialdatall_interest_in_gardening_in_household": self.commercialdatall_interest_in_gardening_in_household,
            "commercialdatall_interest_in_photography_video_in_household": self.commercialdatall_interest_in_photography_video_in_household,
            "commercialdatall_interest_in_smoking_in_household": self.commercialdatall_interest_in_smoking_in_household,
            "commercialdatall_interest_in_home_furnishings_in_household": self.commercialdatall_interest_in_home_furnishings_in_household,
            "commercialdatall_interest_in_home_improvement_in_household": self.commercialdatall_interest_in_home_improvement_in_household,
            "commercialdatall_interest_in_food_wines_in_household": self.commercialdatall_interest_in_food_wines_in_household,
            "commercialdatall_interest_in_cooking_general_in_household": self.commercialdatall_interest_in_cooking_general_in_household,
            "commercialdatall_interest_in_cooking_gourmet_in_household": self.commercialdatall_interest_in_cooking_gourmet_in_household,
            "commercialdatall_interest_in_foods_natural_in_household": self.commercialdatall_interest_in_foods_natural_in_household,
            "commercialdatall_interest_in_boardgames_puzzles_in_household": self.commercialdatall_interest_in_boardgames_puzzles_in_household,
            "commercialdatall_interest_in_gaming_casino_in_household": self.commercialdatall_interest_in_gaming_casino_in_household,
            "commercialdatall_interest_in_sweepstakes_contests_in_household": self.commercialdatall_interest_in_sweepstakes_contests_in_household,
            "commercialdatall_interest_in_travel_domestic_in_household": self.commercialdatall_interest_in_travel_domestic_in_household,
            "commercialdatall_interest_in_travel_international_in_household": self.commercialdatall_interest_in_travel_international_in_household,
            "commercialdatall_interest_in_travel_cruise_in_household": self.commercialdatall_interest_in_travel_cruise_in_household,
            "commercialdatall_interest_in_exercise_health_in_household": self.commercialdatall_interest_in_exercise_health_in_household,
            "commercialdatall_interest_in_exercise_running_jogging_in_household": self.commercialdatall_interest_in_exercise_running_jogging_in_household,
            "commercialdatall_interest_in_exercise_walking_in_household": self.commercialdatall_interest_in_exercise_walking_in_household,
            "commercialdatall_interest_in_exercise_aerobic_in_household": self.commercialdatall_interest_in_exercise_aerobic_in_household,
            "commercialdatall_interest_in_spectatorsports_auto_racing_in_household": self.commercialdatall_interest_in_spectatorsports_auto_racing_in_household,
            "commercialdatall_interest_in_spectatorsports_on_tv_in_household": self.commercialdatall_interest_in_spectatorsports_on_tv_in_household,
            "commercialdatall_interest_in_spectatorsports_football_in_household": self.commercialdatall_interest_in_spectatorsports_football_in_household,
            "commercialdatall_interest_in_spectatorsports_baseball_in_household": self.commercialdatall_interest_in_spectatorsports_baseball_in_household,
            "commercialdatall_interest_in_spectatorsports_basketball_in_household": self.commercialdatall_interest_in_spectatorsports_basketball_in_household,
            "commercialdatall_interest_in_spectatorsports_hockey_in_household": self.commercialdatall_interest_in_spectatorsports_hockey_in_household,
            "commercialdatall_interest_in_spectatorsports_soccer_in_household": self.commercialdatall_interest_in_spectatorsports_soccer_in_household,
            "commercialdatall_interest_in_tennis_in_household": self.commercialdatall_interest_in_tennis_in_household,
            "commercialdatall_interest_in_golf_in_household": self.commercialdatall_interest_in_golf_in_household,
            "commercialdatall_interest_in_snow_skiing_in_household": self.commercialdatall_interest_in_snow_skiing_in_household,
            "commercialdatall_interest_in_motorcycling_in_household": self.commercialdatall_interest_in_motorcycling_in_household,
            "commercialdatall_interest_in_nascar_in_household": self.commercialdatall_interest_in_nascar_in_household,
            "commercialdatall_interest_in_boating_sailing_in_household": self.commercialdatall_interest_in_boating_sailing_in_household,
            "commercialdatall_interest_in_scuba_diving_in_household": self.commercialdatall_interest_in_scuba_diving_in_household,
            "commercialdatall_interest_in_sports_leisure_in_household": self.commercialdatall_interest_in_sports_leisure_in_household,
            "commercialdatall_interest_in_hunting_in_household": self.commercialdatall_interest_in_hunting_in_household,
            "commercialdatall_interest_in_fishing_in_household": self.commercialdatall_interest_in_fishing_in_household,
            "commercialdatall_interest_in_camping_hiking_in_household": self.commercialdatall_interest_in_camping_hiking_in_household,
            "commercialdatall_interest_in_shooting_in_household": self.commercialdatall_interest_in_shooting_in_household,
            "commercialdatall_interest_in_automotive_parts_accessories_in_household": self.commercialdatall_interest_in_automotive_parts_accessories_in_household,
            "commercialdatall_gun_owner_concealed_permit": self.commercialdatall_gun_owner_concealed_permit,
            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }


class Commercialhomepurchasing(models.Model):
    commercialdata_upscalebuyerinhome = models.BooleanField(default=False)
    commercialdata_upscalemalebuyerinhome = models.BooleanField(default=False)
    commercialdata_upscalefemalebuyerinhome = models.BooleanField(default=False)
    commercialdata_bookbuyerinhome = models.BooleanField(default=False)
    commercialdata_familymagazineinhome = models.BooleanField(default=False)
    commercialdata_femaleorientedmagazineinhome = models.BooleanField(default=False)
    commercialdata_religiousmagazineinhome = models.BooleanField(default=False)
    commercialdata_gardeningmagazineinhome = models.BooleanField(default=False)
    commercialdata_culinaryinterestmagazineinhome = models.BooleanField(default=False)
    commercialdata_healthfitnessmagazineinhome = models.BooleanField(default=False)
    commercialdata_doityourselfermagazineinhome = models.BooleanField(default=False)
    commercialdata_financialmagazineinhome = models.BooleanField(default=False)
    commercialdata_religiouscontributorinhome = models.BooleanField(default=False)
    commercialdata_politicalcontributerinhome = models.BooleanField(default=False)
    commercialdata_donatesenvironmentcauseinhome = models.BooleanField(default=False)
    commercialdata_donatestocharityinhome = models.BooleanField(default=False)
    commercialdata_presenceofpremcredcrdinhome = models.BooleanField(default=False)
    commercialdata_computerownerinhome = models.BooleanField(default=False)
    commercialdata_stateincomedecile = models.DecimalField(decimal_places=2,  default=0)
    commercialdata_pcnthhwithchildren = models.FloatField(default=0)
    commercialdata_pcnthhmarriedcouplewithchild = models.FloatField(default=0)
    commercialdata_pcnthhmarriedcouplenochild = models.FloatField(default=0)
    commercialdata_pcnthhspanishspeaking = models.FloatField(default=0)
    commercialdata_medianeducationyears = models.FloatField(default=0)
    commercialdata_mosaicz4 = models.CharField(default='unk')
    commercialdata_likelyunion = models.BooleanField(default=False)
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "commercialdata_upscalebuyerinhome": self.commercialdata_upscalebuyerinhome,
            "commercialdata_upscalemalebuyerinhome": self.commercialdata_upscalemalebuyerinhome,
            "commercialdata_upscalefemalebuyerinhome": self.commercialdata_upscalefemalebuyerinhome,
            "commercialdata_bookbuyerinhome": self.commercialdata_bookbuyerinhome,
            "commercialdata_familymagazineinhome": self.commercialdata_familymagazineinhome,
            "commercialdata_femaleorientedmagazineinhome": self.commercialdata_femaleorientedmagazineinhome,
            "commercialdata_religiousmagazineinhome": self.commercialdata_religiousmagazineinhome,
            "commercialdata_gardeningmagazineinhome": self.commercialdata_gardeningmagazineinhome,
            "commercialdata_culinaryinterestmagazineinhome": self.commercialdata_culinaryinterestmagazineinhome,
            "commercialdata_healthfitnessmagazineinhome": self.commercialdata_healthfitnessmagazineinhome,
            "commercialdata_doityourselfermagazineinhome": self.commercialdata_doityourselfermagazineinhome,
            "commercialdata_financialmagazineinhome": self.commercialdata_financialmagazineinhome,
            "commercialdata_religiouscontributorinhome": self.commercialdata_religiouscontributorinhome,
            "commercialdata_politicalcontributerinhome": self.commercialdata_politicalcontributerinhome,
            "commercialdata_donatesenvironmentcauseinhome": self.commercialdata_donatesenvironmentcauseinhome,
            "commercialdata_donatestocharityinhome": self.commercialdata_donatestocharityinhome,
            "commercialdata_presenceofpremcredcrdinhome": self.commercialdata_presenceofpremcredcrdinhome,
            "commercialdata_computerownerinhome": self.commercialdata_computerownerinhome,
            "commercialdata_stateincomedecile": self.commercialdata_stateincomedecile,
            "commercialdata_pcnthhwithchildren": self.commercialdata_pcnthhwithchildren,
            "commercialdata_pcnthhmarriedcouplewithchild": self.commercialdata_pcnthhmarriedcouplewithchild,
            "commercialdata_pcnthhmarriedcouplenochild": self.commercialdata_pcnthhmarriedcouplenochild,
            "commercialdata_pcnthhspanishspeaking": self.commercialdata_pcnthhspanishspeaking,
            "commercialdata_medianeducationyears": self.commercialdata_medianeducationyears,
            "commercialdata_mosaicz4": self.commercialdata_mosaicz4,
            "commercialdata_likelyunion": self.commercialdata_likelyunion,
            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }


class Votehistory(models.Model):
    vote_frequency = models.FloatField(default=0)
    general_2000_11_xx = models.BooleanField(default=False)
    general_2001_11_xx = models.BooleanField(default=False)
    general_2002_11_xx = models.BooleanField(default=False)
    general_2003_11_xx = models.BooleanField(default=False)
    general_2004_11_xx = models.BooleanField(default=False)
    general_2005_11_xx = models.BooleanField(default=False)
    general_2006_11_xx = models.BooleanField(default=False)
    general_2007_11_xx = models.BooleanField(default=False)
    general_2008_11_xx = models.BooleanField(default=False)
    general_2009_11_xx = models.BooleanField(default=False)
    general_2010_11_xx = models.BooleanField(default=False)
    general_2011_11_xx = models.BooleanField(default=False)
    general_2012_11_xx = models.BooleanField(default=False)
    general_2013_11_xx = models.BooleanField(default=False)
    general_2014_11_xx = models.BooleanField(default=False)
    primary_2000_xx_xx = models.BooleanField(default=False)
    primary_2001_xx_xx = models.BooleanField(default=False)
    primary_2002_xx_xx = models.BooleanField(default=False)
    primary_2003_xx_xx = models.BooleanField(default=False)
    primary_2004_xx_xx = models.BooleanField(default=False)
    primary_2005_xx_xx = models.BooleanField(default=False)
    primary_2006_xx_xx = models.BooleanField(default=False)
    primary_2007_xx_xx = models.BooleanField(default=False)
    primary_2008_xx_xx = models.BooleanField(default=False)
    primary_2009_xx_xx = models.BooleanField(default=False)
    primary_2010_xx_xx = models.BooleanField(default=False)
    primary_2011_xx_xx = models.BooleanField(default=False)
    primary_2012_xx_xx = models.BooleanField(default=False)
    primary_2013_xx_xx = models.BooleanField(default=False)
    primary_2014_xx_xx = models.BooleanField(default=False)
    presidential_primary_2000_xx_xx = models.BooleanField(default=False)
    presidential_primary_2004_xx_xx = models.BooleanField(default=False)
    presidential_primary_2008_xx_xx = models.BooleanField(default=False)
    presidential_primary_2012_xx_xx = models.BooleanField(default=False)
    pri_blt_2000_xx_xx = models.CharField(default='unk')
    pri_blt_2001_xx_xx = models.CharField(default='unk')
    pri_blt_2002_xx_xx = models.CharField(default='unk')
    pri_blt_2003_xx_xx = models.CharField(default='unk')
    pri_blt_2004_xx_xx = models.CharField(default='unk')
    pri_blt_2005_xx_xx = models.CharField(default='unk')
    pri_blt_2006_xx_xx = models.CharField(default='unk')
    pri_blt_2007_xx_xx = models.CharField(default='unk')
    pri_blt_2008_xx_xx = models.CharField(default='unk')
    pri_blt_2009_xx_xx = models.CharField(default='unk')
    pri_blt_2010_xx_xx = models.CharField(default='unk')
    pri_blt_2011_xx_xx = models.CharField(default='unk')
    pri_blt_2012_xx_xx = models.CharField(default='unk')
    pri_blt_2013_xx_xx = models.CharField(default='unk')
    pri_blt_2014_xx_xx = models.CharField(default='unk')
    voters_active = models.CharField(default='unk')
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "vote_frequency": self.vote_frequency,
"general_2000_11_xx": self.general_2000_11_xx,
"general_2001_11_xx": self.general_2001_11_xx,
"general_2002_11_xx": self.general_2002_11_xx,
"general_2003_11_xx": self.general_2003_11_xx,
"general_2004_11_xx": self.general_2004_11_xx,
"general_2005_11_xx": self.general_2005_11_xx,
"general_2006_11_xx": self.general_2006_11_xx,
"general_2007_11_xx": self.general_2007_11_xx,
"general_2008_11_xx": self.general_2008_11_xx,
"general_2009_11_xx": self.general_2009_11_xx,
"general_2010_11_xx": self.general_2010_11_xx,
"general_2011_11_xx": self.general_2011_11_xx,
"general_2012_11_xx": self.general_2012_11_xx,
"general_2013_11_xx": self.general_2013_11_xx,
"general_2014_11_xx": self.general_2014_11_xx,
"primary_2000_xx_xx": self.primary_2000_xx_xx,
"primary_2001_xx_xx": self.primary_2001_xx_xx,
"primary_2002_xx_xx": self.primary_2002_xx_xx,
"primary_2003_xx_xx": self.primary_2003_xx_xx,
"primary_2004_xx_xx": self.primary_2004_xx_xx,
"primary_2005_xx_xx": self.primary_2005_xx_xx,
"primary_2006_xx_xx": self.primary_2006_xx_xx,
"primary_2007_xx_xx": self.primary_2007_xx_xx,
"primary_2008_xx_xx": self.primary_2008_xx_xx,
"primary_2009_xx_xx": self.primary_2009_xx_xx,
"primary_2010_xx_xx": self.primary_2010_xx_xx,
"primary_2011_xx_xx": self.primary_2011_xx_xx,
"primary_2012_xx_xx": self.primary_2012_xx_xx,
"primary_2013_xx_xx": self.primary_2013_xx_xx,
"primary_2014_xx_xx": self.primary_2014_xx_xx,
"presidential_primary_2000_xx_xx": self.presidential_primary_2000_xx_xx,
"presidential_primary_2004_xx_xx": self.presidential_primary_2004_xx_xx,
"presidential_primary_2008_xx_xx": self.presidential_primary_2008_xx_xx,
"presidential_primary_2012_xx_xx": self.presidential_primary_2012_xx_xx,
"pri_blt_2000_xx_xx": self.pri_blt_2000_xx_xx,
"pri_blt_2001_xx_xx": self.pri_blt_2001_xx_xx,
"pri_blt_2002_xx_xx": self.pri_blt_2002_xx_xx,
"pri_blt_2003_xx_xx": self.pri_blt_2003_xx_xx,
"pri_blt_2004_xx_xx": self.pri_blt_2004_xx_xx,
"pri_blt_2005_xx_xx": self.pri_blt_2005_xx_xx,
"pri_blt_2006_xx_xx": self.pri_blt_2006_xx_xx,
"pri_blt_2007_xx_xx": self.pri_blt_2007_xx_xx,
"pri_blt_2008_xx_xx": self.pri_blt_2008_xx_xx,
"pri_blt_2009_xx_xx": self.pri_blt_2009_xx_xx,
"pri_blt_2010_xx_xx": self.pri_blt_2010_xx_xx,
"pri_blt_2011_xx_xx": self.pri_blt_2011_xx_xx,
"pri_blt_2012_xx_xx": self.pri_blt_2012_xx_xx,
"pri_blt_2013_xx_xx": self.pri_blt_2013_xx_xx,
"pri_blt_2014_xx_xx": self.pri_blt_2014_xx_xx,
"voters_active": self.voters_active,
            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }


class CsDrtvVoter(models.Model):

    email = models.EmailField(default='unk@unk.unk')
    state = models.CharField(default='unk')
    uid = models.FloatField(default=0)
    voterid = models.FloatField(default=0)
    isregistered = models.BooleanField(default=False)
    ismostrecentregistration = models.BooleanField(default=False)

    salutation = models.CharField(default='unk',max_length=3,choices=('unk','mr','mrs','ms','miss'))
    firstname = models.CharField(default='unk')
    middlename = models.CharField(default='unk')
    lastname = models.CharField(default='unk')
    suffix = models.CharField(default='unk')
    gender = models.CharField(default='unk')
    dob = models.DateTimeField(default=datetime.utcnow())
    dob_year = models.DateTimeField(default=datetime.utcnow())
    dob_month = models.DateTimeField(default=datetime.utcnow())
    dob_day = models.DateTimeField(default=datetime.utcnow())
    agerange = models.FloatField(default=0)

    hhmember_firstname = models.CharField(default='unk')
    hhmember_middlename = models.CharField(default='unk')
    hhmember_lastname = models.CharField(default='unk')
    individual_order = models.FloatField(default=0)
    m_householdid = models.FloatField(default=0)
    m_numberinhh = models.FloatField(default=0)
    ethnicity = models.CharField(default='unk')
    religion = models.CharField(default='unk')
    language = models.CharField(default='unk')
    regrace = models.CharField(default='unk')
    race = models.CharField(default='unk')
    isdeceased = models.BooleanField(default=False)

    phone = models.FloatField(default=0)
    phonesource = models.CharField(default='unk')
    phonelinetype = models.CharField(default='unk')
    cellphone = models.FloatField(default=0)
    cellphonesource = models.CharField(default='unk')

    cy = models.FloatField(default=0)
    cname = models.CharField(default='unk')
    cd = models.FloatField(default=0)
    sd = models.CharField(default='unk')
    ld = models.FloatField(default=0)
    jd = models.FloatField(default=0)
    munic = models.CharField(default='unk')
    munin = models.CharField(default='unk')
    township = models.CharField(default='unk')
    ward = models.CharField(default='unk')
    pr = models.FloatField(default=0)
    prsplit = models.FloatField(default=0)
    bb = models.CharField(default='unk')
    pname = models.CharField(default='unk')
    vintage = models.CharField(default='unk')

    addressdifferent = models.BooleanField(default=False)
    rlocationid = models.FloatField(default=0)
    r_addrline1 = models.CharField(default='unk')
    r_addrline2 = models.CharField(default='unk')
    r_city = models.CharField(default='unk')
    r_state = models.CharField(default='unk')
    r_zip5 = models.FloatField(default=0)
    r_uspszip4 = models.FloatField(default=0)
    r_fips = models.FloatField(default=0)
    r_countyname = models.CharField(default='unk')

    mlocationid = models.FloatField(default=0)
    m_addrline1 = models.CharField(default='unk')
    m_addrline2 = models.CharField(default='unk')
    m_city = models.CharField(default='unk')
    m_state = models.CharField(default='unk')
    m_zip5 = models.FloatField(default=0)
    m_uspszip4 = models.FloatField(default=0)
    m_fips = models.FloatField(default=0)
    m_countyname = models.CharField(default='unk')

    ncoa = models.CharField(default='unk')
    ncoa_type = models.CharField(default='unk')
    ncoa_date = models.FloatField(default=0)
    rdate = models.DateTimeField(default=datetime.utcnow())
    party = models.CharField(default='unk')
    ractive = models.CharField(default='unk')
    pabs = models.CharField(default='unk')
    pbf = models.FloatField(default=0)
    
    vh15g = models.IntegerField(default=0)
    vh15p = models.IntegerField(default=0)
    vh15mg = models.IntegerField(default=0)
    vh15mp = models.IntegerField(default=0)
    vh15sg = models.IntegerField(default=0)
    vh15sp = models.IntegerField(default=0)
    vh14g = models.IntegerField(default=0)
    vh14p = models.IntegerField(default=0)
    vh14mg = models.IntegerField(default=0)
    vh14mp = models.IntegerField(default=0)
    vh14sg = models.IntegerField(default=0)
    vh14sp = models.IntegerField(default=0)
    vh13g = models.IntegerField(default=0)
    vh13p = models.IntegerField(default=0)
    vh13mg = models.IntegerField(default=0)
    vh13mp = models.IntegerField(default=0)
    vh13sg = models.IntegerField(default=0)
    vh13sp = models.IntegerField(default=0)
    vh12g = models.IntegerField(default=0)
    vh12p = models.IntegerField(default=0)
    vh12pp = models.IntegerField(default=0)
    vh12mg = models.IntegerField(default=0)
    vh12mp = models.IntegerField(default=0)
    vh12sg = models.IntegerField(default=0)
    vh12sp = models.IntegerField(default=0)
    vh11g = models.IntegerField(default=0)
    vh11p = models.IntegerField(default=0)
    vh11mg = models.IntegerField(default=0)
    vh11mp = models.IntegerField(default=0)
    vh11sg = models.IntegerField(default=0)
    vh11sp = models.IntegerField(default=0)
    vh10g = models.IntegerField(default=0)
    vh10p = models.IntegerField(default=0)
    vh10mg = models.IntegerField(default=0)
    vh10mp = models.IntegerField(default=0)
    vh10sg = models.IntegerField(default=0)
    vh10sp = models.IntegerField(default=0)
    vh09g = models.IntegerField(default=0)
    vh09p = models.IntegerField(default=0)
    vh09mg = models.IntegerField(default=0)
    vh09mp = models.IntegerField(default=0)
    vh09sg = models.IntegerField(default=0)
    vh09sp = models.IntegerField(default=0)
    vh08g = models.IntegerField(default=0)
    vh08p = models.IntegerField(default=0)
    vh08mg = models.IntegerField(default=0)
    vh08mp = models.IntegerField(default=0)
    vh08pp = models.IntegerField(default=0)
    vh08sg = models.IntegerField(default=0)
    vh08sp = models.IntegerField(default=0)
    vh07g = models.IntegerField(default=0)
    vh07p = models.IntegerField(default=0)
    vh07mg = models.IntegerField(default=0)
    vh07mp = models.IntegerField(default=0)
    vh07sg = models.IntegerField(default=0)
    vh07sp = models.IntegerField(default=0)
    vh06g = models.IntegerField(default=0)
    vh06p = models.IntegerField(default=0)
    vh06mg = models.IntegerField(default=0)
    vh06mp = models.IntegerField(default=0)
    vh06sg = models.IntegerField(default=0)
    vh06sp = models.IntegerField(default=0)
    vh05g = models.IntegerField(default=0)
    vh05p = models.IntegerField(default=0)
    vh05mg = models.IntegerField(default=0)
    vh05mp = models.IntegerField(default=0)
    vh05sg = models.IntegerField(default=0)
    vh05sp = models.IntegerField(default=0)
    vh04g = models.IntegerField(default=0)
    vh04p = models.IntegerField(default=0)
    vh04mg = models.IntegerField(default=0)
    vh04mp = models.IntegerField(default=0)
    vh04pp = models.IntegerField(default=0)
    vh04sg = models.IntegerField(default=0)
    vh04sp = models.IntegerField(default=0)
    vh03g = models.IntegerField(default=0)
    vh03p = models.IntegerField(default=0)
    vh03mg = models.IntegerField(default=0)
    vh03mp = models.IntegerField(default=0)
    vh03sg = models.IntegerField(default=0)
    vh03sp = models.IntegerField(default=0)
    vh02g = models.IntegerField(default=0)
    vh02p = models.IntegerField(default=0)
    vh02mg = models.IntegerField(default=0)
    vh02mp = models.IntegerField(default=0)
    vh02sg = models.IntegerField(default=0)
    vh02sp = models.IntegerField(default=0)
    vh01g = models.IntegerField(default=0)
    vh01p = models.IntegerField(default=0)
    vh01mg = models.IntegerField(default=0)
    vh01mp = models.IntegerField(default=0)
    vh01sg = models.IntegerField(default=0)
    vh01sp = models.IntegerField(default=0)
    vh00g = models.IntegerField(default=0)
    vh00p = models.IntegerField(default=0)
    vh00pp = models.IntegerField(default=0)
    vh00sg = models.IntegerField(default=0)
    vh00sp = models.IntegerField(default=0)

    affinitymodel = models.DecimalField(decimal_places=9, default=0)
    propensitymodel = models.DecimalField(decimal_places=9, default=0)
    soconlife = models.DecimalField(decimal_places=9, default=0)
    soconmarriage = models.DecimalField(decimal_places=9, default=0)
    fiscontax = models.DecimalField(decimal_places=9, default=0)
    fisconspending = models.DecimalField(decimal_places=9, default=0)
    healthcaremodel = models.DecimalField(decimal_places=9, default=0)
    r7l2_voter = EmbeddedModelField('R7L2Voter')
    aggregated_voter = EmbeddedModelField('AggregatedVoter')
    meta = {'allow_inheritance': True}
    def as_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "state": self.state,
            "uid": self.uid,
            "voterid": self.voterid,
            "isregistered": self.isregistered,
            "ismostrecentregistration": self.ismostrecentregistration,
            "salutation": self.salutation,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "suffix": self.suffix,
            "gender": self.gender,
            "dob": self.dob,
            "dob_year": self.dob_year,
            "dob_month": self.dob_month,
            "dob_day": self.dob_day,
            "agerange": self.agerange,
            "hhmember_firstname": self.hhmember_firstname,
            "hhmember_middlename": self.hhmember_middlename,
            "hhmember_lastname": self.hhmember_lastname,
            "individual_order": self.individual_order,
            "m_householdid": self.m_householdid,
            "m_numberinhh": self.m_numberinhh,
            "ethnicity": self.ethnicity,
            "religion": self.religion,
            "language": self.language,
            "regrace": self.regrace,
            "race": self.race,
            "isdeceased": self.isdeceased,
            "phone": self.phone,
            "phonesource": self.phonesource,
            "phonelinetype": self.phonelinetype,
            "cellphone": self.cellphone,
            "cellphonesource": self.cellphonesource,
            "cy": self.cy,
            "cname": self.cname,
            "cd": self.cd,
            "sd": self.sd,
            "ld": self.ld,
            "jd": self.jd,
            "munic": self.munic,
            "munin": self.munin,
            "township": self.township,
            "ward": self.ward,
            "pr": self.pr,
            "prsplit": self.prsplit,
            "bb": self.bb,
            "pname": self.pname,
            "vintage": self.vintage,
            "addressdifferent": self.addressdifferent,
            "rlocationid": self.rlocationid,
            "r_addrline1": self.r_addrline1,
            "r_addrline2": self.r_addrline2,
            "r_city": self.r_city,
            "r_state": self.r_state,
            "r_zip5": self.r_zip5,
            "r_uspszip4": self.r_uspszip4,
            "r_fips": self.r_fips,
            "r_countyname": self.r_countyname,
            "mlocationid": self.mlocationid,
            "m_addrline1": self.m_addrline1,
            "m_addrline2": self.m_addrline2,
            "m_city": self.m_city,
            "m_state": self.m_state,
            "m_zip5": self.m_zip5,
            "m_uspszip4": self.m_uspszip4,
            "m_fips": self.m_fips,
            "m_countyname": self.m_countyname,
            "ncoa": self.ncoa,
            "ncoa_type": self.ncoa_type,
            "ncoa_date": self.ncoa_date,
            "rdate": self.rdate,
            "party": self.party,
            "ractive": self.ractive,
            "pabs": self.pabs,
            "pbf": self.pbf,
            "vh15g": self.vh15g,
            "vh15p": self.vh15p,
            "vh15mg": self.vh15mg,
            "vh15mp": self.vh15mp,
            "vh15sg": self.vh15sg,
            "vh15sp": self.vh15sp,
            "vh14g": self.vh14g,
            "vh14p": self.vh14p,
            "vh14mg": self.vh14mg,
            "vh14mp": self.vh14mp,
            "vh14sg": self.vh14sg,
            "vh14sp": self.vh14sp,
            "vh13g": self.vh13g,
            "vh13p": self.vh13p,
            "vh13mg": self.vh13mg,
            "vh13mp": self.vh13mp,
            "vh13sg": self.vh13sg,
            "vh13sp": self.vh13sp,
            "vh12g": self.vh12g,
            "vh12p": self.vh12p,
            "vh12pp": self.vh12pp,
            "vh12mg": self.vh12mg,
            "vh12mp": self.vh12mp,
            "vh12sg": self.vh12sg,
            "vh12sp": self.vh12sp,
            "vh11g": self.vh11g,
            "vh11p": self.vh11p,
            "vh11mg": self.vh11mg,
            "vh11mp": self.vh11mp,
            "vh11sg": self.vh11sg,
            "vh11sp": self.vh11sp,
            "vh10g": self.vh10g,
            "vh10p": self.vh10p,
            "vh10mg": self.vh10mg,
            "vh10mp": self.vh10mp,
            "vh10sg": self.vh10sg,
            "vh10sp": self.vh10sp,
            "vh09g": self.vh09g,
            "vh09p": self.vh09p,
            "vh09mg": self.vh09mg,
            "vh09mp": self.vh09mp,
            "vh09sg": self.vh09sg,
            "vh09sp": self.vh09sp,
            "vh08g": self.vh08g,
            "vh08p": self.vh08p,
            "vh08mg": self.vh08mg,
            "vh08mp": self.vh08mp,
            "vh08pp": self.vh08pp,
            "vh08sg": self.vh08sg,
            "vh08sp": self.vh08sp,
            "vh07g": self.vh07g,
            "vh07p": self.vh07p,
            "vh07mg": self.vh07mg,
            "vh07mp": self.vh07mp,
            "vh07sg": self.vh07sg,
            "vh07sp": self.vh07sp,
            "vh06g": self.vh06g,
            "vh06p": self.vh06p,
            "vh06mg": self.vh06mg,
            "vh06mp": self.vh06mp,
            "vh06sg": self.vh06sg,
            "vh06sp": self.vh06sp,
            "vh05g": self.vh05g,
            "vh05p": self.vh05p,
            "vh05mg": self.vh05mg,
            "vh05mp": self.vh05mp,
            "vh05sg": self.vh05sg,
            "vh05sp": self.vh05sp,
            "vh04g": self.vh04g,
            "vh04p": self.vh04p,
            "vh04mg": self.vh04mg,
            "vh04mp": self.vh04mp,
            "vh04pp": self.vh04pp,
            "vh04sg": self.vh04sg,
            "vh04sp": self.vh04sp,
            "vh03g": self.vh03g,
            "vh03p": self.vh03p,
            "vh03mg": self.vh03mg,
            "vh03mp": self.vh03mp,
            "vh03sg": self.vh03sg,
            "vh03sp": self.vh03sp,
            "vh02g": self.vh02g,
            "vh02p": self.vh02p,
            "vh02mg": self.vh02mg,
            "vh02mp": self.vh02mp,
            "vh02sg": self.vh02sg,
            "vh02sp": self.vh02sp,
            "vh01g": self.vh01g,
            "vh01p": self.vh01p,
            "vh01mg": self.vh01mg,
            "vh01mp": self.vh01mp,
            "vh01sg": self.vh01sg,
            "vh01sp": self.vh01sp,
            "vh00g": self.vh00g,
            "vh00p": self.vh00p,
            "vh00pp": self.vh00pp,
            "vh00sg": self.vh00sg,
            "vh00sp": self.vh00sp,
            "affinitymodel": self.affinitymodel,
            "propensitymodel": self.propensitymodel,
            "soconlife": self.soconlife,
            "soconmarriage": self.soconmarriage,
            "fiscontax": self.fiscontax,
            "fisconspending": self.fisconspending,
            "healthcaremodel": self.healthcaremodel,
            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }


class R7L2Voter(models.Model):

    mseq = models.FloatField(default=0)
    seq = models.FloatField(default=0)
    somedate = models.DateTimeField(default=datetime.utcnow())
    round = models.FloatField(default=0)
    caller_id = models.FloatField(default=0)
    time_stamp = models.DateTimeField(default=datetime.utcnow())
    poling_result = models.CharField(default='unk')
    sheet = models.CharField(default='unk')
    state = models.CharField(default='unk')
    lalvoterid = models.CharField(default='unk')
    lalid = models.CharField(default='unk')
    absenteetypes_description = models.CharField(default='unk')
    source = models.CharField(default='none')
    aggregated_voter = EmbeddedModelField('AggregatedVoter',blank=True, null=True)
    meta = {'allow_inheritance': True}

    def as_dict(self):
        return {
            "id": self.id,
            "mseq": self.mseq,
            "seq": self.seq,
            "somedate": self.somedate,
            "round": self.round,
            "caller_id": self.caller_id,
            "time_stamp": self.time_stamp,
            "poling_result": self.poling_result,
            "sheet": self.sheet,
            "state": self.state,
            "lalvoterid": self.lalvoterid,
            "lalid": self.lalid,
            "absenteetypes_description": self.absenteetypes_description,
            "source": self.source,
            "r7l2_voter": self.r7l2_voter.mseq if self.r7l2_voter else '',
            # other stuff
        }


class AggregatedVoter():

    # aggregate_id = models.CharField(default=str(uuid.uuid1()))
    aggregate_name = models.CharField(default='unk')
    sourceids = ListField(default=[0])
    r7_l2_dedupe = ListField(default=[0])
    cs_drtv_dedupe = ListField(default=[0])
    aggregate_dedupe = ListField(default=[0])

    def as_dict(self):
        return {
            "id": self.id,
            "aggregate_name": self.aggregate_name,
            "sourceids": self.sourceids,
            "r7_l2_dedupe": self.r7_l2_dedupe,
            "cs_drtv_dedupe": self.cs_drtv_dedupe,
            "aggregate_dedupe": self.aggregate_dedupe,
            # other stuff
        }


"""

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



from time import time
from mongoengine import *

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
"""



