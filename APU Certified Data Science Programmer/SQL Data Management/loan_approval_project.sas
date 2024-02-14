/***********************************************************************

                 Name: Mohammad Najman Bin Md Noor
         Job position: Student
      Name of program: my_dm_sas_program.sas
          Description: Loan approval project
   Date first written: Tue,6-May-2023
    Date last updated: Tue,8-July-2023
  Project folder name: MYDMCLASS_MAY_2023
Permanent SAS library: MYLIB_DM

***********************************************************************/

/* CHAPTER 3: Data exploration and analysis 

   Step 1: display the two data dictionaries */
PROC CONTENTS DATA = MYLIB_DM.TRAINING_DS;

RUN;

PROC CONTENTS DATA = MYLIB_DM.TESTING_DS;

RUN;

/* CHAPTER 3.1: Analysis of variables found in the MYLIB_DM.TRAINING_DS 
           3.2: Univariate Analysis of variables 
           3.3: Univariate Analysis of the Categorical variable - GENDER 
           
           Univariate is the analysis of one variable at a time */

TITLE '3.3 SAS CODES to do Univariate Analysis of the Categorical variable: GENDER';

PROC FREQ DATA = MYLIB_DM.TRAINING_DS;

TABLE GENDER;

RUN;

ODS GRAPHICS / RESET WIDTH = 3.0 IN HEIGHT = 4.0 IN IMAGEMAP;

PROC SGPLOT DATA = MYLIB_DM.TRAINING_DS;

VBAR GENDER;

TITLE '3.3 SAS CODES to do Univariate Analysis of the Categorical variable: GENDER';

RUN;

/* CHAPTER 3.4: Univariate Analysis of the Categorical variable - LOAN_APPROVAL_STATUS */

TITLE '3.4 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_APPROVAL_STATUS';
FOOTNOTE 'Good Variable';

PROC FREQ DATA = MYLIB_DM.TRAINING_DS;

TABLE LOAN_APPROVAL_STATUS;

RUN;

ODS GRAPHICS / RESET WIDTH = 3.0 IN HEIGHT = 4.0 IN IMAGEMAP;

PROC SGPLOT DATA = MYLIB_DM.TRAINING_DS;

VBAR LOAN_APPROVAL_STATUS;

TITLE '3.4 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_APPROVAL_STATUS';

RUN;

/* CHAPTER 3.5: Univariate Analysis of the Categorical variable - LOAN_HISTORY */

TITLE '3.5 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_HISTORY';

PROC FREQ DATA = MYLIB_DM.TRAINING_DS;

TABLE LOAN_HISTORY;

RUN;

ODS GRAPHICS / RESET WIDTH = 3.0 IN HEIGHT = 4.0 IN IMAGEMAP;

PROC SGPLOT DATA = MYLIB_DM.TRAINING_DS;

VBAR LOAN_HISTORY;

TITLE '3.5 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_HISTORY';

RUN;

/* CHAPTER 3.6: Univariate Analysis of the Categorical variable - LOAN_LOCATION */

TITLE '3.6 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_LOCATION';
FOOTNOTE 'Good Variable';

PROC FREQ DATA = MYLIB_DM.TRAINING_DS;

TABLE LOAN_LOCATION;

RUN;

ODS GRAPHICS / RESET WIDTH = 3.0 IN HEIGHT = 4.0 IN IMAGEMAP;

PROC SGPLOT DATA = MYLIB_DM.TRAINING_DS;

VBAR LOAN_LOCATION;

TITLE '3.6 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_LOCATION';

RUN;

/* CHAPTER 3.7: Univariate Analysis of the Categorical variable - MARITAL_STATUS */

TITLE '3.7 SAS CODES to do Univariate Analysis of the Categorical variable: MARITAL_STATUS';

PROC FREQ DATA = MYLIB_DM.TRAINING_DS;

TABLE MARITAL_STATUS;

RUN;

ODS GRAPHICS / RESET WIDTH = 3.0 IN HEIGHT = 4.0 IN IMAGEMAP;

