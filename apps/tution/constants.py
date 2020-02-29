TAG = 1
GROUP = 2
SEARCH_TAG = 3

TAG_TYPES = (
    (TAG, "Tag"),
    (GROUP, "Group"),
    (SEARCH_TAG, "Search Tag"),
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

PRIVATE_TUTION = 1
GROUP_TUTION = 2

TUTION_TYPES = (
    (PRIVATE_TUTION,"Private Tution"),
    (GROUP_TUTION,"Group Tution")
)
AT_TUTOR_HOME = 1
AT_STUDENT_HOME = 2
AT_INSTITUTE = 3

LOCATION_PREFERENCE = (
    (AT_TUTOR_HOME, "At Tutor Home"),
    (AT_STUDENT_HOME, "At Student Home"),
    (AT_INSTITUTE, "At Insitute")
)
