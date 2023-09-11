from django.shortcuts import render
from django.http import JsonResponse, HttpResponse #this is needed to return specific json responses:
from rest_framework.parsers import JSONParser
from .models import Members, ChatRoom, Messages
from .serializers import ChatRoomSerializer, MessagesSerializer, UserSerialzier
from django.contrib.auth.models import User, auth #importing the user model:
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response #to give a response we will need to import the Response from the rest_framework.
#in other words to provide the get response, we will need to use the Response.

from rest_framework.views import APIView #this is the apiView from the rest framework
#this api view will allow us to create a function or a class on it, so taht we can be able to use everything available on the api view.


import io
# Create your views here.

# @csrf_exempt 
def index(request):



    return render(request, 'index.html')
    

def logintesting(request):

    if request.method == 'POST':
        jungo = request.POST


        user = auth.authenticate(username=jungo.get('username'), password=jungo.get('password'))

        if user is not None: #that means user does exist, we should assign token to that user:
            token = Token.objects.get_or_create(user=user)
            return JsonResponse({"message": "this is the coolio way of logging in", "token": token[0].key})
        
        else:
            return JsonResponse({"messages": "the user def doesn't extist my dude"})
    


@csrf_exempt
def SignUp(request):

    if request.method == 'POST':
        data = request.POST

        #check to see if the user exists:
        if User.objects.filter(username=data.get('username')) | User.objects.filter(email=data.get('email')):
            return JsonResponse ({'userFound': True})#return a response that the user already exissts to the front end
        else:
            #create the user and deserialize it:
            UsersSerializer = UserSerialzier(data = data)
            if UsersSerializer.is_valid():
                UsersSerializer.save()
                return JsonResponse({'userFound': False})

@csrf_exempt
def Login(request):

    if request.method == 'POST':
        data = request.POST
        #log the user in with the provided credentials:
        user = auth.authenticate(username=data.get('username'), password=data.get('password'))

        #this condition runs if the user is found:
        if user is not None:
            token = Token.objects.get_or_create(user=user)
            print(f'other token information: {token[0].user}')
            return JsonResponse({"userFound": True, "token": token[0].key})
        else:
            return JsonResponse({'userFound': False})

        
        
class CreateChatRoom2(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            data = request.POST
            sentToken = request.headers['Authorization'].replace('Token ', '')
            
            #since we need to get the user information we first get the username of the token and then get the user object that matches the username.
            token = Token.objects.get(key=sentToken)
            gottenUser = User.objects.get(username=token.user)

            print(f'the created room is: {data.get("nameslug")}')
            
            #because an object can not exist, we need to catch the exception correctly:
            try:

                ChatRoom.objects.get(name=data.get('name'))

                return Response({'createdRoomFound': True})
            
            except ObjectDoesNotExist:
                chatroomserializer2 = ChatRoomSerializer(data={'name': data.get('name'), 'nameslug': data.get('nameslug'), 'description': data.get('description'), 'createdBy': {'username': gottenUser.username, 'email': gottenUser.email, 'password': gottenUser.password}})

                if chatroomserializer2.is_valid():
                    submittedChatRoom = chatroomserializer2.save()
                    return Response({"createdRoomFound": False})
                
                else: 
                    return Response({'message': 'hey hey ehye hey hey ehye'})
            

class GettingChatrooms2(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):

        chatrooms = ChatRoom.objects.all()
        chatroomsSerializer = ChatRoomSerializer(chatrooms, many=True)
        chatroomData = chatroomsSerializer.data
        return Response({"message": "you are able to get the chatrooms", "Chatrooms": chatroomData})
    


class GettingChatRooms(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        chatrooms = ChatRoom.objects.all()
        chatroomsSerializer = ChatRoomSerializer(chatrooms, many=True)
        chatroomData = chatroomsSerializer.data
        return Response({"message": "you are able to get the chatrooms", "Chatrooms": chatroomData})
    
    

class GettingMessages(APIView):

    permsion_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):

        #get specific chat room:
        specific_chat_room = kwargs['messagesinchat']
        print(f'when trying to get the string we get: {specific_chat_room}')
        try:
            #check to see if certain chat room exists: if it doesn't run the exception
            chatroom = ChatRoom.objects.get(nameslug=specific_chat_room)
            print(chatroom.name)
            quickfilter = Messages.objects.order_by('dateCreated').filter(chatroom__name = chatroom.name)
            print(quickfilter)

            #this makes sure to send which user you're currently logged in as to arrange the messages appropriately. 
            authToken = request.headers['Authorization'].replace('Token ', '')
            token = Token.objects.get(key=authToken)

            messagesSerializer = MessagesSerializer(quickfilter, many=True)
            messageData = messagesSerializer.data
            return Response({"message": "you are able to get the chatrooms", "MessagesInChatRoom": messageData, "currentUser": str(token.user), 'RoomFound': True})
            
        except ObjectDoesNotExist:
            return Response({'RoomRound': False})

        #specific_chat_room = kwargs['messagesinchat'].replace('-', ' ')
       
class CreateMessages(APIView):

    permission_classes = (IsAuthenticated, )

    def post (self, request, *args, **kwargs):
        data = request.POST
        specific_chat_room = kwargs['chatroom']
        sentToken = request.headers['Authorization'].replace('Token ', '')

        token = Token.objects.get(key=sentToken)
        getChatRoom = ChatRoom.objects.get(nameslug=specific_chat_room)
        gottenUser = User.objects.get(username=token.user)
        getMessageSeralizer = MessagesSerializer(data = {'message': data.get('message'), 'author': str(token.user), 'chatroom': {'name': getChatRoom.name, 'nameslug': getChatRoom.nameslug, 'description': getChatRoom.description,'createdBy': {'username': gottenUser.username, 'email': gottenUser.email, 'password': gottenUser.password}}})
        if getMessageSeralizer.is_valid():
            getMessageSeralizer.save()

            return Response({'message': 'we were able to create a message though'})
        else:
            return Response({'message': "we were not able to create a message though"})
        


class YourChatRooms(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
    
        sentToken = request.headers['Authorization'].replace('Token ', '')
        token = Token.objects.get(key=sentToken)
        Chatrooms = ChatRoom.objects.filter(createdBy__username = str(token.user))

        yourChatRoomsSerializer = ChatRoomSerializer(Chatrooms, many=True)
        yourchatroomdata = yourChatRoomsSerializer.data
        return Response({"message": "here are the filtered chat rooms", 'yourchatrooms': yourchatroomdata})