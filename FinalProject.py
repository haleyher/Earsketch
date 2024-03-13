# description: 
from earsketch import *

setTempo(110)
tracks = [1,2,3]
tracks2 = [4,5,6,7]

# User Input
bob = True
while bob== True:
    request = input("Would you like to hear hip hop or latin? (enter 'hip hop' or 'latin')")
    if request == "latin":
        i = 1
        while i <4:
            setEffect(i, VOLUME, GAIN, -60)
            i+=1
        bob = False

    elif request == "hip hop":
        i = 4
        while i <8:
            setEffect(i, VOLUME, GAIN, -60)
            i+=1
        bob = False
    else:
        print("The only genres available are hip hop and latin.")
print("Thanks for listening! :)")


## TRACK 1: DRUMS 
time = 1
counter = 0

while counter<8:
    makeBeat(RD_WORLD_PERCUSSION_DRUMPART_24, tracks[0],time, "0++-0++-0++++++++++++++-")
    counter += 1
    time +=1.5

### TRACK 2: PIANO

start = 1
end = 3
counter = 0
while counter < 3:
    fitMedia(YG_HIP_HOP_ELECTRIC_PIANO_1, tracks[1], start, end)
    start += 2
    end +=2
    counter += 1

makeBeatSlice(YG_GOSPEL_GUITAR_1, 2, 8, "0++++--0++++--0++++--0++++++++", [2.7,3.5])
makeBeat(YG_GOSPEL_GUITAR_1,2, 10, "0++++++++++")

fitMedia(YG_HIP_HOP_ELECTRIC_PIANO_1, 2, 11, 13)

# TRACK 3: hihat
def hihat(time):
    insertMedia(ENTREP_PERC_HIHAT,3,time)

counter = 1

while counter<12:
    hihat(counter)
    counter+= 2

## EFFECTS
# TRACK 1
start = 1
if request == "latin":
    vol1 = -60
    vol2 = -60
    vol3 = -60
else:
    vol1 = -30
    vol2 = 0
    vol3 = 5
setEffect(tracks[1], VOLUME, GAIN, vol1, start, vol2,2)
setEffect(tracks[0], VOLUME, GAIN, vol1, start, vol3,2)

# TRACK 2
start = 12
setEffect(tracks[1], VOLUME, GAIN, vol2, 12, vol1,13)
setEffect(tracks[0], VOLUME, GAIN, vol3, 12, vol1,13)


setEffect(2, PITCHSHIFT, PITCHSHIFT_SHIFT, -10)
setEffect(2, PITCHSHIFT, PITCHSHIFT_SHIFT, -10,7,-12,8)

# TRACK 3
time = 1
counter = 0
while counter <6:
    rhythmEffects(3, FILTER, FILTER_FREQ, [300, 3000, 1000], time, "0+++1+++2+++1+++")
    time += 2
    counter +=1

#SONG 2

beats = [HIPHOP_BASSSUB_007,HIPHOP_HITS_006,HIPHOP_STOMP_BEAT_PART_007,IRCA_SALSA_2_PIANO,IRCA_OS2_TIMBITA_SLAP]
newtracks = [4,5,6,7]
counter = 0
start = 1
while counter<3:
    beatB = "0+++0+++0+++0+++0+++++++++++++++"
    beatsA = makeBeat (beats[3], newtracks[2], start, beatB)
    counter+=1
    start+=2
fitMedia(beats[4], newtracks[3],3,7)
fitMedia(beats[0], newtracks[0], 1,7)
fitMedia(YG_NEW_HIP_HOP_CLAP_2,newtracks[1],1,3)




    
    
