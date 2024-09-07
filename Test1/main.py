def calculate_can_chi_calendar_1(year=int):
    match year % 10:
        case 0:
            can = "Canh"
        case 1:
            can = "Tân"
        case 2:
            can = "Nhâm"
        case 3:
            can = "Quý"
        case 4:
            can = "Giáp"
        case 5:
            can = "Ất"
        case 6:
            can = "Bính"
        case 7:
            can = "Đinh"
        case 8:
            can = "Mậu"
        case 9:
            can = "Kỷ"

    match year % 12:
        case 0:
            chi = "Thân"
        case 1:
            chi = "Dậu"
        case 2:
            chi = "Tuất"
        case 3:
            chi = "Hợi"
        case 4:
            chi = "Tí"
        case 5:
            chi = "Sửu"
        case 6:
            chi = "Dần"
        case 7:
            chi = "Mão"
        case 8:
            chi = "Thìn"
        case 9:
            chi = "Tị"
        case 10:
            chi = "Ngọ"
        case 11:
            chi = "Mùi"

    result = can + " " + chi
    return result


# Test case
print(calculate_can_chi_calendar_1(2024))
print(calculate_can_chi_calendar_1(2023))
print(calculate_can_chi_calendar_1(1977))
