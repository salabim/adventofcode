from pathlib import Path

filename = Path('../../../../.config/aocd/token')

# for iPad
# put here the token for this year

token = '53616c7465645f5f87f3fbfc61260480eb42d40f9eaef34c4081beebecf5b0566556c952d400612027117769ab3c30794eb7e252a97ebc1bc09c5afe6d8aa952'
    
with open(filename,'w') as f:
    f.write(token)
    
print('done')