PROC SGPLOT DATA = MYLIB_DM.TRAINING_DS;

VBAR MARITAL_STATUS;

TITLE '3.7 SAS CODES to do Univariate Analysis of the Categorical variable: MARITAL_STATUS';

RUN;

/* CHAPTER 3.8: Univariate Analysis of the Categorical variable - LOAN_DURATION */

TITLE '3.8 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_DURATION';

PROC FREQ DATA = MYLIB_DM.TRAINING_DS;

TABLE LOAN_DURATION;

RUN;

ODS GRAPHICS / RESET WIDTH = 3.0 IN HEIGHT = 4.0 IN IMAGEMAP;

PROC SGPLOT DATA = MYLIB_DM.TRAINING_DS;

VBAR LOAN_DURATION;

TITLE '3.8 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_DURATION';

RUN;

/* CHAPTER 3.9: Univariate Analysis of the Categorical variable - LOAN_AMOUNT */

TITLE '3.9 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_AMOUNT';

PROC FREQ DATA = MYLIB_DM.TRAINING_DS;

TABLE LOAN_AMOUNT;

RUN;

ODS GRAPHICS / RESET WIDTH = 3.0 IN HEIGHT = 4.0 IN IMAGEMAP;

PROC SGPLOT DATA = MYLIB_DM.TRAINING_DS;

VBAR LOAN_AMOUNT;

TITLE '3.9 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_AMOUNT';

RUN;

/* CHAPTER 3.10: Univariate Analysis of the Categorical variable - CANDIDATE_INCOME */

TITLE '3.10 SAS CODES to do Univariate Analysis of the Categorical variable: CANDIDATE_INCOME';
FOOTNOTE 'Good Variable';

PROC FREQ DATA = MYLIB_DM.TRAINING_DS;

TABLE CANDIDATE_INCOME;

RUN;

ODS GRAPHICS / RESET WIDTH = 3.0 IN HEIGHT = 4.0 IN IMAGEMAP;

PROC SGPLOT DATA = MYLIB_DM.TRAINING_DS;

VBAR CANDIDATE_INCOME;

TITLE '3.10 SAS CODES to do Univariate Analysis of the Categorical variable: CANDIDATE_INCOME';

RUN;

/* CHAPTER 3.11: Univariate Analysis of the Categorical variable - LOAN_APPROVAL_STATUS */

TITLE '3.11 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_APPROVAL_STATUS';
FOOTNOTE 'Good Variable';

PROC FREQ DATA = MYLIB_DM.TESTING_DS;

TABLE LOAN_APPROVAL_STATUS;

RUN;

ODS GRAPHICS / RESET WIDTH = 3.0 IN HEIGHT = 4.0 IN IMAGEMAP;

PROC SGPLOT DATA = MYLIB_DM.TESTING_DS;

VBAR LOAN_APPROVAL_STATUS;

TITLE '3.11 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_APPROVAL_STATUS';

RUN;

/* CHAPTER 3.12: Univariate Analysis of the Categorical variable - LOAN_HISTORY */

TITLE '3.12 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_HISTORY';

PROC FREQ DATA = MYLIB_DM.TESTING_DS;

TABLE LOAN_HISTORY;

RUN;

ODS GRAPHICS / RESET WIDTH = 3.0 IN HEIGHT = 4.0 IN IMAGEMAP;

PROC SGPLOT DATA = MYLIB_DM.TESTING_DS;

VBAR LOAN_HISTORY;

TITLE '3.12 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_HISTORY';

RUN;

/* CHAPTER 3.13: Univariate Analysis of the Categorical variable - LOAN_LOCATION */

TITLE '3.13 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_LOCATION';
FOOTNOTE 'Good Variable';

PROC FREQ DATA = MYLIB_DM.TESTING_DS;

TABLE LOAN_LOCATION;

RUN;

ODS GRAPHICS / RESET WIDTH = 3.0 IN HEIGHT = 4.0 IN IMAGEMAP;

PROC SGPLOT DATA = MYLIB_DM.TESTING_DS;

