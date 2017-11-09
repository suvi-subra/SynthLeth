### This module infers synthetic lethal gene pairs of a target organism Plasmodium falciparum ("pfal") from synthetic lethal gene pairs of Saccharomyces Cerevisiae ("scer").
### Input: 3 files - 	a) "BioSC.txt" - Synthetic lethal interaction data of Saccharomyces Cerevisiae
###						b) "orthologs.txt" - List of pairwise orthologs between Saccharomyces cerevisiae-Homo sapiens & Saccharomyces cerevisiae-Plasmodium falciparum & Homo sapiens-Plasmodium falciparum
###						c) "groups.txt" - Groups containing orthologs of Saccharomyces cerevisiae, Homo sapiens & Plasmodium falciparum
### Output: 1 file - 	"final_sl_pfal.txt"- List of inferred synthetic lethal gene pairs in target organism Plasmodium falciparum
###			3 intermediate files - "scer_pfal.txt", "scer_pfal_only.txt", "sph.txt" (needed for the module to run)			
### For questions contact: Suvitha Subramaniam (suvi.subra@gmail.com)

org="pfal"

column_idx = {
	'A_S1_ID':0,
	'B_PN':1,
	'C_PrAb':2,
	'D_P1_ID':3,
	'E_PN':4,
	'F_PrAb':5,
	'G_S1_Sym':6,
	'H_S1_Des':7,
	'I_PrAb':8,
	'J_PN':9,
	'K_S2_ID':10,
	'L_PN':11,
	'M_PrAb':12,
	'N_P2_ID':13,
	'O_PN':14,
	'P_PrAb':15,
	'Q_S2_Sym':16,
	'R_S2_Des':17,
	'S_PrAb':18,
	'T_PN':19
	}

target_columns = [
			('Systematic Name Interactor A','A_S1_ID'),
			('Official Symbol Interactor A','G_S1_Sym'),
			('Synonyms Interactor A','H_S1_Des'),
			('Systematic Name Interactor B','K_S2_ID'),
			('Official Symbol Interactor B','Q_S2_Sym'),
			('Synonyms Interactor B','R_S2_Des'),
		]

import time
def main():
	data = one()
	data = two()
	scer_data = get_scer_data(org)
	print("got scerdata")
	data = three(data,scer_data)
	print( len(data) )
	print("step3 complete")
	data = four(data,scer_data)
	print( len(data) )
	print("step4 complete")
	data = five(data)
	print("step5 complete")
	data = six(org,data)
	print("step6 complete")
	data = seven(data)
	print("step7 complete")
	data = eight(data)
	print("step8 complete", len(data))

	data = nine(data)
	print("step9 complete", len(data))

	data = ten(data)
	print("step10 complete", len(data))

	with open("sph.txt") as file:
		sph_lines = file.readlines()
	print("sph read", len(sph_lines))

	data = eleven(data, sph_lines, column_idx['A_S1_ID'], column_idx['B_PN'])
	print("step11 complete", len(data))

	data = eleven(data, sph_lines, column_idx['K_S2_ID'], column_idx['L_PN'])
	print("step12 complete", len(data))
	data = eleven(data, sph_lines, column_idx['D_P1_ID'], column_idx['E_PN'])
	print("step13 complete", len(data))
	data = eleven(data, sph_lines, column_idx['N_P2_ID'], column_idx['O_PN'])
	print("step14 complete", len(data))
	data = fifteen(data, column_idx['B_PN'],  column_idx['E_PN'], column_idx['J_PN'])
	print("step15 complete", len(data))
	data = fifteen(data, column_idx['L_PN'], column_idx['O_PN'], column_idx['T_PN'] )
	print("step16 complete", len(data))
	seventeen(org,data)
	print("step17 complete")



def get_scer_data(org):
	scer_data = []
	for line in open ("scer_"+org+".txt"):
		col=line.split('\t')
		x=col[1].replace('scer|scer_s288c__','')
		y=col[0].replace(org+'|','')
		scer_data.append([x,y])
	return scer_data


