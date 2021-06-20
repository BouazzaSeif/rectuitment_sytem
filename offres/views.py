from rest_framework import viewsets, permissions
from .models import Offre, Condidature
from .serializers import OffreSerializer,CondidatureSerializer, OffrePublicSrerializer
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from pyresparser import ResumeParser
import pprint

pp = pprint.PrettyPrinter(indent=4)

class CondidatureViewSet(viewsets.ModelViewSet):
    serializer_class = CondidatureSerializer
    queryset = Condidature.objects.all()
    def create(self, request):
        data = request.data
        serializer = CondidatureSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        path = 'CvExtractor/' + str(request.data['CV']) 
        extracted_data = ResumeParser(path).get_extracted_data()
        pp.pprint(extracted_data)
        data['mobile_number'] = extracted_data['mobile_number']
        data['college_name'] = extracted_data['college_name']
        data['company_names'] = extracted_data['company_names']
        data['degree'] = extracted_data['degree']
        data['designation'] = extracted_data['designation']
        data['experience'] = str(extracted_data['experience'])
        data['skills'] = str(extracted_data['skills'])
        data['total_experience'] = int(extracted_data['total_experience'])

        serializer = CondidatureSerializer(data=data)   
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
        


class OffreViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = OffreSerializer
    
    def get_queryset(self):
        return Offre.objects.filter(entreprise=self.request.user)

    def perform_create(self, serializer):
        serializer.save(entreprise=self.request.user)
        


class OffrePublicViewSet(viewsets.ModelViewSet):
    serializer_class = OffrePublicSrerializer
    queryset = Offre.objects.filter(masqué=False)




   


class SendMailView(APIView):
    def post(self, request, *args, **kwargs):
        template =  f"""
Bonjour [[nom_condidat]], \n
L'entreprise [[entreprise]] vous a accordé une acceptation provisoire concernant votre condidature pour l'offre [[offre]] , à cet égard vous êtes appelé à passer un entretien d'embauche à son local situé à [[adresse_entreprise]] le [[date]] à [[temps]]. \n
veuillez apporter tout les documents qui certifient les données évoquées dans votre cv.
Soyez au rendez-vous et bonne chance.
"""
        msg = template.replace('[[temps]]', request.data['temps'] )  
        msg = msg.replace('[[adresse_entreprise]]', request.data['adresse_entreprise'] )    
        msg = msg.replace('[[nom_condidat]]', request.data['nom_condidat'] )
        msg = msg.replace('[[entreprise]]', request.data['entreprise'] )
        msg = msg.replace('[[offre]]', request.data['offre'] )
        msg = msg.replace('[[date]]', request.data['date'] )

        mail_of_sender=request.data['mail_of_sender']
        mail_of_destination=request.data['mail_of_destination']

        send_mail(
            'acceptation de condidature',
            msg,
            mail_of_sender,
            [mail_of_destination]
        )
        
        return Response(data={"results":'success'})


