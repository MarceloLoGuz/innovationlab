from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from users.models import MyAbsUser
from users.forms import UsersForm
from django.http import JsonResponse, HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


class MyUserClass(APIView):
    permission_classes = (AllowAny, )

    # Create an user
    def post(self, request, format=None, *args, **kwargs):
        try:
            form = UsersForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Success'}, status=status.HTTP_201_CREATED, safe=False)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = {'error': 'An error occurred', 'message': str(e)}
            return JsonResponse(response_data, status=status.HTTP_400_BAD_REQUEST)
    
    

    # Update an user by id
    def put(self, request, id, *args, **kwargs):
        try:
            user = MyAbsUser.objects.get(pk=int(id))
            user_update = UsersForm(request.data, instance=user)

            if user_update.is_valid():
                user_update.save()
                return JsonResponse({'message': 'Updated'}, status=status.HTTP_200_OK, safe=False)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = {'error': 'An error occurred', 'message': str(e)}
            return JsonResponse(response_data, status=status.HTTP_400_BAD_REQUEST)

        

    # Delete and user by id
    def delete(self, request, id, *args, **kwargs):
        user = MyAbsUser.objects.get(pk=int(id))
        user.delete()
        return JsonResponse({'message': 'Deleted'}, status=status.HTTP_200_OK, safe=False)
        
    


    # Get PDF
    def get(self, request, format=None, *args, **kwargs):
        users = MyAbsUser.objects.all()
        response = HttpResponse(content_type='application/pdf')

        # Create PDF document
        pdf = SimpleDocTemplate(response, pagesize=letter)
        elements = []

        table_data = create_pdf_table(users)
        table = Table(table_data, colWidths=[100, 100, 100, 100, 100, 100])
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.black),
            ('LINEBELOW', (0, -1), (-1, -1), 1, colors.black),
        ])


        table.setStyle(style)
        elements.append(table)
        # Build PDF
        pdf.build(elements)
        return response




class MyUserFilters(APIView):
    permission_classes = (AllowAny, )

    def post(self, request, format=None, *args, **kwargs):
        data = request.data
        get_user_object = MyAbsUser.objects.all()
        users = [MyAbsUser(name=user.name, first_name=user.first_name, last_name=user.last_name, email=user.email, phone=user.phone, age=user.age) for user in get_user_object]
       
        sort_by_youngest_to_older = bool(data.get('sort_by_youngest_to_older'))
        sort_by_age = int(data.get('sort_by_age'))
        sort_by_first_name = bool(data.get('sort_by_first_name'))

        sorted = [{}]

        if(sort_by_youngest_to_older == True):
            sorted = quicksort(users, 'age')
        elif(sort_by_age > 0):
            sorted = MyAbsUser.objects.filter(age=sort_by_age)
        elif(sort_by_first_name == True):
            sorted = quicksort(users, 'first_name')
            
        response_data = [{'name':user.name, 'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email, 'phone':user.phone, 'age':user.age} for user in sorted]
        return JsonResponse({'data': response_data,}, status=status.HTTP_200_OK, safe=True)     
        




def quicksort(users, option):
    try:
        if len(users) <= 1:
            return users

        pivot = users[len(users) // 2]
        if(option == 'age'):
            left = [user for user in users if user.age < pivot.age]
            middle = [user for user in users if user.age == pivot.age]
            right = [user for user in users if user.age > pivot.age]
        elif(option == 'first_name'):
            ## To ignore case differences: casefold() is used...
            left = [user for user in users if user.first_name.casefold() < pivot.first_name.casefold()]
            middle = [user for user in users if user.first_name.casefold() == pivot.first_name.casefold()]
            right = [user for user in users if user.first_name.casefold() > pivot.first_name.casefold()]

        return quicksort(left, option) + middle + quicksort(right, option)
    except Exception as e:
        return []




def create_pdf_table(data):
    table_data = [['Nombre', 'Apellido Paterno', 'Apellido Materno', 'Email', 'Teléfono', 'Edad']]
    
    for user in data:
        table_data.append([
            user.name,
            user.first_name,
            user.last_name,
            user.email,
            user.phone,
            str(user.age),
        ])

    return table_data