def one():#To create 3 intermediate files for retrieval of yeast orthologs in P.falciparum
	sp=[] 
	sh=[] 
	ph=[] 
	cnt_sp=0 
	cnt_sh=0 
	cnt_ph=0 
	x='' 
	y='' 
	sph=[]
	cnt=0
	cnt1=0
	with open('orthologs.txt') as file:
		for line in file:
			if line.find("scer") !=-1 and line.find(org) !=-1: #Finds orthologs between S.cerevisiae and target organism.
				sp.append(line) 
				cnt_sp=cnt_sp+1 #Can be printed for number of orthologs to be known.
			if line.find("scer") !=-1 and line.find("hsap") !=-1:#Finds orthologs between S.cerevisiae and H.sapiens.
				sh.append(line) 
				cnt_sh=cnt_sh+1 #Can be printed for no.of orthologs to be known.
			if line.find(org) !=-1 and line.find("hsap") !=-1: #Finds orthologs between target organism and H.sapiens.
				ph.append(line) 
				cnt_ph=cnt_ph+1 #Can be printed for no.of orthologs to be known.
	print("No.of orthologs between S.cer & "+org+" =")
	print(len(sp)) 
	output=open("scer_"+org+".txt","w")
	for item in sp:
		output.write(item)
	output.close()
	while (cnt<9): #Repeats loop 10 times to avoid bug in python.
		for item in sh:
			col=item.split() 
			x=col[1] #If alphabet of target organism <H then x=col[0], otherwise x=col[1].
			for item in sp:
				if item.find(x)!=-1: 
					sp.remove(item) #If ortholog of S.cerevisiae with H.Sapiens is present in array sp, line containing this pair is removed.
		cnt = cnt+1
	while (cnt1<9):
		for item in ph:
			col=item.split()
			y=col[1] #If alphabet of target organism <H then y=col[0], otherwise y=col[1].
			for item in sp:
				if item.find(y)!=-1: 
					sp.remove(item) #If ortholog of target organisms with H.sapiens is present in array sp,line containing this pair is removed.
		cnt1 = cnt1+1
	print("No.of orthologs between S.cer & "+org+" ONLY(excluding those in H.sap)=")
	print(len(sp)) 
	output=open("scer_"+org+"_only.txt","w")
	for item in sp:
		output.write(item)
	output.close()
	with open('groups.txt') as file:
		for line in file:
			if line.find("scer") !=-1 and line.find(org) !=-1 and line.find("hsap") !=-1: #Finds clusters containing orthologs in S.cerevisiae, target organism and H.sap.
				sph.append(line) 
	print("No.of clusters with S.cer, "+org+" & H.sap =")
	print(len(sph)) 
	output=open("sph.txt","w")
	for item in sph:
		output.write(item)
	output.close()
	
def two():#To retrieve yeast synthetic lethal gene pairs from input file 1 "BioSC.txt"
		
	organism_data = []

	with open ('BioSC.txt') as file:
		lines = file.readlines()
		headings = lines[0].split('\t')
		column_index = { }

		for col in target_columns:
			column_index[col[0]] = headings.index(col[0])


		for line in lines:
			if line.find("Synthetic Lethality")==-1:
				continue
			
			items=line.split('\t')
			#Finds gene pairs with synthetic lethal interaction

			row = [None] * 20
			for column in target_columns:
				row[ column_idx[column[1]] ] = items[column_index[column[0]]].strip()

			organism_data.append( row )

	return organism_data

#To find orthologs of yeast in target organism
def three(organism_data,scer_data):

	filtered_data = []

	for line in organism_data:
		for item in scer_data:
			if line[ column_idx['A_S1_ID'] ]==item[0]:
				tmp = line[:]
				tmp[ column_idx['D_P1_ID'] ] = item[1]
				filtered_data.append(tmp)

	return filtered_data