VBAR LOAN_LOCATION;

TITLE '3.13 SAS CODES to do Univariate Analysis of the Categorical variable: LOAN_LOCATION';

RUN;

/* CHAPTER 3.14: Univariate Analysis of the Categorical variable - MARITAL_STATUS */

TITLE '3.14 SAS CODES to do Univariate Analysis of the Categorical variable: MARITAL_STATUS';
FOOTNOTE 'Good Variable';

PROC FREQ DATA = MYLIB_DM.TESTING_DS;

TABLE MARITAL_STATUS;

RUN;

ODS GRAPHICS / RESET WIDTH = 3.0 IN HEIGHT = 4.0 IN IMAGEMAP;

PROC SGPLOT DATA = MYLIB_DM.TESTING_DS;

VBAR MARITAL_STATUS;

TITLE '3.14 SAS CODES to do Univariate Analysis of the Categorical variable: MARITAL_STATUS';

RUN;

/* TRAINING_DS variable value status */
/* MISSING: GENDER, LOAN_HISTORY, MARITAL_STATUS */

/* TESTING_DS variable value status */
/* MISSING: GENDER, LOAN_HISTORY */

/* STEP 3.15: Univariate Analysis of the continuous  or numerical variables */
/* STEP 3.15.1: Univariate Analysis of the continuous  or numerical variables - LOAN_AMOUNT */

TITLE 'STEP 3.15.1: Univariate Analysis of the continuous  or numerical variables - LOAN_AMOUNT';
FOOTNOTE '22 Observations with missing values';

PROC MEANS DATA = MYLIB_DM.TRAINING_DS N NMISS MIN MAX MEAN MEDIAN STD;

VAR LOAN_AMOUNT;

RUN;

/* STEP 3.15.2: Univariate Analysis of the continuous  or numerical variables - CANDIDATE_INCOME */

TITLE 'STEP 3.15.2: Univariate Analysis of the continuous  or numerical variables - CANDIDATE_INCOME';
FOOTNOTE 'Good variable';

PROC MEANS DATA = MYLIB_DM.TRAINING_DS N NMISS MIN MAX MEAN MEDIAN STD;

VAR CANDIDATE_INCOME;

RUN;

/* STEP 3.15.3: Univariate Analysis of the continuous  or numerical variables - LOAN_DURATION */

TITLE 'STEP 3.15.3: Univariate Analysis of the continuous  or numerical variables - LOAN_DURATION';
FOOTNOTE '14 Observations with missing values';

PROC MEANS DATA = MYLIB_DM.TRAINING_DS N NMISS MIN MAX MEAN MEDIAN STD;

VAR LOAN_DURATION;

RUN;

/* STEP 3.16.1: Univariate Analysis of the continuous  or numerical variables - LOAN_AMOUNT */

TITLE 'STEP 3.16.1: Univariate Analysis of the continuous  or numerical variables - LOAN_AMOUNT';
FOOTNOTE '5 Observations with missing values';

PROC MEANS DATA = MYLIB_DM.TESTING_DS N NMISS MIN MAX MEAN MEDIAN STD;

VAR LOAN_AMOUNT;

RUN;

/* STEP 3.16.2: Univariate Analysis of the continuous  or numerical variables - LOAN_DURATION */

TITLE 'STEP 3.16.2: Univariate Analysis of the continuous  or numerical variables - LOAN_DURATION';
FOOTNOTE '6 Observations with missing values';

PROC MEANS DATA = MYLIB_DM.TESTING_DS N NMISS MIN MAX MEAN MEDIAN STD;

VAR LOAN_DURATION;

RUN;

/* STEP 3.16.3: Univariate Analysis of the continuous  or numerical variables - CANDIDATE_INCOME */

TITLE 'STEP 3.16.3: Univariate Analysis of the continuous  or numerical variables - CANDIDATE_INCOME';
FOOTNOTE 'Good variable';

PROC MEANS DATA = MYLIB_DM.TESTING_DS N NMISS MIN MAX MEAN MEDIAN STD;

