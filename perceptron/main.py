import pprint
from lib import helpers

my_list = helpers.csv_to_dict_list('datasets/credit.csv')
pp = pprint.PrettyPrinter(width=150)


def unique_values(a_list):
  return list(set(a_list))


def btoi(condition):
  return 1 if condition == True else 0


# prop = 'job'
# all_values = list(map(lambda x: x[prop], my_list))
# pp.pprint(list(map(lambda x: '"is_' + prop + '_' + x +
#                    '": btoi(item[' + "'" + prop + "'] == " + '"' + x + '"),', unique_values(all_values))))


def modifier(item):
  return {
      "class": btoi(item['class'] == 'good'),
      "is_checking_status_'no checking'": btoi(item['checking_status'] == "'no checking'"),
      "is_checking_status_'>=200'": btoi(item['checking_status'] == "'>=200'"),
      "is_checking_status_'<0'": btoi(item['checking_status'] == "'<0'"),
      "is_checking_status_'0<=X<200'": btoi(item['checking_status'] == "'0<=X<200'"),
      "duration": btoi(item['duration']),
      "is_credit_history_'delayed previously'": btoi(item['credit_history'] == "'delayed previously'"),
      "is_credit_history_'critical/other existing credit'": btoi(item['credit_history'] == "'critical/other existing credit'"),
      "is_credit_history_'existing paid'": btoi(item['credit_history'] == "'existing paid'"),
      "is_credit_history_'no credits/all paid'": btoi(item['credit_history'] == "'no credits/all paid'"),
      "is_credit_history_'all paid'": btoi(item['credit_history'] == "'all paid'"),
      "is_purpose_radio/tv": btoi(item['purpose'] == "radio/tv"),
      "is_purpose_furniture/equipment": btoi(item['purpose'] == "furniture/equipment"),
      "is_purpose_other": btoi(item['purpose'] == "other"),
      "is_purpose_'new car'": btoi(item['purpose'] == "'new car'"),
      "is_purpose_'domestic appliance'": btoi(item['purpose'] == "'domestic appliance'"),
      "is_purpose_repairs": btoi(item['purpose'] == "repairs"),
      "is_purpose_education": btoi(item['purpose'] == "education"),
      "is_purpose_business": btoi(item['purpose'] == "business"),
      "is_purpose_retraining": btoi(item['purpose'] == "retraining"),
      "is_purpose_'used car'": btoi(item['purpose'] == "'used car'"),
      "credit_amount": btoi(item['credit_amount']),
      "is_savings_status_'no known savings'": btoi(item['savings_status'] == "'no known savings'"),
      "is_savings_status_'>=1000'": btoi(item['savings_status'] == "'>=1000'"),
      "is_savings_status_'500<=X<1000'": btoi(item['savings_status'] == "'500<=X<1000'"),
      "is_savings_status_'<100'": btoi(item['savings_status'] == "'<100'"),
      "is_savings_status_'100<=X<500'": btoi(item['savings_status'] == "'100<=X<500'"),
      "is_employment_'4<=X<7'": btoi(item['employment'] == "'4<=X<7'"),
      "is_employment_unemployed": btoi(item['employment'] == "unemployed"),
      "is_employment_'<1'": btoi(item['employment'] == "'<1'"),
      "is_employment_'>=7'": btoi(item['employment'] == "'>=7'"),
      "is_employment_'1<=X<4'": btoi(item['employment'] == "'1<=X<4'"),
      "installment_commitment": btoi(item['installment_commitment']),
      "is_personal_status_'male mar/wid'": btoi(item['personal_status'] == "'male mar/wid'"),
      "is_personal_status_'male div/sep'": btoi(item['personal_status'] == "'male div/sep'"),
      "is_personal_status_'female div/dep/mar'": btoi(item['personal_status'] == "'female div/dep/mar'"),
      "is_personal_status_'male single'": btoi(item['personal_status'] == "'male single'"),
      "is_other_parties_none": btoi(item['other_parties'] == "none"),
      "is_other_parties_guarantor": btoi(item['other_parties'] == "guarantor"),
      "is_other_parties_'co applicant'": btoi(item['other_parties'] == "'co applicant'"),
      "residence_since": btoi(item['residence_since']),
      "is_property_magnitude_'no known property'": btoi(item['property_magnitude'] == "'no known property'"),
      "is_property_magnitude_car": btoi(item['property_magnitude'] == "car"),
      "is_property_magnitude_'real estate'": btoi(item['property_magnitude'] == "'real estate'"),
      "is_property_magnitude_'life insurance'": btoi(item['property_magnitude'] == "'life insurance'"),
      "age": btoi(item['age']),
      "is_other_payment_plans_bank": btoi(item['other_payment_plans'] == "bank"),
      "is_other_payment_plans_none": btoi(item['other_payment_plans'] == "none"),
      "is_other_payment_plans_stores": btoi(item['other_payment_plans'] == "stores"),
      "is_housing_rent": btoi(item['housing'] == "rent"),
      "is_housing_own": btoi(item['housing'] == "own"),
      "is_housing_'for free'": btoi(item['housing'] == "'for free'"),
      "existing_credits": btoi(item['existing_credits']),
      "is_job_skilled": btoi(item['job'] == "skilled"),
      "is_job_'unemp/unskilled non res'": btoi(item['job'] == "'unemp/unskilled non res'"),
      "is_job_'unskilled resident'": btoi(item['job'] == "'unskilled resident'"),
      "is_job_'high qualif/self emp/mgmt'": btoi(item['job'] == "'high qualif/self emp/mgmt'"),
      "num_dependents": btoi(item['num_dependents']),
      "own_telephone": btoi(item['own_telephone'] == 'yes'),
      "foreign_worker": btoi(item['foreign_worker'] == 'yes')
  }


pp.pprint(len(helpers.examples_to_vectors(modifier, my_list)))
