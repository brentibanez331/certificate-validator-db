from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from apis.models.user_models import CustomUser
from apis.serializers import UserSerializer
from rest_framework import status

@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_users(request):
    person_user_id = request.query_params.get('user', None)
    try:
        if person_user_id:
            users = CustomUser.objects.filter(personUserId=person_user_id)
        else:
            users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'success': True, 'users': serializer.data})
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request, person_user_id):
    print(person_user_id)
    try:
        user = CustomUser.objects.get(personUserId=person_user_id)
        print(user)
        user.delete()
        return Response({'success': True, 'message': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT', 'PATCH'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def update_user(request, person_user_id):
    if not person_user_id:
        return Response({'error': 'personUserId is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.get(personUserId=person_user_id)
        if request.method == 'PUT':
            serializer = UserSerializer(user, data=request.data)
        elif request.method == 'PATCH':
            serializer = UserSerializer(user, data=request.data, partial=True)
        else:
            return Response({'error': 'Wrong Method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'user': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User Not Found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
