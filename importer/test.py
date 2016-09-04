import sys, os, random
abs_path = os.path.abspath("../")
sys.path.append(abs_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "voterx_project.settings")
from django.conf import settings
from voterx_app.models import models

new_name_rec = models.Name()
new_r7l2_rec = models.R7L2Voter()


new_r7l2_rec.mseq = random.random()
new_r7l2_rec.save()

new_name_rec.mseq = 'fname-{}'.format(random.random())
new_name_rec.seq = 'mname-{}'.format(random.random())
new_name_rec.voters_lastname = 'lname-{}'.format(random.random())
new_name_rec.voters_namesuffix = 'suffix-{}'.format(random.random())
new_name_rec.r7l2_voter = new_r7l2_rec
new_name_rec.save()

rec = models.Name.objects.all()
if rec:
    print(rec[len(rec)-1].as_dict())
#print(rec)


#import ipdb; ipdb.set_trace()