#To find orthologs of yeast in target organism
def four(organism_data,scer_data):

	filtered_data = []

	for line in organism_data:
		for item in scer_data:
			if line[ column_idx['K_S2_ID'] ]==item[0]:
				tmp = line[:]
				tmp[ column_idx['N_P2_ID'] ] = item[1]
				filtered_data.append(tmp)
	
	return filtered_data
	
	
def five(organism_data):#To label the presence/absence of yeast orthologs in H.sap
	sp=[]
	for line in open("scer_"+org+"_only.txt"):
		col=line.split()
		x=col[1].replace('scer|scer_s288c__','')
		sp.append(x)

	for line in organism_data:
		cnt=0
		cnt1=0
		for item in sp:
			if item==line[ column_idx['A_S1_ID'] ]:
				cnt=1
			if line[ column_idx['K_S2_ID'] ].find(item)!=-1:
				cnt1=1
		if cnt==0 and cnt1==0:
			line[ column_idx['C_PrAb'] ] = 'present'
			line[ column_idx['M_PrAb'] ] = 'present'
		elif cnt==0 and cnt1==1:
			line[ column_idx['C_PrAb'] ] = 'present'
			line[ column_idx['M_PrAb'] ] = 'absent'
		elif cnt==1 and cnt1==0:
			line[ column_idx['C_PrAb'] ] = 'absent'
			line[ column_idx['M_PrAb'] ] = 'present'
		elif cnt==1 and cnt1==1:
			line[ column_idx['C_PrAb'] ] = 'absent'
			line[ column_idx['M_PrAb'] ] = 'absent'


	return organism_data
	
	
def six(org, organism_data): #To label the presence/absence of target organism orthologs in H.sap

	sp=[]
	for line in open("scer_"+org+"_only.txt"):
		col=line.split()
		x=col[0].replace(org+'|','')
		sp.append(x)


	for line in organism_data:
		cnt=0
		cnt1=0
		for item in sp:
			if item==line[ column_idx['D_P1_ID'] ]:
				cnt=1
			if line[ column_idx['N_P2_ID'] ].find(item)!=-1:
				cnt1=1
		if cnt==0 and cnt1==0:
			line[ column_idx['F_PrAb'] ] = 'present'
			line[ column_idx['P_PrAb'] ] = 'present'
		elif cnt==0 and cnt1==1:
			line[ column_idx['F_PrAb'] ] = 'present'
			line[ column_idx['P_PrAb'] ] = 'absent'
		elif cnt==1 and cnt1==0:
			line[ column_idx['F_PrAb'] ] = 'absent'
			line[ column_idx['P_PrAb'] ] = 'present'
		elif cnt==1 and cnt1==1:
			line[ column_idx['F_PrAb'] ] = 'absent'
			line[ column_idx['P_PrAb'] ] = 'absent'
	


	return organism_data


def seven(organism_data):#To label overall presence/absence of orthologs in H.sap for each unit 1 of SL pairs

	for line in organism_data:
		
		if line[ column_idx['C_PrAb'] ]=="present" and line[ column_idx['F_PrAb'] ]=="present":
			line[ column_idx['I_PrAb'] ] = "present"
		elif line[ column_idx['C_PrAb'] ]=="absent" and line[ column_idx['F_PrAb'] ]=="present":
			line[ column_idx['I_PrAb'] ] = "present"
		elif line[ column_idx['C_PrAb'] ]=="present" and line[ column_idx['F_PrAb'] ]=="absent":
			line[ column_idx['I_PrAb'] ] = "present"
		elif line[ column_idx['C_PrAb'] ]=="absent" and line[ column_idx['F_PrAb'] ]=="absent":
			line[ column_idx['I_PrAb'] ] = "absent"

	return organism_data
	

	
