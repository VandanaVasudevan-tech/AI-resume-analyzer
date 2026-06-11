# import re
# from datetime import datetime
#
#
# def extract_experience(text):
#
#     text = text.lower()
#
#     # Pattern 1: "5 years experience"
#     years_pattern = r'(\d+(?:\.\d+)?)\s+years?'
#
#     years_matches = re.findall(
#         years_pattern,
#         text
#     )
#
#     explicit_years = 0
#
#     if years_matches:
#         explicit_years = max(
#             float(y)
#             for y in years_matches
#         )
#
#     # Pattern 2: 05/2019 - 07/2024
#
#     date_pattern_1 = r'(\d{2})/(\d{4})\s*-\s*(\d{2})/(\d{4})'
#
#     matches1 = re.findall(
#         date_pattern_1,
#         text
#     )
#
#     months_from_pattern1 = 0
#
#     for start_month, start_year, end_month, end_year in matches1:
#
#         months = (
#             (int(end_year) - int(start_year)) * 12
#             +
#             (int(end_month) - int(start_month))
#         )
#
#         months_from_pattern1 += months
#
#     # Pattern 3:
#     # Jan 2024 - May 2025
#
#     month_map = {
#         "jan": 1,
#         "feb": 2,
#         "mar": 3,
#         "apr": 4,
#         "may": 5,
#         "jun": 6,
#         "june": 6,
#         "jul": 7,
#         "aug": 8,
#         "sep": 9,
#         "oct": 10,
#         "nov": 11,
#         "dec": 12
#     }
#
#     date_pattern_2 = r'([a-z]+)\s+(\d{4})\s*-\s*([a-z]+)\s+(\d{4})'
#
#     matches2 = re.findall(
#         date_pattern_2,
#         text
#     )
#
#     months_from_pattern2 = 0
#
#     for start_month, start_year, end_month, end_year in matches2:
#
#         start_month_num = month_map.get(
#             start_month[:3],
#             1
#         )
#
#         end_month_num = month_map.get(
#             end_month[:3],
#             1
#         )
#
#         months = (
#             (int(end_year) - int(start_year)) * 12
#             +
#             (end_month_num - start_month_num)
#         )
#
#         months_from_pattern2 += months
#
#     calculated_years = round(
#         max(
#             months_from_pattern1,
#             months_from_pattern2
#         ) / 12,
#         1
#     )
#
#     if explicit_years > 0:
#         return explicit_years
#
#     return calculated_years


import re

def extract_experience(text):
    text = text.lower()

    # -----------------------------
    # 1. Explicit "X years experience"
    # -----------------------------
    years_pattern = r'(\d+(?:\.\d+)?)\s+years?'
    years_matches = re.findall(years_pattern, text)

    explicit_years = max([float(y) for y in years_matches], default=0)

    # -----------------------------
    # 2. Numeric date ranges (MM/YYYY)
    # -----------------------------
    date_pattern_1 = r'(\d{1,2})/(\d{4})\s*-\s*(\d{1,2})/(\d{4})'
    matches1 = re.findall(date_pattern_1, text)

    months_total = 0

    for sm, sy, em, ey in matches1:
        sm, sy, em, ey = int(sm), int(sy), int(em), int(ey)

        if ey < sy:
            continue  # skip wrong data

        months = (ey - sy) * 12 + (em - sm)
        months_total += max(months, 0)

    # -----------------------------
    # 3. Text date ranges (Jan 2022 - Mar 2024)
    # -----------------------------
    month_map = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4,
        "may": 5, "jun": 6, "jul": 7, "aug": 8,
        "sep": 9, "oct": 10, "nov": 11, "dec": 12
    }

    date_pattern_2 = r'([a-z]{3,})\s+(\d{4})\s*-\s*([a-z]{3,})\s+(\d{4})'
    matches2 = re.findall(date_pattern_2, text)

    for sm, sy, em, ey in matches2:
        sm = month_map.get(sm[:3], 1)
        em = month_map.get(em[:3], 1)
        sy, ey = int(sy), int(ey)

        if ey < sy:
            continue

        months = (ey - sy) * 12 + (em - sm)
        months_total += max(months, 0)

    # -----------------------------
    # Final calculation
    # -----------------------------
    calculated_years = round(months_total / 12, 1)

    # -----------------------------
    # Final decision
    # -----------------------------
    if explicit_years > 0:
        return explicit_years

    return calculated_years