The queries I used: 
-  Artist.objects.create(stage_name ="Hamaki", social_link="hamaki/facebook.com")
-  Artist.objects.create(stage_name ="Hamaki", social_link="hamaki2/facebook.com")
-  Artist.objects.create(stage_name ="Tamer Hosni", social_link="Tamer/facebook.com")
-  Artist.objects.create(stage_name ="Elissa", social_link="elissa/facebook.com")
-  Artist.objects.all()
-  Artist.objects.all().order_by('-stage_name') 
-  Artist.objects.create(stage_name ="Ahmed", social_link="ahmed/facebook.com")
-  Artist.objects.all().filter(stage_name__startswith = 'a') 
- TamerHosni  = Artist.objects.get(stage_name__startswith = 'Tamer')
- Album.objects.create(name='Love' , release_date='2022-11-9',cost=255.6, author=TamerHosni )
- Album.objects.create(name='Sad' , release_date='2022-11-5',cost=255.6, author=TamerHosni )
-  NewAlbum = Album(release_date = '2022-11-23' , cost = 999.99 )
-  NewAlbum.author = Artist.objects.get(pk = 2)
- NewAlbum.save()
- Album.objects.all().order_by('-release_date')[0]
- Album.objects.all().filter(release_date)







The output: 
- <Artist: Hamaki>
- django.db.utils.IntegrityError: UNIQUE constraint failed: artist_artist.stage_name
- <Artist: Tamer Hosni>
- <Artist: Elissa>
- <QuerySet [<Artist: Elissa>, <Artist: Hamaki>, <Artist: Tamer Hosni>]>
- <QuerySet [<Artist: Tamer Hosni>, <Artist: Hamaki>, <Artist: Elissa>]>
- <Artist: Ahmed>
- <QuerySet [<Artist: Ahmed>]>
- django.db.utils.IntegrityError: NOT NULL constraint failed: albums_album.release_date
- <Album: Love>
- <Album: Sad>
- <Album: Sad HOw>
- <Album: New Album>






