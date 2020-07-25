from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes =[BasicAuthentication, SessionAuthentication]
    permission_classes =[IsAuthenticatedOrReadOnly] #퍼미션 설정
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    #search 용
    filter_backends = [SearchFilter]
    search_fields = ('title','body')  #title과body 검색  제목혹은 본문은 검색 
    # 어떤 칼럼을 기반으로 검색을 할 건지 -> 튜풀  쉼표를 꼭 추가해줘야댐 !
    def get_queryset(self):
        #여기 내부에서 쿼리셋을 지지고 볶음 
        qs = super().get_queryset()  #상위클래스의 queryset을 가지고옴
        #qs = qs.filter(author__id = 1) #필터링 하는 숫자  지정
        # .filet .exclude
        
        # 만약 로그인이 안되어있다면 -> 비어있는 쿼리셋을 리턴해라!!
        if self.request.user.is_authenticated:
            # 지금 로그인이 되어있다면 -> 지금 로그인한 유저의 글만 필터링 해라!!!
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()   
            
        
        return qs     

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)