VAR CANDIDATE_INCOME;

RUN;

/* Variable with missing value found in TRAINING_DS */
/* LOAN_DURATION & LOAN_AMOUNT */
/* Variable with missing value found in TESTING_DS */
/* LOAN_DURATION & LOAN_AMOUNT*/

/* CHAPTER 3.17: Bivariate Analysis of variables */
/*         3.17.1: Bivariate Analysis of the variables found in the MYLIB_DM.TRAINING_DS */
/*         3.17.2: Bivariate Analysis of the variables (Categorical variable vs Categorical variable) */
/*         3.17.3: Bivariate Analysis of the variables (GENDER vs LOAN_LOCATION) */

TITLE1 'Figure Number Bivariate analysis of the variables: ';
TITLE2 'Categorical variable [GENDER] vs [LOAN_LOCATION]';

PROC FREQ DATA = MYLIB_DM.TRAINING_DS;

TABLE gender * loan_location/
PLOTS = FREQPLOT ( TWOWAY = STACKED SCALE = GROUPPCT);

RUN;

/*         3.17.4: Bivariate Analysis of the variables (GENDER vs MARITAL_STATUS) */

TITLE1 'Figure Number Bivariate analysis of the variables: ';
TITLE2 'Categorical variable [GENDER] vs [MARITAL_STATUS]';

PROC FREQ DATA = MYLIB_DM.TRAINING_DS;

TABLE gender * marital_status/
PLOTS = FREQPLOT ( TWOWAY = STACKED SCALE = GROUPPCT);

RUN;

/*         3.18.1: Bivariate Analysis of the variables (Categorical variable vs Continuous variable) */
/*         3.18.2: Bivariate Analysis of the variables (GENDER vs LOAN_AMOUNT) */

TITLE1 'Figure Number Bivariate analysis of the variables: ';
TITLE2 'Categorical variable [GENDER] vs [LOAN_AMOUNT]';

PROC MEANS DATA = MYLIB_DM.TRAINING_DS;

CLASS gender;
VAR loan_amount;

RUN;

/*         3.18.3: Bivariate Analysis of the variables (MARITAL_STATUS vs LOAN_AMOUNT) */

TITLE1 'Figure Number Bivariate analysis of the variables: ';
TITLE2 'Categorical variable [MARITAL_STATUS] vs [LOAN_AMOUNT]';

PROC MEANS DATA = MYLIB_DM.TRAINING_DS;

CLASS MARITAL_STATUS;
VAR LOAN_AMOUNT;

RUN;

/*         3.18.4: Bivariate Analysis of the variables (GENDER vs MARITAL_STATUS) */

TITLE1 'Figure Number Bivariate analysis of the variables: ';
TITLE2 'Categorical variable [GENDER] vs [MARITAL_STATUS]';

PROC FREQ DATA = MYLIB_DM.TESTING_DS;

TABLE gender * marital_status/
PLOTS = FREQPLOT ( TWOWAY = STACKED SCALE = GROUPPCT);

RUN;

/*         3.18.5: Bivariate Analysis of the variables (GENDER vs LOAN_AMOUNT) (BOTH GENDER AND LOAN AMOUNT HAVE MISSING VARIABLES) */

TITLE1 'Figure Number Bivariate analysis of the variables: ';
TITLE2 'Categorical variable [GENDER] vs [LOAN_AMOUNT]';

PROC MEANS DATA = MYLIB_DM.TESTING_DS;

CLASS GENDER;
VAR LOAN_AMOUNT;

RUN;

/*         3.18.6: Bivariate Analysis of the variables (MARITAL_STATUS vs CANDIDATE_INCOME) */

TITLE1 'Figure Number Bivariate analysis of the variables: ';
TITLE2 'Categorical variable [MARITAL_STATUS] vs [CANDIDATE_INCOME]';

PROC MEANS DATA = MYLIB_DM.TESTING_DS;

CLASS MARITAL_STATUS;
VAR CANDIDATE_INCOME;

