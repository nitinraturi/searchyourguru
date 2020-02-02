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

ANYTIME = 1
MORNING = 2
AFTERNOON = 3
EVENING = 4

TUTION_TIMINGS = (
    (ANYTIME, "Any Time"),
    (MORNING, "Morning"),
    (AFTERNOON, "Afternoon"),
    (EVENING, "Evening")
)
