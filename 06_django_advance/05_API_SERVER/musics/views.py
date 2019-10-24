# from django.views.decorators.http import require_http_methods  # GET, POST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Artist, Music
from .serializers import ArtistSerializer, MusicSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer
# import json
# 달라, 써라, 수정, 삭제
# Read, Create, Update, Delete
# GET, POST, PATCH, DELETE


# @api_view(['GET'])
# def artist_list(request):
#     artists = Artist.objects.all()
#     dataset = []
#     for artist in artists:
#         d = {
#             "id": artist.id,
#             "name": artist.name,
#         }
#         dataset.append(d)
#     res_data = json.dump(dataset)
    
#     # 공용어로 바꾸다.(Serialization: 직렬화)
#     return HttpResponse(res_data)


@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)


@api_view(['POST'])
def create_comment(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    ser = CommentSerializer(data=request.POST)
    if ser.is_valid(raise_exception=True):
        ser.save(music_id=music.id)  # 저장 완료
    return Response(ser.data)  # 저장한 데이터