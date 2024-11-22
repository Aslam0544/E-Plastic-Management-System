from plasticmanagement.models import WastageModel, UserModel


def getwastages(role,username):

    wastages=[]

    if role == "agent":
        for wastage in WastageModel.objects.filter(assignedto=username):

            customer=UserModel.objects.filter(username=wastage.customerid).first()

            wastage.image = str(wastage.image).split("/")[1]
            wastage.customername=customer.name
            wastage.customeraddress = customer.address
            wastage.mobile = customer.mobile

            wastages.append(wastage)

    elif role == "user":
        for wastage in WastageModel.objects.filter(customerid=username):

            customer = UserModel.objects.filter(username=wastage.customerid).first()

            wastage.image = str(wastage.image).split("/")[1]
            wastage.customername = customer.name
            wastage.customeraddress = customer.address
            wastage.mobile = customer.mobile

            wastages.append(wastage)

    elif role == "admin":
        for wastage in WastageModel.objects.all():

            customer = UserModel.objects.filter(username=wastage.customerid).first()

            wastage.image = str(wastage.image).split("/")[1]
            wastage.customername = customer.name
            wastage.customeraddress = customer.address
            wastage.mobile = customer.mobile

            wastages.append(wastage)

    return wastages