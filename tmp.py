model = \
"""
    mseq = models.FloatField(default=0)
    seq = models.FloatField(default=0)
    somedate = models.DateTimeField(default=datetime.utcnow())
    round = models.FloatField(default=0)
    caller_id = models.FloatField()
    time_stamp = models.DateTimeField(default=datetime.utcnow())
    poling_result = models.CharField(default='unk')
    sheet = models.CharField(default='unk')
    state = models.CharField(default='unk')
    lalvoterid = models.CharField(default='unk')
    lalid = models.CharField(default='unk')
    absenteetypes_description = models.CharField(default='unk')
    source = models.CharField(default='none')
"""
out = ''

def convert_to_dict_style(line):
    ret = ""
    #print(line)
    ele = line.split("=")
    ret = '"{}": self.{},'.format(ele[0].strip(), ele[0].strip(),)
    return ret

for line in model.splitlines():
    print(line)
    if line.strip():
        out += convert_to_dict_style(line) +'\n'

print('#'*30)

print(out)