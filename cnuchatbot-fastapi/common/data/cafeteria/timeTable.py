from datetime import time

# 기숙사식당
dormitory = {
    "breakfast": {
        "weekday": {
            "open": time(7, 30),
            "close": time(9, 00)
        },
        "weekend": {
            "open": time(7, 30),
            "close": time(9, 00)
        }
    },
    "lunch": {
        "weekday": {
            "open": time(11, 30),
            "close": time(13, 30)
        },
        "weekend": {
            "open": time(11, 30),
            "close": time(13, 30)
        }
    },
    "dinner": {
        "weekday": {
            "open": time(17, 00),
            "close": time(19, 00)
        },
        "weekend": {
            "open": time(17, 30),
            "close": time(19, 00)
        }
    }
}

# 제1학생회관
# student_1 = {
#     "라면&간식": {
#         "breakfast": "미운영",
#         "lunch": {
#             "open": time(10, 00),
#             "close": time(14, 00)
#         },
#         "dinner": {
#             "open": time(17, 30),
#             "close": time(19, 00)
#         }
#     },
#     "양식": {
#         "breakfast": "미운영",
#         "lunch": {
#             "open": time(10, 00),
#             "close": time(14, 00)
#         },
#         "dinner": {
#             "open": time(17, 30),
#             "close": time(19, 00)
#         }
#     },
#     "스낵": {
#         "breakfast": "미운영",
#         "lunch": {
#             "open": time(10, 00),
#             "close": time(14, 00)
#         },
#         "dinner": "미운영"
#     },
#     "한식": {
#         "breakfast": "미운영",
#         "lunch": {
#             "open": time(10, 00),
#             "close": time(14, 00)
#         },
#         "dinner": "미운영"
#     },
#     "일식": {
#         "breakfast": "미운영",
#         "lunch": {
#             "open": time(10, 00),
#             "close": time(14, 00)
#         },
#         "dinner": "미운영"
#     },
#     "중식": {
#         "breakfast": "미운영",
#         "lunch": {
#             "open": time(10, 00),
#             "close": time(14, 00)
#         },
#         "dinner": "미운영"
#     }
# }

# 제2학생회관
student_2 = {
    "breakfast": {
        "weekday": {
            "open": time(8, 00),
            "close": time(9, 00)
        },
        "weekend": "미운영"
    },
    "lunch": {
        "weekday": {
            "open": time(11, 30),
            "close": time(14, 00)
        },
        "weekend": "미운영"
    },
    "dinner": {
        "weekday": "미운영",
        "weekend": "미운영"
    }
}

# 제3학생회관
student_3 = {
    "breakfast": {
        "weekday": "미운영",
        "weekend": "미운영"
    },
    "lunch": {
        "weekday": {
            "open": time(11, 30),
            "close": time(14, 00)
        },
        "weekend": "미운영"
    },
    "dinner": {
        "weekday": "미운영",
        "weekend": "미운영"
    }
}

# 제4학생회관(상록회관)
student_4 = "미운영"

# 생활과학대학
domestic_science = "미운영"
