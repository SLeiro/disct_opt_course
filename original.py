import pandas as pd
import os

myDir = os.getcwd()


def make_cc_transfers():
    """Loops through all relaunches and finds the latest one
    """

    # Load Relaunches in an array

    relaunches = pd.read_csv(os.path.join(myDir, 'input', 'SELECT_cc_viejo__cc_nuevo__fecha_lanz_de.csv'))
    actSkus = []
    dateInfoDic = {}
    # Circular References
    circ_ref = []
    # Loop through table
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
            if numNew > 1:
                raise ValueError("More than one new sku for an old one: " + oldSku)
            # Check if circular reference
            elif numLoops > 50:
                print oldSku
                circ_ref.append(oldSku)
                break
            # Set new date
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
    if len(circ_ref) > 0:
        raise ValueError("Circular references for: " + str(len(circ_ref)))
    # Insert into data frame
    relaunches['cc_actual'] = actSkus
    relaunches = relaunches.drop('desde', 1)
    # Insert into DB
    print(dateInfoDic)
    dateInfo = []
    for i, r in dateInfoDic.iteritems():
        dateInfo.append([i, r[0], r[1]])
    dateInfoDF = pd.DataFrame(data=dateInfo, columns=['cc', 'desde', 'hasta'])


if __name__ == '__main__':
    make_cc_transfers()
