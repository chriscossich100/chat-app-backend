from rest_framework import serializers
from .models import ChatRoom, Messages #importing the Members model:
from django.contrib.auth.models import User, auth

#The first thing we need to get started on our Web API is to provide a way of serializing and deserializing the snippet instances into representations such as json



#we can also use the modelSerializer as a way to not replicate a lot of information. This is the same thing as Form and ModelForm classes. Its a good way to refactor

class UserSerialzier(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
      
        submittedUser = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
        submittedUser.save()
        return submittedUser



class ChatRoomSerializer(serializers.ModelSerializer):
    createdBy = UserSerialzier()

    class Meta:
        model = ChatRoom
        fields = ('name', 'description', 'createdBy')
    

    def create(self, validated_data):
       gottenUser = User.objects.get(username=validated_data['createdBy']['username'])
      
       submittedChatroom = ChatRoom(name=validated_data['name'], description=validated_data['description'], createdBy = gottenUser)
       submitterBabe = submittedChatroom.save()
       return submittedChatroom


class MessagesSerializer(serializers.ModelSerializer):

    chatroom = ChatRoomSerializer()

    class Meta:
        model = Messages
        fields = ('message', 'author', 'dateCreated', 'chatroom')

    def create(self, validated_data):
        getChatRoom = ChatRoom.objects.get(name=validated_data['chatroom']['name'])
        submittedMessage = Messages(message=validated_data['message'], author=validated_data['author'], chatroom = getChatRoom)
        submittedMessage.save()
        return submittedMessage
    