from datetime import time

reference_room = {
    "신문열람실": {
        "semester": {
            "weekday": {
                "open": time(6, 00),
                "close": time(0)
            },
            "weekend": {
                "open": time(6, 00),
                "close": time(0)
            }
        },
        "vacation": {
            "weekday": {
                "open": time(6, 00),
                "close": time(0)
            },
            "weekend": {
                "open": time(6, 00),
                "close": time(0)
            }
        }
    },
    # "연속간행물실": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(18, 00)
    #         },
    #         "weekend": "미운영"
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(18, 00)
    #         },
    #         "weekend": "미운영"
    #     }
    # },
    # "외국학술지지원센터": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(18, 00)
    #         },
    #         "weekend": "미운영"
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(18, 00)
    #         },
    #         "weekend": "미운영"
    #     }
    # },
    # "학위논문실": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(18, 00)
    #         },
    #         "weekend": "미운영"
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(18, 00)
    #         },
    #         "weekend": "미운영"
    #     }
    # },
    # "고서실": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(18, 00)
    #         },
    #         "weekend": "미운영"
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(18, 00)
    #         },
    #         "weekend": "미운영"
    #     }
    # },
    "대출실": {
        "semester": {
            "weekday": {
                "open": time(9, 00),
                "close": time(20, 00)
            },
            "weekend": "미운영"
        },
        "vacation": {
            "weekday": {
                "open": time(9, 00),
                "close": time(18, 00)
            },
            "weekend": "미운영"
        }
    },
    "제1자료실": {
        "semester": {
            "weekday": {
                "open": time(9, 00),
                "close": time(20, 00)
            },
            "weekend": "미운영"
        },
        "vacation": {
            "weekday": {
                "open": time(9, 00),
                "close": time(18, 00)
            },
            "weekend": "미운영"
        }
    },
    # "제2자료실": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(20, 00)
    #         },
    #         "weekend": "미운영"
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(18, 00)
    #         },
    #         "weekend": "미운영"
    #     }
    # },
    # "제3자료실": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(20, 00)
    #         },
    #         "weekend": "미운영"
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(18, 00)
    #         },
    #         "weekend": "미운영"
    #     }
    # }
}

creative_zone = {
    # "1인 미디어 편집공간": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(17, 00)
    #         },
    #         "weekend": "미운영"
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(17, 00)
    #         },
    #         "weekend": "미운영"
    #     }
    # },
    # "Game Space": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(17, 00)
    #         },
    #         "weekend": "미운영"
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(17, 00)
    #         },
    #         "weekend": "미운영"
    #     }
    # },
    "컨퍼런스룸": {
        "semester": {
            "weekday": {
                "open": time(9, 00),
                "close": time(17, 00)
            },
            "weekend": "미운영"
        },
        "vacation": {
            "weekday": {
                "open": time(9, 00),
                "close": time(17, 00)
            },
            "weekend": "미운영"
        }
    },
    "그룹스터디룸": {
        "semester": {
            "weekday": {
                "open": time(7, 00),
                "close": time(23, 00)
            },
            "weekend": {
                "open": time(7, 00),
                "close": time(23, 00)
            }
        },
        "vacation": {
            "weekday": {
                "open": time(7, 00),
                "close": time(23, 00)
            },
            "weekend": {
                "open": time(7, 00),
                "close": time(23, 00)
            }
        }
    },
    # "그룹스터디룸(5~10인실)": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(7, 00),
    #             "close": time(23, 00)
    #         },
    #         "weekend": {
    #             "open": time(7, 00),
    #             "close": time(23, 00)
    #         }
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(7, 00),
    #             "close": time(23, 00)
    #         },
    #         "weekend": {
    #             "open": time(7, 00),
    #             "close": time(23, 00)
    #         }
    #     }
    # },
    "컴퓨터활용 학습공간": {
        "semester": {
            "weekday": {
                "open": time(7, 00),
                "close": time(23, 00)
            },
            "weekend": {
                "open": time(7, 00),
                "close": time(23, 00)
            }
        },
        "vacation": {
            "weekday": {
                "open": time(7, 00),
                "close": time(23, 00)
            },
            "weekend": {
                "open": time(7, 00),
                "close": time(23, 00)
            }
        }
    },
    # "멀티미디어 활용공간": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(17, 00)
    #         },
    #         "weekend": "미운영"
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(17, 00)
    #         },
    #         "weekend": "미운영"
    #     }
    # },
    # "VR 체험부스": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(17, 00)
    #         },
    #         "weekend": "미운영"
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(17, 00)
    #         },
    #         "weekend": "미운영"
    #     }
    # },
    # "그룹스터디룸(6~10인실)": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(7, 00),
    #             "close": time(23, 00)
    #         },
    #         "weekend": {
    #             "open": time(7, 00),
    #             "close": time(23, 00)
    #         }
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(7, 00),
    #             "close": time(23, 00)
    #         },
    #         "weekend": {
    #             "open": time(7, 00),
    #             "close": time(23, 00)
    #         }
    #     }
    # },
    # "미디어 제작실": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(17, 00)
    #         },
    #         "weekend": "미운영"
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(9, 00),
    #             "close": time(17, 00)
    #         },
    #         "weekend": "미운영"
    #     }
    # }
}

