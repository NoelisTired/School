

"""

Aan deze code hoeft je niet te doen, en niets te begrijpen!
Deze kleine "library" zorgt ervoor dat je op een makkelijke manier,
de resultaten vanuit pandas netjes kunt printen.

"""

import math, pandas as pd
#? Waarom werd datetime geimporteed? Dat heb ik niet nodig toch? We gebruiken hiervoor pandas toch?

#! Deze regel zorgt ervoor dat je geen waarschuwingen krijgt
#! als je een dataframe aanpast, eerste kreeg ik een SettingWithCopyWarning en deze regel zorgt ervoor dat die niet meer komt.
pd.options.mode.chained_assignment = None 
def prettify(dataframe, type="", columns=None):
    index = True
    if type == "zwartboek" or type == "eregalerij":
        columns = ["datum", "team1", "team2", "uitslag", "scheidsrechter"]
        if type == "zwartboek":
            columns.append("overtredingen")

        #! De datum wordt nu in de goede volgorde weergegeven, dayfirst heb ik toegevoegd omdat je anders een output error krijgt.
        #! die standaard word onderdrukt maar dit is netter.
        dataframe["datum"] = pd.to_datetime(dataframe["datum"], format="%d-%m-%Y", dayfirst=True)
        index = False
    return dataframe.to_string(columns=columns, index=index, na_rep="0", float_format=round_str)

def round_str(num):
    if(math.isnan(num)):
        return "0"
    else:
        return str(round(num))
