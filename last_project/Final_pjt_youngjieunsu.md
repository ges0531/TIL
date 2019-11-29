# Fullstack | Last Project | 191128

## 김은수, 노영지 (Eunsudalji's Movie Home)

#### 1. 목표

* 영화 추천 서비스 구현
* HTML/CSS, Javascript(Vue.js/Vanilla JS), Django, Database 등을 활용한 실제 서비스 설계 
* Git을 통한 소스코드 버전 관리 및 협업 
* 서비스 배포 

#### 2. 필수 기능

* Modeling (accounts)

  ```python
  class User(AbstractUser):
      fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars')
  
      def __str__(self):
          return self.username
      
      def get_absolute_url(self):
          return reverse("accounts:user_detail", kwargs={"user_id": self.pk})
  ```
  
* Modeling (movies)

  ```python
  User = get_user_model()
  
  class Genre(models.Model):
      name = models.CharField(max_length=100, blank=True)
  
  
  class Movie(models.Model):
      title = models.CharField(max_length=100)
      overview = models.TextField()
      popularity = models.FloatField(null=True)
      poster_url = models.CharField(max_length=100)
      release_date = models.CharField(max_length=100)
      genre = models.ManyToManyField(Genre, related_name='movie_genre')
      like_users = models.ManyToManyField(User, related_name='like_movies')
      def get_absolute_url(self):
          return reverse("movies:movie_detail", kwargs={"movie_id": self.pk})
  
  
  class Review(models.Model):
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
      content = models.CharField(max_length=100)
      rate = models.IntegerField(
          validators=[
              MaxValueValidator(10),
              MinValueValidator(1)
          ]
      )
      user = models.ForeignKey(User, on_delete=models.CASCADE)
  ```
  
* 관리자 권한의 유저만 영화 등록 및 수정 / 삭제 권한을 가집니다. 

* 관리자 권한의 유저는 유저 관리 (수정 / 삭제 권한)을 가집니다.

  ```bash
  $ python manage.py create superuser
  ```

* 관리자 페이지를 제외하고 최소한 5개 이상의 URL 및 페이지 구성을 하여야 합니다. 

  ```python
  # master urls
  path('admin/', admin.site.urls),
  path('accounts/', include('accounts.urls')),
  path('movies/', include('movies.urls')),
  path('', include('title.urls'))
  
  # accounts urls
  path('', views.user_list, name='user_list'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('<int:user_id>/', views.user_detail, name='user_detail'),
  path('follow/<int:user_id>/', views.follow, name='follow'),
  
  # movies urls
  path('', views.movie_list, name='movie_list'),
  path('<int:movie_id>/',views.movie_detail,name='movie_detail'),
  path('<int:movie_id>/reviews/new/', views.create_review, name='create_review'),
  path('<int:movie_id>/reviews/<int:review_id>/delete/', views.delete_review, name='delete_review'),
  path('<int:movie_id>/like/', views.movie_like, name='movie_like'),
  path('title/', views.page_title, name='page_title'),
  ```

* 모든 로그인 된 유저는 영화에 대한 평점을 등록 / 수정 / 삭제 등을 할 수 있어야 합니다. 

  ```python
  @login_required
  def create_review(request, movie_id):
      movie = get_object_or_404(Movie, id=movie_id)
      form = ReviewModelForm(request.POST)
      review = Review()
      review.content = request.POST.get('input_content')
      review.rate = request.POST.get('input_rate')
      review.movie_id = movie.id
      review.user = request.user
      if review.rate and review.content:
          review.save()
      return redirect(movie)
  
  
  @login_required
  def delete_review(request, review_id, movie_id):
      review = get_object_or_404(Review, id=review_id, movie_id=movie_id)
      review.delete()
      return redirect(review.movie)
  ```

* 평점을 등록한 유저는 해당 정보를 기반으로 영화를 추천 받을 수 있어야 합니다. 

  ```python
  # accounts/views.py
  
  @login_required
  def user_detail(request, user_id):
      # user = get_object_or_404(User, id=user_id)
      user = get_object_or_404(User, id=user_id)
      reviews = Review.objects.filter(user=user)
      return render(request, 'accounts/detail.html', {
          # 'user': user,
          'user': user,
          'reviews': reviews,
      })
  
  # accounts/templates/accounts/detail.html
  <div class="rela-block content">
      {% for review in reviews %}
      <div class="rela-inline image">
          <a href="{% url 'movies:movie_detail' review.movie.pk %}">
              <img src="{{ review.movie.poster_url }}" alt="">
          </a>
      </div>
      {% endfor %}
  </div>
  # 자신이 댓글 단 영화를 보여줍니다.
  ```



#### 3. 분담 내용

* 팀원 정보 및 업무 분담 내역

  김은수: movies app Modeling 및 함수 구현, TMDB에서 영화 데이터 수집 및 가공, movies app css

  노영지: accounts app Modeling 및 함수 구현, title 화면, Vue 파트, accounts app css, 배포

* 핵심 기능

  리뷰, 평점, 좋아요를 기반으로 한 시대별 영화 추천 서비스

* 배포 서버 URL

  https://stormy-bastion-34814.herokuapp.com

* 느낀점

  git branch를 사용하는데 많은 어려움이 있었습니다. 그래서 branch에 대해 좀 더 알 수 있는 계기가 되었습니다. 처음부터 기힉, 설계, 구성을 한 첫 프로젝트였기 때문에 배포를 할 때 굉장히 뿌듯했습니다.

  Css가 생각보다 원하는데로 되지 않아서 처음에는 고생을 했는데 시간이 지나고 많이 사용 해 볼수록 잘 사용할 수 있게 되어서 Css에 자신감을 얻었습니다.

  협업을 하면서 업무를 정확히 분담해서 자신의 업무를 집중해서 하고 서로 상의를 하면서 작업한 부분을 합치는 부분에서  협업의 중요성을 많이 느꼈습니다.