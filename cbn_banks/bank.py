from nigeria_banks.database.db import bankdb


def getBank(name=None, bank_code=None, cbn_code=None, ussd_code = None):
    data = bankdb()
    if name:
        for bank in data:
            if (bank["bank_short_name"]).lower() == name.lower():
                return bank
    elif bank_code:
        for bank in data:
            if bank["bank_code"] == bank_code:
                return bank
    elif cbn_code:
        for bank in data:
            if bank["cbn_code"] == cbn_code:
                return bank
    elif ussd_code:
        if "*" not in ussd_code or "#" not in ussd_code:
            return None
        for bank in data:
            if bank["ussd_code"] == ussd_code:
                return bank
    return None


def getBanks():
    """ Method to return all the banks in Nigeria. """
    return bankdb()






