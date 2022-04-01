import pandas as pd

data = {
    'A1': ['ujauzito', 'mimba', 'umeshajifungua', 'ulijifungulia', 'kujifungua', 'wajawazito', 'jifungua', 'mimba',
           'mjamzito', 'mama','mtoto'],
    'A2': ['corona', 'covid', 'covid-19', 'kifua', 'mafua','makali'],
    'A3': ['chanjo', 'sindano'],
    'A4': ['mtoto', 'kuharisha', 'kuhara', 'utapiamlo'],
    'A5': ['uzito', 'nyonya', 'nyonyesha', 'mtoto','mchanga', 'maziwa', 'urefu', 'kipimo'],
    'A6': ['kijana', 'uzazi', 'balehe', 'kubalehe', 'uzazi', 'msichana', 'mvulana'],
    'A7': ['afya', 'kliniki', 'dawa', 'shinikizo la damu', 'damu', 'presha', 'kipimo', 'chumba', 'kituo',
           'huduma za afya'],
    'B1': ['udumavu'],
    'C3': ['ukimwi']
}
data2 = {
    'A1': {'A11':['ujauzito', 'mimba', 'umeshajifungua', 'ulijifungulia', 'kujifungua', 'wajawazito', 'jifungua', 'mimba',
           'mjamzito', 'mama','mtoto'],
           'A12': ['kitandani'],
           'A13': ['tetenasi', 'kutu',],
           'A14': ['sera','sheria'],
           'A15': []},
    'A2': {
        'A21': ['dalili za covid', 'kukohoa','mafua','makali'],
        'A22': ['tiba','covid'],
        'A23': ['chanjo', 'covax'],
        'A24': ['kinga za covid', 'barakoa', 'covid', 'epuka mikusanyiko'],
        'A25': ['ujumbe','corona', 'covid', 'covid-19']},
    'A3': {
        'A31': ['chanjo'],
        'A32': [],
        'A33': ['Kuhara, kipindupindu'],
        'A34': ['Homa ya manjano'],
        'A35': ['uti wa mgongo'],
        'A36': ['surua'],
        'A37': ['polio'],
        'A38': [],
        'A39': ['sindano']},
    'A4': {
        'A41': [],
        'A42': [],
        'A43': [],
        'A44': ['kuhara','kuharisha'],
        'A45': [],
        'A46': [],
        'A47': [],
        'A48': [],
        'A49': [],
        'A410': ['utapiamlo','mtoto']},
    'A5': {
        'A51': ['wafanyakazi','kazi'],
        'A52': ['uzito','mchanga','urefu','kipimo'],
        'A53': [],
        'A54': ['maziwa','nyonyesha','nyonya','ujauzito'],
        'A55': [],
        'A56': ['mtoto']},
    'A6': {
        'A61': ['uzazi'],
        'A62': ['kubalehe','balehe','msichana','mvulana'],
        'A63': ['akili'],
        'A64': [],
        'A65': ['kijana'], },
    'A7': {'A71': ['afya', 'kliniki', 'dawa', 'shinikizo la damu', 'damu', 'presha', 'kipimo', 'chumba', 'kituo',
                   'huduma za afya']},

    'D1': {
        'D11': ['elimu'],
        'D12': ['kubalehe', 'balehe', 'msichana', 'mvulana'],
        'D14': ['vijana'],
        'D15': ['kijana'], },

    'D2': {
        'D24' : ['tangazo', 'matangazo', 'ureport',],
        'D26' : ['tv', 'radio', 'ureport','simu']
    },

    'D4': {
        'D41' : ['ujumbe', 'huduma']
    },
    'D6': {
        'D61' : ['kipato', 'ustawi']
    },
    'C2': {
        'C14' : ['ujumbe', 'huduma']
    }
}

