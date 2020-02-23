SUPERUSER = 1
STAFF = 2
STUDENT = 3
TUTOR = 4

USER_TYPE_CHOICES = (
    (SUPERUSER, 'Superuser'),
    (STAFF, 'Staff'),
    (STUDENT, 'Student'),
    (TUTOR, 'Tutor'),
)

ACCOUNT_ACTIVE = "active"
ACCOUNT_INACTIVE = "inactive"
ACCOUNT_DOESNOTEXIST = "doesnotexist"

MALE = 1
FEMALE = 2
OTHER = 3

GENDER_CHOICES = (
    (MALE, "Male"),
    (FEMALE, "Female"),
    (OTHER, "Other")
)

BELOW_2_YEARS = 1
BETWEEN2AND5YEARS = 2
ABOVE5YEARS = 3

EXPERIENCE_CHOICES = (
    (BELOW_2_YEARS, "Below 2 years"),
    (BETWEEN2AND5YEARS, "Between 2 and 5 Years"),
    (ABOVE5YEARS, "5+ Years")
)
