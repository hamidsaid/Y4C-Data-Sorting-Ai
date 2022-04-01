import csv

print('Start')
# Keywords that represent a particular category with a unique code
# Make sure maneno unayoweka hapa yanaappear zaidi katika context ya mafile yako
# If many caterogies, you can add in the data dictionary
# My files had health context so my list has only health categories, be sure to verify your category before using the script
# Make sure to change the name of the old file and new file each time you run the script for multiple files
# Make sure all the files are in the same directory as the script and execute from the terminal

data = {

    'A1': ['mzazi', 'MZazi', 'ujauzito', 'mimba', 'umeshajifungua', 'kujifungua', 'jifungua', 'mimba', 'mama',
           'mjamzito', 'mama na mtoto', 'ulijifungulia', 'MAMA', 'Mama'],
    'A2': ['corona', 'covid', 'covid-19', 'kifua', 'mafua makali'],
    'A3': ['chanjo', 'sindano'],
    'A4': ['mtoto', 'kuharisha', 'chanjo', 'kuhara', 'utapiamlo'],
    'A5': ['uzito', 'nyonya', 'nyonyesha', 'mtoto mchanga', 'maziwa', 'urefu', 'kipimo'],
    'A6': ['mtoto', 'kijana', 'uzazi', 'balehe', 'kubalehe', 'elimu ya uzazi', 'msichana', 'mvulana'],
    'A7': ['afya', 'kliniki', 'dawa', 'shinikizo la damu', 'damu', 'presha', 'kupima', 'kipimo'],
    'D1': ['huduma', 'ujumbe', 'kifua'],
    'D4': ['kusaidia', 'huduma', 'HUDUMA', 'ujumbe'],
    'A1': ['mzazi', 'mimba', 'kliniki', 'ujauzito', 'kituo cha afya', 'kujifungua', 'unyonyeshaji', 'mama', 'mjamzito',
           'mama na mtoto'],
    'A2': ['corona', 'covid', 'covid-19', 'kifua', 'mafua makali'],
    'A3': ['chanjo', 'sindano', 'sana'],
    'A4': ['mtoto', 'kuharisha', 'chanjo', 'kuhara', 'utapiamlo'],
    'A5': ['uzito', 'nyonya', 'nyonyesha', 'mtoto mchanga', 'maziwa', 'urefu', 'kipimo'],
    'A6': ['mtoto', 'kijana', 'uzazi', 'balehe', 'kubalehe', 'elimu ya uzazi', 'msichana', 'mvulana'],
    'A7': ['afya', 'kliniki', 'dawa', 'shinikizo la damu', 'damu', 'presha', 'kupima', 'kipimo'],
    'C2': ['ukimwi', 'vvu', 'maumbukizi'],
    'G2': ['usalama', 'raia', 'polisi', ],
    'D4': ['ureport'],
    'G6': ['kipato', 'ustawi', ],
    'A6': ['hedhi', 'mzunguko', 'uzazi', 'balehe', 'kubalehe', 'siku zao', 'uzazi', 'msichana', 'kitambaa', 'chupi',
           'siku', 'pedi', 'taulo', 'bakteria', 'ukeni', 'usafi', 'mimba'],
    'G3': ['mahusiano', 'mpenzi', 'uhusiano', 'kusalitiwa', 'kimapenzi', 'watu wawili', 'valentine', 'love', 'hisia',
           'mwenza', 'ajira', 'vijana', 'skauti', 'uwezeshaji', 'kuku', 'ngombe'],
    'G4': ['ukeketaji', 'mimba za utoton', 'damu', 'mila', 'vifo', 'kifo'],
    'D1': ['ureport', 'elimu', 'vijana', 'vipind', 'ushauri', 'mitandao', 'mtandao', 'taarifa', 'radio', 'tv',
           'redioni', 'elimu', 'tangazo', 'matangazo', 'ureport', 'u report', 'mashirika'],
    'D4': ['elimu', 'ndoa', 'majarida', 'midahalo', 'sauti', 'makund', 'semina', 'kuhimiza', 'simu', 'taasisi',
           'tasisi', 'kutembelea', 'maswali', 'swali', 'jibu', 'wilaya', 'mtaan', 'mwongozo'],
    'D2': ['matokeo', 'kujifunza', 'jifunza', 'mafunzo'],
    'D3': ['mikutano', 'mkutano', 'mtandao', 'kutembelea', 'mitandao', 'marafiki', 'rafiki', 'fb', 'face', 'ndugu',
           'jamaa', 'elimisha', 'kuelimisha']

}

polarity = {

    'P': ['je', 'Je','asante', 'tafadhali', 'jitahidi', 'wazo', 'mzima wa afya', 'afya', 'kuuliza','Habari yako','habari',
          'Asante', 'Habari', 'maoni', 'Karibu', 'Samahani','Nashukur','nashukuru','namshukur','namshukuru','asante','nashukulu','nzuri','zuri','mazuri','tafadhali','inaelimisha',
            'inahitajika','iliyoboreshwa','naendeelea vizuri','naendelea vizuli','salama','naendeleya','mwema', 'Naomba'],


    'N' : ['usenge', 'sitaki', 'sitakii','SITAKI','SI HITAJ','sihitaji','Mbona','mbn','sijakuelewa','samahani','ebu','mwatukera','nikera','unakera','sikupi','nimechoka','sipewi','mbn',
           'hamkunipa','hamniletei','nime shi ndwa mche zowenu','hamnip','fucken','usengecpendi','sipendi','spend'
            ,'sparms','kumamazao','pumbavu','pumbav','sitaki','stak','staki','xtaki','ctak','ctk','ctki','xtak','xtk'
           ]

}



# Open the file that has the particular data
with open('user7_Msgs_File_5.csv', newline='') as csv_file:
    file = csv.reader(csv_file, delimiter=',')
    # Loop through each row in the file
    for row in file:
        print('     ')
        print("Row before:")
        print(row)
        print('<<<<<<<*******************>>>>>>')
        ids = []
        polarities = []
        # Check if the keywords in the dictionaries appear in the messages
        for key, wordlist in data.items():
            for word in wordlist:
                if word in row[3] and key not in ids:
                    # Store the keys in a single list
                    ids.append(key)
        for key, wordlist in polarity.items():
            for wordd in wordlist:
                 if wordd in row[3] and key not in polarities:
                     # Store the keys in a single list
                     polarities.append(key)
                # Create a copy of the csv file that will store the filled version
        with open('user7_Msgs_File_5(sorted).csv', mode='a', newline='') as csvFileR:
            write = csv.writer(csvFileR, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for id in ids:
                if id not in row[1]:
                    # Append the list into the csv file
                    row[1] = ','.join(ids)
            for id in polarities:
                if id not in row[2]:
                    # Append the list into the csv file
                    row[2] = ','.join(polarities)
            write.writerow(row)
            print("Row After")
            print(row)
            print('     ')
            print('     ')
            print('Write Successful.')
    csv_file.flush()
    csv_file.close()


print('Finished.')