def eight(organism_data):#To label overall presence/absence of orthologs in H.sap for each unit 2 of SL pairs

	for line in organism_data:
		
		if line[ column_idx['M_PrAb'] ]=="present" and line[ column_idx['P_PrAb'] ]=="present":
			line[ column_idx['S_PrAb'] ] = "present"
		elif line[ column_idx['M_PrAb'] ]=="absent" and line[ column_idx['P_PrAb'] ]=="present":
			line[ column_idx['S_PrAb'] ] = "present"
		elif line[ column_idx['M_PrAb'] ]=="present" and line[ column_idx['P_PrAb'] ]=="absent":
			line[ column_idx['S_PrAb'] ] = "present"
		elif line[ column_idx['M_PrAb'] ]=="absent" and line[ column_idx['P_PrAb'] ]=="absent":
			line[ column_idx['S_PrAb'] ] = "absent"

	return organism_data

	
def nine(organism_data):#To decide on which pairs to accept or reject based on presence/absence of orthologs in H.sap in both units

	filtered_data = []
	for line in organism_data:
		if line[ column_idx['I_PrAb'] ]=="absent" and line[ column_idx['S_PrAb'] ]=="present":
			filtered_data.append( line )

		if line[ column_idx['I_PrAb'] ]=="present" and line[ column_idx['S_PrAb'] ]=="absent":
			filtered_data.append( line )

		if line[ column_idx['I_PrAb'] ]=="absent" and line[ column_idx['S_PrAb'] ]=="absent":
			filtered_data.append( line )

	return filtered_data
	
	

def ten(organism_data):#To remove duplicates and reciprocal duplicates

	filtered_data = []
	for line in organism_data:
		if line not in filtered_data and line[10:] + line[:10] not in filtered_data:
			filtered_data.append(line[:])	

	return filtered_data
	
	
def eleven(organism_data, sph_lines, find_col, label_col ):#To label the presence/absence of S.cerevisiae orthologs in clusters containing H.sap orthologs for unit 1
	
	filtered_data = []
	check = 0

	for line in organism_data:

		check=0

		for sph_line in sph_lines:
			if sph_line.find(line[ find_col ])!=-1:
				line[ label_col ] = "P"
				filtered_data.append( line )
				check=1
		if check==0:
			line[ label_col ] = "N"
			filtered_data.append( line )
		

	return filtered_data
	


	

	
def fifteen(organism_data, col1, col2, col3):#To label the overall presence/absence of orthologs in clusters containing H.sap orthologs for unit 1
	filtered_data = []
	for line in organism_data:

		if line[ col1 ]=="P" and line[ col2 ]=="P":
			line[ col3 ] = "P"
			filtered_data.append( line )

		if line[ col1 ]=="N" and line[ col2 ]=="P":
			line[ col3 ] = "P"
			filtered_data.append( line )

		if line[ col1 ]=="P" and line[ col2 ]=="N":
			line[ col3 ] = "P"
			filtered_data.append( line )

		if line[ col1 ]=="N" and line[ col2 ]=="N":
			line[ col3 ] = "N"
			filtered_data.append( line )

	return filtered_data


	
def seventeen(org, organism_data):#To decide on which pairs to accept or reject based on presence/absence of orthologs in clusters containing H.sap orthologs for both units

	total = 0
	output=open("Final_sl_"+org+".txt","w")
	for line in organism_data:
		if line[ column_idx['J_PN'] ]=="N" and line[ column_idx['T_PN'] ]=="P":
			write_line(output, line)
			total+=1

		if line[ column_idx['J_PN'] ]=="P" and line[ column_idx['T_PN'] ]=="N":
			write_line(output, line)
			total+=1

		if line[ column_idx['J_PN'] ]=="N" and line[ column_idx['T_PN'] ]=="N":
			write_line(output, line)
			total+=1

	print("No.of inferred synthetic lethal gene pairs = ",total)

def write_line(output, line):
	for col in line:
		output.write('{}\t'.format(col))
	output.write('\n')

if __name__ == '__main__':
    main()
	
