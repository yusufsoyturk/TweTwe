from django.contrib import admin
from tweetapp.models import Tweet

# Register your models here.
# superuser bilgileri
# username = yusuf
# email = yusuf@gmail.com
# password = yusuf1234.


class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Message Group", {"fields": ["message"]}),
        ("Nickname Group", {"fields": ["nickname"]})
    ]
    # fields = ["message", "nickname"] #admin panelinde message ve nickname yer deiştirme

admin.site.register(Tweet, TweetAdmin)