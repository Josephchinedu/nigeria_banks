📦 nigeria_banks 
=======================

Nigeria Banks is a basic python package that returns details of particular bank in Nigeria.

## Installation

You can install nigeria_banks from [PyPI](https://pypi.org/project/nigeria_banks/):

    pip install nigeria_banks



## How to use

    $ from nigeria_banks import bank
    # get bank details using ussd_code
    get_bank = getBank(ussd_code="*945#")
    # result = {'bank_code': '000017', 'cbn_code': '035', 'name': 'Wema Bank', 'bank_short_name': 'wema', 'disabled_for_vnuban': 'None', 'ussd_code': '*945#'}

    # get bank details using bank_code
    get_bank = getBank(bank_code="000017")
    # result = {'bank_code': '000017', 'cbn_code': '035', 'name': 'Wema Bank', 'bank_short_name': 'wema', 'disabled_for_vnuban': 'None', 'ussd_code': '*945#'}

    # get bank details using cbn_code
    get_bank = getBank(cbn_code="035")
    # result =  {'bank_code': '000017', 'cbn_code': '035', 'name': 'Wema Bank', 'bank_short_name': 'wema', 'disabled_for_vnuban': 'None', 'ussd_code': '*945#'}

    # get bank details using name
    get_bank = getBank(name="wema")
    # result = {'bank_code': '000017', 'cbn_code': '035', 'name': 'Wema Bank', 'bank_short_name': 'wema', 'disabled_for_vnuban': 'None', 'ussd_code': '*945#'}

     

