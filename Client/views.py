from rest_framework.response import Response
from .models import * 
from .serializer import *
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import *






class ClientAPI(APIView):
    def get(self,request):
        client_obj = Client.objects.all()
        client_serializer = ClientSerializer(client_obj,many=True)
        return Response(client_serializer.data)
    
    def post(self,request):
        validated_data = request.data 
        client_serializer = ClientSerializer(data=validated_data)
        if client_serializer.is_valid():
            user_data = validated_data.pop('user_id')
            user_obj = CoreUser.objects.create(**user_data)
            user_obj.set_password(user_data['password'])
            user_obj.save()
            client_obj = Client.objects.create(user_id=user_obj,**validated_data)
            
            return Response({"Message":"Client created successfully"}
                            )
        return Response({"Message":client_serializer.errors})  
    
    def patch(self,request):
        validated_data=request.data 
        client_update = request.GET.get('client_update')
        client_obj = Client.objects.get(client_id=client_update)
        client_serializer = ClientSerializer(client_obj,data=validated_data,partial=True)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response({'Message':'Data updated successfully'}
                            )
        return Response(client_serializer.errors)  
    def delete(self,request):
        delete_client = request.GET.get('delete_client')
        client_obj = Client.objects.get(client_id=delete_client)
        client_obj.delete()
        return Response({'Message':"Client deleted successfully"})
    

class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = ClientFilter
            





 
class InvoiceAPI(APIView):
    def get(self,request ):
        sort_by = request.GET.get('sort_by')
        if sort_by=='Ascending':
            invoice_obj = Invoice.objects.raw("SELECT * FROM invoice ORDER BY total_amount;")
            invoice_serializer = InvoiceSerializer(invoice_obj,many=True)
            return Response(invoice_serializer.data)
        elif sort_by=='descending':
            invoice_obj = Invoice.objects.raw("SELECT * FROM invoice ORDER BY total_amount desc;")
            invoice_serializer = InvoiceSerializer(invoice_obj,many=True)
            return Response(invoice_serializer.data)
        else:
            invoice_obj = Invoice.objects.raw("SELECT * FROM invoice")
            invoice_serializer = InvoiceSerializer(invoice_obj,many=True)
            return Response(invoice_serializer.data)
            
              
    

    def post(self,request):
        validated_data = request.data
        invoice_serializer = InvoiceSerializer(data=validated_data)

        if invoice_serializer.is_valid():
           invoice_serializer.save()
           return Response({"message":"data posted successfully","data":invoice_serializer.data})
        else:
            return Response(invoice_serializer._errors)  


    def put(self,request):
        validated_data = request.data
        invoice_obj = Invoice.objects.get(invoice_id=validated_data['invoice_id'])
       
        invoice_serializer = InvoiceSerializer(invoice_obj,data=validated_data,partial=True)
        
        if invoice_serializer.is_valid():
            invoice_serializer.save()
            return Response({"message":"data updated successfully","data":invoice_serializer.data} )
        
        else:
            return Response(invoice_serializer.errors)   


    def delete(self,request):
        delete = request.GET.get('delete')
        if delete:
            invoice_obj = Invoice.objects.get(invoice_id=delete)
            invoice_obj.delete()
            return Response({"message":"data deleted successfully "})  
        

# class InvoiceListView(generics.ListAPIView):  # Apply Filtering in Invoice Model 
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer
#     filter_backends = [SearchFilter , DjangoFilterBackend]
#     fielterset_class = InvoiceFilter


@api_view(['GET'])                          # Apply Filtering in Invoice Model
def invoicefilter(request , id=None):
    if request.method=="GET":
        invoive_obj = Invoice.objects.filter(invoice_id=id)
        serializer_obj = InvoiceSerializer(invoive_obj, many=True)
        return Response(serializer_obj.data)
        










class Technology_optionViewSet(viewsets.ModelViewSet):
    queryset = Technology_option.objects.all()
    serializer_class = Technology_optionSerializer
    

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    

class Payment_methodViewSet(viewsets.ModelViewSet):
    queryset = Payment_method.objects.all()
    serializer_class = Payment_methodSerializer



class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer





