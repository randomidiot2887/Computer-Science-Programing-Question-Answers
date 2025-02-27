
PickerName = ['Steve-0', 'Steve-1', 'Steve-2', 'Steve-3', 'Steve-4', 'Steve-5', 'Steve-6', 'Steve-7', 'Steve-8', 'Steve-9', 'Steve-10', 'Steve-11', 'Steve-12', 'Steve-13', 'Steve-14', 'Steve-15', 'Steve-16', 'Steve-17', 'Steve-18', 'Steve-19', 'Steve-20', 'Steve-21', 'Steve-22', 'Steve-23', 'Steve-24', 'Steve-25', 'Steve-26', 'Steve-27', 'Steve-28', 'Steve-29', 'Steve-30', 'Steve-31', 'Steve-32', 'Steve-33', 'Steve-34', 'Steve-35', 'Steve-36', 'Steve-37', 'Steve-38', 'Steve-39', 'Steve-40', 'Steve-41', 'Steve-42', 'Steve-43', 'Steve-44', 'Steve-45', 'Steve-46', 'Steve-47', 'Steve-48', 'Steve-49', 'Steve-50', 'Steve-51', 'Steve-52', 'Steve-53', 'Steve-54', 'Steve-55', 'Steve-56', 'Steve-57', 'Steve-58', 'Steve-59', 'Steve-60', 'Steve-61', 'Steve-62', 'Steve-63', 'Steve-64', 'Steve-65', 'Steve-66', 'Steve-67', 'Steve-68', 'Steve-69', 'Steve-70', 'Steve-71', 'Steve-72', 'Steve-73', 'Steve-74', 'Steve-75', 'Steve-76', 'Steve-77', 'Steve-78', 'Steve-79', 'Steve-80', 'Steve-81', 'Steve-82', 'Steve-83', 'Steve-84', 'Steve-85', 'Steve-86', 'Steve-87', 'Steve-88', 'Steve-89', 'Steve-90', 'Steve-91', 'Steve-92', 'Steve-93', 'Steve-94', 'Steve-95', 'Steve-96', 'Steve-97', 'Steve-98', 'Steve-99', 'Steve-100', 'Steve-101', 'Steve-102', 'Steve-103', 'Steve-104', 'Steve-105', 'Steve-106', 'Steve-107', 'Steve-108', 'Steve-109', 'Steve-110', 'Steve-111', 'Steve-112', 'Steve-113', 'Steve-114', 'Steve-115', 'Steve-116', 'Steve-117', 'Steve-118', 'Steve-119', 'Steve-120', 'Steve-121', 'Steve-122', 'Steve-123', 'Steve-124', 'Steve-125', 'Steve-126', 'Steve-127', 'Steve-128', 'Steve-129', 'Steve-130', 'Steve-131', 'Steve-132', 'Steve-133', 'Steve-134', 'Steve-135', 'Steve-136', 'Steve-137', 'Steve-138', 'Steve-139', 'Steve-140', 'Steve-141', 'Steve-142', 'Steve-143', 'Steve-144', 'Steve-145', 'Steve-146', 'Steve-147', 'Steve-148', 'Steve-149', 'Steve-150', 'Steve-151', 'Steve-152', 'Steve-153', 'Steve-154', 'Steve-155', 'Steve-156', 'Steve-157', 'Steve-158', 'Steve-159', 'Steve-160', 'Steve-161', 'Steve-162', 'Steve-163', 'Steve-164', 'Steve-165', 'Steve-166', 'Steve-167', 'Steve-168', 'Steve-169', 'Steve-170', 'Steve-171', 'Steve-172', 'Steve-173', 'Steve-174', 'Steve-175', 'Steve-176', 'Steve-177', 'Steve-178', 'Steve-179', 'Steve-180', 'Steve-181', 'Steve-182', 'Steve-183', 'Steve-184', 'Steve-185', 'Steve-186', 'Steve-187', 'Steve-188', 'Steve-189', 'Steve-190', 'Steve-191', 'Steve-192', 'Steve-193', 'Steve-194', 'Steve-195', 'Steve-196', 'Steve-197', 'Steve-198', 'Steve-200']
PickedWeight = [0 for _ in range(len(PickerName))]
PickerCertificate = ["" for _ in range(len(PickerName))]
print("Inputing the weigh of mambers picks.")
#Getting weigh 1 and weigh 2. for validation for 200 users
for Member in range(len(PickerName)):
    print(f"Hey {PickerName[Member]}, Input the weigh of your PICK!\nInput it twice")
    while True:
        try:

            weigh1, weigh2 = map(float, input("For example, '30,30'\n: - ").split(",")) 
            if weigh1 == weigh2: PickedWeight[Member] = round(weigh1,1); break
            else: print("Both weights must match. Please reinput")
        except ValueError:
            print("You inputted your weights incorrectly\nInput it in the format '20,20' (<Weigh1>,<Weigh2>)")
#Sorting arrys in decending order.
while True:
    Swap = False
    for element in range(len(PickerName)-1):
        if PickedWeight[element] < PickedWeight[element+1]:
            Swap, PickedWeight[element], PickedWeight[element+1], PickerName[element], PickerName[element+1] = True, PickedWeight[element+1], PickedWeight[element], PickerName[element+1], PickerName[element]
    if not Swap: break
#Printing best in group and second best in group
print(f"{PickerName[0]} is Best in Group with pick of {PickedWeight[0]}kg\n{PickerName[1]} is Second best in Group with pick of {PickedWeight[1]}kg")

#Counting the number of certificates to be prined
#Notes their names in PickerCertifcate.
no_certificates = 0
for member in range(len(PickerName)):
    if PickedWeight[member] > 3: PickerCertificate[no_certificates] = PickerName[member]; no_certificates += 1
#Printing no certificates to be printed
print(f"{no_certificates} certificates need to be printed]\n:>")