reading_room = {
    "제 1,2,3 열람실": {
        "semester": {
            "weekday": {
                "open": time(6, 00),
                "close": time(23, 00)
            },
            "weekend": {
                "open": time(6, 00),
                "close": time(23, 00)
            }
        },
        "vacation": {
            "weekday": {
                "open": time(6, 00),
                "close": time(23, 00)
            },
            "weekend": {
                "open": time(6, 00),
                "close": time(23, 00)
            }
        }
    },
    "지하 1~2층 열람실": {
        "semester": {
            "weekday": {
                "open": time(6, 00),
                "close": time(23, 00)
            },
            "weekend": {
                "open": time(6, 00),
                "close": time(23, 00)
            }
        },
        "vacation": {
            "weekday": {
                "open": time(6, 00),
                "close": time(23, 00)
            },
            "weekend": {
                "open": time(6, 00),
                "close": time(23, 00)
            }
        }
    },
    "자유열람실": {
        "semester": {
            "weekday": {
                "open": time(6, 00),
                "close": time(23, 00)
            },
            "weekend": {
                "open": time(6, 00),
                "close": time(23, 00)
            }
        },
        "vacation": {
            "weekday": {
                "open": time(6, 00),
                "close": time(23, 00)
            },
            "weekend": {
                "open": time(6, 00),
                "close": time(23, 00)
            }
        }
    },
    # "제1열람실": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(6, 00),
    #             "close": time(0)
    #         },
    #         "weekend": {
    #             "open": time(6, 00),
    #             "close": time(0)
    #         }
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(6, 00),
    #             "close": time(0)
    #         },
    #         "weekend": {
    #             "open": time(6, 00),
    #             "close": time(0)
    #         }
    #     }
    # },
    # "제2열람실": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(6, 00),
    #             "close": time(0)
    #         },
    #         "weekend": {
    #             "open": time(6, 00),
    #             "close": time(0)
    #         }
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(6, 00),
    #             "close": time(0)
    #         },
    #         "weekend": {
    #             "open": time(6, 00),
    #             "close": time(0)
    #         }
    #     }
    # },
    # "제3열람실": {
    #     "semester": {
    #         "weekday": {
    #             "open": time(6, 00),
    #             "close": time(0)
    #         },
    #         "weekend": {
    #             "open": time(6, 00),
    #             "close": time(0)
    #         }
    #     },
    #     "vacation": {
    #         "weekday": {
    #             "open": time(6, 00),
    #             "close": time(0)
    #         },
    #         "weekend": {
    #             "open": time(6, 00),
    #             "close": time(0)
    #         }
    #     }
    # }
}
