import graphlab
sf=graphlab.SFrame('/media/sf_ubuntu/ML/people-example.csv')


sf['Full Name'] = sf['First Name'] + ' ' + sf['Last Name']
print sf