RUN;

/* CHAPTER 4: Data Cleasing */
/* 4.1 Impute (cleanse) the Categorical variables found in the MYLIB_DM.TRAINING_DS */

/* 4.1.1 Impute (cleanse) the Categorical variable - GENDER */

TITLE '4.1.1 List the details of the applicants (observation) with missing values';

PROC SQL;

SELECT *
FROM MYLIB_DM.TRAINING_DS e
WHERE ( e.gender eq '' ) OR ( e.gender IS MISSING );

QUIT;

/* 4.1.2 Count the total number of missing values */

TITLE '4.1.1 List the details of the applicants (observation) with missing values';

PROC SQL;

SELECT COUNT(*) Label = 'Total of missing value'
FROM MYLIB_DM.TRAINING_DS e
WHERE ( e.gender eq '' ) OR ( e.gender IS MISSING );

QUIT;

/* 4.1.3 Store the statistics (gender vs counts) in a dataset */

TITLE '4.1.1 List the details of the applicants (observation) with missing values';

PROC SQL;

CREATE TABLE MYLIB_DM.TRAINING_GENDER_DS AS
SELECT e.gender AS gender,
	   COUNT(*) AS no_of_applicants
FROM MYLIB_DM.TRAINING_DS e
WHERE ( ( e.gender ne '' ) OR 
		( e.gender IS NOT MISSING ) )
GROUP BY e.gender;

QUIT;

/* 4.1.3.1 Make a backup copy of the ds */

PROC SQL;

CREATE TABLE  MYLIB_DM.TRAINING_BK_DS AS
SELECT *
FROM MYLIB_DM.TRAINING_DS;

QUIT;

/* 4.1.4 Impute the missing values found in the variable gender */
/* replace the MISSING gender with 'male' */

PROC SQL;

UPDATE MYLIB_DM.TRAINING_DS
SET gender = 
( SELECT e.gender AS gender
  FROM MYLIB_DM.TRAINING_GENDER_DS e
  WHERE e.no_of_applicants eq ( SELECT MAX(e.no_of_applicants) AS no_of_applicants
							  FROM MYLIB_DM.TRAINING_GENDER_DS e ) )
							  /* sub-program to choose gender that has highest value */
WHERE ( ( gender eq '' ) OR
	    ( gender IS MISSING ) );
	    
QUIT;

/* 5.1 Impute (cleanse) the Categorical variables found in the TESTING_DS */

/* 5.1.1 Impute (cleanse) the Categorical variables - GENDER */
/* 5.1.2 Find the missing GENDER */
PROC SQL;

SELECT COUNT(*) Label = 'Number of observations/applicants'
FROM MYLIB_DM.TESTING_DS e
WHERE ( ( gender eq '' ) OR
		( gender IS MISSING ) );

QUIT;

/* 5.1.3 Store the statistics in a ds */

PROC SQL;

CREATE TABLE MYLIB_DM.TESTING_GENDER_DS AS
SELECT  e.gender AS gender,
		COUNT(*) AS no_of_applicants
FROM MYLIB_DM.TESTING_DS e
WHERE ( ( e.gender ne '' ) OR
		( e.gender IS NOT MISSING ) )
GROUP BY e.gender;
		
QUIT;

/* 5.1.3 Create a backup DS copy */

PROC SQL;

CREATE TABLE MYLIB_DM.TESTING_BK_DS AS
SELECT *
FROM MYLIB_DM.TESTING_DS e;

QUIT;

/* 5.1.4 Impute the missing values found in the variable gender */
/* replace the MISSING gender with 'male' */

PROC SQL;

UPDATE MYLIB_DM.TESTING_DS
SET gender = 
( SELECT e.gender AS gender
  FROM MYLIB_DM.TESTING_GENDER_DS e
  WHERE e.no_of_applicants eq ( SELECT MAX(e.no_of_applicants) AS no_of_applicants
							  FROM MYLIB_DM.TESTING_GENDER_DS e ) )
							  /* sub-program to choose gender that has highest value */
