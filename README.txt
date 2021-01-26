===================================== PASAT-C =====================================
The task was created with PsychoPy and originally based on the PASAT-c created by Lejuez and colleagues. 

Original source:
Lejuez, C. W., Kahler, C. W., & Brown, R. A. (2003). A modified computer version of the Paced Auditory Serial Addition Task (PASAT) 
	as a laboratory-based stressor. The Behavior Therapist. 

The PASAT-C is the computerized version of the Paced Auditory Serial Addition Task. 
The main goal of this task is to increase stress levels, to measure information processing and to test the working memory. 

The main goal is to add up the last two digits that are mentioned by the computer. 
I.e.: Firstly, a 2 is mentioned, you click on number 2. Next, a 4 is mentioned, so you have to add up 2+4 (click number 6).
Afterward, number 5 is mentioned. Then you have to add up the last 2 digits (so 4+5). This means that you have to click on number 9. 
If then number 3 is mentiones, you have to add up 5 and 3. So click on number 8. 

There are two versions, namely the dutch (PASAT_NL) and the English (PASAT_EN). 

Some parameters that can be manipulated: 
- The amount of trials 				(EN: Trial_repeats, NL: Trial_herhalingen)
- The duration of one trial 				(EN: pres_duration, NL: duur)
- Whether you'd like to have each block going faster and faster (each block speeds up with 0.4 seconds)
- Turn the facial feedback on- and off 			(EN: enable_facial_feedback, NL: gezichtsfeedback_aanzetten)
- Which values are linked to the facial feedback 		(EN: perfect, good, okay, bad, NL: perfect, goed, mwa, slecht)
- With what value of facial feedback does a participant start* 	[ :D, :), :|, :( or >:( ]. 

*Note: fill in the corresponding number that you also filled in on the perfect,good, okay or bad criterions!



In the csv-file you'll get after doing the task contains several important columns: 

round_number (EN) or ronde_nummer (NL): 		which block are you in. Note: the first block (practice) starts at 0!
current_stim (EN) or huidige_stim (NL): 			which stimulus is in this trial presented.
valid_stim (EN) or juiste_waarde (NL): 			which was the correct value? 
reg_resp (EN) or geregistreerd_resp (NL): 			which number did you click. 
Score (EN and NL): 					was it correct (1) or incorrect (0)

Instruction_text.started (EN) or Instructie_tekst.started (NL): 	how long did it take to read the instructions in seconds. 
rest_text (EN) or pauze_tekst (NL): 			after how many seconds did you finish a trial block? 
globalClockTime (EN and NL): 				how long did it take to complete the whole experiment? 