class TeamAPIView(APIView):
    def get(self, request):
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data)

    def post(self, request):
        validated_data = request.data
        serializer_obj = TeamSerializer(data=validated_data)

        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({"message":"team create successfully","Data":serializer_obj.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request):
        validated_data = request.data
        team = Team.objects.get(team_id=validated_data['team_id'])
        serializer_obj = TeamSerializer(team, data=request.data)

        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({"Message":"Team update Successfully ","Data":serializer_obj.data})
        else:
            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request):
        delete = request.GET.get('delete')
        if delete:
            team_obj = Team.objects.get(team_id=delete)
            team_obj.delete()
            return Response({"message":"Data deleted successfully"},status=status.HTTP_204_NO_CONTENT)
 








class ProjectAPIView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        validated_data = request.data
        serializer_obj = ProjectSerializer(data=validated_data)

        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({"message":"project create successfully","Data":serializer_obj.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request):
        validated_data = request.data
        project_obj = Project.objects.get(project_id = validated_data['project_id']) 
        serializer_obj = ProjectSerializer(project_obj, data=validated_data)

        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({"message":"Project update successfully","Data":serializer_obj.data})
        else:
            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request):
        delete = request.GET.get('delete')
        if delete:
            project_obj = Project.objects.get(project_id = delete)
            project_obj.delete()
            return Response({"message":"data deleted successfully "},status=status.HTTP_204_NO_CONTENT)
        

# class projectListView(generics.ListAPIView):  # Apply Filtering in Project Model 
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     filter_backends = [SearchFilter , DjangoFilterBackend]
#     filterset_class = ProjectFilter
 


@api_view(['GET'])                         # Apply Filtering in Project Model
def projectFilter(request):

    if request.method == 'GET':
        project_name=request.GET.get("project_name" , None)
        project_obj = Project.objects.filter(project_name=project_name)
        serializer_obj = ProjectSerializer(project_obj,many=True)
        return Response(serializer_obj.data)









class InvoiceitemAPI(APIView):
    def get(self,request):
        invoiceitem_obj = Invoice_item.objects.all()
        invoiceitem_serializer = InvoiceitemSerializer(invoiceitem_obj,many=True)
        return Response(invoiceitem_serializer.data)  
    

    def post(self,request):
        validated_data = request.data
        invoiceitem_serializer = InvoiceitemSerializer(data=validated_data)

        if invoiceitem_serializer.is_valid():
           invoiceitem_serializer.save()
           return Response({"message":"data posted successfully","data":invoiceitem_serializer.data})
        else:
            return Response(invoiceitem_serializer._errors)  


    def put(self,request):
        validated_data = request.data
        invoiceitem_obj = Invoice_item.objects.get(invoice_item_id=validated_data['invoice_item_id'])
       
        invoiceitem_serializer = InvoiceitemSerializer(invoiceitem_obj,data=validated_data,partial=True)
        
        if invoiceitem_serializer.is_valid():
            invoiceitem_serializer.save()
            return Response({"message":"data updated successfully","data":invoiceitem_serializer.data} )
        
        else:
            return Response(invoiceitem_serializer.errors)   


    def delete(self,request):
        delete = request.GET.get('delete')
        if delete:
            invoiceitem_obj = Invoice_item.objects.get(invoice_item_id=delete)
            invoiceitem_obj.delete()
            return Response({"message":"data deleted successfully "})  
        














class PaymentAPIView(APIView):
    def get(self, request):
        payment_obj = Payment.objects.all()
        serializer_obj = PaymentSerializer(payment_obj, many=True)
        return Response(serializer_obj.data)
    

    def post(self, request):
        validated_data = request.data
        serializer_obj = PaymentSerializer(data=validated_data)

        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({"message":"created payment successfully","data":serializer_obj.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request):
        validated_data = request.data
        payment_obj = Payment.objects.get(payment_id = validated_data['payment_id'])
        serializer_obj = PaymentSerializer(payment_obj ,data=validated_data)

        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({"message":"Updated successfully","data":serializer_obj.data},status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request):
        delete = request.GET.get('delete')

        if delete:
            payment_obj = Payment.objects.get(payment_id=delete)
            payment_obj.delete()
            return Response({"message":"data deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        

class TechnologyListView(generics.ListAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = TechnologyFilter

class TeamListView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = TeamFilter