data3 ={'P':['Nashukur','nashukuru','namshukur','namshukuru','asante','nashukulu','nzuri',
            'zuri','mazuri','tafadhali','inaelimisha','inahitajika','iliyoboreshwa','naendeelea','vizuri',
            'naendelea','vizuli','salama','naendeleya','mwema','hongera','je', 'Je','asante', 'tafadhali', 'jitahidi', 'wazo', 'mzima wa afya', 'afya', 'kuuliza','Habari yako','habari',
          'Asante', 'Habari', 'maoni', 'Karibu', 'Samahani','Nashukur','nashukuru','namshukur','namshukuru','asante','nashukulu','nzuri','zuri','mazuri','tafadhali','inaelimisha',
            'inahitajika','iliyoboreshwa','naendeelea vizuri','naendelea vizuli','salama','naendeleya','mwema', 'Naomba'],
       'N':['Mbona','mbn','sijakuelewa','samahani','ebu','mwatukera','nikera','unakera','sikupi','nimechoka','sipewi','mbn',
            'hamkunipa','hamniletei','hamnip','fucken','usenge','cpendi','sipendi','spend','sparms','kumamazao','pumbavu','pumbav',
            'sitaki','stak','staki','xtaki','ctak','ctk','ctki','xtak','xtk','usenge', 'sitaki', 'sitakii','SITAKI','SI HITAJ','sihitaji','Mbona','mbn','sijakuelewa','samahani','ebu','mwatukera','nikera','unakera','sikupi','nimechoka','sipewi','mbn',
           'hamkunipa','hamniletei','nime shi ndwa mche zowenu','hamnip','fucken','usengecpendi','sipendi','spend'
            ,'sparms','kumamazao','pumbavu','pumbav','sitaki','stak','staki','xtaki','ctak','ctk','ctki','xtak','xtk'],
       'O':[]}

#Change name of file here
file = pd.read_csv('user7_Msgs_File_4.csv')
Polarity={}
Topic_code ={}
TopicId = {}
for i in range(len(file.index)):
    Polarity[i]=''

for i in range(0, len(file.index)):
    # TOPIC ID
    TopicId = file['Topic_id']
    TopicId = str(TopicId[i])
    TopicId = TopicId.split(',')
    # text
    Text = file['Text'].iloc[i]
    for ch in ['.', '?', ',', '/']:
        Text = Text.replace(ch, '')
    Text = Text.split(' ')

    #polarity
    for word in Text:
        for key, wordlist in data3.items():
            if word.lower() in wordlist:
                Polarity[i] = key


    #topic code
    for Id in TopicId:
        for superkey, Id_Text in data2.items():
            if Id == superkey:
                for word in Text:
                    for code in Id_Text:
                        wordlist = data2[superkey][code]
                        if word.lower() in wordlist:
                           Topic_code[i]=code
                    for code in Id_Text:
                        wordlist = data2[superkey][code]
                        if word.lower() in wordlist:
                            if code not in Topic_code[i]:
                                Topic_code[i] = Topic_code[i] + ',' + code
                    for code in Id_Text:
                        wordlist = data2[superkey][code]
                        if word.lower() in wordlist:
                            if code not in Topic_code[i]:
                                Topic_code[i] = Topic_code[i] + ',' + code
                    for code in Id_Text:
                        wordlist = data2[superkey][code]
                        if word.lower() in wordlist:
                            if code not in Topic_code[i]:
                                Topic_code[i] = Topic_code[i] + ',' + code
    for Id in TopicId:
        for superkey, Id_Text in data2.items():
            if Id == superkey:
                for word in Text:
                    for code in Id_Text:
                        wordlist = data2[superkey][code]
                        if word.lower() in wordlist:
                            if code not in Topic_code[i]:
                               Topic_code[i] = Topic_code[i]+','+code
                    for code in Id_Text:
                        wordlist = data2[superkey][code]
                        if word.lower() in wordlist:
                            if code not in Topic_code[i]:
                                Topic_code[i] = Topic_code[i] + ',' + code
                    for code in Id_Text:
                        wordlist = data2[superkey][code]
                        if word.lower() in wordlist:
                            if code not in Topic_code[i]:
                                Topic_code[i] = Topic_code[i] + ',' + code
                    for code in Id_Text:
                        wordlist = data2[superkey][code]
                        if word.lower() in wordlist:
                            if code not in Topic_code[i]:
                                Topic_code[i] = Topic_code[i] + ',' + code

for i in range(len(file.index)):
    Polarity[i]=Polarity[i]+''
    if len(Polarity[i]) == 0:
        print(len(Polarity[i]))
        Polarity[i]='O'


output = pd.DataFrame({'Topic_id': file['Topic_id'], 'Topic_code': Topic_code,'Polariy':Polarity, 'Text': file.Text})

# print(Topic_id)

# output=pd.DataFrame({'Topic_id':Topic_id,'Text':file.Text})

#Enter name of output file here
output.to_csv('user7_Msgs_File_4(sorted).csv', index=False)

