import poslist1 as ps1
import poslist2 as ps2
import poslist3 as ps3
import poslist4 as ps4
import poslist5 as ps5
import poslist6 as ps6
import poslist7 as ps7
import poslist8 as ps8
import poslist9 as ps9
import poslist10 as ps10
import poslist11 as ps11
import poslist12 as ps12
import poslist13 as ps13

import poslist14 as ps14
import poslist15 as ps15

def drawlist():
	ps = ps1.drawlist()
	
	ps = ps + ps2.drawlist()

	ps = ps + ps3.drawlist() + ps4.drawlist() 

	ps = ps + ps5.drawlist() + ps6.drawlist() + ps7.drawlist() 

	ps = ps + ps8.drawlist() + ps9.drawlist() + ps10.drawlist()
	return ps

