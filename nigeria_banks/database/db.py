def bankdb():
    data = [
        {
            "bank_code":"000014",
            "cbn_code":"044",
            "name":"Access Bank Nigeria",
            "bank_short_name":"access",
            "ussd_code":"*901#"
        },
        {
            "bank_code":"090001",
            "cbn_code":"401",
            "name":"Aso Savings And Loans",
            "bank_short_name":"aso-savings",
            "ussd_code":""
        },
        {
            "bank_code":"090154",
            "cbn_code":"50823",
            "name":"CEMCS MFB",
            "bank_short_name":"cemcs",
            "ussd_code":""
        },
        {
            "bank_code":"000009",
            "cbn_code":"023",
            "name":"Citibank Nigeria",
            "bank_short_name":"citibankng",
            "ussd_code":""
        },
        {
            "bank_code":"000010",
            "cbn_code":"050",
            "name":"Ecobank Bank",
            "bank_short_name":"ecobank",
            "ussd_code":"*326#"
        },
        {
            "bank_code":"090097",
            "cbn_code":"562",
            "name":"Ekondo MFB",
            "bank_short_name":"ekondo",
            "ussd_code":"*540*178#"
        },
        {
            "bank_code":"000007",
            "cbn_code":"070",
            "name":"Fidelity Bank",
            "bank_short_name":"fidelity",
            "ussd_code":"*770#"
        },
        {
            "bank_code":"000016",
            "cbn_code":"011",
            "name":"First Bank of Nigeria",
            "bank_short_name":"firstbank",
            "ussd_code":"*894#"
        },
        {
            "bank_code":"000003",
            "cbn_code":"214",
            "name":"First City Monument Bank",
            "bank_short_name":"fcmb",
            "ussd_code":"*329#"
        },
        {
            "bank_code":"000013",
            "cbn_code":"058",
            "name":"Guaranty Trust Bank",
            "bank_short_name":"gtb",
            "ussd_code":"*737#"
        },
        {
            "bank_code":"090121",
            "cbn_code":"50383",
            "name":"Hasal MFB",
            "bank_short_name":"mfb",
            "ussd_code":"*322*127#"
        },
        {
            "bank_code":"000020",
            "cbn_code":"030",
            "name":"Heritage Bank",
            "bank_short_name":"heritage",
            "ussd_code":"*322#"
        },
        {
            "bank_code":"000006",
            "cbn_code":"301",
            "name":"Jaiz Bank",
            "bank_short_name":"jaiz",
            "ussd_code":"*389*301#"
        },
        {
            "bank_code":"000002",
            "cbn_code":"082",
            "name":"Keystone Bank",
            "bank_short_name":"keystone",
            "ussd_code":"*7111#"
        },
        {
            "bank_code":"090267",
            "cbn_code":"50211",
            "name":"Kuda MFB",
            "bank_short_name":"kuda",
            "ussd_code":""
        },
        {
            "bank_code":"100026",
            "cbn_code":"565",
            "name":"One Finance",
            "bank_short_name":"one-finace",
            "ussd_code":"*1303#"
        },
        {
            "bank_code":"090004",
            "cbn_code":"526",
            "name":"Parallex MFB",
            "bank_short_name":"parallex",
            "ussd_code":"*322*318*0#"
        },
        {
            "bank_code":"000008",
            "cbn_code":"076",
            "name":"Polaris Bank",
            "bank_short_name":"PBL",
            "ussd_code":"*833#"
        },
        {
            "bank_code":"000023",
            "cbn_code":"101",
            "name":"Providus Bank",
            "bank_short_name":"providus",
            "ussd_code":""
        },
        {
            "bank_code":"090175",
            "cbn_code":"125",
            "name":"Rubies MFB",
            "bank_short_name":"RMB",
            "ussd_code":"*7797#"
        },
        {
            "bank_code":"090325",
            "cbn_code":"51310",
            "name":"Sparkle Bank",
            "bank_short_name":"SPKL",
            "ussd_code":""
        },
        {
            "bank_code":"000012",
            "cbn_code":"221",
            "name":"Stanbic IBTC",
            "bank_short_name":"stanbic",
            "ussd_code":"*909#"
        },
        {
            "bank_code":"000021",
            "cbn_code":"068",
            "name":"Standard Chartered Bank",
            "bank_short_name":"standard-chartered",
            "ussd_code":""
        },
        {
            "bank_code":"000001",
            "cbn_code":"232",
            "name":"Sterling Bank",
            "bank_short_name":"sterling",
            "ussd_code":"*822#"
        },
        {
            "bank_code":"000022",
            "cbn_code":"100",
            "name":"Suntrust Bank",
            "bank_short_name":"suntrust",
            "ussd_code":"*5230#"
        },
        {
            "bank_code":"000026",
            "cbn_code":"302",
            "name":"Taj Bank",
            "bank_short_name":"taj-bank",
            "ussd_code":"*898#"
        },
        {
            "bank_code":"090115",
            "cbn_code":"51211",
            "name":"TCF MFB",
            "bank_short_name":"tcf-bank",
            "ussd_code":"*908#"
        },
        {
            "bank_code":"000025",
            "cbn_code":"102",
            "name":"Titan Trust Bank",
            "bank_short_name":"titan-trust",
            "ussd_code":"*922#"
        },
        {
            "bank_code":"000018",
            "cbn_code":"032",
            "name":"Union Bank of Nigeria",
            "bank_short_name":"unionbank",
            "ussd_code":"*826#"
        },
        {
            "bank_code":"000004",
            "cbn_code":"033",
            "name":"United Bank for Africa",
            "bank_short_name":"uba",
            "ussd_code":"*919#"
        },
        {
            "bank_code":"000011",
            "cbn_code":"215",
            "name":"Unity Bank",
            "bank_short_name":"unity-bank",
            "ussd_code":"*7799#"
        },
        {
            "bank_code":"090110",
            "cbn_code":"566",
            "name":"VFD MFB",
            "bank_short_name":"vfd",
            "ussd_code":""
        },
        {
            "bank_code":"000017",
            "cbn_code":"035",
            "name":"Wema Bank",
            "bank_short_name":"wema",
            "ussd_code":"*945#"
        },
        {
            "bank_code":"000015",
            "cbn_code":"057",
            "name":"Zenith Bank",
            "bank_short_name":"zenith",
            "ussd_code":"*966#"
        }
    ]

    return data