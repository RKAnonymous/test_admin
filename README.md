# Simple Admin site in Django

### Models

#### Apartment
       +--------------+-------------------------------------------------------------------+
       |     NAME     |                            DESCRIPTION                           |
       +--------------+------------------------------------------------------------------+
       |  ID          |  Identification number of Aparments.                             |
       |              |  Generated automatically while creation of raw data.             |
       +--------------+------------------------------------------------------------------+
       |  AREA        |  Apartment size                                                  |
       +--------------+------------------------------------------------------------------+
       |  FLOOR       |  Located floor                                                   |
       +--------------+------------------------------------------------------------------+
       |  STATUS      |  Current status of an Apartment                                  |
       +--------------+------------------------------------------------------------------+
       |  STATE       |  Current state of an Apartment.                                  |
       |              |  Text description is provided when STATUS changed from {active}  |
       +--------------+------------------------------------------------------------------+
       |  PRICE       |  Apartment price                                                 |
       +--------------+------------------------------------------------------------------+
       |  BUILDING    |  Name of the building object that Apartment is located           |
       +--------------+------------------------------------------------------------------+
       |  CUSTOMER    |  Client                                                          |
       +--------------+------------------------------------------------------------------+
       |  CREATED_AT  |  Date of Apartment added into Database                           |
       +--------------+------------------------------------------------------------------+
       |  UPDATED_AT  |  Date of Apartment raw data is updated                           |
       +--------------+------------------------------------------------------------------+

#### Apartment Booking
       +--------------+-------------------------------------------------------------------+
       |     NAME     |                            DESCRIPTION                           |
       +--------------+------------------------------------------------------------------+
       |  ID          |  Identification number of Aparments.                             |
       |              |  Generated automatically while creation of raw data.             |
       +--------------+------------------------------------------------------------------+
       |  APARTMENT   |  Apartment object                                                |
       +--------------+------------------------------------------------------------------+
       |  CUSTOMER    |  Client who made a booking for an Apartment                      |
       +--------------+------------------------------------------------------------------+
       |  CREATED_AT  |  Date of Apartment added into Database                           |
       +--------------+------------------------------------------------------------------+
       |  UPDATED_AT  |  Date of Apartment raw data is updated                           |
       +--------------+------------------------------------------------------------------+

#### CustomUser ==> User

       +--------------------+--------------------------------------------------------+
       |        NAME        |                     DESCRIPTION                        |    
       +--------------------+--------------------------------------------------------+
       |  ID                |  Identification number of Aparments.                   |
       |                    |  Generated automatically while creation of raw data    |
       +--------------------+--------------------------------------------------------+
       |  USERNAME          |  Username/Nickname                                     |
       +--------------------+--------------------------------------------------------+
       |  EMAIL             |  E-mail address                                        |
       +--------------------+--------------------------------------------------------+
       |  PHONE             |  Phone number                                          |
       +--------------------+--------------------------------------------------------+
       |  ROLES             |  User role. [ADMIN, CUSTOMER, MANAGER]                 |
       +--------------------+--------------------------------------------------------+
       |  CONTRACTS         |  Amount of contracts. (If only user role is MANAGER)   |                                                                         |
       +--------------------+--------------------------------------------------------+
       |  PASSWORD          |  User account password                                 |
       +--------------------+--------------------------------------------------------+
       |  FIRST_NAME        |  First name                                            |
       +--------------------+--------------------------------------------------------+
       |  LAST_NAME         |  Last name                                             |       
       +--------------------+--------------------------------------------------------+
       |  IS_STAFF          |  True. If only user role is ADMIN                      |       
       +--------------------+--------------------------------------------------------+
       |  IS_ACTTIVE        |  True. If only user currently logged in                |       
       +--------------------+--------------------------------------------------------+
       |  DATE_JOINED       |  User data created date                                |      
       +--------------------+--------------------------------------------------------+
       |  GROUPS            |  User groups                                           |       
       +--------------------+--------------------------------------------------------+
       |  USER_PERMISSIONS  |  User permissions                                      |
       +--------------+--------------------------------------------------------------+


### What was done?

1. CRUD for User.
2. CRUD for Apartments.
3. User LOGIN, LOGOUT.
4. Filters API up to the STATUS and BUILDING fields of Apartment model.
5. Simple pages without some sort of certain design.


_**Note: In order to lack of information, specifically Technical Requirement,
template development was chosen instead of API development.
In addition, some kind of misunderstandings might be faced while
observing the code and overall logic of the project written, 
because there was not enough time to cover certain functionalities with tests**_