WHERE ( ( gender eq '' ) OR
	    ( gender IS MISSING ) );
	    
QUIT;

/* 6.1 Impute (cleanse) the Continuous/Numeric variables found in the TRAINING_DS */
/* 6.1.1 Impute (cleanse) the Continuous/Numeric variables - loan_amount */
/* 6.1.1 Find the missing loan_amount */

TITLE 'STEP 6.1.1: Find the missing loan_amount';

PROC SQL;

SELECT *
FROM MYLIB_DM.TRAINING_DS e
WHERE ( ( e.loan_amount eq . ) OR
		( e.loan_amount IS MISSING ) );
QUIT;

/* 6.1.2 Count the total missing Continuous/Numeric variables - loan_amount */

PROC SQL;

SELECT COUNT(*) Label = 'Number of observations'
FROM MYLIB_DM.TRAINING_DS e
WHERE ( ( e.loan_amount eq . ) OR
		( e.loan_amount IS MISSING ) );
		
QUIT;

/* 6.1.3 Impute the missing values found in Continuous/Numeric variables - loan_amount */

PROC STDIZE DATA = MYLIB_DM.TRAINING_DS REPONLY

METHOD = MEAN OUT = MYLIB_DM.TRAINING_DS;
VAR loan_amount;

QUIT;

PROC SQL;

SELECT COUNT(*) Label = 'Number of observations'
FROM MYLIB_DM.TRAINING_DS e
WHERE ( ( e.loan_amount eq . ) OR
		( e.loan_amount IS MISSING ) );
		
QUIT;

/* 7.1 Impute (cleanse) the Continuous/Numeric variables found in the TESTING_DS */
/* 7.1.1 Impute (cleanse) the Continuous/Numeric variables - loan_amount */

/* 7.1.1 Find the missing loan_amount */

TITLE 'STEP 7.1.1: Missing loan_amount';

PROC SQL;

SELECT *
FROM MYLIB_DM.TESTING_DS e
WHERE ( ( e.loan_amount eq . ) OR
		( e.loan_amount IS MISSING ) );
QUIT;

/* 7.1.2 Make a backup copy */
PROC SQL;

CREATE TABLE MYLIB_DM.TESTING_BK2_DS AS
SELECT *
FROM MYLIB_DM.TESTING_DS;

QUIT;

/* 7.1.3 Impute the missing values found in Continuous/Numeric variables - loan_amount */

PROC STDIZE DATA = MYLIB_DM.TESTING_DS REPONLY

METHOD = MEAN OUT = MYLIB_DM.TESTING_DS;
VAR loan_amount;

QUIT;

TITLE 'Missing loan_amount';

PROC SQL;

SELECT COUNT(*) Label = 'No of observations'
FROM MYLIB_DM.TESTING_DS e
WHERE ( ( e.loan_amount eq . ) OR
		( e.loan_amount IS MISSING ) );
QUIT;

/* Create LR model */
PROC LOGISTIC DATA = MYLIB_DM.TRAINING_DS OUTMODEL = MYLIB_DM.TRAINING_LR_MODEL;  
CLASS 
GENDER 
LOAN_LOCATION  
LOAN_HISTORY
MARITAL_STATUS
;
/* Above are categorical variables */ 
MODEL LOAN_APPROVAL_STATUS = /*place here all independent variables */
/* LOAN_APPLICATION_STATUS is a dependent variable */
GENDER 
LOAN_LOCATION  
LOAN_HISTORY
MARITAL_STATUS 
LOAN_AMOUNT
LOAN_DURATION;
OUTPUT OUT = MYLIB_DM.TRAINING_OUT_DS P = PRED_PROB;
/*PRED_PROB ->Predicted probability - variable to hold predicted probability 
OUT -> the output will be stored in the dataset 
Akaike Information criterion must ( AIC ) < SC (Schwarz Criterion) */
/*If Pr > ChiSq is <= 0.05, it means that that independent variable is an 
important variable and as is truely contributing to predite dependent varibale*/
RUN;