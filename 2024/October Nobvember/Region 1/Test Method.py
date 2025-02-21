#This is nthe same original script modified for testing using the random module

import random #TEST
for _ in range(100): #testing it with 1000 posiible sets of data
    #Sample info
    MemberName = ['steve--1','steve-0','steve-1','steve-2','steve-3','steve-4','steve-5','steve-6','steve-7','steve-8','steve-9','steve-10','steve-11','steve-12','steve-13','steve-14','steve-15','steve-16','steve-17','steve-18','steve-19','steve-20','steve-21','steve-22','steve-23','steve-24','steve-25','steve-26','steve-27','steve-28','steve-29','steve-30','steve-31','steve-32','steve-33','steve-34','steve-35','steve-36','steve-37','steve-38','steve-39','steve-40','steve-41','steve-42','steve-43','steve-44','steve-45','steve-46','steve-47','steve-48','steve-49','steve-50','steve-51','steve-52','steve-53','steve-54','steve-55','steve-56','steve-57','steve-58','steve-59','steve-60','steve-61','steve-62','steve-63','steve-64','steve-65','steve-66','steve-67','steve-68','steve-69','steve-70','steve-71','steve-72','steve-73','steve-74','steve-75','steve-76','steve-77','steve-78','steve-79','steve-80','steve-81','steve-82','steve-83','steve-84','steve-85','steve-86','steve-87','steve-88','steve-89','steve-90','steve-91','steve-92','steve-93','steve-94','steve-95','steve-96','steve-97','steve-98','steve-99','steve-100','steve-101','steve-102','steve-103','steve-104','steve-105','steve-106','steve-107','steve-108','steve-109','steve-110','steve-111','steve-112','steve-113','steve-114','steve-115','steve-116','steve-117','steve-118','steve-119','steve-120','steve-121','steve-122','steve-123','steve-124','steve-125','steve-126','steve-127','steve-128','steve-129','steve-130','steve-131','steve-132','steve-133','steve-134','steve-135','steve-136','steve-137','steve-138','steve-139','steve-140','steve-141','steve-142','steve-143','steve-144','steve-145','steve-146','steve-147','steve-148','steve-149','steve-150','steve-151','steve-152','steve-153','steve-154','steve-155','steve-156','steve-157','steve-158','steve-159','steve-160','steve-161','steve-162','steve-163','steve-164','steve-165','steve-166','steve-167','steve-168','steve-169','steve-170','steve-171','steve-172','steve-173','steve-174','steve-175','steve-176','steve-177','steve-178','steve-179','steve-180','steve-181','steve-182','steve-183','steve-184','steve-185','steve-186','steve-187','steve-188','steve-189','steve-190','steve-191','steve-192','steve-193','steve-194','steve-195','steve-196','steve-197','steve-309']
    MemberTime = [0 for _ in range(200)]
    MemberCertificate = ["" for _ in range(200)]
    #Requirnment 1: - allows members’ times to be input twice and verifies that the inputs match
    for member in range(200):
        print(f"Hey {MemberName[member]}!")
        while True:
            r_gen_time = random.randint(10, 1000) #TEST
            print("Please input your time\n: - ") #Prompts for input of time first time, changed to print for testing
            Time = r_gen_time #TEST
            print("Please input your time again\n: - ") #Prompts again for confrimation, changed to print for testing
            Time_Confirm = r_gen_time #TEST
            #Validation block
            if Time == Time_Confirm: MemberTime[member] = Time;break
            else: print("Your times dont match, and you have to reenter it again (bummer!)")

    #Using bubblesort to swap the lists MemberName and MemberTime in accendinbg order of MemberTime
    while True:
        swap = False #Initialises swap to no swaps occured.
        for element in range(200-1):
            if MemberTime[element] > MemberTime[element+1]: #if the currunt element is larger then the next element
                #Swaps like this, if its num1, num2 = num2, num1, if num 1 is 1 and num 2 is 2, after swap, num 1 will be 2 and num 2 will be 1.
                MemberTime[element], MemberTime[element+1] = MemberTime[element+1], MemberTime[element]
                MemberName[element], MemberName[element+1] = MemberName[element+1], MemberName[element]
                swap = True #Setting swap to true, indicating a swap has occured
        if swap != True:
            break

    #top 3 members names are in index 0, 1 and 2.
    print(f"{MemberName[0]} got first place\n{MemberName[1]} got second place\n{MemberName[2]} got third place")

    #Identifies the number of certificates to be printed, and store the names of members who get certificates in MemberCertificate.
    no_certificates = 0
    for member in range(200):
        if MemberTime[member] < 240:
            MemberCertificate[no_certificates] = MemberName[member]
            no_certificates += 1

    #prints the number of certificates to be printed
    print(f"A total of {no_certificates} certificates need to be printed")
print("testing passed")