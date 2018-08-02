import pandas as pd
import os
import datetime

myDir = os.getcwd()

def make_cc_transfers():
    """Loops through all relaunches deletes circulat references and finds the latest one
    """
    """Finds circular references and delete them."""
    #load relaunches
    relaunches = pd.read_csv(os.path.join(myDir, 'input','relanz_2018.03.19.csv'))
    # relaunches = pd.read_excel(os.path.join(myDir, 'input', '00. To-From Dictionary (3).xlsx'), sheetname=0)
    for i, r in relaunches.iterrows():
        # Save old and new sku
        oldSku = r['cc_viejo']
        newSku = r['cc_nuevo']
        # Get number of new skus
        numNew = len(relaunches[relaunches['cc_viejo'] == newSku])
        # Init list of relaunches chain
        relan_analized = []
        # While there is at least one
        while numNew > 0:
            # Check if more than one
            if numNew > 1:
                print(oldSku)
                raise ValueError("More than one new sku for an old one: " + oldSku)
            if newSku == oldSku:
                relaunches = relaunches[relaunches['cc_viejo'] != oldSku]
                q = ("DELETE FROM d01_relan_cc WHERE cc_viejo = '{cc_viejo}'".format(cc_viejo=oldSku))
                print(q)
                break
            # Set new sku
            # Check if circular reference
            if [oldSku, newSku] not in relan_analized:
                relan_analized.append([oldSku, newSku])
            else:
                break
            newSku = relaunches['cc_nuevo'][relaunches['cc_viejo'] == newSku].values[0]
            # Get number of new skus
            numNew = len(relaunches[relaunches['cc_viejo'] == newSku])
    # Init actual sku
    actSkus = []
    dateInfoDic = {}
    for i, r in relaunches.iterrows():
        # Save old and new sku
        oldSku = r['cc_viejo']
        newSku = r['cc_nuevo']
        to = r['desde']
        # Save old sku
        if oldSku in dateInfoDic.keys():
            dateInfoDic[oldSku] = [dateInfoDic[oldSku][0], to]
        else:
            dateInfoDic[oldSku] = [None, to]
        # Save new sku
        if newSku not in dateInfoDic.keys():
            dateInfoDic[newSku] = [to, None]
        # Get number of new skus
        numNew = len(relaunches[relaunches['cc_viejo'] == newSku])
        numLoops = 0
        # While there is at least one
        while numNew > 0:
            # Check if more than one
            if numLoops == 0:
                newDate = relaunches['desde'][relaunches['cc_viejo'] == newSku].values[0]
                dateInfoDic[newSku] = [to, newDate]
            # Set new sku
            newSku = relaunches['cc_nuevo'][relaunches['cc_viejo'] == newSku].values[0]
            # Get number of new skus
            numNew = len(relaunches[relaunches['cc_viejo'] == newSku])
            numLoops += 1
        # Update list of actuals
        actSkus.append(newSku)
        # print(dateInfoDic)
    # Insert into data frame
    relaunches['cc_actual'] = actSkus
    relaunches = relaunches.drop('desde', 1)
    relaunches.to_csv(os.path.join(myDir, 'output', 'relaunches.csv'), index=False)
     # Build dates data frame
    dateInfo = []
    for i, r in dateInfoDic.iteritems():
        dateInfo.append([i, r[0], r[1]])
    dateInfoDF = pd.DataFrame(data=dateInfo, columns=['cc', 'desde', 'hasta'])

    # Upload dates to DB

if __name__ == '__main__':
    make_cc_transfers()
